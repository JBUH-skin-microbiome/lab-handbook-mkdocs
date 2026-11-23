"""Render legacy links without rewriting authors' original Markdown."""
import html
import posixpath
import re
from pathlib import Path
from urllib.parse import urlsplit
import yaml

PAGES = {}

def on_config(config):
    PAGES.clear()
    for path in Path(config.docs_dir).rglob('*.md'):
        text = path.read_text(encoding='utf-8-sig')
        meta = yaml.safe_load(text.split('---', 2)[1]) if text.startswith('---') else {}
        PAGES[path.relative_to(config.docs_dir).as_posix()] = meta or {}
    return config

SECTION_PAGES = {}

def on_nav(nav, config, files):
    """Use MkDocs navigation as the single source for section overviews."""
    SECTION_PAGES.clear()
    def first_page(item):
        if item.is_page:
            return item
        if item.is_section and item.children:
            return first_page(item.children[0])
        return None
    def visit(items):
        for item in items:
            if not item.is_section:
                continue
            if (item.children and item.children[0].is_page
                    and PAGES[item.children[0].file.src_uri].get('has_children')):
                overview = item.children[0]
                SECTION_PAGES[overview.file.src_uri] = [
                    (child.title, first_page(child))
                    for child in item.children[1:] if first_page(child)
                ]
            visit(item.children)
    visit(nav.items)
    return nav

def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if src == 'index.md':
        def recent_documents(match):
            # The plugin includes images and other assets. Select documents
            # before applying the limit, so the homepage shows 10 actual pages.
            table = [line for line in match[1].splitlines() if line.startswith('|')]
            rows = []
            for line in table[2:]:
                # Preserve the plugin's headers, cells and formatting verbatim.
                link = re.match(r'\|\s*\[([^\]]+)\]\(([^)]+)\)', line)
                if not link:
                    continue
                target = posixpath.normpath(link[2])
                if target not in PAGES or target == src:
                    continue
                cells = line.split('|')
                aliases = config.get('extra', {}).get('author_aliases', {})
                author = html.unescape(cells[3].strip())
                if author in aliases:
                    cells[3] = ' ' + html.escape(aliases[author]) + ' '
                rows.append('|'.join(cells))
                if len(rows) == 10:
                    break
            if not rows:
                raise ValueError('Recent documents list is empty; check plugin output')
            return '\n\n' + '\n'.join(table[:2] + rows) + '\n\n'
        markdown = re.sub(r'<!-- recent-documents:start -->(.*?)<!-- recent-documents:end -->',
                          recent_documents, markdown, flags=re.S)
    base = page.url if page.url.endswith('/') else posixpath.dirname(page.url)
    def url(path):
        return posixpath.relpath(path.lstrip('/') or '.', base or '.') + ('/' if path.endswith('/') else '')
    markdown = re.sub(r'\{\{\s*[\'"]([^\'"]+)[\'"]\s*\|\s*relative_url\s*\}\}', lambda m: url(m[1]), markdown)
    markdown = re.sub(r'https://jbuh-skin-microbiome.github.io/lab-handbook/([^\s)\"<>]*)',
                      lambda m: url('/' + m[1]), markdown, flags=re.I)
    if SECTION_PAGES.get(src):
        markdown += '\n\n## 관련 문서\n\n'
        for title, child in SECTION_PAGES[src]:
            target = posixpath.relpath(child.file.src_uri, posixpath.dirname(src) or '.')
            title = title.replace('[', r'\[').replace(']', r'\]')
            markdown += f'- [{title}]({target})\n'
    if page.meta.get('destination'):
        dest = page.meta['destination']
        parsed = urlsplit(dest)
        if parsed.netloc.lower() == 'jbuh-skin-microbiome.github.io' and parsed.path.startswith('/lab-handbook/'):
            dest = url(parsed.path[len('/lab-handbook'):])
        page.meta['handbook_destination'] = dest
        markdown += '\n\n[자료 열기](' + dest + '){ .md-button .md-button--primary }\n'
    if '{{' in markdown or '{%' in markdown:
        raise ValueError(f'Unconverted Liquid in {src}')
    # Markdown links are resolved from source directories; raw HTML links above
    # are resolved from the rendered URL. Convert only Markdown destinations.
    def source_link(match):
        target = match[2]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path or target.startswith('#'):
            return match[0]
        absolute = posixpath.normpath(posixpath.join(base, parsed.path))
        source = next((p for p, m in PAGES.items() if m.get('permalink', '').strip('/') == absolute.strip('/')), None)
        if absolute.startswith('assets/'):
            source = absolute
        if source:
            relative = posixpath.relpath(source, posixpath.dirname(src) or '.')
            if parsed.fragment:
                relative += '#' + parsed.fragment
            return match[1] + relative + ')'
        return match[0]
    markdown = re.sub(r'(!?\[[^\]]*\]\()([^\s)]+)\)', source_link, markdown)
    return markdown

def on_page_content(content, page, config, files):
    """Number sections and their TOC entries without changing anchor IDs."""
    numbers = {}
    def number(items, prefix=()):
        index = 0
        for item in items:
            if item.level == 1:
                number(item.children, prefix)
                continue
            index += 1
            parts = prefix + (index,)
            label = '.'.join(map(str, parts))
            numbers[item.id] = label
            item.title = label + '. ' + re.sub(r'^\d+(?:\.\d+)*[.)]\s+', '', item.title)
            number(item.children, parts)
    number(page.toc.items)
    def heading(match):
        opening, anchor, body, closing = match.groups()
        label = numbers.get(html.unescape(anchor))
        if not label:
            return match[0]
        body = re.sub(r'^\d+(?:\.\d+)*[.)]\s+', '', body)
        return opening + label + '. ' + body + closing
    return re.sub(r'(<h[2-6]\b[^>]*\bid="([^"]+)"[^>]*>)(.*?)(</h[2-6]>)', heading, content, flags=re.S)

def on_post_page(output, page, config):
    dest = page.meta.get('handbook_destination')
    if dest:
        output = output.replace('</head>', '<meta http-equiv="refresh" content="0; url=' + html.escape(dest, quote=True) + '"></head>')
    return output
