#!/usr/bin/env python3
"""Build a pure-HTML static site from the raw design mockups.

Source mockups stay untouched under ./podxero*/ ; the deployable site is
written to ./site/ which GitHub Pages serves from the repo root.

Usage: python3 tools/build_site.py
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
ASSETS = os.path.join(SITE, "assets")

# nav key -> output filename
MAP = {
    "home": "index.html",
    "solutions": "solutions.html",
    "platform": "platform.html",
    "benchmarks": "benchmarks.html",
    "comparison": "comparison.html",
    "diagnostic": "diagnostic.html",
}

# output file -> source mockup html
SRC = {
    "index.html": "podxero_geo_ai_1/code.html",
    "solutions.html": "podxero_geo_ai_2/code.html",
    "platform.html": "podxero/code.html",
    "benchmarks.html": "podxero_geo/code.html",
    "comparison.html": "podxero_seo_vs_podxero_geo/code.html",
}

TITLES = {
    "index.html": "Podxero | 企业级生成式引擎优化 (GEO) 与 AI 搜索智能平台",
    "solutions.html": "解决方案 | Podxero GEO 企业级生成式引擎优化",
    "platform.html": "智能平台 | Podxero 多模型实时感知与引用编排控制台",
    "benchmarks.html": "基准与洞察 | Podxero GEO 行业权威评测",
    "comparison.html": "方案对比 | SEO vs GEO | Podxero",
    "diagnostic.html": "免费 GEO 诊断 | Podxero",
}

NAV_ITEMS = [
    ("home", "首页", "index.html"),
    ("solutions", "解决方案", "solutions.html"),
    ("platform", "智能平台", "platform.html"),
    ("benchmarks", "基准与洞察", "benchmarks.html"),
    ("comparison", "方案对比", "comparison.html"),
]

NAV_RE = re.compile(
    r'<nav class="hidden xl:flex items-center gap-1 bg-surface-container-lowest p-1 rounded-full".*?</nav>',
    re.S,
)

NAV_LINK_TMPL = (
    '<a class="px-4 py-2 rounded-full font-button-md text-button-md transition-all {cls}"'
    ' data-path="{key}" href="{href}">{label}</a>'
)
INACTIVE_CLS = "text-on-surface-variant hover:text-on-surface hover:bg-surface-soft"
ACTIVE_CLS = "text-[#001e2b] font-semibold bg-surface-soft"


def build_nav(active_key: str) -> str:
    links = []
    for key, label, href in NAV_ITEMS:
        if key == active_key:
            cls = ACTIVE_CLS
            links.append(
                '<a aria-current="page" class="%s" data-path="%s" href="%s">%s</a>'
                % (cls, key, href, label)
            )
        else:
            links.append(NAV_LINK_TMPL.format(cls=INACTIVE_CLS, key=key, href=href, label=label))
    return (
        '<nav class="hidden xl:flex items-center gap-1 bg-surface-container-lowest p-1 rounded-full"'
        ' data-active-classes="text-[#001e2b] font-semibold bg-surface-soft rounded-full">'
        + "".join(links)
        + "</nav>"
    )


MOBILE_NAV_RE = re.compile(r'(</div>\s*</header>)', re.S)


def build_mobile_nav(active_key: str) -> str:
    links = []
    for key, label, href in NAV_ITEMS:
        active = ' aria-current="page"' if key == active_key else ""
        cls = (
            "px-3 py-1.5 rounded-full text-caption font-button-md"
            + (" bg-surface-soft text-[#001e2b] font-semibold" if key == active_key
               else " text-on-surface-variant")
        )
        links.append(
            '<a class="%s" data-path="%s" href="%s"%s>%s</a>' % (cls, key, href, active, label)
        )
    return (
        '<nav class="xl:hidden w-full overflow-x-auto border-t border-hairline bg-surface-container-lowest">'
        '<div class="flex items-center gap-1 px-4 py-2 whitespace-nowrap">'
        + "".join(links)
        + "</div></nav>"
    )


def rewrite_links(html: str) -> str:
    """Turn every <a data-path="X" href="#"> into a real relative link."""

    def repl(m):
        tag = m.group(0)
        p = re.search(r'data-path="([^"]*)"', tag)
        if not p:
            return tag
        href = MAP.get(p.group(1))
        if not href or 'href="#"' not in tag:
            return tag
        return tag.replace('href="#"', 'href="%s"' % href)

    return re.sub(r"<a\b[^>]*>", repl, html)


def strip_aria_current(html: str) -> str:
    return re.sub(r'\s+aria-current="page"', "", html)


def set_title(html: str, title: str) -> str:
    if "<title>" in html:
        return re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, html, flags=re.S)
    return html.replace("<head>", "<head><title>%s</title>" % title, 1)


def main():
    os.makedirs(ASSETS, exist_ok=True)

    for out, src in SRC.items():
        html = open(os.path.join(ROOT, src), encoding="utf-8").read()
        html = rewrite_links(html)
        html = strip_aria_current(html)
        active = next(k for k, _, f in nav_items() if f == out)
        html, n = NAV_RE.subn(build_nav(active), html, count=1)
        assert n == 1, "nav not found in %s" % src
        if '<nav class="xl:hidden' not in html:
            html = html.replace("</header>", build_mobile_nav(active) + "</header>", 1)
        html = set_title(html, TITLES[out])
        open(os.path.join(SITE, out), "w", encoding="utf-8").write(html)
        print("built", out, "<-", src)

    # hand-written pages (not derived from a mockup)
    for extra in sorted(os.listdir(os.path.join(ROOT, "src"))):
        if extra.endswith(".html"):
            shutil.copy(os.path.join(ROOT, "src", extra), os.path.join(SITE, extra))
            print("copied", extra, "<- src/" + extra)

    # GitHub Pages serves these as-is; .nojekyll keeps Jekyll from ignoring
    # files/dirs that start with an underscore.
    open(os.path.join(SITE, ".nojekyll"), "w").close()
    print("wrote site/.nojekyll")


def nav_items():
    return NAV_ITEMS


if __name__ == "__main__":
    main()
