#!/usr/bin/env python3
"""Generate 1280×720 fslides HTML pages for the Cisco Search / AI deck."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

BASE_CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { width: 100%; height: 100%; overflow: hidden; background: #22242C; }
body {
  width: 1280px; height: 720px; overflow: hidden; position: absolute;
  font-family: 'Inter', -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased; background: #22242C;
  display: flex; flex-direction: column; color: #fff;
}
body::before {
  content: ''; position: fixed; inset: 0;
  background-image: radial-gradient(circle, rgba(255,255,255,0.035) 1px, transparent 1px);
  background-size: 28px 28px; pointer-events: none; z-index: 0;
}
.accent-bar {
  position: fixed; top: 0; left: 0; width: 4px; height: 100%;
  background: #00BFB3; z-index: 20;
}
@keyframes fade-up {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
.f1 { opacity: 0; animation: fade-up 0.5s ease forwards 0.10s; }
.f2 { opacity: 0; animation: fade-up 0.5s ease forwards 0.22s; }
.f3 { opacity: 0; animation: fade-up 0.5s ease forwards 0.34s; }
.f4 { opacity: 0; animation: fade-up 0.5s ease forwards 0.50s; }
.f5 { opacity: 0; animation: fade-up 0.5s ease forwards 0.66s; }
.f6 { opacity: 0; animation: fade-up 0.5s ease forwards 0.82s; }
.f7 { opacity: 0; animation: fade-up 0.5s ease forwards 1.00s; }
.slide {
  position: relative; z-index: 10; flex: 1; min-height: 0;
  display: flex; flex-direction: column; padding: 28px 52px 20px;
}
.eyebrow {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.16em;
  text-transform: uppercase; color: #00BFB3; margin-bottom: 8px;
}
.headline {
  font-size: 2.05rem; font-weight: 300; letter-spacing: -0.025em;
  line-height: 1.12; color: #fff; margin-bottom: 6px;
}
.headline strong { font-weight: 800; color: #00BFB3; }
.sub { font-size: 0.86rem; color: rgba(255,255,255,0.45); max-width: 820px; }
.divider { height: 1px; background: rgba(255,255,255,0.07); margin: 14px 0 18px; }
.footer {
  margin-top: auto; padding-top: 12px;
  display: flex; align-items: center; gap: 12px;
  font-size: 0.68rem; color: rgba(255,255,255,0.28);
}
.footer .tag { color: #049FD9; font-weight: 600; }
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; flex: 1; min-height: 0; }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; flex: 1; min-height: 0; }
.card {
  background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px; padding: 18px 20px;
}
.card .label {
  font-size: 0.62rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: #00BFB3; margin-bottom: 8px;
}
.card h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 8px; }
.card p { font-size: 0.82rem; color: rgba(255,255,255,0.55); line-height: 1.5; }
.card ul { margin: 8px 0 0 1.1rem; font-size: 0.8rem; color: rgba(255,255,255,0.55); line-height: 1.55; }
.card li { margin: 4px 0; }
.card li strong { color: #fff; font-weight: 600; }
.pill-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0 0; }
.pill {
  font-size: 0.68rem; padding: 5px 12px; border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.14); color: rgba(255,255,255,0.55);
}
.pill.hot { border-color: rgba(0,191,179,0.55); color: #00BFB3; }
.pill.future { border-color: rgba(167,139,250,0.55); color: #c4b5fd; }
.quote {
  border-left: 3px solid #049FD9; padding: 12px 16px;
  background: rgba(4,159,217,0.07); border-radius: 0 10px 10px 0;
  font-size: 0.92rem; color: rgba(255,255,255,0.85); line-height: 1.45;
}
.mono { font-family: 'JetBrains Mono', ui-monospace, monospace; color: #00BFB3; font-size: 0.85em; }
"""


def page(title: str, extra_css: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
{BASE_CSS}
{extra_css}
  </style>
</head>
<body>
  <div class="accent-bar"></div>
{body}
</body>
</html>
"""


def footer(tag: str = "Cisco × Elastic · Serverless Search") -> str:
    return f"""  <div class="footer">
    <span class="tag">{tag}</span>
    <span>·</span>
    <span>The Search AI Company</span>
  </div>"""


SLIDES: dict[str, str] = {}

# ── Cover ────────────────────────────────────────────────────────────────────
SLIDES["cover.html"] = page(
    "Elastic Search — AI, Federated Sources & Agent Builder",
    """
    body { justify-content: space-between; }
    .elastic-mark {
      position: fixed; right: -80px; top: 50%; transform: translateY(-50%);
      width: 560px; height: 560px; pointer-events: none; z-index: 1; opacity: 0.9;
    }
    .content {
      position: relative; z-index: 10; padding: 0 6vw; flex: 1;
      display: flex; flex-direction: column; justify-content: center; max-width: 62%;
    }
    .c-eyebrow {
      font-size: 0.75rem; font-weight: 700; letter-spacing: 0.16em;
      text-transform: uppercase; color: #00BFB3; margin-bottom: 1.4rem;
    }
    .c-title {
      font-size: 3.4rem; font-weight: 800; letter-spacing: -0.03em;
      line-height: 1.05; margin-bottom: 1.2rem;
    }
    .c-sub {
      font-size: 1.1rem; font-weight: 400; color: rgba(255,255,255,0.62);
      line-height: 1.55; max-width: 520px; margin-bottom: 1.8rem;
    }
    .cover-foot {
      position: relative; z-index: 10; padding: 0 6vw 36px;
      display: flex; align-items: center; gap: 14px;
      font-size: 0.78rem; color: rgba(255,255,255,0.35);
    }
    .cover-foot .word { font-weight: 700; color: rgba(255,255,255,0.7); }
    """,
    """
  <svg class="elastic-mark" viewBox="0 0 237 236" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path fill="#F04E23" d="M118.5 0C53 0 0 53 0 118.5S53 237 118.5 237 237 184 237 118.5 184 0 118.5 0z" opacity="0.12"/>
    <circle cx="168" cy="72" r="28" fill="#FEC514" opacity="0.35"/>
    <circle cx="72" cy="96" r="22" fill="#00BFB3" opacity="0.4"/>
    <circle cx="150" cy="150" r="34" fill="#00A9E0" opacity="0.28"/>
    <circle cx="90" cy="168" r="18" fill="#F04E23" opacity="0.35"/>
  </svg>
  <div class="content">
    <div class="c-eyebrow f1">Cisco × Elastic · Workshop briefing</div>
    <h1 class="c-title f2">AI Search.<br>Federated Sources.<br>Agent Builder.</h1>
    <p class="c-sub f3">One Serverless Search project. Hybrid retrieval, unified query across Cisco knowledge, and grounded agents for the NOC — without Observability or Security SKUs.</p>
    <div class="pill-row f4">
      <span class="pill hot">Serverless Search</span>
      <span class="pill">ES|QL</span>
      <span class="pill">Connectors</span>
      <span class="pill future">Blob federation roadmap</span>
    </div>
  </div>
  <div class="cover-foot f5">
    <span class="word">elastic</span>
    <span>·</span>
    <span>The Search AI Company</span>
    <span>·</span>
    <span>Instruqt lab ~3–4 min to ready</span>
  </div>
""",
)

# ── Agenda ───────────────────────────────────────────────────────────────────
SLIDES["agenda.html"] = page(
    "Agenda — Three modules",
    """
    .mod { display: flex; flex-direction: column; gap: 8px; }
    .num {
      font-family: 'JetBrains Mono', monospace; font-size: 0.7rem;
      font-weight: 700; color: #049FD9; letter-spacing: 0.08em;
    }
    .mod h3 { font-size: 1.15rem; font-weight: 700; }
    .mod p { font-size: 0.82rem; color: rgba(255,255,255,0.5); line-height: 1.5; }
    .arrow {
      align-self: center; color: rgba(255,255,255,0.25); font-size: 1.4rem; padding: 0 4px;
    }
    .flow { display: flex; align-items: stretch; gap: 10px; flex: 1; }
    .flow .card { flex: 1; display: flex; flex-direction: column; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Today</div>
    <h1 class="headline f2">Three beats. <strong>One Search project.</strong></h1>
    <p class="sub f2">Same indices power search, federation, and agents — Search-led GTM for Cisco.</p>
    <div class="divider"></div>
    <div class="flow">
      <div class="card mod f3">
        <span class="num">MODULE 01</span>
        <h3>AI Search</h3>
        <p>Hybrid + semantic retrieval on <span class="mono">cisco-network-kb</span>. Exact TAC phrases and natural-language questions in one ranked result set.</p>
      </div>
      <div class="arrow f3">→</div>
      <div class="card mod f4">
        <span class="num">MODULE 02</span>
        <h3>Federated sources</h3>
        <p>KB, internal runbooks, Meraki events — connectors and multi-index ES|QL without ripping out existing systems.</p>
      </div>
      <div class="arrow f4">→</div>
      <div class="card mod f5">
        <span class="num">MODULE 03</span>
        <h3>Agent Builder</h3>
        <p>ES|QL triage + agents grounded in the same Search indices. Cisco NOC story, Search-only motion.</p>
      </div>
    </div>
{footer()}
  </div>
""",
)

# ── Pain ─────────────────────────────────────────────────────────────────────
SLIDES["pain.html"] = page(
    "NOC knowledge in silos",
    """
    .silos {
      display: flex; align-items: center; justify-content: space-between;
      gap: 10px; margin: 8px 0 20px; flex-wrap: wrap;
    }
    .silo {
      flex: 1; min-width: 140px; text-align: center;
      padding: 16px 12px; border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.1);
      background: rgba(255,255,255,0.03);
    }
    .silo strong { display: block; font-size: 0.9rem; margin-bottom: 4px; }
    .silo span { font-size: 0.72rem; color: rgba(255,255,255,0.4); }
    .hop { color: rgba(240,78,35,0.7); font-size: 1.3rem; font-weight: 300; }
    .bars { display: flex; align-items: flex-end; gap: 28px; height: 140px; margin-top: 8px; }
    .bar-col { flex: 1; text-align: center; }
    .bar {
      width: 100%; border-radius: 8px 8px 0 0;
      background: linear-gradient(180deg, #049FD9, #0369a1);
    }
    .bar.bad { height: 92%; opacity: 0.85; }
    .bar.good {
      height: 38%;
      background: linear-gradient(180deg, #00BFB3, #0d9488);
    }
    .bar-col span { display: block; margin-top: 10px; font-size: 0.75rem; color: rgba(255,255,255,0.45); }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Why this matters</div>
    <h1 class="headline f2">Cisco NOC pain: <strong>knowledge in silos</strong></h1>
    <p class="sub f2">Engineers tab-hop across Meraki, IOS-XE runbooks, DNA Center, and internal wikis while MTTR climbs.</p>
    <div class="divider"></div>
    <div class="silos f3">
      <div class="silo"><strong>Meraki</strong><span>Dashboard</span></div>
      <span class="hop">→</span>
      <div class="silo"><strong>IOS-XE</strong><span>Runbooks</span></div>
      <span class="hop">→</span>
      <div class="silo"><strong>DNA Center</strong><span>Assurance</span></div>
      <span class="hop">→</span>
      <div class="silo"><strong>Internal wiki</strong><span>Escalation</span></div>
    </div>
    <div class="bars f4">
      <div class="bar-col"><div class="bar bad"></div><span>Today · tab hopping · long MTTR</span></div>
      <div class="bar-col"><div class="bar good"></div><span>Target · one Search · faster resolution</span></div>
    </div>
{footer()}
  </div>
""",
)

# ── Serverless ───────────────────────────────────────────────────────────────
SLIDES["serverless.html"] = page(
    "One Serverless Search project",
    "",
    f"""
  <div class="slide">
    <div class="eyebrow f1">Platform choice</div>
    <h1 class="headline f2">One <strong>Serverless Search</strong> project — advantages</h1>
    <p class="sub f2">Search-led motion for Cisco: no Observability or Security provisioning for this workshop.</p>
    <div class="divider"></div>
    <div class="grid2">
      <div class="card f3"><div class="label">Speed to lab</div><h3>~3–4 min startup</h3><p>Single vector Search project + seeded Cisco indices — no multi-product wait.</p></div>
      <div class="card f3"><div class="label">GTM fit</div><h3>Search consolidation</h3><p>Position AI on Search; avoid O11Y/Sec where Cisco isn’t buying those SKUs.</p></div>
      <div class="card f4"><div class="label">Technical</div><h3>ES|QL everywhere</h3><p>Same query language for KB, connectors, and agent tools — one skill for SEs.</p></div>
      <div class="card f4"><div class="label">Economics</div><h3>Serverless ops</h3><p>Per-learner Cloud projects in Instruqt; elastic scale for POVs and workshops.</p></div>
    </div>
{footer()}
  </div>
""",
)

# ── AI Search ────────────────────────────────────────────────────────────────
SLIDES["ai-search.html"] = page(
    "AI Search — what & why",
    "",
    f"""
  <div class="slide">
    <div class="eyebrow f1">Module 1</div>
    <h1 class="headline f2">AI Search — <strong>what &amp; why</strong></h1>
    <p class="sub f2">Hybrid + semantic search on <span class="mono">cisco-network-kb</span> — Meraki, BGP, DNA runbooks in seconds.</p>
    <div class="divider"></div>
    <div class="grid2">
      <div class="card f3">
        <div class="label">What</div>
        <h3>Keyword + vector</h3>
        <ul>
          <li><strong>BM25</strong> for exact TAC phrases and error codes</li>
          <li><strong>Semantic / ELSER</strong> for “AP keeps going offline”</li>
          <li><strong>RRF merge</strong> for one ranked result set</li>
        </ul>
      </div>
      <div class="card f4">
        <div class="label">Why buyers care</div>
        <h3>Shorter MTTR</h3>
        <ul>
          <li><strong>One surface</strong> instead of six portals</li>
          <li><strong>Scale</strong> via connectors (Module 2)</li>
          <li><strong>Proof</strong> live Search + ES|QL in the first 20 minutes</li>
        </ul>
      </div>
    </div>
    <div class="quote f5" style="margin-top:16px">“Can we search IOS-XE and Meraki docs in one place?” — this module is the answer.</div>
{footer("Module 1 · AI Search")}
  </div>
""",
)

# ── Hybrid diagram ───────────────────────────────────────────────────────────
SLIDES["hybrid.html"] = page(
    "Hybrid retrieval",
    """
    .ig { flex: 1; display: flex; align-items: center; justify-content: center; }
    .ig svg { width: 100%; max-height: 420px; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Module 1 · Infographic</div>
    <h1 class="headline f2">Hybrid retrieval — <strong>how it works</strong></h1>
    <p class="sub f2">Exact TAC phrases + natural language → one hybrid result set on the Cisco KB.</p>
    <div class="divider"></div>
    <div class="ig f3">
      <svg viewBox="0 0 1100 320" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="120" width="150" height="80" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.15)"/>
        <text x="95" y="152" fill="#fff" font-size="15" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">NOC query</text>
        <text x="95" y="176" fill="rgba(255,255,255,0.45)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">“AP offline”</text>
        <path d="M170 160 H230" stroke="#049FD9" stroke-width="2.5"/>
        <path d="M230 100 H300" stroke="#049FD9" stroke-width="2.5"/>
        <path d="M230 160 H300" stroke="#00BFB3" stroke-width="2.5"/>
        <path d="M230 220 H300" stroke="#a78bfa" stroke-width="2.5"/>
        <rect x="300" y="70" width="200" height="60" rx="12" fill="rgba(4,159,217,0.1)" stroke="#049FD9"/>
        <text x="400" y="105" fill="#049FD9" font-size="14" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Keyword (BM25)</text>
        <rect x="300" y="145" width="200" height="60" rx="12" fill="rgba(0,191,179,0.1)" stroke="#00BFB3"/>
        <text x="400" y="180" fill="#00BFB3" font-size="14" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Semantic (vector)</text>
        <path d="M500 100 H560" stroke="#049FD9" stroke-width="2.5"/>
        <path d="M500 175 H560" stroke="#00BFB3" stroke-width="2.5"/>
        <path d="M560 160 H620" stroke="#6ee7c7" stroke-width="2.5"/>
        <rect x="620" y="115" width="200" height="90" rx="14" fill="rgba(0,191,179,0.12)" stroke="#00BFB3"/>
        <text x="720" y="155" fill="#fff" font-size="16" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">RRF merge</text>
        <text x="720" y="180" fill="rgba(255,255,255,0.5)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">ranked runbooks</text>
        <path d="M820 160 H880" stroke="#6ee7c7" stroke-width="2.5"/>
        <rect x="880" y="120" width="190" height="80" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.15)"/>
        <text x="975" y="158" fill="#6ee7c7" font-size="13" font-weight="700" text-anchor="middle" font-family="JetBrains Mono,monospace">cisco-network-kb</text>
        <text x="975" y="180" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">answers in seconds</text>
      </svg>
    </div>
{footer("Module 1 · AI Search")}
  </div>
""",
)

# ── Federated ────────────────────────────────────────────────────────────────
SLIDES["federated.html"] = page(
    "Federated data sources",
    """
    .ig { flex: 1; display: flex; align-items: center; }
    .ig svg { width: 100%; max-height: 380px; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Module 2</div>
    <h1 class="headline f2">Federated data sources — <strong>what &amp; why</strong></h1>
    <p class="sub f2">Federate, don’t rip-and-replace. Leave Meraki/DNA in place; Elastic becomes the query layer.</p>
    <div class="divider"></div>
    <div class="ig f3">
      <svg viewBox="0 0 1100 300" xmlns="http://www.w3.org/2000/svg">
        <rect x="40" y="30" width="160" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)"/>
        <text x="120" y="60" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">cisco.com KB</text>
        <text x="120" y="80" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">product docs</text>
        <rect x="40" y="115" width="160" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)"/>
        <text x="120" y="145" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Internal runbooks</text>
        <text x="120" y="165" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">escalation</text>
        <rect x="40" y="200" width="160" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)"/>
        <text x="120" y="230" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Meraki events</text>
        <text x="120" y="250" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">connector signals</text>
        <path d="M200 65 C280 65 280 150 360 150" fill="none" stroke="#049FD9" stroke-width="2.5"/>
        <path d="M200 150 H360" fill="none" stroke="#049FD9" stroke-width="2.5"/>
        <path d="M200 235 C280 235 280 150 360 150" fill="none" stroke="#049FD9" stroke-width="2.5"/>
        <rect x="360" y="100" width="240" height="100" rx="14" fill="rgba(0,191,179,0.1)" stroke="#00BFB3" stroke-dasharray="6 4"/>
        <text x="480" y="140" fill="#00BFB3" font-size="15" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">Serverless Search</text>
        <text x="480" y="165" fill="rgba(255,255,255,0.5)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">connectors + indices</text>
        <text x="480" y="185" fill="rgba(255,255,255,0.35)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">leave sources in place</text>
        <path d="M600 150 H680" stroke="#6ee7c7" stroke-width="2.5"/>
        <rect x="680" y="105" width="180" height="90" rx="12" fill="rgba(4,159,217,0.12)" stroke="#049FD9"/>
        <text x="770" y="145" fill="#049FD9" font-size="15" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">One ES|QL</text>
        <text x="770" y="170" fill="rgba(255,255,255,0.5)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">cross-index story</text>
        <path d="M860 150 H920" stroke="#6ee7c7" stroke-width="2.5"/>
        <rect x="920" y="110" width="140" height="80" rx="12" fill="rgba(0,191,179,0.12)" stroke="#00BFB3"/>
        <text x="990" y="150" fill="#6ee7c7" font-size="14" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">Unified</text>
        <text x="990" y="172" fill="rgba(255,255,255,0.45)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">NOC view</text>
      </svg>
    </div>
{footer("Module 2 · Federated sources")}
  </div>
""",
)

# ── ES|QL ────────────────────────────────────────────────────────────────────
SLIDES["esql.html"] = page(
    "ES|QL across sources",
    """
    .code {
      flex: 1; background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 22px 26px; font-family: 'JetBrains Mono', monospace;
      font-size: 0.92rem; line-height: 1.7; color: rgba(255,255,255,0.75); overflow: hidden;
    }
    .code .kw { color: #00BFB3; }
    .code .str { color: #FEC514; }
    .code .cm { color: rgba(255,255,255,0.3); }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Module 2 · Query layer</div>
    <h1 class="headline f2">One language: <strong>ES|QL</strong></h1>
    <p class="sub f2">Offline Meraki event + internal escalation + KB runbook — one query, one skill for SEs and agents.</p>
    <div class="divider"></div>
    <div class="code f3">
      <span class="cm">// Correlate branch offline signal with runbook steps</span><br>
      <span class="kw">FROM</span> cisco-meraki-events, cisco-internal-runbooks, cisco-network-kb<br>
      <span class="kw">| WHERE</span> branch.id == <span class="str">"4471"</span> <span class="kw">OR</span> topic <span class="kw">LIKE</span> <span class="str">"*offline*"</span><br>
      <span class="kw">| KEEP</span> @timestamp, source, title, severity, next_steps<br>
      <span class="kw">| SORT</span> @timestamp <span class="kw">DESC</span><br>
      <span class="kw">| LIMIT</span> 20
    </div>
{footer("Module 2 · Federated sources")}
  </div>
""",
)

# ── Agents ───────────────────────────────────────────────────────────────────
SLIDES["agents.html"] = page(
    "Agent Builder",
    """
    .ig { flex: 1; display: flex; align-items: center; }
    .ig svg { width: 100%; max-height: 360px; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Module 3</div>
    <h1 class="headline f2">Agent Builder — <strong>search to action</strong></h1>
    <p class="sub f2">Agents + ES|QL on Search indices. Grounded tools — no hallucinated runbooks. Still Search-only.</p>
    <div class="divider"></div>
    <div class="ig f3">
      <svg viewBox="0 0 1100 280" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="90" width="150" height="90" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)"/>
        <text x="105" y="130" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">Network</text>
        <text x="105" y="152" fill="rgba(255,255,255,0.45)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">signals</text>
        <path d="M180 135 H230" stroke="#049FD9" stroke-width="2.5"/>
        <rect x="230" y="90" width="140" height="90" rx="12" fill="rgba(4,159,217,0.1)" stroke="#049FD9"/>
        <text x="300" y="130" fill="#049FD9" font-size="14" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">ES|QL</text>
        <text x="300" y="152" fill="rgba(255,255,255,0.45)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">triage</text>
        <path d="M370 135 H420" stroke="#a78bfa" stroke-width="2.5"/>
        <rect x="420" y="70" width="200" height="130" rx="14" fill="rgba(167,139,250,0.1)" stroke="#a78bfa"/>
        <text x="520" y="115" fill="#c4b5fd" font-size="15" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">Agent Builder</text>
        <text x="520" y="140" fill="rgba(255,255,255,0.5)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">tools → indices</text>
        <text x="520" y="162" fill="rgba(255,255,255,0.4)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">grounded retrieval</text>
        <text x="520" y="182" fill="rgba(255,255,255,0.35)" font-size="11" text-anchor="middle" font-family="Inter,sans-serif">no fake runbooks</text>
        <path d="M620 135 H670" stroke="#00BFB3" stroke-width="2.5"/>
        <rect x="670" y="90" width="150" height="90" rx="12" fill="rgba(0,191,179,0.1)" stroke="#00BFB3"/>
        <text x="745" y="130" fill="#00BFB3" font-size="13" font-weight="700" text-anchor="middle" font-family="Inter,sans-serif">KB + events</text>
        <text x="745" y="152" fill="rgba(255,255,255,0.4)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">same corpus</text>
        <path d="M820 135 H870" stroke="#6ee7c7" stroke-width="2.5"/>
        <rect x="870" y="90" width="180" height="90" rx="12" fill="rgba(0,191,179,0.14)" stroke="#00BFB3"/>
        <text x="960" y="130" fill="#6ee7c7" font-size="14" font-weight="800" text-anchor="middle" font-family="Inter,sans-serif">NOC action</text>
        <text x="960" y="152" fill="rgba(255,255,255,0.45)" font-size="12" text-anchor="middle" font-family="Inter,sans-serif">timeline + escalate</text>
      </svg>
    </div>
{footer("Module 3 · Agent Builder")}
  </div>
""",
)

# ── NOC story ────────────────────────────────────────────────────────────────
SLIDES["noc-story.html"] = page(
    "Three beats — executive arc",
    """
    .beat { display: flex; gap: 18px; align-items: flex-start; margin-bottom: 14px; }
    .beat .n {
      flex-shrink: 0; width: 42px; height: 42px; border-radius: 10px;
      background: rgba(0,191,179,0.12); border: 1px solid rgba(0,191,179,0.35);
      display: flex; align-items: center; justify-content: center;
      font-weight: 800; color: #00BFB3; font-size: 1rem;
    }
    .beat h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 4px; }
    .beat p { font-size: 0.88rem; color: rgba(255,255,255,0.55); line-height: 1.45; }
    .beats { flex: 1; display: flex; flex-direction: column; justify-content: center; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Executive arc</div>
    <h1 class="headline f2">Three beats in <strong>90 seconds</strong></h1>
    <p class="sub f2">Use this close in Module 3 — Branch 4471 style incident.</p>
    <div class="divider"></div>
    <div class="beats">
      <div class="beat f3"><div class="n">1</div><div><h3>Search</h3><p>“Find Meraki offline runbook in &lt;10s.”</p></div></div>
      <div class="beat f4"><div class="n">2</div><div><h3>Federate</h3><p>“Offline event + internal escalation + KB — one ES|QL query.”</p></div></div>
      <div class="beat f5"><div class="n">3</div><div><h3>Agent</h3><p>“Copilot summarizes timeline and next steps for Branch 4471.”</p></div></div>
    </div>
{footer("Module 3 · Agent Builder")}
  </div>
""",
)

# ── Future ───────────────────────────────────────────────────────────────────
SLIDES["future.html"] = page(
    "Future — federated blob sources",
    """
    .compare { display: grid; grid-template-columns: 1fr auto 1fr; gap: 16px; flex: 1; align-items: stretch; }
    .hub {
      align-self: center; writing-mode: vertical-rl; transform: rotate(180deg);
      font-size: 0.72rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
      color: #049FD9; padding: 12px 8px; border: 1px dashed rgba(4,159,217,0.4); border-radius: 8px;
    }
    .card.future-card { border-color: rgba(167,139,250,0.35); background: rgba(124,58,237,0.08); }
    .tiers { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px; }
    .tier {
      border-radius: 10px; padding: 14px 16px; font-size: 0.8rem;
      border: 1px solid rgba(255,255,255,0.1);
    }
    .tier.hot { border-color: rgba(0,191,179,0.4); background: rgba(0,191,179,0.07); }
    .tier.cold { border-color: rgba(167,139,250,0.4); background: rgba(124,58,237,0.08); }
    .tier .t { font-size: 0.62rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 6px; }
    .tier.hot .t { color: #00BFB3; }
    .tier.cold .t { color: #c4b5fd; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Search · future</div>
    <h1 class="headline f2">Serverless Search &amp; <strong>federated blob sources</strong></h1>
    <p class="sub f2">Roadmap: same Serverless project → register S3 / GCS / Azure prefixes. Query archives in place.</p>
    <div class="pill-row f2" style="margin-bottom:12px">
      <span class="pill future">Enterprise Search roadmap</span>
      <span class="pill">S3 · GCS · Azure</span>
      <span class="pill hot">One Serverless project</span>
    </div>
    <div class="compare">
      <div class="card f3">
        <div class="label">Today (this lab)</div>
        <h3>Managed indices + connectors</h3>
        <p>Hot corpus: KB, runbooks, Meraki events. Sub-second UX. Federated <em>indices</em> via ES|QL.</p>
      </div>
      <div class="hub f3">Same project</div>
      <div class="card future-card f4">
        <div class="label">Roadmap</div>
        <h3>+ Federated object storage</h3>
        <p>JSON / Parquet archives. Schema-on-read. No second sized cluster on cold data.</p>
      </div>
    </div>
    <div class="tiers f5">
      <div class="tier hot"><div class="t">Managed search tier</div>Lexical + semantic · autocomplete · interactive ms–s</div>
      <div class="tier cold"><div class="t">Federated object tier</div>Query blob in place · archive economics · cents/GB-month</div>
    </div>
{footer("Roadmap · Federated blobs")}
  </div>
""",
)

# ── Architecture ─────────────────────────────────────────────────────────────
SLIDES["architecture.html"] = page(
    "Architecture — sources to tiers",
    """
    .arch { display: flex; flex-direction: column; gap: 12px; flex: 1; }
    .row3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
    .src {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
      border-radius: 10px; padding: 14px 16px;
    }
    .src.blob { border-color: rgba(167,139,250,0.4); background: rgba(124,58,237,0.08); }
    .src h3 { font-size: 0.92rem; font-weight: 700; margin-bottom: 4px; }
    .src p { font-size: 0.75rem; color: rgba(255,255,255,0.45); line-height: 1.4; }
    .hub-box {
      text-align: center; padding: 16px;
      border: 1px dashed rgba(167,139,250,0.5); border-radius: 12px;
      background: rgba(167,139,250,0.07); color: #ddd6fe;
      font-weight: 700; font-size: 0.95rem;
    }
    .hub-box small { display: block; margin-top: 6px; font-weight: 400; font-size: 0.75rem; color: rgba(255,255,255,0.4); }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Architecture (future)</div>
    <h1 class="headline f2">Sources → <strong>Serverless project</strong> → tiers</h1>
    <p class="sub f2">Enterprise Search UI · ES|QL · semantic rerank · connectors — same surface as today’s workshop.</p>
    <div class="divider"></div>
    <div class="arch">
      <div class="row3 f3">
        <div class="src"><h3>Managed Search indices</h3><p>Product docs · runbooks · sub-second UX</p></div>
        <div class="src"><h3>Content connectors</h3><p>SharePoint · web · API sync · incremental ingest</p></div>
        <div class="src blob"><h3>Blob archives</h3><p>S3 / GCS / Azure · JSON &amp; Parquet · federated read</p></div>
      </div>
      <div class="hub-box f4">Serverless Search + federation layer<small>Elastic-operated · no cluster sizing · schema-on-read · prefix mapping · tier-to-blob</small></div>
      <div class="row3 f5" style="grid-template-columns:1fr 1fr">
        <div class="src" style="border-color:rgba(0,191,179,0.4)"><h3>Managed search tier</h3><p>ELSER · autocomplete · interactive search</p></div>
        <div class="src blob"><h3>Federated object tier</h3><p>Query blob in place · long-retention corpora</p></div>
      </div>
    </div>
{footer("Roadmap · Architecture")}
  </div>
""",
)

# ── Outcomes ─────────────────────────────────────────────────────────────────
SLIDES["outcomes.html"] = page(
    "Outcomes — unified search",
    "",
    f"""
  <div class="slide">
    <div class="eyebrow f1">Outcomes</div>
    <h1 class="headline f2">Unified search &amp; <strong>simpler admin</strong></h1>
    <p class="sub f2">Bridge: today’s lab = hot tier + federated indices → blob federation is the next hop.</p>
    <div class="divider"></div>
    <div class="grid2">
      <div class="card f3"><div class="label">Unified search</div><h3>One query, many tiers</h3><p>Span managed indices and federated blob prefixes in a single ES|QL or Search request.</p></div>
      <div class="card f3"><div class="label">Easy administration</div><h3>Register sources in UI</h3><p>No shard math on cold storage. Federate instead of archive clusters on blob.</p></div>
      <div class="card f4"><div class="label">Economics</div><h3>Lower TCO</h3><p>Avoid paying twice for frozen/archive — blob economics for retention, Serverless for hot + AI.</p></div>
      <div class="card f4"><div class="label">Bridge to today</div><h3>This lab proves the pattern</h3><p>Modules 2–3 preview the unified query story on the same Serverless Search project.</p></div>
    </div>
{footer("Roadmap · Outcomes")}
  </div>
""",
)

# ── Lab ──────────────────────────────────────────────────────────────────────
SLIDES["lab.html"] = page(
    "Lab provisioning",
    """
    .steps { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 14px; }
    .step {
      display: flex; gap: 16px; align-items: center;
      padding: 16px 20px; border-radius: 12px;
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    }
    .step .n {
      width: 36px; height: 36px; border-radius: 50%;
      background: rgba(0,191,179,0.15); color: #00BFB3;
      display: flex; align-items: center; justify-content: center;
      font-weight: 800; font-size: 0.9rem; flex-shrink: 0;
    }
    .step p { font-size: 0.95rem; color: rgba(255,255,255,0.75); }
    .step code { font-family: 'JetBrains Mono', monospace; color: #00BFB3; font-size: 0.88em; }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">While you wait</div>
    <h1 class="headline f2">Lab provisioning — <strong>~3–4 minutes</strong></h1>
    <p class="sub f2">When the Elastic Serverless Search tab opens, start Module 1.</p>
    <div class="divider"></div>
    <div class="steps">
      <div class="step f3"><div class="n">1</div><p>Create <strong>Serverless Search</strong> (vector) via <code>es3-api</code></p></div>
      <div class="step f4"><div class="n">2</div><p>Proxy Kibana on port <code>8080</code></p></div>
      <div class="step f5"><div class="n">3</div><p>Seed <code>cisco-network-kb</code>, runbooks, Meraki events, network events</p></div>
    </div>
{footer("Instruqt · cisco-serverless-workshop")}
  </div>
""",
)

# ── Close ────────────────────────────────────────────────────────────────────
SLIDES["close.html"] = page(
    "Takeaways",
    """
    .take { display: flex; flex-direction: column; gap: 12px; flex: 1; justify-content: center; }
    .take .card { display: flex; gap: 16px; align-items: flex-start; }
    .take .icon {
      flex-shrink: 0; width: 40px; height: 40px; border-radius: 10px;
      background: rgba(0,191,179,0.12); color: #00BFB3;
      display: flex; align-items: center; justify-content: center; font-weight: 800;
    }
    """,
    f"""
  <div class="slide">
    <div class="eyebrow f1">Close</div>
    <h1 class="headline f2">Why we win on <strong>Search</strong></h1>
    <p class="sub f2">Five lines for your notes — Search-led Cisco motion.</p>
    <div class="divider"></div>
    <div class="take">
      <div class="card f3"><div class="icon">1</div><div><h3>Hybrid AI Search</h3><p>Keyword + semantic on Cisco KB — MTTR, not portal hopping.</p></div></div>
      <div class="card f3"><div class="icon">2</div><div><h3>Federate sources</h3><p>Connectors + multi-index ES|QL without rip-and-replace.</p></div></div>
      <div class="card f4"><div class="icon">3</div><div><h3>Agents on Search</h3><p>Grounded tools on the same indices — NOC action, Search SKU.</p></div></div>
      <div class="card f4"><div class="icon">4</div><div><h3>Serverless economics</h3><p>One Cloud project, workshop-ready in minutes.</p></div></div>
      <div class="card f5"><div class="icon">5</div><div><h3>Roadmap: blob federation</h3><p>Same project → query S3/GCS/Azure archives in place.</p></div></div>
    </div>
{footer()}
  </div>
""",
)

# ── Thank you ────────────────────────────────────────────────────────────────
SLIDES["thank-you.html"] = page(
    "Thank you",
    """
    body { justify-content: center; align-items: center; }
    .thanks {
      position: relative; z-index: 10; text-align: center; max-width: 720px; padding: 0 40px;
    }
    .thanks h1 {
      font-size: 3.6rem; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 1rem;
    }
    .thanks p { font-size: 1.1rem; color: rgba(255,255,255,0.55); line-height: 1.55; margin-bottom: 1.6rem; }
    .thanks a { color: #00BFB3; text-decoration: none; font-weight: 600; }
    """,
    """
  <div class="thanks">
    <div class="eyebrow f1" style="justify-content:center;display:flex">Cisco × Elastic</div>
    <h1 class="f2">Thank you.</h1>
    <p class="f3">Questions welcome. Lab: <a href="https://play.instruqt.com/manage/elastic/tracks/cisco-serverless-workshop">cisco-serverless-workshop</a><br>
    Deck + wait screen: GitHub Pages on this repo.</p>
    <div class="pill-row f4" style="justify-content:center">
      <span class="pill hot">AI Search</span>
      <span class="pill">Federated Sources</span>
      <span class="pill">Agent Builder</span>
      <span class="pill future">Blob roadmap</span>
    </div>
  </div>
""",
)


NOTES = {
    "cover.html": "- Welcome — Search-led Cisco workshop: AI Search, Federated Sources, Agent Builder.\n- One Serverless Search project only — no O11Y/Security for this motion.\n- Lab ready in ~3–4 minutes while we walk the deck.",
    "agenda.html": "- Three modules, same indices end-to-end.\n- Module 1 proves hybrid retrieval; 2 federates; 3 acts with agents.\n- Keep the GTM frame: Search consolidation, not a multi-SKU sell.",
    "pain.html": "- Pain is swivel-chair: Meraki → IOS-XE → DNA → wiki.\n- Elastic meets engineers where they search.\n- Target: one Search surface, shorter MTTR.",
    "serverless.html": "- Why Serverless Search: speed, GTM fit, ES|QL skill reuse, workshop economics.\n- Explicitly call out no Observability/Security requirement.",
    "ai-search.html": "- Hybrid is the product story: BM25 + semantic + RRF.\n- Buyer quote: one place for IOS-XE and Meraki docs.",
    "hybrid.html": "- Walk the diagram left to right. Pause on RRF merge.\n- Index name cisco-network-kb is what they will verify in the lab.",
    "federated.html": "- Federate don't rip-and-replace — DCOS language.\n- Sources stay; Elastic is the unified query layer.",
    "esql.html": "- Same ES|QL for humans and agent tools.\n- Branch 4471 is the recurring story thread into Module 3.",
    "agents.html": "- Grounded tools on Search indices — no hallucinated runbooks.\n- Still Search-only; no Observability SKU.",
    "noc-story.html": "- 90-second exec close: Search → Federate → Agent.\n- Practice this out loud before Module 3.",
    "future.html": "- Clear bridge: today = managed + federated indices; roadmap = blob prefixes.\n- Economic punch: don't pay twice for cold/archive.",
    "architecture.html": "- Sources → federation layer → hot/cold tiers.\n- Same tooling surface as the workshop (ES|QL, Enterprise Search, agents).",
    "outcomes.html": "- Unified search, easy admin, TCO, bridge to lab.\n- Leave analysts with 'one query across tiers'.",
    "lab.html": "- Orient learners: es3-api, port 8080, four seed indices.\n- When Kibana opens, start Module 1.",
    "close.html": "- Five takeaways — leave these on screen for questions.",
    "thank-you.html": "- Point to Instruqt manage URL and Pages deck for follow-up.",
}


def main() -> None:
    for name, html in SLIDES.items():
        path = ROOT / name
        path.write_text(html, encoding="utf-8")
        print(f"  wrote {name}")
    import json
    (ROOT / "notes.json").write_text(json.dumps(NOTES, indent=2) + "\n", encoding="utf-8")
    print("  wrote notes.json")
    print(f"\n✓ {len(SLIDES)} slides generated in {ROOT}")


if __name__ == "__main__":
    main()
