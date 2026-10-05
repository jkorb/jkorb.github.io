#!/usr/bin/env python3
"""Check a production Hugo build without third-party Python dependencies."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.switcher = []
        self.in_languages = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == 'nav' and attrs.get('class') == 'languages':
            self.in_languages = True
            assert attrs.get('aria-label'), 'Language navigation needs a name'
        if tag == 'a' and self.in_languages:
            self.switcher.append(attrs)

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_languages = False

    def select(self, tag, **attrs):
        return [a for t, a in self.elements if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def check_site(root, require_cvs, embargoed):
    source = Path(__file__).resolve().parents[1]
    cvs = json.loads((source / 'data/cv.json').read_text())
    dictionaries = [(source / 'i18n' / (language + '.yaml')).read_text() for language in cvs]
    keysets = [set(re.findall(r'^([a-z_]+):', dictionary, re.M)) for dictionary in dictionaries]
    assert all(keys == keysets[0] for keys in keysets), 'Translation dictionary keys differ'
    # Preserve source links and publication fields across translated project bundles.
    english = (source / 'content/projects/digital-proof-tools/index.md').read_text()
    for language in ['de', 'nl', 'it']:
        translated = (source / f'content/projects/digital-proof-tools/index.{language}.md').read_text()
        assert re.findall(r'\]\((https://[^)]+)\)', translated) == re.findall(r'\]\((https://[^)]+)\)', english), 'Translated project links changed'
        for field in ['title', 'date', 'publishDate', 'draft', 'layout', 'funder', 'funder_url']:
            assert re.search(rf'^{field}:.*$', translated, re.M)[0] == re.search(rf'^{field}:.*$', english, re.M)[0], f'Changed protected field: {field}'
    locales = {'en': 'en-US', 'de': 'de-DE', 'nl': 'nl-NL', 'it': 'it-IT'}
    prefixes = {'en': '/', 'de': '/de/', 'nl': '/nl/', 'it': '/it/'}
    project = 'projects/digital-proof-tools/'
    slide = 'slides/excalidraw-presentation/'
    routes = ['', 'slides/', slide] + ([] if embargoed else [project])
    pages = {}
    for lang, prefix in prefixes.items():
        for route in routes:
            url = prefix + route
            path = root / url.lstrip('/') / 'index.html'
            assert path.is_file(), f'Missing page: {url}'
            page = pages[url] = Document(path)
            assert page.select('html', lang=locales[lang]), f'Wrong language: {url}'
            canonical = 'https://jkorbmacher.org' + url
            assert page.select('link', rel='canonical', href=canonical), f'Wrong canonical: {url}'
            assert len(page.switcher) == 4, f'Incomplete language switcher: {url}'
            assert len([a for a in page.switcher if a.get('aria-current') == 'page']) == 1
            for target, target_prefix in prefixes.items():
                expected = target_prefix + route
                link = next(a for a in page.switcher if a['hreflang'] == locales[target])
                assert link['href'] == expected, f'Wrong translated destination: {url}'
                assert link.get('aria-label') and link.get('title') and link.get('lang')
                assert 'target' not in link, 'Language switches must stay in the same tab'
                assert (link.get('aria-current') == 'page') == (target == lang)
                assert page.select('link', rel='alternate', hreflang=locales[target], href='https://jkorbmacher.org' + expected)
            assert page.select('link', rel='alternate', hreflang='x-default', href='https://jkorbmacher.org/' + route)
            if not route:
                assert page.select('a', href='/' + cvs[lang]['path']), f'Wrong CV: {url}'
                assert bool(page.select('a', href=prefix + project)) != embargoed
                assert page.select('a', href=prefix + slide), f'Slide link loses language: {url}'
                assert page.select('img')[0].get('alt'), f'Missing portrait description: {url}'
                raw = path.read_text()
                for name in ['Johannes Korbmacher', 'Utrecht University', 'Philosophical Logic', 'Truthmaker Semantics', 'Google Scholar', 'PhilPeople']:
                    assert name in raw, f'Official name changed: {name}'
                contact_label = {'en': 'Contact', 'de': 'Kontakt', 'nl': 'Contact', 'it': 'Contatti'}[lang]
                assert re.search(r'id=["\']?contact-title["\']?[^>]*>' + contact_label + '</h2>', raw), f'Untranslated contact heading: {url}'
            if route in [project, slide]:
                assert page.select('a', href=prefix, **{'class': 'site-return'}), f'Home link loses language: {url}'
            if route == slide:
                assert page.select('iframe', src='https://link.excalidraw.com/p/readonly/wWzsSFToiHH92Ijb7wwL', title='No Variables (Gap.12, September 2025)')
            if route == project:
                raw = path.read_text()
                for name in ['Digital Proof Tools for Philosophical Logic', 'NWO Open Competition – XS', 'Mark Jago']:
                    assert name in raw, f'Official name changed: {name}'
                assert len(page.select('li', **{'class': 'milestone milestone--planned'})) == 4
        assert not (root / prefix.lstrip('/') / 'projects/index.html').exists(), 'Draft section published'
        if embargoed:
            assert not (root / prefix.lstrip('/') / project / 'index.html').exists(), 'Embargoed project published'
    # Check all published local links, assets and fragment identifiers.
    allowed_cvs = {'/' + cv['path'] for cv in cvs.values()}
    for url, page in pages.items():
        for tag, attrs in page.elements:
            if tag == 'script':
                raise AssertionError(f'Unexpected JavaScript on {url}')
            value = attrs.get('href') if tag in ['a', 'link'] else attrs.get('src') if tag in ['img', 'iframe'] else None
            if not value:
                continue
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                if parsed.netloc != 'jkorbmacher.org':
                    continue
            path = unquote(parsed.path) or url
            if path in allowed_cvs and not require_cvs:
                continue
            assert path.startswith('/'), f'Unexpected relative URL: {value}'
            target = root / path.lstrip('/')
            if path.endswith('/'):
                target /= 'index.html'
            assert target.is_file(), f'Broken local link on {url}: {value}'
            if parsed.fragment:
                document = Document(target)
                assert any(a.get('id') == parsed.fragment for _, a in document.elements), f'Broken fragment: {value}'
    for cv in cvs.values():
        if require_cvs:
            data = (root / cv['path']).read_bytes()
            assert data.startswith(b'%PDF-') and b'%%EOF' in data[-1024:]
    for sitemap in root.rglob('sitemap.xml'):
        ET.parse(sitemap)
    print(f'Checked {len(pages)} pages: languages, navigation, metadata, names, local links, assets, and publication rules.' + (' All four CVs are valid PDFs.' if require_cvs else ' CV downloads not required.'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', nargs='?', type=Path, default=Path('public'))
    parser.add_argument('--require-cvs', action='store_true')
    parser.add_argument('--embargoed', action='store_true', help='Expect project pages to be absent (build with --clock 2026-08-31T12:00:00Z).')
    args = parser.parse_args()
    check_site(args.destination, args.require_cvs, args.embargoed)
