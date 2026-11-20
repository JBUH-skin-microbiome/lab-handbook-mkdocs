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

def children(src):
    parent = PAGES[src]
    return sorted((p for p, m in PAGES.items() if m.get('parent') == parent.get('title')
                  and (not m.get('grand_parent') or m['grand_parent'] == parent.get('parent'))),
                  key=lambda p: PAGES[p].get('nav_order', 999))

def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    base = page.url if page.url.endswith('/') else posixpath.dirname(page.url)
    def url(path):
        return posixpath.relpath(path.lstrip('/') or '.', base or '.') + ('/' if path.endswith('/') else '')
    markdown = re.sub(r'\{\{\s*[\'"]([^\'"]+)[\'"]\s*\|\s*relative_url\s*\}\}', lambda m: url(m[1]), markdown)
    markdown = re.sub(r'https://jbuh-skin-microbiome.github.io/lab-handbook/([^\s)\"<>]*)',
                      lambda m: url('/' + m[1]), markdown, flags=re.I)
    if '{% assign tutorial_groups' in markdown:
        markdown = markdown.split('{% assign tutorial_groups', 1)[0]
        for group in children(src):
            markdown += '\n## ' + PAGES[group]['title'] + '\n\n'
            for child in children(group):
                markdown += f'- [{PAGES[child]["title"]}]({url(PAGES[child]["permalink"])})\n'
    elif page.meta.get('has_children') and page.meta.get('has_toc', True):
        markdown += '\n\n## 관련 문서\n\n'
        for child in children(src):
            markdown += f'- [{PAGES[child]["title"]}]({url(PAGES[child]["permalink"])})\n'
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

def on_post_page(output, page, config):
    dest = page.meta.get('handbook_destination')
    if dest:
        output = output.replace('</head>', '<meta http-equiv="refresh" content="0; url=' + html.escape(dest, quote=True) + '"></head>')
    return output
