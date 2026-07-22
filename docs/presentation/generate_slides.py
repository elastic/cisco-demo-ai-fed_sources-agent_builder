#!/usr/bin/env python3
"""Generate Metrics Analyst–quality 1280×720 slides (except handcrafted foundations.html)."""
from __future__ import annotations

import json
from pathlib import Path

from _common import wrap

ROOT = Path(__file__).resolve().parent
HANDCRAFTED = {"foundations.html"}  # never overwrite


def write(name: str, html: str) -> None:
    if name in HANDCRAFTED and (ROOT / name).exists():
        print(f"  skip {name} (handcrafted)")
        return
    (ROOT / name).write_text(html, encoding="utf-8")
    print(f"  wrote {name}")


SLIDES = {}

# ── Cover ────────────────────────────────────────────────────────────────────
SLIDES["cover.html"] = wrap(
    "Elastic Search — AI, Federated Sources & Agent Builder",
    """
    body { justify-content: space-between; }
    .elastic-mark {
      position: fixed; right: -90px; top: 48%; transform: translateY(-50%);
      width: 580px; height: 580px; pointer-events: none; z-index: 1; opacity: 0.95;
      animation: mark-breathe 8s ease-in-out infinite;
    }
    @keyframes mark-breathe {
      0%,100% { transform: translateY(-50%) scale(1); }
      50% { transform: translateY(-51%) scale(1.02); }
    }
    .content {
      position: relative; z-index: 10; padding: 0 6vw; flex: 1;
      display: flex; flex-direction: column; justify-content: center; max-width: 64%;
    }
    .c-eyebrow {
      font-size: 0.75rem; font-weight: 700; letter-spacing: 0.16em;
      text-transform: uppercase; color: #00BFB3; margin-bottom: 1.35rem;
    }
    .c-title {
      font-size: 3.35rem; font-weight: 300; letter-spacing: -0.03em;
      line-height: 1.05; margin-bottom: 1.15rem;
    }
    .c-title strong { font-weight: 800; color: #fff; }
    .c-title em { font-style: normal; font-weight: 800; color: #00BFB3; }
    .c-sub {
      font-size: 1.05rem; color: rgba(255,255,255,0.58); line-height: 1.55;
      max-width: 520px; margin-bottom: 1.6rem;
    }
    .pill-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .pill {
      font-size: 0.68rem; padding: 5px 12px; border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.14); color: rgba(255,255,255,0.55);
    }
    .pill.hot { border-color: rgba(0,191,179,0.55); color: #00BFB3; }
    .pill.future { border-color: rgba(167,139,250,0.55); color: #c4b5fd; }
    .cover-foot {
      position: relative; z-index: 10; padding: 0 6vw 28px;
      display: flex; gap: 12px; font-size: 0.75rem; color: rgba(255,255,255,0.32);
    }
    """,
    """
  <svg class="elastic-mark" viewBox="0 0 237 236" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <circle cx="168" cy="72" r="28" fill="#FEC514" opacity="0.32"/>
    <circle cx="72" cy="96" r="22" fill="#00BFB3" opacity="0.38"/>
    <circle cx="150" cy="150" r="34" fill="#00A9E0" opacity="0.26"/>
    <circle cx="90" cy="168" r="18" fill="#F04E23" opacity="0.32"/>
  </svg>
  <div class="content">
    <div class="c-eyebrow fade-up-1">Cisco × Elastic · practitioner workshop</div>
    <h1 class="c-title fade-up-2"><strong>AI Search.</strong><br><em>Federated Sources.</em><br><strong>Agent Builder.</strong></h1>
    <p class="c-sub fade-up-3">One Elastic Search Serverless project. Hybrid retrieval, unified Cisco knowledge, grounded agents for the NOC — without Observability or Security.</p>
    <div class="pill-row fade-up-4">
      <span class="pill hot">Serverless Search</span>
      <span class="pill">ES|QL</span>
      <span class="pill">Connectors</span>
      <span class="pill future">Blob federation roadmap</span>
    </div>
  </div>
  <div class="cover-foot fade-up-5">
    <span>The Search AI Company</span><span>·</span><span>Lab ready in ~3–4 minutes</span>
  </div>
""",
    bottom="This is a **Search-only** lab. Same indices power find → unify → act.",
)

# ── Agenda ───────────────────────────────────────────────────────────────────
SLIDES["agenda.html"] = wrap(
    "Agenda",
    """
    .flow { display: flex; align-items: stretch; gap: 12px; flex: 1; min-height: 0; padding-bottom: 8px; }
    .card {
      flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 20px 18px; display: flex; flex-direction: column; gap: 8px;
    }
    .num {
      font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; font-weight: 700;
      letter-spacing: 0.1em; color: #049FD9;
    }
    .card h3 { font-size: 1.2rem; font-weight: 700; }
    .card p { font-size: 0.82rem; color: rgba(255,255,255,0.5); line-height: 1.5; flex: 1; }
    .card .mono { font-family: 'JetBrains Mono', monospace; color: #00BFB3; font-size: 0.78rem; }
    .arrow { align-self: center; color: rgba(255,255,255,0.22); font-size: 1.5rem; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Today</div>
    <h1 class="headline fade-up-2">Three beats. <strong>One Search project.</strong></h1>
    <p class="sub fade-up-3">Same indices end-to-end — explore AI Search, federation, and agents on Elastic Search Serverless.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="flow">
      <div class="card fade-up-4">
        <span class="num">MODULE 01</span>
        <h3>AI Search</h3>
        <p>Hybrid + semantic on the Cisco KB. Exact TAC phrases and natural-language questions in one ranked set.</p>
        <span class="mono">cisco-network-kb</span>
      </div>
      <div class="arrow fade-up-4">→</div>
      <div class="card fade-up-5">
        <span class="num">MODULE 02</span>
        <h3>Federated sources</h3>
        <p>KB, runbooks, Meraki events — connectors and multi-index ES|QL without ripping systems out.</p>
        <span class="mono">FROM * | WHERE …</span>
      </div>
      <div class="arrow fade-up-5">→</div>
      <div class="card fade-up-6">
        <span class="num">MODULE 03</span>
        <h3>Agent Builder</h3>
        <p>ES|QL triage + agents grounded in the same indices. Cisco NOC story on Elastic Search Serverless.</p>
        <span class="mono">tools → indices</span>
      </div>
    </div>
  </div>
""",
    bottom="Find → unify → act. If your team only remembers one chain, make it this one.",
)

# ── Pain (canvas MTTR) ───────────────────────────────────────────────────────
SLIDES["pain.html"] = wrap(
    "NOC knowledge in silos",
    """
    .layout { flex: 1; display: grid; grid-template-columns: 1.05fr 1fr; gap: 28px; min-height: 0; padding-bottom: 6px; }
    .silos { display: flex; flex-direction: column; gap: 10px; justify-content: center; }
    .silo {
      display: flex; align-items: center; gap: 12px;
      padding: 12px 14px; border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03);
    }
    .silo .dot {
      width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0;
      background: #F04E23; box-shadow: 0 0 10px rgba(240,78,35,0.5);
    }
    .silo strong { display: block; font-size: 0.92rem; }
    .silo span { font-size: 0.72rem; color: rgba(255,255,255,0.4); }
    .chart-wrap { position: relative; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);
      background: rgba(0,0,0,0.2); overflow: hidden; }
    .chart-wrap canvas { width: 100%; height: 100%; display: block; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Why this matters</div>
    <h1 class="headline fade-up-2">Cisco NOC pain: <strong>knowledge in silos</strong></h1>
    <p class="sub fade-up-3">Tab-hopping across Meraki, IOS-XE, DNA Center, and wikis while MTTR climbs.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="layout">
      <div class="silos fade-up-4">
        <div class="silo"><span class="dot"></span><div><strong>Meraki Dashboard</strong><span>Offline APs · client health</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>IOS-XE runbooks</strong><span>TAC phrases · CLI recovery</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>DNA Center</strong><span>Assurance · path traces</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>Internal wiki</strong><span>Escalation · tribal knowledge</span></div></div>
      </div>
      <div class="chart-wrap fade-up-5"><canvas id="cvMttr"></canvas></div>
    </div>
  </div>
""",
    scripts="""
<script>
(function(){
  const canvas = document.getElementById('cvMttr');
  const r = window.devicePixelRatio || 1;
  function size(){ const rect = canvas.getBoundingClientRect();
    const w = Math.round(rect.width)||520, h = Math.round(rect.height)||360;
    canvas.width = w*r; canvas.height = h*r; return {ctx: canvas.getContext('2d'), w, h}; }
  let frame = 0;
  function draw(){
    const {ctx,w,h} = size(); ctx.setTransform(r,0,0,r,0,0);
    ctx.clearRect(0,0,w,h);
    const pad = {l:48,r:24,t:40,b:48}; const iw=w-pad.l-pad.r, ih=h-pad.t-pad.b;
    const prog = Math.min(frame/55,1);
    // title
    ctx.font='700 11px JetBrains Mono, monospace'; ctx.fillStyle='rgba(255,255,255,0.4)';
    ctx.fillText('MTTR (illustrative)', pad.l, 24);
    const bars = [
      {label:'Today', v:0.92, color:'#049FD9'},
      {label:'One Search', v:0.34, color:'#00BFB3'},
    ];
    const bw = iw/bars.length - 36;
    bars.forEach((b,i)=>{
      const x = pad.l + i*(iw/bars.length) + 18;
      const bh = b.v*ih*prog;
      const y = pad.t + ih - bh;
      const grad = ctx.createLinearGradient(0,y,0,pad.t+ih);
      grad.addColorStop(0,b.color); grad.addColorStop(1,'rgba(0,0,0,0)');
      ctx.fillStyle = grad; ctx.shadowColor=b.color; ctx.shadowBlur=14;
      ctx.beginPath();
      const rad=8;
      ctx.moveTo(x, pad.t+ih); ctx.lineTo(x,y+rad);
      ctx.quadraticCurveTo(x,y,x+rad,y); ctx.lineTo(x+bw-rad,y);
      ctx.quadraticCurveTo(x+bw,y,x+bw,y+rad); ctx.lineTo(x+bw,pad.t+ih); ctx.closePath();
      ctx.fill(); ctx.shadowBlur=0;
      ctx.font='600 12px Inter,sans-serif'; ctx.fillStyle='rgba(255,255,255,0.55)';
      ctx.textAlign='center'; ctx.fillText(b.label, x+bw/2, pad.t+ih+22);
      ctx.textAlign='left';
    });
    if(frame<70){ frame++; requestAnimationFrame(draw); }
  }
  draw();
})();
</script>
""",
    bottom="Elastic meets engineers <strong>where they already search</strong> — one surface, shorter MTTR.",
)

# ── Serverless ───────────────────────────────────────────────────────────────
SLIDES["serverless.html"] = wrap(
    "One Serverless Search project",
    """
    .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1; min-height: 0; padding-bottom: 8px; }
    .card {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 18px 20px;
    }
    .card .label {
      font-family: 'JetBrains Mono', monospace; font-size: 0.58rem; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase; color: #00BFB3; margin-bottom: 8px;
    }
    .card h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; }
    .card p { font-size: 0.82rem; color: rgba(255,255,255,0.52); line-height: 1.5; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Platform choice</div>
    <h1 class="headline fade-up-2">One <strong>Serverless Search</strong> project — advantages</h1>
    <p class="sub fade-up-3">Search-only workshop for Cisco practitioners on Elastic Search Serverless.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4"><div class="label">Speed</div><h3>~3–4 min to ready</h3><p>Single vector Search project + seeded Cisco indices — no multi-product wait.</p></div>
      <div class="card fade-up-4"><div class="label">Scope</div><h3>Search-only lab</h3><p>AI Search, federated indices, and Agent Builder — Observability and Security are out of scope for this workshop.</p></div>
      <div class="card fade-up-5"><div class="label">Skill</div><h3>ES|QL everywhere</h3><p>KB, connectors, and agent tools — one query language for engineers and agents.</p></div>
      <div class="card fade-up-5"><div class="label">Economics</div><h3>Serverless ops</h3><p>Per-learner Cloud projects in Instruqt; elastic scale for internal POCs.</p></div>
    </div>
  </div>
""",
    bottom="If you only remember one platform call: <strong>Serverless Search</strong> — not a stack of products.",
)

# ── AI Search ────────────────────────────────────────────────────────────────
SLIDES["ai-search.html"] = wrap(
    "AI Search",
    """
    .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1; min-height: 0; }
    .card {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 18px 20px;
    }
    .card .label {
      font-family: 'JetBrains Mono', monospace; font-size: 0.58rem; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase; color: #00BFB3; margin-bottom: 8px;
    }
    .card h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 8px; }
    .card ul { margin: 0 0 0 1.1rem; font-size: 0.8rem; color: rgba(255,255,255,0.52); line-height: 1.55; }
    .card li strong { color: #fff; }
    .quote {
      margin-top: 12px; border-left: 3px solid #049FD9; padding: 12px 16px;
      background: rgba(4,159,217,0.07); border-radius: 0 10px 10px 0;
      font-size: 0.9rem; color: rgba(255,255,255,0.82);
    }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 1</div>
    <h1 class="headline fade-up-2">AI Search — <strong>what &amp; why</strong></h1>
    <p class="sub fade-up-3">Hybrid + semantic on <span style="font-family:JetBrains Mono,monospace;color:#00BFB3">cisco-network-kb</span> — Meraki, BGP, DNA in seconds.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4">
        <div class="label">What</div><h3>Keyword + vector</h3>
        <ul>
          <li><strong>BM25</strong> for exact TAC phrases and error codes</li>
          <li><strong>ELSER / vectors</strong> for natural-language questions</li>
          <li><strong>RRF</strong> for one ranked result set</li>
        </ul>
      </div>
      <div class="card fade-up-5">
        <div class="label">Why teams care</div><h3>Shorter MTTR</h3>
        <ul>
          <li><strong>One surface</strong> instead of six portals</li>
          <li><strong>Scale</strong> via connectors in Module 2</li>
          <li><strong>Proof</strong> live in the first 20 minutes</li>
        </ul>
      </div>
    </div>
    <div class="quote fade-up-6">“Can we search IOS-XE and Meraki docs in one place?” — this module is the answer.</div>
  </div>
""",
    bottom="Next slide is the foundation — Keyword · Semantic · <strong>Hybrid</strong> with live motion.",
)

# Skip hybrid — use foundations as the hero; keep a short hybrid pointer slide or remove from config
# We'll keep hybrid.html as a thin "lab proof" slide
SLIDES["hybrid.html"] = wrap(
    "Lab proof — hybrid",
    """
    .steps { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 12px; }
    .step {
      display: flex; gap: 16px; align-items: center; padding: 14px 18px; border-radius: 12px;
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    }
    .step .n {
      width: 36px; height: 36px; border-radius: 50%; background: rgba(0,191,179,0.15);
      color: #00BFB3; display: flex; align-items: center; justify-content: center;
      font-weight: 800; flex-shrink: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;
    }
    .step p { font-size: 0.95rem; color: rgba(255,255,255,0.72); }
    .step code { font-family: 'JetBrains Mono', monospace; color: #00BFB3; font-size: 0.88em; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 1 · Lab</div>
    <h1 class="headline fade-up-2">Prove it on <strong>cisco-network-kb</strong></h1>
    <p class="sub fade-up-3">When Kibana opens, this is the first 10 minutes.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="steps">
      <div class="step fade-up-4"><div class="n">1</div><p>Open Search / Discover — confirm index <code>cisco-network-kb</code></p></div>
      <div class="step fade-up-5"><div class="n">2</div><p>Run a keyword query for a TAC-style phrase, then a natural-language offline question</p></div>
      <div class="step fade-up-6"><div class="n">3</div><p>Call out hybrid: same corpus, better rank — set up Module 2 federation</p></div>
    </div>
  </div>
""",
    bottom="Don’t linger on UI chrome — land the <strong>one place for Meraki + IOS-XE</strong> line.",
)

# ── Federated ────────────────────────────────────────────────────────────────
SLIDES["federated.html"] = wrap(
    "Federated data sources",
    """
    .canvas-wrap { flex: 1; min-height: 0; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);
      background: rgba(0,0,0,0.18); overflow: hidden; margin-bottom: 4px; }
    .canvas-wrap canvas { width: 100%; height: 100%; display: block; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 2</div>
    <h1 class="headline fade-up-2">Federate — <strong>don’t rip-and-replace</strong></h1>
    <p class="sub fade-up-3">Leave Meraki and DNA in place. Elastic becomes the unified query layer.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="canvas-wrap fade-up-4"><canvas id="cvFed"></canvas></div>
  </div>
""",
    scripts="""
<script>
(function(){
  const canvas=document.getElementById('cvFed');
  const r=window.devicePixelRatio||1;
  const sources=['cisco.com KB','Internal runbooks','Meraki events','Network signals'];
  let t=0;
  function draw(){
    const rect=canvas.getBoundingClientRect();
    const w=Math.round(rect.width)||1100, h=Math.round(rect.height)||380;
    canvas.width=w*r; canvas.height=h*r;
    const ctx=canvas.getContext('2d'); ctx.setTransform(r,0,0,r,0,0);
    ctx.clearRect(0,0,w,h);
    const hub={x:w*0.48,y:h*0.48};
    // hub
    ctx.beginPath(); ctx.arc(hub.x,hub.y,54,0,Math.PI*2);
    ctx.fillStyle='rgba(0,191,179,0.1)'; ctx.strokeStyle='#00BFB3'; ctx.lineWidth=2;
    ctx.shadowColor='#00BFB3'; ctx.shadowBlur=20; ctx.fill(); ctx.stroke(); ctx.shadowBlur=0;
    ctx.font='700 12px Inter,sans-serif'; ctx.fillStyle='#00BFB3'; ctx.textAlign='center';
    ctx.fillText('Serverless', hub.x, hub.y-4);
    ctx.fillText('Search', hub.x, hub.y+14);
    // sources orbiting / connected
    sources.forEach((s,i)=>{
      const ang=-Math.PI/2 + (i/sources.length)*Math.PI*1.6 + 0.35;
      const rad=Math.min(w,h)*0.34;
      const x=hub.x + Math.cos(ang)*rad;
      const y=hub.y + Math.sin(ang)*rad;
      const pulse=0.5+0.5*Math.sin(t*2+i);
      ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(hub.x,hub.y);
      ctx.strokeStyle='rgba(4,159,217,'+(0.25+pulse*0.2)+')'; ctx.lineWidth=1.5; ctx.stroke();
      // particle
      const p=(t*0.4+i*0.2)%1;
      const px=x+(hub.x-x)*p, py=y+(hub.y-y)*p;
      ctx.beginPath(); ctx.arc(px,py,3,0,Math.PI*2);
      ctx.fillStyle='#049FD9'; ctx.shadowColor='#049FD9'; ctx.shadowBlur=8; ctx.fill(); ctx.shadowBlur=0;
      // box
      ctx.fillStyle='rgba(255,255,255,0.04)'; ctx.strokeStyle='rgba(255,255,255,0.14)';
      ctx.beginPath(); ctx.roundRect(x-70,y-22,140,44,8); ctx.fill(); ctx.stroke();
      ctx.font='600 11px Inter,sans-serif'; ctx.fillStyle='#fff'; ctx.textAlign='center';
      ctx.fillText(s,x,y+4);
    });
    // ES|QL node
    const ex=w*0.82, ey=h*0.48;
    ctx.beginPath(); ctx.moveTo(hub.x+54,hub.y); ctx.lineTo(ex-70,ey);
    ctx.strokeStyle='rgba(110,231,199,0.45)'; ctx.lineWidth=2; ctx.stroke();
    ctx.fillStyle='rgba(4,159,217,0.12)'; ctx.strokeStyle='#049FD9';
    ctx.beginPath(); ctx.roundRect(ex-70,ey-28,140,56,10); ctx.fill(); ctx.stroke();
    ctx.font='800 13px JetBrains Mono,monospace'; ctx.fillStyle='#049FD9'; ctx.textAlign='center';
    ctx.fillText('One ES|QL', ex, ey-2);
    ctx.font='500 10px Inter,sans-serif'; ctx.fillStyle='rgba(255,255,255,0.45)';
    ctx.fillText('unified NOC view', ex, ey+16);
    if(!CanvasRenderingContext2D.prototype.roundRect){
      CanvasRenderingContext2D.prototype.roundRect=function(x,y,w,h,r){
        this.moveTo(x+r,y); this.arcTo(x+w,y,x+w,y+h,r); this.arcTo(x+w,y+h,x,y+h,r);
        this.arcTo(x,y+h,x,y,r); this.arcTo(x,y,x+w,y,r); this.closePath();
      };
    }
    t+=0.025; requestAnimationFrame(draw);
  }
  draw();
})();
</script>
""",
    bottom="Federate sources in place — <strong>connectors + ES|QL</strong> unify the query layer.",
)

# ── ES|QL ────────────────────────────────────────────────────────────────────
SLIDES["esql.html"] = wrap(
    "ES|QL",
    """
    .code {
      flex: 1; background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 24px 28px; font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem; line-height: 1.75; color: rgba(255,255,255,0.78); margin-bottom: 4px;
    }
    .kw { color: #00BFB3; } .str { color: #FEC514; } .cm { color: rgba(255,255,255,0.28); }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 2 · Query layer</div>
    <h1 class="headline fade-up-2">One language: <strong>ES|QL</strong></h1>
    <p class="sub fade-up-3">Offline Meraki event + escalation + KB — one skill for humans and agents.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="code fade-up-4">
      <span class="cm">// Branch 4471 — correlate signal with runbook steps</span><br>
      <span class="kw">FROM</span> cisco-meraki-events, cisco-internal-runbooks, cisco-network-kb<br>
      <span class="kw">| WHERE</span> branch.id == <span class="str">"4471"</span> <span class="kw">OR</span> topic <span class="kw">LIKE</span> <span class="str">"*offline*"</span><br>
      <span class="kw">| KEEP</span> @timestamp, source, title, severity, next_steps<br>
      <span class="kw">| SORT</span> @timestamp <span class="kw">DESC</span><br>
      <span class="kw">| LIMIT</span> 20
    </div>
  </div>
""",
    bottom="ES|QL is the bridge from Module 2 into Agent Builder tools — <strong>same queries, same indices</strong>.",
)

# ── Agents ───────────────────────────────────────────────────────────────────
SLIDES["agents.html"] = wrap(
    "Agent Builder",
    """
    .canvas-wrap { flex: 1; min-height: 0; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);
      background: rgba(0,0,0,0.18); overflow: hidden; margin-bottom: 4px; }
    .canvas-wrap canvas { width: 100%; height: 100%; display: block; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 3</div>
    <h1 class="headline fade-up-2">Agent Builder — <strong>search to action</strong></h1>
    <p class="sub fade-up-3">Grounded tools on Search indices. No hallucinated runbooks. Elastic Search Serverless only.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="canvas-wrap fade-up-4"><canvas id="cvAgent"></canvas></div>
  </div>
""",
    scripts="""
<script>
(function(){
  const canvas=document.getElementById('cvAgent');
  const r=window.devicePixelRatio||1;
  const stages=[
    {label:'Signals', sub:'cisco-network-events', c:'#fff'},
    {label:'ES|QL', sub:'triage', c:'#049FD9'},
    {label:'Agent', sub:'grounded tools', c:'#a78bfa'},
    {label:'KB', sub:'runbooks', c:'#00BFB3'},
    {label:'NOC', sub:'escalate', c:'#6ee7c7'},
  ];
  let t=0;
  function draw(){
    const rect=canvas.getBoundingClientRect();
    const w=Math.round(rect.width)||1100, h=Math.round(rect.height)||380;
    canvas.width=w*r; canvas.height=h*r;
    const ctx=canvas.getContext('2d'); ctx.setTransform(r,0,0,r,0,0);
    ctx.clearRect(0,0,w,h);
    const y=h*0.48, gap=w/(stages.length+0.5), boxW=130;
    stages.forEach((s,i)=>{
      const x=gap*(i+0.75);
      const active=Math.floor((t*0.6)%stages.length)===i;
      ctx.strokeStyle=s.c; ctx.fillStyle=active?'rgba(255,255,255,0.06)':'rgba(255,255,255,0.03)';
      ctx.lineWidth=active?2.5:1.5; ctx.shadowColor=s.c; ctx.shadowBlur=active?16:0;
      ctx.beginPath(); ctx.roundRect(x-boxW/2,y-36,boxW,72,12); ctx.fill(); ctx.stroke(); ctx.shadowBlur=0;
      ctx.font='800 14px Inter,sans-serif'; ctx.fillStyle=s.c; ctx.textAlign='center';
      ctx.fillText(s.label,x,y-4);
      ctx.font='500 11px JetBrains Mono,monospace'; ctx.fillStyle='rgba(255,255,255,0.4)';
      ctx.fillText(s.sub,x,y+16);
      if(i<stages.length-1){
        const x2=gap*(i+1.75);
        ctx.beginPath(); ctx.moveTo(x+boxW/2+4,y); ctx.lineTo(x2-boxW/2-4,y);
        ctx.strokeStyle='rgba(255,255,255,0.15)'; ctx.lineWidth=2; ctx.stroke();
        const p=((t*0.6)+i*0.2)%1;
        const px=x+boxW/2+4 + (x2-boxW/2-4 - x-boxW/2-4)*p;
        ctx.beginPath(); ctx.arc(px,y,3.5,0,Math.PI*2);
        ctx.fillStyle='#00BFB3'; ctx.shadowColor='#00BFB3'; ctx.shadowBlur=10; ctx.fill(); ctx.shadowBlur=0;
      }
    });
    if(!CanvasRenderingContext2D.prototype.roundRect){
      CanvasRenderingContext2D.prototype.roundRect=function(x,y,w,h,r){
        this.moveTo(x+r,y); this.arcTo(x+w,y,x+w,y+h,r); this.arcTo(x+w,y+h,x,y+h,r);
        this.arcTo(x,y+h,x,y,r); this.arcTo(x,y,x+w,y,r); this.closePath();
      };
    }
    t+=0.04; requestAnimationFrame(draw);
  }
  draw();
})();
</script>
""",
    bottom="Agents don’t invent Cisco runbooks — they <strong>retrieve</strong> them from the same Search corpus.",
)

# ── NOC story ────────────────────────────────────────────────────────────────
SLIDES["noc-story.html"] = wrap(
    "Workshop story arc",
    """
    .beats { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 14px; }
    .beat { display: flex; gap: 18px; align-items: flex-start; }
    .beat .n {
      flex-shrink: 0; width: 44px; height: 44px; border-radius: 10px;
      background: rgba(0,191,179,0.12); border: 1px solid rgba(0,191,179,0.35);
      display: flex; align-items: center; justify-content: center;
      font-weight: 800; color: #00BFB3; font-size: 1.05rem;
      font-family: 'JetBrains Mono', monospace;
    }
    .beat h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 4px; }
    .beat p { font-size: 0.92rem; color: rgba(255,255,255,0.55); }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Workshop story arc</div>
    <h1 class="headline fade-up-2">Three beats in <strong>90 seconds</strong></h1>
    <p class="sub fade-up-3">Branch 4471 — practice this recap before Module 3.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="beats">
      <div class="beat fade-up-4"><div class="n">1</div><div><h3>Search</h3><p>“Find Meraki offline runbook in &lt;10s.”</p></div></div>
      <div class="beat fade-up-5"><div class="n">2</div><div><h3>Federate</h3><p>“Offline event + escalation + KB — one ES|QL query.”</p></div></div>
      <div class="beat fade-up-6"><div class="n">3</div><div><h3>Agent</h3><p>“Copilot summarizes timeline and next steps for Branch 4471.”</p></div></div>
    </div>
  </div>
""",
    bottom="If the room only hears one story, make it <strong>4471</strong>.",
)

# ── Future ───────────────────────────────────────────────────────────────────
SLIDES["future.html"] = wrap(
    "Future — federated blobs",
    """
    .compare { display: grid; grid-template-columns: 1fr auto 1fr; gap: 16px; flex: 1; align-items: stretch; min-height: 0; }
    .card {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
      border-radius: 12px; padding: 18px 20px;
    }
    .card.future { border-color: rgba(167,139,250,0.4); background: rgba(124,58,237,0.08); }
    .card .label {
      font-family: 'JetBrains Mono', monospace; font-size: 0.58rem; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase; color: #00BFB3; margin-bottom: 8px;
    }
    .card.future .label { color: #c4b5fd; }
    .card h3 { font-size: 1.05rem; font-weight: 700; margin-bottom: 8px; }
    .card p { font-size: 0.82rem; color: rgba(255,255,255,0.5); line-height: 1.5; }
    .hub {
      align-self: center; writing-mode: vertical-rl; transform: rotate(180deg);
      font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
      color: #049FD9; padding: 14px 8px; border: 1px dashed rgba(4,159,217,0.4); border-radius: 8px;
    }
    .tiers { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
    .tier { border-radius: 10px; padding: 12px 14px; font-size: 0.78rem; border: 1px solid rgba(255,255,255,0.1); }
    .tier.hot { border-color: rgba(0,191,179,0.4); background: rgba(0,191,179,0.07); }
    .tier.cold { border-color: rgba(167,139,250,0.4); background: rgba(124,58,237,0.08); }
    .tier .t { font-size: 0.58rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 4px; }
    .tier.hot .t { color: #00BFB3; } .tier.cold .t { color: #c4b5fd; }
    .pill-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; }
    .pill { font-size: 0.65rem; padding: 4px 10px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.14); color: rgba(255,255,255,0.5); }
    .pill.future { border-color: rgba(167,139,250,0.55); color: #c4b5fd; }
    .pill.hot { border-color: rgba(0,191,179,0.55); color: #00BFB3; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Search · future</div>
    <h1 class="headline fade-up-2">Serverless Search &amp; <strong>federated blob sources</strong></h1>
    <p class="sub fade-up-3">Same project → register S3 / GCS / Azure. Query archives in place. No second sized cluster on cold data.</p>
    <div class="pill-row fade-up-3">
      <span class="pill future">Enterprise Search roadmap</span>
      <span class="pill">S3 · GCS · Azure</span>
      <span class="pill hot">One Serverless project</span>
    </div>
    <div class="compare">
      <div class="card fade-up-4"><div class="label">Today (lab)</div><h3>Managed indices + connectors</h3><p>Hot corpus: KB, runbooks, Meraki events. Federated <em>indices</em> via ES|QL.</p></div>
      <div class="hub fade-up-4">Same project</div>
      <div class="card future fade-up-5"><div class="label">Roadmap</div><h3>+ Federated object storage</h3><p>JSON / Parquet. Schema-on-read. Blob economics for retention.</p></div>
    </div>
    <div class="tiers fade-up-6">
      <div class="tier hot"><div class="t">Managed search tier</div>Lexical + semantic · autocomplete · interactive ms–s</div>
      <div class="tier cold"><div class="t">Federated object tier</div>Query blob in place · archive economics · cents/GB-month</div>
    </div>
  </div>
""",
    bottom="Don’t pay twice for cold — <strong>federate blob</strong>, keep hot Search for AI.",
)

# ── Architecture ─────────────────────────────────────────────────────────────
SLIDES["architecture.html"] = wrap(
    "Architecture",
    """
    .arch { display: flex; flex-direction: column; gap: 12px; flex: 1; min-height: 0; padding-bottom: 4px; }
    .row3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
    .src {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);
      border-radius: 10px; padding: 14px 16px;
    }
    .src.blob { border-color: rgba(167,139,250,0.4); background: rgba(124,58,237,0.08); }
    .src h3 { font-size: 0.9rem; font-weight: 700; margin-bottom: 4px; }
    .src p { font-size: 0.74rem; color: rgba(255,255,255,0.45); line-height: 1.4; }
    .hub-box {
      text-align: center; padding: 16px; border: 1px dashed rgba(167,139,250,0.5);
      border-radius: 12px; background: rgba(167,139,250,0.07); color: #ddd6fe;
      font-weight: 700; font-size: 0.95rem;
    }
    .hub-box small { display: block; margin-top: 6px; font-weight: 400; font-size: 0.74rem; color: rgba(255,255,255,0.4); }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Architecture (future)</div>
    <h1 class="headline fade-up-2">Sources → <strong>Serverless project</strong> → tiers</h1>
    <p class="sub fade-up-3">Enterprise Search UI · ES|QL · semantic rerank · connectors — same surface as today’s lab.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="arch">
      <div class="row3 fade-up-4">
        <div class="src"><h3>Managed Search indices</h3><p>Product docs · runbooks · sub-second UX</p></div>
        <div class="src"><h3>Content connectors</h3><p>SharePoint · web · API sync · incremental</p></div>
        <div class="src blob"><h3>Blob archives</h3><p>S3 / GCS / Azure · JSON &amp; Parquet</p></div>
      </div>
      <div class="hub-box fade-up-5">Serverless Search + federation layer<small>no cluster sizing · schema-on-read · prefix mapping · tier-to-blob</small></div>
      <div class="row3 fade-up-6" style="grid-template-columns:1fr 1fr">
        <div class="src" style="border-color:rgba(0,191,179,0.4)"><h3>Managed search tier</h3><p>ELSER · autocomplete · interactive</p></div>
        <div class="src blob"><h3>Federated object tier</h3><p>Query blob in place · long retention</p></div>
      </div>
    </div>
  </div>
""",
    bottom="One query layer across hot indices and cold prefixes — that’s the analyst takeaway.",
)

# ── Outcomes ─────────────────────────────────────────────────────────────────
SLIDES["outcomes.html"] = wrap(
    "Outcomes",
    """
    .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1; min-height: 0; padding-bottom: 6px; }
    .card {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 16px 18px;
    }
    .card .label {
      font-family: 'JetBrains Mono', monospace; font-size: 0.58rem; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase; color: #00BFB3; margin-bottom: 6px;
    }
    .card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 6px; }
    .card p { font-size: 0.8rem; color: rgba(255,255,255,0.5); line-height: 1.45; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Outcomes</div>
    <h1 class="headline fade-up-2">Unified search &amp; <strong>simpler admin</strong></h1>
    <p class="sub fade-up-3">Today’s lab = hot tier + federated indices. Blob federation is the next hop on the same project.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4"><div class="label">Unified</div><h3>One query, many tiers</h3><p>Managed indices and federated blob prefixes in a single ES|QL or Search request.</p></div>
      <div class="card fade-up-4"><div class="label">Admin</div><h3>Register sources in UI</h3><p>No shard math on cold storage. Federate instead of archive clusters on blob.</p></div>
      <div class="card fade-up-5"><div class="label">Economics</div><h3>Lower TCO</h3><p>Avoid paying twice for frozen/archive — blob for retention, Serverless for hot + AI.</p></div>
      <div class="card fade-up-5"><div class="label">Bridge</div><h3>This lab proves the pattern</h3><p>Modules 2–3 preview the unified query story your team can try on internal data next.</p></div>
    </div>
  </div>
""",
    bottom="Leave them with: <strong>one query across tiers</strong>.",
)

# ── Lab / Close / Thanks ─────────────────────────────────────────────────────
SLIDES["lab.html"] = wrap(
    "Lab provisioning",
    """
    .steps { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 12px; }
    .step {
      display: flex; gap: 16px; align-items: center; padding: 16px 20px; border-radius: 12px;
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    }
    .step .n {
      width: 36px; height: 36px; border-radius: 50%; background: rgba(0,191,179,0.15);
      color: #00BFB3; display: flex; align-items: center; justify-content: center;
      font-weight: 800; font-family: 'JetBrains Mono', monospace; flex-shrink: 0;
    }
    .step p { font-size: 0.95rem; color: rgba(255,255,255,0.72); }
    .step code { font-family: 'JetBrains Mono', monospace; color: #00BFB3; font-size: 0.88em; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">While you wait</div>
    <h1 class="headline fade-up-2">Lab provisioning — <strong>~3–4 minutes</strong></h1>
    <p class="sub fade-up-3">When Elastic Serverless Search opens, start Module 1.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="steps">
      <div class="step fade-up-4"><div class="n">1</div><p>Create <strong>Serverless Search</strong> (vector) via <code>es3-api</code></p></div>
      <div class="step fade-up-5"><div class="n">2</div><p>Proxy Kibana on port <code>8080</code></p></div>
      <div class="step fade-up-6"><div class="n">3</div><p>Seed <code>cisco-network-kb</code>, runbooks, Meraki events, network events</p></div>
    </div>
  </div>
""",
    bottom="Track: <strong>cisco-serverless-workshop</strong> · confirm the KB index first.",
)

SLIDES["close.html"] = wrap(
    "Takeaways",
    """
    .take { display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: center; }
    .card {
      display: flex; gap: 14px; align-items: flex-start;
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px; padding: 12px 16px;
    }
    .icon {
      flex-shrink: 0; width: 36px; height: 36px; border-radius: 10px;
      background: rgba(0,191,179,0.12); color: #00BFB3;
      display: flex; align-items: center; justify-content: center; font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
    }
    .card h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 2px; }
    .card p { font-size: 0.78rem; color: rgba(255,255,255,0.5); }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Close</div>
    <h1 class="headline fade-up-2">What you learned on <strong>Search</strong></h1>
    <p class="sub fade-up-3">Five lines for your notes — share with peers after the lab.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="take">
      <div class="card fade-up-4"><div class="icon">1</div><div><h3>Hybrid AI Search</h3><p>Keyword + semantic on Cisco KB — MTTR, not portal hopping.</p></div></div>
      <div class="card fade-up-4"><div class="icon">2</div><div><h3>Federate sources</h3><p>Connectors + multi-index ES|QL without rip-and-replace.</p></div></div>
      <div class="card fade-up-5"><div class="icon">3</div><div><h3>Agents on Search</h3><p>Grounded tools — NOC action on Elastic Search Serverless only.</p></div></div>
      <div class="card fade-up-5"><div class="icon">4</div><div><h3>Serverless economics</h3><p>One Cloud project, workshop-ready in minutes.</p></div></div>
      <div class="card fade-up-6"><div class="icon">5</div><div><h3>Roadmap: blob federation</h3><p>Same project → query S3/GCS/Azure archives in place.</p></div></div>
    </div>
  </div>
""",
    bottom="Leave with three beats to try on your data: <strong>Search → Federate → Agents</strong>.",
)

SLIDES["thank-you.html"] = wrap(
    "Thank you",
    """
    .thanks {
      position: relative; z-index: 10; flex: 1; display: flex; flex-direction: column;
      align-items: center; justify-content: center; text-align: center; padding: 0 40px;
    }
    .thanks h1 { font-size: 3.5rem; font-weight: 300; letter-spacing: -0.03em; margin: 0.6rem 0 1rem; }
    .thanks h1 strong { font-weight: 800; }
    .thanks p { font-size: 1.05rem; color: rgba(255,255,255,0.5); line-height: 1.55; max-width: 640px; }
    .thanks a { color: #00BFB3; text-decoration: none; font-weight: 600; }
    .pill-row { display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; margin-top: 1.4rem; }
    .pill {
      font-size: 0.68rem; padding: 5px 12px; border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.14); color: rgba(255,255,255,0.55);
    }
    .pill.hot { border-color: rgba(0,191,179,0.55); color: #00BFB3; }
    .pill.future { border-color: rgba(167,139,250,0.55); color: #c4b5fd; }
    """,
    """
  <div class="thanks">
    <div class="eyebrow fade-up-1">Cisco × Elastic</div>
    <h1 class="fade-up-2">Thank <strong>you</strong>.</h1>
    <p class="fade-up-3">Questions welcome.<br>
    Lab: <a href="https://play.instruqt.com/manage/elastic/tracks/cisco-serverless-workshop">cisco-serverless-workshop</a></p>
    <div class="pill-row fade-up-4">
      <span class="pill hot">AI Search</span>
      <span class="pill">Federated Sources</span>
      <span class="pill">Agent Builder</span>
      <span class="pill future">Blob roadmap</span>
    </div>
  </div>
""",
    bottom="elastic.co · The Search AI Company",
)


NOTES = {
    "cover.html": "- Search-only Cisco practitioner workshop. One Serverless Search project.\n- Lab ready ~3–4 min while we walk the deck.",
    "agenda.html": "- Three modules, same indices. Find → unify → act.\n- Search-only scope — no O11Y/Sec.",
    "pain.html": "- Swivel-chair pain. Point at the MTTR bars as they animate.\n- Target: one Search surface.",
    "serverless.html": "- Four advantages. Explicitly: no Observability/Security required.",
    "ai-search.html": "- Hybrid product story. NOC quote lands the module.",
    "foundations.html": "- Walk KEYWORD → SEMANTIC → HYBRID. Pause on RRF fuse.\n- Bottom line: hybrid is what you prove live on cisco-network-kb.",
    "hybrid.html": "- Lab checklist. Don't linger on UI — land the one-surface line.",
    "federated.html": "- Animated converge. Federate don't rip-and-replace.",
    "esql.html": "- Branch 4471 thread into Module 3.",
    "agents.html": "- Grounded tools. Elastic Search Serverless only. Watch the pulse along the pipeline.",
    "noc-story.html": "- 90-second recap. Practice out loud with a peer.",
    "future.html": "- Clear bridge today vs roadmap. Economic punch: don't pay twice for cold.",
    "architecture.html": "- Sources → federation → tiers. Takeaway: one query layer.",
    "outcomes.html": "- Unified / admin / TCO / bridge.",
    "lab.html": "- Orient: es3-api, 8080, four seed indices.",
    "close.html": "- Five takeaways on screen for Q&A.",
    "thank-you.html": "- Point to Instruqt manage URL.",
}


def main() -> None:
    for name, html in SLIDES.items():
        write(name, html)
    (ROOT / "notes.json").write_text(json.dumps(NOTES, indent=2) + "\n", encoding="utf-8")
    print("  wrote notes.json")
    print(f"\n✓ Generated {len(SLIDES)} slides (+ foundations handcrafted)")


if __name__ == "__main__":
    main()
