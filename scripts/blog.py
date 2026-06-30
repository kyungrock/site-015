#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""기프트카드(site-015) 블로그 HTML 생성 — 페이스북 스타일"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
SITE_PATH = ROOT / "config" / "site.json"
MEDIA_CLASSES = ("gift", "warm", "calm", "nature", "sunset", "luxe")

HOME_STATIC = [
    {
        "href": "posts/nail-art-hand-massage-gift.html",
        "title": "네일아트·손 마사지 기프트카드 — 손끝까지 챙기는 선물",
        "summary": "네일 시술 후 뭉친 손·팔, 타이핑 피로까지 — 손 마사지 기프트카드 선물 가이드와 예약 팁.",
        "category": "팁",
        "date": "2026-06-18",
        "emoji": "💅",
        "media": "luxe",
    },
    {
        "href": "posts/spa-vs-massage-gift.html",
        "title": "스파 vs 타이·스웨디시 — 선물 맞춤 선택 가이드",
        "summary": "호텔 스파, 동네 마사지샵, 프리미엄 웰니스 — 받는 분 취향에 맞는 선물 고르기.",
        "category": "팁",
        "date": "2026-06-17",
        "emoji": "🛁",
        "media": "luxe",
    },
    {
        "href": "posts/digital-gift-card-tips.html",
        "title": "디지털 기프트카드 보내는 법 — 카톡·문자·이메일",
        "summary": "당일 전달 가능한 e-기프트카드. 발송 방법, 메시지 예시, 보안·사기 주의까지.",
        "category": "가이드",
        "date": "2026-06-17",
        "emoji": "💌",
        "media": "calm",
    },
    {
        "href": "posts/gift-card-vs-coupon.html",
        "title": "기프트카드 vs 할인쿠폰 — 뭐가 더 좋을까?",
        "summary": "선물·자기 이용 모두, 두 방식의 차이와 상황별 선택 기준을 비교표로 정리했어요.",
        "category": "가이드",
        "date": "2026-06-16",
        "emoji": "🔄",
        "media": "gift",
    },
    {
        "href": "posts/holiday-season-gift.html",
        "title": "명절·연말 마사지 선물 — 시즌별 기프트카드 가이드",
        "summary": "설·추석·크리스마스, 바쁜 시즌에 센스 있는 힐링 선물. 배송·포장·메시지 팁.",
        "category": "팁",
        "date": "2026-06-16",
        "emoji": "🧧",
        "media": "warm",
    },
    {
        "href": "posts/how-to-use-massage-gift.html",
        "title": "기프트카드 사용법 — 예약부터 이용·환불까지",
        "summary": "받은 기프트카드, 어떻게 쓰나요? 온·오프라인 예약, 유효기간, 잔액 확인 방법을 안내합니다.",
        "category": "가이드",
        "date": "2026-06-15",
        "emoji": "📱",
        "media": "calm",
    },
    {
        "href": "posts/self-care-gift-card.html",
        "title": "나를 위한 선물 — 셀프케어 마사지 기프트카드",
        "summary": "번아웃·스트레스, 스스로에게 주는 힐링 선물. 셀프케어 루틴과 잘 어울리는 이용법.",
        "category": "팁",
        "date": "2026-06-14",
        "emoji": "✨",
        "media": "nature",
    },
    {
        "href": "posts/corporate-gift-card.html",
        "title": "직장·거래처 선물 — 마사지 기프트카드 실무 팁",
        "summary": "팀원 회식 대신, 거래처 감사 선물로 마사지 기프트카드를 활용하는 방법과 주의점.",
        "category": "팁",
        "date": "2026-06-13",
        "emoji": "💼",
        "media": "gift",
    },
    {
        "href": "posts/birthday-wellness-gift.html",
        "title": "생일 웰니스 선물 — 마사지 기프트카드 고르는 법",
        "summary": "친구·동료·가족 생일, 취향별 맞춤 마사지 선물. 디지털 vs 실물 카드 비교도 포함.",
        "category": "팁",
        "date": "2026-06-12",
        "emoji": "🎉",
        "media": "luxe",
    },
    {
        "href": "posts/gift-card-amount-guide.html",
        "title": "기프트카드 금액 가이드 — 5만·10만·20만 어떻게?",
        "summary": "관계·상황·코스별 적정 금액표. 부담 없이 센스 있게 선물하는 기준을 정리했습니다.",
        "category": "가이드",
        "date": "2026-06-11",
        "emoji": "💳",
        "media": "calm",
    },
    {
        "href": "posts/couple-massage-gift.html",
        "title": "연인·커플 마사지 기프트 — 기념일 선물 아이디어",
        "summary": "발렌타인·생일·100일, 둘이 함께 즐기는 커플 마사지 기프트카드 추천과 예약 팁.",
        "category": "팁",
        "date": "2026-06-09",
        "emoji": "💕",
        "media": "sunset",
    },
    {
        "href": "posts/gift-for-parents-massage.html",
        "title": "부모님 효도 선물 — 마사지 기프트카드 이렇게 고르세요",
        "summary": "어버이날·생신·명절, 부모님께 드리기 좋은 마사지 선물. 금액·코스·메시지 카드 팁까지.",
        "category": "팁",
        "date": "2026-06-07",
        "emoji": "💐",
        "media": "warm",
    },
    {
        "href": "posts/gift-card-basics-guide.html",
        "title": "마사지 기프트카드란? 완벽 입문 가이드",
        "summary": "처음 선물하시는 분도, 받는 분도 — 기프트카드의 종류, 장점, 고르는 기준을 한눈에 정리했어요.",
        "category": "가이드",
        "date": "2026-06-05",
        "emoji": "📘",
        "media": "gift",
    },
    {
        "href": "guide.html",
        "title": "마사지 기프트카드 가이드 모음",
        "summary": "입문·금액·사용법·디지털 선물까지 핵심 가이드를 한곳에 모았습니다.",
        "category": "가이드",
        "date": "2026-06-04",
        "emoji": "📖",
        "media": "gift",
    },
    {
        "href": "tips.html",
        "title": "선물 팁 — 상황별 마사지 기프트카드 추천",
        "summary": "부모님·연인·생일·직장·셀프케어 등 상황별 선물 아이디어를 모았습니다.",
        "category": "팁",
        "date": "2026-06-03",
        "emoji": "💡",
        "media": "warm",
    },
]


def esc(s: str) -> str:
    return (
        (s or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def load_site() -> dict:
    site = json.loads(SITE_PATH.read_text(encoding="utf-8"))
    site.setdefault("domain", "https://site-015.kyungrock.deno.net")
    site.setdefault("site_name", site.get("site_title", "기프트카드"))
    site.setdefault("tagline", "마사지 기프트카드 선물 · 힐링·웰니스 정보 허브")
    return site


def load_blog_posts() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    posts = [p for p in data.get("posts", []) if p.get("published", True)]
    posts.sort(key=lambda p: p.get("date", ""), reverse=True)
    return posts


def load_all_posts_raw() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    return data.get("posts", [])


def save_posts(posts: list[dict]) -> None:
    POSTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def slugify(text: str) -> str:
    s = (text or "").strip().lower()
    s = re.sub(r"[^\w\s-가-힣]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60] or "post"


def format_date_display(d: str) -> str:
    if not d or len(d) < 10:
        return d or ""
    y, m, day = d[:10].split("-")
    return f"{y}년 {int(m)}월 {int(day)}일"


def format_date_short(d: str) -> str:
    if not d or len(d) < 10:
        return d or ""
    y, m, day = d[:10].split("-")
    return f"{y}.{m}.{day}"


def inline_format(text: str) -> str:
    s = esc(text)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    return s


def fix_escaped_html(content: str) -> str:
    if "&lt;a " not in content and "&lt;/a&gt;" not in content:
        return content
    import html as html_module

    return html_module.unescape(content)


def markdown_to_html(text: str) -> str:
    lines = (text or "").replace("\r\n", "\n").split("\n")
    parts: list[str] = []
    in_ul = False

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            parts.append("</ul>")
            in_ul = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            close_ul()
            continue
        if re.search(r"^<a\s+href=", stripped, re.I) or re.search(
            r"^<p>\s*<a\s+href=", stripped, re.I
        ):
            close_ul()
            parts.append(stripped if stripped.startswith("<p>") else f"<p>{stripped}</p>")
        elif stripped.startswith("<") and (
            stripped.endswith(">") or "</" in stripped
        ):
            close_ul()
            parts.append(stripped)
        elif stripped.startswith("### "):
            close_ul()
            parts.append(f"<h3>{inline_format(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[2:])}</h2>")
        elif stripped.startswith("* "):
            if not in_ul:
                parts.append("<ul>")
                in_ul = True
            parts.append(f"<li>{inline_format(stripped[2:])}</li>")
        else:
            close_ul()
            parts.append(f"<p>{inline_format(stripped)}</p>")

    close_ul()
    return "\n".join(parts)


def normalize_content(content: str) -> str:
    c = (content or "").strip()
    if not c:
        return ""
    if c.startswith("<"):
        return fix_escaped_html(c)
    return fix_escaped_html(markdown_to_html(c))


def site_header(site: dict, *, current: str = "", depth: int = 0) -> str:
    prefix = "../" * depth
    home = f"{prefix}index.html"

    def nav(href: str, label: str, key: str) -> str:
        cls = "fb-nav-link active" if current == key else "fb-nav-link"
        return f'<a href="{href}" class="{cls}">{label}</a>'

    return f"""  <header class="fb-header">
    <div class="fb-header-inner">
      <a href="{home}" class="fb-logo">
        <span class="fb-logo-icon">🎁</span>
        <span>{esc(site["site_name"])}</span>
      </a>
      <button class="fb-nav-toggle" aria-label="메뉴 열기" aria-expanded="false">☰</button>
      <nav class="fb-header-nav">
        {nav(home, "홈", "home")}
        {nav(f"{prefix}guide.html", "가이드", "guide")}
        {nav(f"{prefix}blog.html", "블로그", "blog")}
        {nav(f"{prefix}tips.html", "팁", "tips")}
        {nav(f"{prefix}faq.html", "FAQ", "faq")}
        {nav(f"{prefix}blog-write.html", "글쓰기", "write")}
      </nav>
    </div>
  </header>"""


def site_footer(site: dict, depth: int = 0, *, blog_active: bool = False) -> str:
    prefix = "../" * depth
    blog_cls = ' class="active"' if blog_active else ""
    return f"""  <footer class="fb-footer">
    <p class="fb-footer-brand">{esc(site["site_name"])}</p>
    <p class="fb-footer-tagline">{esc(site.get("tagline", ""))}</p>
    <p class="fb-footer-copy">&copy; 2026 {esc(site.get("site_title", "기프트카드"))} · Deno Deploy · {esc(site.get("slug", "site-015"))}</p>
  </footer>

  <nav class="fb-bottom-nav" aria-label="모바일 내비게이션">
    <div class="fb-bottom-nav-inner">
      <a href="{prefix}index.html"><span class="nav-icon">🏠</span>홈</a>
      <a href="{prefix}guide.html"><span class="nav-icon">📖</span>가이드</a>
      <a href="{prefix}blog.html"{blog_cls}><span class="nav-icon">📝</span>블로그</a>
      <a href="{prefix}tips.html"><span class="nav-icon">💡</span>팁</a>
      <a href="{prefix}faq.html"><span class="nav-icon">❓</span>FAQ</a>
    </div>
  </nav>

  <script src="{prefix}js/main.js"></script>"""


def post_url(post: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    if post.get("href"):
        return f"{prefix}{post['href']}"
    return f"{prefix}blog/{post['id']}.html"


def post_feed_item_fb(post: dict, depth: int = 0, idx: int = 0) -> str:
    url = post_url(post, depth)
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_display(post.get("date", "")))
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    emoji = post.get("emoji") or "🎁"
    media = post.get("media") or MEDIA_CLASSES[idx % len(MEDIA_CLASSES)]
    avatar = post.get("avatar") or emoji
    likes = post.get("likes", 180 + (idx * 17) % 200)

    return f"""      <article class="fb-post">
        <a href="{url}" class="fb-post-header">
          <div class="fb-post-avatar">{avatar}</div>
          <div class="fb-post-meta">
            <span class="fb-post-author">기프트카드<span class="fb-post-badge">{cat}</span></span>
            <span class="fb-post-info">{display} · 🌐</span>
          </div>
        </a>
        <div class="fb-post-body">
          <h2 class="fb-post-title">{title}</h2>
          <p class="fb-post-excerpt">{summary}</p>
        </div>
        <div class="fb-post-media {media}" aria-hidden="true">{emoji}</div>
        <div class="fb-post-stats">
          <div class="fb-reactions">
            <div class="fb-reaction-icons"><span>👍</span><span>❤️</span></div>
            <span>{likes}</span>
          </div>
          <span>댓글 · 공유</span>
        </div>
        <div class="fb-post-actions">
          <span class="fb-action-btn">👍 좋아요</span>
          <span class="fb-action-btn">💬 댓글</span>
          <span class="fb-action-btn">↗️ 공유</span>
        </div>
      </article>"""


def home_feed_items(posts: list[dict]) -> list[dict]:
    items = list(posts) + list(HOME_STATIC)
    items.sort(key=lambda p: p.get("date", ""), reverse=True)
    return items


def home_sidebar_categories_html(posts: list[dict], static_items: list[dict]) -> str:
    lines = [
        '        <a href="guide.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon guide">📖</span>',
        '          <span>가이드</span>',
        '        </a>',
        '        <a href="blog.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon gift">📝</span>',
        '          <span>블로그</span>',
        '        </a>',
        '        <a href="tips.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon tips">💡</span>',
        '          <span>선물 팁</span>',
        '        </a>',
        '        <a href="faq.html" class="fb-shortcut">',
        '          <span class="fb-shortcut-icon faq">❓</span>',
        '          <span>FAQ</span>',
        '        </a>',
    ]
    counts: dict[str, int] = {}
    for p in posts + static_items:
        cat = p.get("category") or "블로그"
        counts[cat] = counts.get(cat, 0) + 1
    for cat, n in sorted(counts.items(), key=lambda x: -x[1]):
        if cat in ("가이드", "팁"):
            continue
        lines.extend([
            f'        <a href="blog.html" class="fb-shortcut">',
            f'          <span class="fb-shortcut-icon gift">🏷️</span>',
            f'          <span>{esc(cat)} ({n})</span>',
            f'        </a>',
        ])
    return "\n".join(lines)


def home_sidebar_recent_html(items: list[dict], limit: int = 5) -> str:
    lines = []
    for p in items[:limit]:
        href = post_url(p)
        title = esc(p.get("title", ""))
        if len(title) > 24:
            title = title[:22] + "…"
        emoji = p.get("emoji") or "🎁"
        lines.extend([
            f'        <a href="{href}" class="fb-shortcut">',
            f'          <span class="fb-shortcut-icon gift">{emoji}</span>',
            f'          <span>{title}</span>',
            f'        </a>',
        ])
    return "\n".join(lines)


def replace_html_block(html: str, block: str, content: str) -> str:
    pattern = rf"(<!-- {block}_START -->).*?(<!-- {block}_END -->)"
    if not re.search(pattern, html, re.S):
        raise ValueError(f"index.html에 <!-- {block}_START/END --> 마커가 없습니다.")
    return re.sub(pattern, rf"\1\n{content}\n      \2", html, count=1, flags=re.S)


def update_post_count(html: str, count: int) -> str:
    return re.sub(
        r'(<div class="fb-stat"><strong>)\d+(</strong> 게시물)',
        rf"\g<1>{count}\2",
        html,
        count=1,
    )


def update_index_html(out_dir: Path, posts: list[dict]) -> None:
    index_path = out_dir / "index.html"
    if not index_path.is_file():
        return
    html = index_path.read_text(encoding="utf-8")
    feed = home_feed_items(posts)
    feed_html = "\n".join(
        post_feed_item_fb(p, idx=i) for i, p in enumerate(feed)
    )
    html = replace_html_block(html, "HOME_FEED", feed_html)
    html = replace_html_block(
        html, "HOME_SIDEBAR_CATEGORIES", home_sidebar_categories_html(posts, HOME_STATIC)
    )
    html = replace_html_block(
        html, "HOME_SIDEBAR_RECENT", home_sidebar_recent_html(feed)
    )
    html = update_post_count(html, len(feed))
    index_path.write_text(html, encoding="utf-8")


def blog_card_item(post: dict, idx: int = 0) -> str:
    url = post_url(post)
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_display(post.get("date", "")))
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    emoji = post.get("emoji") or "🎁"
    media = post.get("media") or MEDIA_CLASSES[idx % len(MEDIA_CLASSES)]
    gradients = {
        "gift": "linear-gradient(135deg,#667eea,#764ba2)",
        "warm": "linear-gradient(135deg,#f093fb,#f5576c)",
        "calm": "linear-gradient(135deg,#4facfe,#00f2fe)",
        "nature": "linear-gradient(135deg,#43e97b,#38f9d7)",
        "sunset": "linear-gradient(135deg,#fa709a,#fee140)",
        "luxe": "linear-gradient(135deg,#a18cd1,#fbc2eb)",
    }
    grad = gradients.get(media, gradients["gift"])
    return f"""        <a href="{url}" class="fb-card">
          <div class="fb-card-thumb" style="background:{grad}">{emoji}</div>
          <div class="fb-card-body">
            <span class="fb-card-badge">{cat}</span>
            <time class="fb-card-date" datetime="{dt}">{display}</time>
            <h2 class="fb-card-title">{title}</h2>
            <p class="fb-card-excerpt">{summary}</p>
            <span class="fb-card-link">글 읽기 →</span>
          </div>
        </a>"""


def render_blog_list(site: dict, posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    all_items = home_feed_items(posts)
    cards = "\n".join(blog_card_item(p, i) for i, p in enumerate(all_items))
    if not cards:
        cards = '        <p class="post-empty">아직 글이 없습니다. <a href="blog-write.html">첫 글 작성하기</a></p>'
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>블로그 — {esc(site["site_name"])}</title>
  <meta name="description" content="마사지 기프트카드·웰니스 블로그. 선물 가이드와 실용 팁을 모았습니다.">
  <meta name="keywords" content="{esc(site.get("keywords", ""))}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{domain}/blog.html">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
{site_header(site, current="blog")}
  <div class="fb-layout">
    <aside class="fb-sidebar fb-sidebar-left"></aside>
    <main class="fb-feed">
      <section class="page-hero">
        <h1>블로그</h1>
        <p>{esc(site.get("topic", ""))} 관련 선물·웰니스 정보를 친근하고 실용적으로 정리했습니다.</p>
        <p class="blog-write-link"><a href="blog-write.html" class="btn-blog-write">✏️ 글 작성하기</a></p>
      </section>
      <div class="fb-card-list">
{cards}
      </div>
    </main>
    <aside class="fb-sidebar fb-sidebar-right"></aside>
  </div>
{site_footer(site, blog_active=True)}
</body>
</html>
"""


def render_blog_post(site: dict, post: dict, all_posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    pid = esc(post["id"])
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    cat = esc(post.get("category", "블로그"))
    dt = esc(post.get("date", ""))
    display = esc(format_date_display(post.get("date", "")))
    author = esc(post.get("author", site["site_name"]))
    content = normalize_content(post.get("content", ""))
    emoji = post.get("emoji") or "🎁"
    media = post.get("media") or "gift"
    tags = post.get("tags") or []
    tag_html = "".join(f'<span class="fb-tag">{esc(t)}</span>' for t in tags)

    others = [p for p in all_posts if p["id"] != post["id"]][:3]
    related = ""
    if others:
        items = "\n".join(
            f'        <li><a href="{esc(p["id"])}.html">{esc(p.get("title", ""))}</a></li>'
            for p in others
        )
        related = f"""      <div class="article-content">
        <h2>다른 글 보기</h2>
        <ul>
{items}
        </ul>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — {esc(site["site_name"])}</title>
  <meta name="description" content="{summary}">
  <meta name="keywords" content="{esc(site.get("keywords", ""))}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{domain}/blog/{pid}.html">
  <meta property="og:type" content="article">
  <meta property="article:published_time" content="{dt}">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/blog.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{title}",
    "datePublished": "{dt}",
    "author": {{ "@type": "Organization", "name": "{author}" }},
    "inLanguage": "ko-KR"
  }}
  </script>
</head>
<body>
{site_header(site, current="blog", depth=1)}
  <article class="article-wrap">
    <nav class="breadcrumb"><a href="../index.html">홈</a> / <a href="../blog.html">블로그</a> / {cat}</nav>
    <article class="fb-post">
      <div class="fb-post-header">
        <div class="fb-post-avatar">{emoji}</div>
        <div class="fb-post-meta">
          <span class="fb-post-author">{esc(site["site_name"])}<span class="fb-post-badge">{cat}</span></span>
          <span class="fb-post-info">{display} · 🌐</span>
        </div>
      </div>
      <div class="fb-post-body">
        <h1 class="fb-post-title">{title}</h1>
        <p class="fb-post-excerpt">{summary}</p>
      </div>
      <div class="fb-post-media {media}" aria-hidden="true">{emoji}</div>
      <div class="fb-post-stats">
        <div class="fb-reactions"><div class="fb-reaction-icons"><span>👍</span><span>❤️</span></div><span>좋아요</span></div>
        <span>댓글 · 공유</span>
      </div>
      <div class="fb-post-actions">
        <span class="fb-action-btn">👍 좋아요</span>
        <span class="fb-action-btn">💬 댓글</span>
        <span class="fb-action-btn">↗️ 공유</span>
      </div>
    </article>
    <div class="article-content">
{content}
    </div>
    {f'<div class="fb-tag-list blog-tags-bottom">{tag_html}</div>' if tag_html else ''}
{related}
    <nav class="article-nav">
      <a href="../blog.html" class="btn btn-primary">블로그 목록</a>
    </nav>
  </article>
{site_footer(site, depth=1, blog_active=True)}
</body>
</html>
"""


def blog_sitemap_urls() -> list[str]:
    return [f"blog/{post['id']}.html" for post in load_blog_posts()]


def write_blog_pages(out_dir: Path, site: dict) -> int:
    posts = load_blog_posts()
    (out_dir / "blog.html").write_text(
        render_blog_list(site, posts), encoding="utf-8"
    )
    update_index_html(out_dir, posts)
    blog_dir = out_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    count = 1
    for post in posts:
        (blog_dir / f"{post['id']}.html").write_text(
            render_blog_post(site, post, posts), encoding="utf-8"
        )
        count += 1
    return count


def merge_draft(draft_path: Path, site: dict) -> dict:
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    if "posts" in draft:
        new_posts = draft["posts"]
    elif "id" in draft:
        new_posts = [draft]
    else:
        raise ValueError("draft JSON must be a post object or {{posts: [...]}}")

    posts = load_all_posts_raw()
    by_id = {p["id"]: i for i, p in enumerate(posts)}
    added, updated = 0, 0
    for p in new_posts:
        if not p.get("id"):
            p["id"] = slugify(p.get("title", "post")) + "-" + date.today().strftime("%Y%m%d")
        if not p.get("date"):
            p["date"] = date.today().isoformat()
        p.setdefault("published", True)
        p.setdefault("author", site.get("site_name", "기프트카드"))
        p.setdefault("category", (p.get("tags") or ["블로그"])[0] if p.get("tags") else "블로그")
        p.setdefault("emoji", "🎁")
        if p.get("content"):
            p["content"] = normalize_content(str(p["content"]))
        if p["id"] in by_id:
            posts[by_id[p["id"]]] = p
            updated += 1
        else:
            posts.append(p)
            added += 1
    posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    save_posts(posts)
    return {"added": added, "updated": updated, "total": len(posts)}


def import_legacy_posts(site: dict) -> int:
    blog_dir = ROOT / "blog"
    if not blog_dir.is_dir():
        return 0
    existing_ids = {p["id"] for p in load_all_posts_raw()}
    imported = 0
    for html_path in sorted(blog_dir.glob("*.html")):
        post_id = html_path.stem
        if post_id in existing_ids:
            continue
        text = html_path.read_text(encoding="utf-8")
        title_m = re.search(r"<h1 class=\"fb-post-title\">(.*?)</h1>", text, re.S)
        if not title_m:
            title_m = re.search(r"<h1>(.*?)</h1>", text, re.S)
        summary_m = re.search(r'<p class="fb-post-excerpt">(.*?)</p>', text, re.S)
        cat_m = re.search(r'<span class="fb-post-badge">(.*?)</span>', text)
        date_m = re.search(r'<time datetime="([^"]+)"', text) or re.search(
            r"datetime=\"([^\"]+)\"", text
        )
        body_m = re.search(
            r'<div class="article-content">\s*(.*?)\s*</div>\s*(?:<div class="fb-tag-list"|'
            r'<nav class="article-nav")',
            text,
            re.S,
        )
        if not title_m or not body_m:
            continue
        post = {
            "id": post_id,
            "title": re.sub(r"<[^>]+>", "", title_m.group(1)).strip(),
            "summary": re.sub(r"<[^>]+>", "", summary_m.group(1)).strip() if summary_m else "",
            "category": cat_m.group(1).strip() if cat_m else "블로그",
            "content": body_m.group(1).strip(),
            "tags": [cat_m.group(1).strip()] if cat_m else [],
            "author": site.get("site_name", "기프트카드"),
            "date": date_m.group(1)[:10] if date_m else date.today().isoformat(),
            "published": True,
            "emoji": "🎁",
        }
        posts = load_all_posts_raw()
        posts.append(post)
        save_posts(posts)
        existing_ids.add(post_id)
        imported += 1
    if imported:
        posts = load_all_posts_raw()
        posts.sort(key=lambda x: x.get("date", ""), reverse=True)
        save_posts(posts)
    return imported
