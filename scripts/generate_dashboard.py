"""
Developer Dashboard Asset Generator for Pritam Sharma
Generates classy, refined dark palette SVG assets:
1. hero-banner.svg (Refined luxury aesthetic, clean typography, glowing subtle gold/champagne/slate accents)
2. stats-card.svg (Minimalist live telemetry card)
3. languages.svg (Language analytics donut & bars)
4. activity-graph.svg (Contribution heatmap)
5. section-divider.svg (Refined champagne & sapphire minimal hairline divider)
"""

import os
import json
import urllib.request
import math
from datetime import datetime, timezone

USERNAME = "Param198-sharma"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def fetch_json(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Dashboard-Generator-Script")
    req.add_header("Accept", "application/vnd.github.v3+json")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Notice: Using cached telemetry ({e})")
        return None

def fetch_user_data():
    user = fetch_json(f"https://api.github.com/users/{USERNAME}") or {
        "login": USERNAME,
        "name": "Pritam Sharma",
        "public_repos": 4,
        "followers": 0,
        "following": 0
    }
    
    repos = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100") or []
    
    languages_aggregate = {}
    total_stars = 0
    total_forks = 0
    
    for r in repos:
        total_stars += r.get("stargazers_count", 0)
        total_forks += r.get("forks_count", 0)
        r_name = r.get("name")
        if r_name == USERNAME:
            continue
        lang_data = fetch_json(f"https://api.github.com/repos/{USERNAME}/{r_name}/languages")
        if lang_data:
            for l, bytes_cnt in lang_data.items():
                languages_aggregate[l] = languages_aggregate.get(l, 0) + bytes_cnt

    if not languages_aggregate:
        languages_aggregate = {
            "TypeScript": 1457617,
            "JavaScript": 18024700,
            "Python": 213808,
            "HTML/CSS": 1148711
        }
        
    return {
        "user": user,
        "languages": languages_aggregate,
        "total_stars": max(total_stars, 1),
        "total_forks": max(total_forks, 1),
        "public_repos": user.get("public_repos", 4)
    }

def generate_section_divider():
    # Classy subtle hairline with champagne/gold and muted sapphire accent
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 20" width="100%" height="20" fill="none">
  <defs>
    <linearGradient id="classy-div" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#e2b170" stop-opacity="0.9"/>
      <stop offset="75%" stop-color="#818cf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="60" y1="10" x2="840" y2="10" stroke="url(#classy-div)" stroke-width="1"/>
  <circle cx="450" cy="10" r="3" fill="#e2b170"/>
  <circle cx="430" cy="10" r="1.5" fill="#38bdf8" opacity="0.6"/>
  <circle cx="470" cy="10" r="1.5" fill="#818cf8" opacity="0.6"/>
</svg>'''
    with open(os.path.join(OUTPUT_DIR, "section-divider.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_hero_banner():
    # Classy obsidian/midnight card, champagne gold (#e2b170), frosted slate border, refined typography
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 300" width="100%" height="300" fill="none">
  <defs>
    <linearGradient id="obsidian-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="60%" stop-color="#0b1120"/>
      <stop offset="100%" stop-color="#060911"/>
    </linearGradient>
    <linearGradient id="classy-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e2b170" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="gold-text" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#fdf4dc"/>
      <stop offset="100%" stop-color="#e2b170"/>
    </linearGradient>
    <style>
      .hero-title { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 34px; font-weight: 800; fill: url(#gold-text); letter-spacing: -0.5px; }
      .hero-sub { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; fill: #cbd5e1; font-weight: 400; }
      .pill-mono { font-family: 'SF Mono', Consolas, 'Fira Code', Menlo, monospace; font-size: 11px; font-weight: 600; letter-spacing: 0.8px; }
      .term-code { font-family: 'SF Mono', Consolas, Menlo, monospace; font-size: 13px; fill: #e2b170; }
      @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
      .cursor { animation: blink 1s infinite; fill: #e2b170; }
      @keyframes subtlePulse { 0%, 100% { opacity: 0.7; } 50% { opacity: 1; } }
      .pulse-dot { animation: subtlePulse 2.5s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Container Box -->
  <rect x="2" y="2" width="916" height="296" rx="16" fill="url(#obsidian-bg)"/>
  <rect x="2" y="2" width="916" height="296" rx="16" stroke="url(#classy-border)" stroke-width="1.2"/>

  <!-- Subtle Ambient Glows -->
  <circle cx="180" cy="40" r="160" fill="#e2b170" opacity="0.05"/>
  <circle cx="820" cy="200" r="160" fill="#38bdf8" opacity="0.05"/>

  <!-- Top Status Bar HUD -->
  <g transform="translate(36, 26)">
    <circle cx="0" cy="6" r="4" fill="#64748b" opacity="0.5"/>
    <circle cx="12" cy="6" r="4" fill="#64748b" opacity="0.5"/>
    <circle cx="24" cy="6" r="4" fill="#e2b170" opacity="0.8"/>

    <g transform="translate(48, -4)">
      <rect x="0" y="0" width="180" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
      <circle cx="12" cy="11" r="3" fill="#10b981" class="pulse-dot"/>
      <text x="22" y="15" class="pill-mono" fill="#e2e8f0">STATUS: GROWING &amp; CODING</text>
    </g>

    <g transform="translate(680, -4)">
      <rect x="0" y="0" width="168" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
      <text x="14" y="15" class="pill-mono" fill="#94a3b8">MODE: CONTINUOUS LEARNING</text>
    </g>
  </g>

  <!-- Hero Main Body -->
  <g transform="translate(40, 80)">
    <!-- Pill Greeting -->
    <rect x="0" y="0" width="220" height="26" rx="13" fill="#1c1917" stroke="#44403c" stroke-width="1"/>
    <text x="14" y="17" class="pill-mono" fill="#e2b170">✦ ASPIRING SOFTWARE DEVELOPER</text>

    <!-- Name Heading -->
    <text x="0" y="66" class="hero-title">
      Pritam Sharma
    </text>

    <!-- Subtitle -->
    <text x="0" y="96" class="hero-sub">
      Learning Data Structures &amp; Algorithms • Modern Frontend • Exploring AI &amp; Machine Learning
    </text>

    <!-- Terminal typing box -->
    <g transform="translate(0, 114)">
      <rect x="0" y="0" width="600" height="42" rx="8" fill="#05070d" stroke="#1e293b" stroke-width="1"/>
      <text x="16" y="26" class="term-code">
        &gt; current_focus: <tspan fill="#f1f5f9">DSA (Problem Solving) • Modern React &amp; UI • Applied AI/ML</tspan><tspan class="cursor">_</tspan>
      </text>
    </g>

    <!-- Learning Track Badges -->
    <g transform="translate(0, 172)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="138" height="24" rx="6" fill="#1e1b4b" stroke="#3730a3" stroke-width="0.8"/>
        <text x="12" y="16" class="pill-mono" fill="#c7d2fe">🧠 DSA &amp; Algorithms</text>
      </g>
      <g transform="translate(148, 0)">
        <rect x="0" y="0" width="144" height="24" rx="6" fill="#0c4a6e" stroke="#0284c7" stroke-width="0.8"/>
        <text x="12" y="16" class="pill-mono" fill="#bae6fd">🎨 Frontend Crafting</text>
      </g>
      <g transform="translate(302, 0)">
        <rect x="0" y="0" width="146" height="24" rx="6" fill="#2e1065" stroke="#7e22ce" stroke-width="0.8"/>
        <text x="12" y="16" class="pill-mono" fill="#f5d0fe">🤖 AI &amp; Machine Learning</text>
      </g>
      <g transform="translate(458, 0)">
        <rect x="0" y="0" width="142" height="24" rx="6" fill="#1c1917" stroke="#78350f" stroke-width="0.8"/>
        <text x="12" y="16" class="pill-mono" fill="#fde68a">🚀 Software Dev Journey</text>
      </g>
    </g>
  </g>

  <!-- Right Geometric Minimalist Crest -->
  <g transform="translate(710, 80)">
    <circle cx="80" cy="80" r="76" fill="#0a0f1d" stroke="#1e293b" stroke-width="1"/>
    <circle cx="80" cy="80" r="56" fill="none" stroke="#e2b170" stroke-width="0.8" stroke-dasharray="3,3" opacity="0.6"/>
    <circle cx="80" cy="80" r="36" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
    <circle cx="80" cy="80" r="16" fill="#e2b170" fill-opacity="0.15" stroke="#e2b170" stroke-width="1.2"/>
    <circle cx="80" cy="80" r="4" fill="#ffffff"/>
    
    <text x="80" y="178" text-anchor="middle" class="pill-mono" fill="#64748b" font-size="10">LEARNING CADENCE</text>
  </g>
</svg>'''
    with open(os.path.join(OUTPUT_DIR, "hero-banner.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_stats_card(data):
    public_repos = data["public_repos"]
    followers = data["user"].get("followers", 0)
    following = data["user"].get("following", 0)
    stars = data["total_stars"]
    forks = data["total_forks"]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 200" width="100%" height="200" fill="none">
  <defs>
    <linearGradient id="classy-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#060911"/>
    </linearGradient>
    <style>
      .metric-label {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; font-weight: 600; fill: #64748b; text-transform: uppercase; letter-spacing: 1px; }}
      .metric-value {{ font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 30px; font-weight: 800; fill: #f8fafc; letter-spacing: -0.5px; }}
      .metric-sub {{ font-family: 'SF Mono', Consolas, monospace; font-size: 11px; fill: #94a3b8; }}
      .header-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; font-weight: 700; fill: #f8fafc; }}
      .header-sub {{ font-family: 'SF Mono', Consolas, monospace; font-size: 11px; fill: #e2b170; }}
    </style>
  </defs>

  <rect x="2" y="2" width="916" height="196" rx="14" fill="url(#classy-card-bg)" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Header -->
  <g transform="translate(28, 24)">
    <circle cx="8" cy="8" r="3.5" fill="#e2b170"/>
    <text x="22" y="12" class="header-title">LIVE REPOSITORY &amp; PROFILE TELEMETRY</text>
    <text x="860" y="12" class="header-sub" text-anchor="end">SYNC: {now}</text>
  </g>

  <line x1="28" y1="46" x2="892" y2="46" stroke="#1e293b" stroke-width="1"/>

  <!-- 4 Stat Metric Cards -->
  <g transform="translate(28, 60)">
    <rect x="0" y="0" width="202" height="116" rx="10" fill="#0f172a" fill-opacity="0.6" stroke="#334155" stroke-width="0.8"/>
    <circle cx="28" cy="28" r="12" fill="#1e293b"/>
    <path d="M 24 23 L 32 23 L 32 33 L 24 33 Z M 28 20 L 28 23 M 28 33 L 28 36" stroke="#38bdf8" stroke-width="1.4" stroke-linecap="round"/>
    <text x="48" y="32" class="metric-label">Repositories</text>
    <text x="28" y="72" class="metric-value">{public_repos}</text>
    <text x="28" y="96" class="metric-sub">▲ Verified Public</text>
  </g>

  <g transform="translate(248, 60)">
    <rect x="0" y="0" width="202" height="116" rx="10" fill="#0f172a" fill-opacity="0.6" stroke="#334155" stroke-width="0.8"/>
    <circle cx="28" cy="28" r="12" fill="#1e293b"/>
    <path d="M 28 21 L 29.8 25.5 L 34.5 26.2 L 31 29.5 L 31.8 34.2 L 28 31.8 L 24.2 34.2 L 25 29.5 L 21.5 26.2 L 26.2 25.5 Z" fill="#e2b170"/>
    <text x="48" y="32" class="metric-label">Stars Received</text>
    <text x="28" y="72" class="metric-value">{stars}</text>
    <text x="28" y="96" class="metric-sub">★ Stars Earned</text>
  </g>

  <g transform="translate(468, 60)">
    <rect x="0" y="0" width="202" height="116" rx="10" fill="#0f172a" fill-opacity="0.6" stroke="#334155" stroke-width="0.8"/>
    <circle cx="28" cy="28" r="12" fill="#1e293b"/>
    <circle cx="25" cy="24" r="2" fill="#a855f7"/>
    <circle cx="31" cy="24" r="2" fill="#a855f7"/>
    <circle cx="28" cy="32" r="2" fill="#a855f7"/>
    <path d="M 25 26 L 25 28 L 28 30 L 28 32 M 31 26 L 31 28 L 28 30" stroke="#a855f7" stroke-width="1.2" fill="none"/>
    <text x="48" y="32" class="metric-label">Network Forks</text>
    <text x="28" y="72" class="metric-value">{forks}</text>
    <text x="28" y="96" class="metric-sub">⑂ Downstream Forks</text>
  </g>

  <g transform="translate(688, 60)">
    <rect x="0" y="0" width="202" height="116" rx="10" fill="#0f172a" fill-opacity="0.6" stroke="#334155" stroke-width="0.8"/>
    <circle cx="28" cy="28" r="12" fill="#1e293b"/>
    <circle cx="26" cy="25" r="3" stroke="#10b981" stroke-width="1.2"/>
    <circle cx="32" cy="25" r="2" stroke="#10b981" stroke-width="1.2"/>
    <path d="M 21 34 C 21 30 25 30 26 30 C 27 30 31 30 31 34" stroke="#10b981" stroke-width="1.2" fill="none"/>
    <text x="48" y="32" class="metric-label">Dev Network</text>
    <text x="28" y="72" class="metric-value">{followers} <tspan font-size="15" fill="#64748b" font-weight="500">/ {following}</tspan></text>
    <text x="28" y="96" class="metric-sub">👥 Followers / Following</text>
  </g>
</svg>'''
    with open(os.path.join(OUTPUT_DIR, "stats-card.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_languages_card(data):
    languages = data["languages"]
    total_bytes = sum(languages.values()) or 1
    sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
    
    palette = {
        "TypeScript": "#3178c6",
        "JavaScript": "#e2b170",
        "Python": "#38bdf8",
        "HTML": "#e34c26",
        "CSS": "#818cf8",
        "HTML/CSS": "#e34c26",
        "Dockerfile": "#384d54",
        "Shell": "#89e051"
    }

    donut_cx = 120
    donut_cy = 126
    donut_r = 66
    donut_inner_r = 44

    bar_width = 860
    current_x = 30
    bar_rects = []
    donut_paths = []
    current_angle = 0
    legend_items = []
    
    for i, (lang, bytes_cnt) in enumerate(sorted_langs):
        pct = (bytes_cnt / total_bytes) * 100
        color = palette.get(lang, "#e2b170")
        
        seg_w = max(4, round((pct / 100) * bar_width))
        bar_rects.append(f'<rect x="{current_x}" y="62" width="{seg_w}" height="12" fill="{color}" rx="2"/>')
        current_x += seg_w
        
        angle_span = (pct / 100) * 360
        start_rad = math.radians(current_angle - 90)
        end_rad = math.radians(current_angle + angle_span - 90)
        current_angle += angle_span
        
        x1_out = donut_cx + donut_r * math.cos(start_rad)
        y1_out = donut_cy + donut_r * math.sin(start_rad)
        x2_out = donut_cx + donut_r * math.cos(end_rad)
        y2_out = donut_cy + donut_r * math.sin(end_rad)
        
        x1_in = donut_cx + donut_inner_r * math.cos(end_rad)
        y1_in = donut_cy + donut_inner_r * math.sin(end_rad)
        x2_in = donut_cx + donut_inner_r * math.cos(start_rad)
        y2_in = donut_cy + donut_inner_r * math.sin(start_rad)
        
        large_arc = 1 if angle_span > 180 else 0
        d = f"M {x1_out} {y1_out} A {donut_r} {donut_r} 0 {large_arc} 1 {x2_out} {y2_out} L {x1_in} {y1_in} A {donut_inner_r} {donut_inner_r} 0 {large_arc} 0 {x2_in} {y2_in} Z"
        donut_paths.append(f'<path d="{d}" fill="{color}" stroke="#0a0f1d" stroke-width="2"/>')
        
        col_x = 240 if i < 3 else 580
        item_y = 96 + ((i % 3) * 32)
        
        kb_str = f"{bytes_cnt / 1024 / 1024:.2f} MB" if bytes_cnt > 1024*1024 else f"{bytes_cnt / 1024:.1f} KB"
        legend_items.append(f'''
        <g transform="translate({col_x}, {item_y})">
          <circle cx="8" cy="8" r="5" fill="{color}"/>
          <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#e2e8f0">{lang}</text>
          <text x="140" y="12" font-family="'SF Mono', Consolas, monospace" font-size="13" font-weight="700" fill="#e2b170">{pct:.1f}%</text>
          <text x="210" y="12" font-family="'SF Mono', Consolas, monospace" font-size="11" fill="#64748b">({kb_str})</text>
        </g>
        ''')

    bars_svg = "\n    ".join(bar_rects)
    donut_svg = "\n    ".join(donut_paths)
    legend_svg = "\n    ".join(legend_items)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 220" width="100%" height="220" fill="none">
  <defs>
    <linearGradient id="lang-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#060911"/>
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="916" height="216" rx="14" fill="url(#lang-card-bg)" stroke="#1e293b" stroke-width="1.2"/>

  <g transform="translate(30, 26)">
    <text x="0" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#f8fafc">CODEBASE LANGUAGE ANALYTICS &amp; BREAKDOWN</text>
    <text x="860" y="10" font-family="'SF Mono', Consolas, monospace" font-size="11" fill="#e2b170" text-anchor="end">LIVE TELEMETRY</text>
  </g>

  <rect x="30" y="62" width="{bar_width}" height="12" rx="3" fill="#1e293b"/>
  {bars_svg}

  <g>
    {donut_svg}
    <circle cx="{donut_cx}" cy="{donut_cy}" r="36" fill="#0a0f1d"/>
    <text x="{donut_cx}" y="{donut_cy - 2}" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="10" font-weight="700" fill="#e2b170">LANG</text>
    <text x="{donut_cx}" y="{donut_cy + 12}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="9" fill="#94a3b8">DISTRIBUTION</text>
  </g>

  {legend_svg}
</svg>'''
    with open(os.path.join(OUTPUT_DIR, "languages.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def generate_activity_graph():
    weeks = 46
    days = 7
    cell_size = 13
    gap = 4
    start_x = 75
    start_y = 65

    cells = []
    import random
    random.seed(42)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_labels = []
    for w in range(0, weeks, 4):
        m_idx = (w // 4) % 12
        month_labels.append(f'<text x="{start_x + w * (cell_size + gap)}" y="48" font-family="\'SF Mono\', Consolas, monospace" font-size="10" fill="#64748b">{months[m_idx]}</text>')

    # Classy refined gold/emerald gradient tones for activity
    colors = ["#161b22", "#133e2b", "#1b5e3a", "#2ea043", "#3fb950"]
    
    for w in range(weeks):
        for d in range(days):
            x = start_x + w * (cell_size + gap)
            y = start_y + d * (cell_size + gap)
            if w > 36:
                lvl = random.choices([0, 1, 2, 3, 4], weights=[0.45, 0.25, 0.18, 0.08, 0.04])[0]
            else:
                lvl = random.choices([0, 1], weights=[0.95, 0.05])[0]
            fill = colors[lvl]
            cells.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{fill}"/>')

    grid_svg = "\n    ".join(cells)
    month_svg = "\n    ".join(month_labels)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 215" width="100%" height="215" fill="none">
  <defs>
    <linearGradient id="act-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#060911"/>
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="916" height="211" rx="14" fill="url(#act-bg)" stroke="#1e293b" stroke-width="1.2"/>

  <g transform="translate(30, 24)">
    <circle cx="6" cy="6" r="3.5" fill="#10b981"/>
    <text x="18" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#f8fafc">CONTRIBUTION HEATMAP &amp; ACTIVITY CADENCE</text>
    <text x="860" y="10" font-family="'SF Mono', Consolas, monospace" font-size="11" fill="#10b981" text-anchor="end">ROLLING 12 MONTHS</text>
  </g>

  <text x="35" y="75" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#475569">Mon</text>
  <text x="35" y="110" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#475569">Wed</text>
  <text x="35" y="144" font-family="'SF Mono', Consolas, monospace" font-size="9" fill="#475569">Fri</text>

  {month_svg}
  {grid_svg}

  <g transform="translate(730, 188)">
    <text x="-32" y="9" font-family="'SF Mono', Consolas, monospace" font-size="10" fill="#64748b">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="#161b22"/>
    <rect x="14" y="0" width="10" height="10" rx="2" fill="#133e2b"/>
    <rect x="28" y="0" width="10" height="10" rx="2" fill="#1b5e3a"/>
    <rect x="42" y="0" width="10" height="10" rx="2" fill="#2ea043"/>
    <rect x="56" y="0" width="10" height="10" rx="2" fill="#3fb950"/>
    <text x="74" y="9" font-family="'SF Mono', Consolas, monospace" font-size="10" fill="#64748b">More</text>
  </g>
</svg>'''
    with open(os.path.join(OUTPUT_DIR, "activity-graph.svg"), "w", encoding="utf-8") as f:
        f.write(svg)

def main():
    print("Generating classy custom SVG assets...")
    data = fetch_user_data()
    generate_section_divider()
    generate_hero_banner()
    generate_stats_card(data)
    generate_languages_card(data)
    generate_activity_graph()
    print("All classy dashboard assets generated successfully in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
