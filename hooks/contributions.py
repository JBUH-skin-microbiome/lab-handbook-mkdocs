"""Build contributor document tables from Git history, not surviving lines."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import html
import posixpath
import subprocess
import yaml

MARKER = '<!-- contributor-documents -->'
KST = timezone(timedelta(hours=9))
AUTHOR_ALIASES = {}


def on_config(config):
    AUTHOR_ALIASES.clear()
    AUTHOR_ALIASES.update(config.get('extra', {}).get('author_aliases', {}))
    return config


def document_authors(repo, path):
    """Merge confirmed name aliases and keep their latest change per document."""
    result = subprocess.run(
        ['git', '-C', str(repo), 'log', '--follow', '--no-merges',
         '--format=%an%x00%ct', '--', str(path)],
        check=True, capture_output=True, encoding='utf-8',
    )
    authors = {}
    for line in result.stdout.splitlines():
        name, timestamp = line.rsplit('\0', 1)
        name = AUTHOR_ALIASES.get(name, name)
        authors[name] = max(authors.get(name, 0), int(timestamp))
    return authors


def cell(text):
    # Keep Git names as text, including names containing Markdown characters.
    return ''.join(f'&#{ord(char)};' if char in '|[]*_`\\"' else html.escape(char)
                   for char in str(text)).replace('\n', ' ')


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown
    repo = Path(config.config_file_path).parent
    contributors = {}
    for file in files.documentation_pages():
        if file.src_uri == page.file.src_uri or not file.abs_src_path:
            continue
        source_text = Path(file.abs_src_path).read_text(encoding='utf-8-sig')
        metadata = (yaml.safe_load(source_text.split('---', 2)[1]) or {}) if source_text.startswith('---') else {}
        title = metadata.get('title') or (file.page.title if file.page else file.name)
        for name, timestamp in document_authors(repo, file.abs_src_path).items():
            contributors.setdefault(name, []).append((timestamp, title, file.src_uri))

    sections = []
    for name in sorted(contributors, key=lambda value: (value.casefold(), value)):
        documents = sorted(contributors[name], key=lambda item: (-item[0], item[2]))
        # Material's existing content tabs provide the contributor selector.
        sections.extend([f'=== "{cell(name)}"', '', f'    수정한 문서: **{len(documents)}개**', '',
                         '    | 문서 | 해당 기여자의 최근 수정일 |',
                         '    | --- | --- |'])
        for timestamp, title, source in documents:
            target = posixpath.relpath(source, posixpath.dirname(page.file.src_uri))
            date = datetime.fromtimestamp(timestamp, KST).strftime('%Y-%m-%d')
            sections.append(f'    | [{cell(title)}]({target}) | {date} |')
        sections.append('')
    return markdown.replace(MARKER, '\n'.join(sections) or '아직 수정 기록이 없습니다.')


def on_page_context(context, page, config, nav):
    """Unify the git-authors footer without modifying its template or Git history."""
    info = context.get('git_info')
    if not info:
        return context
    for key in ('page_authors', 'site_authors'):
        merged = {}
        for author in info.get(key, []):
            name = AUTHOR_ALIASES.get(author['name'], author['name'])
            if name not in merged:
                merged[name] = dict(author, name=name)
            else:
                target = merged[name]
                for field in ('lines', 'lines_all_pages'):
                    target[field] += author[field]
                for field in ('contribution', 'contribution_all_pages'):
                    total = float(target[field].rstrip('%')) + float(author[field].rstrip('%'))
                    target[field] = f'{total:.2f}%'
        info[key] = list(merged.values())
    authors = info['page_authors']
    show_contribution = config.plugins['git-authors'].config.show_contribution
    labels = [html.escape(author['name']) +
              (f" ({author['contribution']})" if show_contribution and len(authors) > 1 else '')
              for author in authors]
    context['git_page_authors'] = "<span class='git-page-authors git-authors'>" + ', '.join(labels) + '</span>'
    context['git_site_authors'] = "<span class='git-authors'><ul>" + ''.join(
        '<li>' + html.escape(author['name']) + '</li>' for author in info['site_authors']) + '</ul></span>'
    return context
