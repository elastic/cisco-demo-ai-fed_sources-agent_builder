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
    "Elastic Search — Find, Federate, Act with Agent Builder & A2A",
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
      display: flex; flex-direction: column; justify-content: center; max-width: 68%;
    }
    .c-eyebrow {
      font-size: 0.75rem; font-weight: 700; letter-spacing: 0.16em;
      text-transform: uppercase; color: #00BFB3; margin-bottom: 1.35rem;
    }
    .c-title {
      font-size: 3.2rem; font-weight: 300; letter-spacing: -0.03em;
      line-height: 1.05; margin-bottom: 1.15rem;
    }
    .c-title strong { font-weight: 800; color: #fff; }
    .c-title em { font-style: normal; font-weight: 800; color: #00BFB3; }
    .c-sub {
      font-size: 1.05rem; color: rgba(255,255,255,0.58); line-height: 1.55;
      max-width: 560px; margin-bottom: 1.6rem;
    }
    .pill-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .pill {
      font-size: 0.68rem; padding: 5px 12px; border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.14); color: rgba(255,255,255,0.55);
    }
    .pill.hot { border-color: rgba(0,191,179,0.55); color: #00BFB3; }
    .pill.cisco { border-color: rgba(4,159,217,0.55); color: #049FD9; }
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
    <div class="c-eyebrow fade-up-1">Cisco × Elastic · Serverless Search workshop</div>
    <h1 class="c-title fade-up-2"><strong>Find.</strong> <em>Federate.</em> <strong>Act.</strong></h1>
    <p class="c-sub fade-up-3"><strong style="color:#fff;font-weight:600">Cisco NOC Copilot</strong> on Agent Builder queries Elastic indices.
    <strong style="color:#fff;font-weight:600">Workflows + A2A</strong> augment with Splunk Observability evidence — without rip-and-replace.</p>
    <div class="pill-row fade-up-4">
      <span class="pill hot">Cisco NOC Copilot</span>
      <span class="pill cisco">Workflows + A2A</span>
      <span class="pill">Branch 4471</span>
      <span class="pill hot">~60–90 min with AI</span>
    </div>
  </div>
  <div class="cover-foot fade-up-5">
    <span>One Serverless Search project</span><span>·</span><span>Lab ready in ~3–4 minutes</span>
  </div>
""",
    bottom="Same lab story end-to-end: **Agent Builder** for Elastic · **Workflows/A2A** for peer-platform augment.",
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
    <div class="eyebrow fade-up-1">Today · matches the Instruqt lab</div>
    <h1 class="headline fade-up-2">Find → Federate → <strong>Act</strong></h1>
    <p class="sub fade-up-3">Nine challenges on one Serverless Search project — Agent Builder, Workflows + Splunk O11Y A2A, then federation.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="flow">
      <div class="card fade-up-4">
        <span class="num">MODULE 01 · FIND</span>
        <h3>Cisco NOC Copilot</h3>
        <p>Stand up the agent, pull Meraki + BGP runbooks, then augment with a stubbed Splunk O11Y A2A workflow.</p>
        <span class="mono">Agent Builder · Workflows</span>
      </div>
      <div class="arrow fade-up-4">→</div>
      <div class="card fade-up-5">
        <span class="num">MODULE 02 · FEDERATE</span>
        <h3>Map the silos</h3>
        <p>Four Search indices + content connectors. Correlate event ↔ runbook. Plan federation without rip-and-replace.</p>
        <span class="mono">indices · ES|QL · connectors</span>
      </div>
      <div class="arrow fade-up-5">→</div>
      <div class="card fade-up-6">
        <span class="num">MODULE 03 · ACT</span>
        <h3>Triage &amp; harden</h3>
        <p>Re-run Branch 4471 with Agent + A2A. Tighten tools. Close with a Find → Federate → Act recap.</p>
        <span class="mono">pager card · P2 note</span>
      </div>
    </div>
  </div>
""",
    bottom="If the room remembers one chain: <strong>Find → Federate → Act</strong> — Agent for Elastic, A2A for peer evidence.",
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
    <h1 class="headline fade-up-2">Branch 4471 pain: <strong>swivel-chair MTTR</strong></h1>
    <p class="sub fade-up-3">Meraki offline + BGP Idle — evidence in Elastic <em>and</em> Splunk O11Y. Today’s lab shows how to query one and augment the other.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="layout">
      <div class="silos fade-up-4">
        <div class="silo"><span class="dot"></span><div><strong>Meraki events</strong><span>device.offline · Branch-4471-Dallas</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>Network / BGP</strong><span>session_down · edge-dfw-01</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>KB + runbooks</strong><span>TAC recovery · escalation owners</span></div></div>
        <div class="silo"><span class="dot"></span><div><strong>Splunk Observability</strong><span>Detectors / APM — augment via A2A, don’t rip out</span></div></div>
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
      {label:'Manual write-ups', v:0.92, color:'#049FD9'},
      {label:'Agent + A2A', v:0.28, color:'#00BFB3'},
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
    bottom="Lab pacing: <strong>~60–90 min with Agent + Workflows</strong> vs ~3.5–4.5 hours of manual RCA write-ups.",
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
    <h1 class="headline fade-up-2">One <strong>Serverless Search</strong> project</h1>
    <p class="sub fade-up-3">Search-only lab — Agent Builder, Workflows, dashboards, and four Cisco indices. No Observability or Security projects.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4"><div class="label">Seeded for you</div><h3>Cisco NOC Copilot</h3><p>Agent Builder agent <code style="color:#00BFB3">cisco-noc-copilot</code> + NOC dashboard + Branch 4471 data.</p></div>
      <div class="card fade-up-4"><div class="label">Augment path</div><h3>A2A workflow stub</h3><p><code style="color:#00BFB3">cisco-branch-4471-splunk-o11y-a2a-rca</code> — Elastic gather → stubbed Splunk O11Y → unified RCA.</p></div>
      <div class="card fade-up-5"><div class="label">Four indices</div><h3>Federation-ready</h3><p><code style="color:#00BFB3">cisco-network-kb</code>, runbooks, Meraki events, network/BGP events — one query surface.</p></div>
      <div class="card fade-up-5"><div class="label">Time</div><h3>~3–4 min to ready</h3><p>Per-learner Cloud project in Instruqt. Then the nine challenges mirror Find → Federate → Act.</p></div>
    </div>
  </div>
""",
    bottom="Platform call: <strong>Serverless Search only</strong> — Splunk stays peer via A2A, not a second Elastic product.",
)

# ── Find · Cisco NOC Copilot ─────────────────────────────────────────────────
SLIDES["ai-search.html"] = wrap(
    "Find — Cisco NOC Copilot",
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
    <div class="eyebrow fade-up-1">Module 1 · Find · Challenges 1 &amp; 3</div>
    <h1 class="headline fade-up-2">Don’t start in Discover — <strong>start the agent</strong></h1>
    <p class="sub fade-up-3"><span style="font-family:JetBrains Mono,monospace;color:#00BFB3">Cisco NOC Copilot</span> queries Serverless Search — then you reuse it for every later challenge.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4">
        <div class="label">What you build</div><h3>Cisco NOC Copilot</h3>
        <ul>
          <li><strong>Tools</strong> on KB, Meraki events, network/BGP events</li>
          <li><strong>Goal</strong> — Branch 4471 investigate + draft next steps</li>
          <li><strong>Proof</strong> — Meraki offline + BGP neighbor runbooks</li>
        </ul>
      </div>
      <div class="card fade-up-5">
        <div class="label">Why teams care</div><h3>AI time compression</h3>
        <ul>
          <li><strong>~5 min</strong> with Agent Builder vs 15–20 manual</li>
          <li><strong>Grounded</strong> tool calls — not invented runbooks</li>
          <li><strong>Peer story</strong> — agent drafts the Slack/email update</li>
        </ul>
      </div>
    </div>
    <div class="quote fade-up-6">“Branch 4471 — Meraki AP offline, edge BGP looking ugly. Where's the recovery runbook?”</div>
  </div>
""",
    bottom="Lab tip: select <strong>Cisco NOC Copilot</strong> (not only Elastic AI Agent). Seeded at setup.",
)

# Lab value — what Instruqt proves today
SLIDES["value.html"] = wrap(
    "What the lab proves",
    """
    .grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; flex: 1; min-height: 0; }
    .card {
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px; padding: 18px 16px; display: flex; flex-direction: column; gap: 8px;
    }
    .card .label {
      font-family: 'JetBrains Mono', monospace; font-size: 0.58rem; font-weight: 700;
      letter-spacing: 0.1em; text-transform: uppercase; color: #00BFB3;
    }
    .card h3 { font-size: 1.05rem; font-weight: 700; }
    .card p { font-size: 0.8rem; color: rgba(255,255,255,0.52); line-height: 1.5; flex: 1; }
    .card .mono { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #049FD9; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Lab value · Instruqt</div>
    <h1 class="headline fade-up-2">Three surfaces. <strong>One Branch 4471 story.</strong></h1>
    <p class="sub fade-up-3">Everything you click in the workshop maps to a customer conversation.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid3">
      <div class="card fade-up-4">
        <div class="label">Agent Builder</div>
        <h3>Query Elastic</h3>
        <p>Cisco NOC Copilot retrieves Meraki + BGP + KB evidence and drafts NOC-ready notes.</p>
        <span class="mono">/app/agent_builder</span>
      </div>
      <div class="card fade-up-5">
        <div class="label">Workflows + A2A</div>
        <h3>Augment Splunk</h3>
        <p>Stubbed Splunk O11Y investigator response — WAN/BGP first, do not RMA the AP.</p>
        <span class="mono">…splunk-o11y-a2a-rca</span>
      </div>
      <div class="card fade-up-6">
        <div class="label">Federation</div>
        <h3>Keep systems</h3>
        <p>Content connectors + four indices. Meraki/ITSM stay authoritative; Search is the query layer.</p>
        <span class="mono">search_connectors</span>
      </div>
    </div>
  </div>
""",
    bottom="Talk track: <strong>augment, don’t rip-and-replace</strong> — Elastic for Search/Agent, Splunk via A2A.",
)

# A2A / Workflows (replaces old hybrid lab-proof slide in the flow)
SLIDES["a2a.html"] = wrap(
    "Workflows + Splunk O11Y A2A",
    """
    .steps { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 10px; }
    .step {
      display: flex; gap: 16px; align-items: flex-start; padding: 14px 18px; border-radius: 12px;
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    }
    .step .n {
      width: 36px; height: 36px; border-radius: 50%; background: rgba(0,191,179,0.15);
      color: #00BFB3; display: flex; align-items: center; justify-content: center;
      font-weight: 800; flex-shrink: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem;
    }
    .step h3 { font-size: 0.95rem; font-weight: 700; margin-bottom: 2px; }
    .step p { font-size: 0.82rem; color: rgba(255,255,255,0.55); line-height: 1.45; }
    .step code { font-family: 'JetBrains Mono', monospace; color: #00BFB3; font-size: 0.85em; }
    """,
    """
  <div class="slide">
    <div class="eyebrow fade-up-1">Module 1 · Challenge 2 · (also 7–8)</div>
    <h1 class="headline fade-up-2">Agent answers Elastic. <strong>A2A augments Splunk.</strong></h1>
    <p class="sub fade-up-3">Workflow gathers Meraki/BGP/KB context, then injects a stubbed Splunk O11Y investigator payload.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="steps">
      <div class="step fade-up-4"><div class="n">1</div><div><h3>Run the workflow</h3><p><code>Cisco Branch 4471 — Splunk O11Y A2A RCA</code> · defaults <code>site=Branch-4471-Dallas</code></p></div></div>
      <div class="step fade-up-5"><div class="n">2</div><div><h3>Confirm stub evidence</h3><p><code>WAN_EDGE_BGP_SESSION_DOWN</code> on edge-dfw-01 · <code>MERAKI_AP_CLOUD_DISCONNECT</code> on MR-AP-4471</p></div></div>
      <div class="step fade-up-6"><div class="n">3</div><div><h3>Feed into Cisco NOC Copilot</h3><p>Paste the A2A summary → correlated RCA: <strong>WAN/BGP first — do not RMA the AP</strong></p></div></div>
    </div>
  </div>
""",
    bottom="Production swap: replace the stub with <strong>http POST</strong> to your A2A bridge — lab pattern stays the same.",
)

# Keep hybrid.html as a short foundations pointer (optional / secondary)
SLIDES["hybrid.html"] = wrap(
    "Why Search ranks",
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
    <div class="eyebrow fade-up-1">Search foundation · supporting</div>
    <h1 class="headline fade-up-2">The agent is only as good as <strong>the corpus</strong></h1>
    <p class="sub fade-up-3">Hybrid retrieval (keyword + semantic) is why Meraki + IOS-XE runbooks land in one ranked set.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="steps">
      <div class="step fade-up-4"><div class="n">1</div><p>Corpus lives in <code>cisco-network-kb</code> (+ events / runbooks)</p></div>
      <div class="step fade-up-5"><div class="n">2</div><p>Agent tools call ES|QL / search — same indices humans verify in Discover</p></div>
      <div class="step fade-up-6"><div class="n">3</div><p>If Discover looks empty: set time to <strong>Last 24 hours</strong></p></div>
    </div>
  </div>
""",
    bottom="Next: federate sources in place — then harden the Copilot for Act.",
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
    <div class="eyebrow fade-up-1">Module 2 · Challenges 4–6</div>
    <h1 class="headline fade-up-2">Federate — <strong>don’t rip-and-replace</strong></h1>
    <p class="sub fade-up-3">Four Search indices simulate connector-fed silos. Content connectors keep Meraki/ITSM authoritative.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="canvas-wrap fade-up-4"><canvas id="cvFed"></canvas></div>
  </div>
""",
    scripts="""
<script>
(function(){
  const canvas=document.getElementById('cvFed');
  const r=window.devicePixelRatio||1;
  const sources=['KB','Runbooks','Meraki events','BGP / network'];
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
    ctx.fillText('Agent + ES|QL', ex, ey-2);
    ctx.font='500 10px Inter,sans-serif'; ctx.fillStyle='rgba(255,255,255,0.45)';
    ctx.fillText('+ A2A augment', ex, ey+16);
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
    bottom="Challenge 6 talk track: connectors feed Search; <strong>Copilot + A2A</strong> query and augment.",
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
    <div class="eyebrow fade-up-1">Module 2 · Challenge 5</div>
    <h1 class="headline fade-up-2">Agent correlates. <strong>ES|QL verifies.</strong></h1>
    <p class="sub fade-up-3">Primary path: ask Cisco NOC Copilot. Optional verify in ES|QL (time picker → <strong>Last 24 hours</strong> if empty).</p>
    <div class="header-divider fade-up-3"></div>
    <div class="code fade-up-4">
      <span class="cm">// Challenge 5 — Meraki offline for Branch 4471</span><br>
      <span class="kw">FROM</span> cisco-meraki-events<br>
      <span class="kw">| WHERE</span> event_type == <span class="str">"device.offline"</span> <span class="kw">AND</span> device_name <span class="kw">LIKE</span> <span class="str">"*4471*"</span><br>
      <span class="kw">| KEEP</span> @timestamp, device_name, site, event_type, detail<br>
      <span class="kw">| SORT</span> @timestamp <span class="kw">DESC</span><br>
      <span class="kw">| LIMIT</span> 5
    </div>
  </div>
""",
    bottom="Then ask the agent for the matching <strong>KB recovery runbook</strong> — event + runbook in one incident card.",
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
    <div class="eyebrow fade-up-1">Module 3 · Challenges 7–8</div>
    <h1 class="headline fade-up-2">Act — <strong>triage, then harden</strong></h1>
    <p class="sub fade-up-3">Re-run Branch 4471 with Copilot + A2A. Put the Splunk workflow into agent instructions.</p>
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
    {label:'Elastic', sub:'Meraki + BGP', c:'#fff'},
    {label:'Copilot', sub:'NOC agent', c:'#049FD9'},
    {label:'A2A', sub:'Splunk stub', c:'#a78bfa'},
    {label:'RCA', sub:'WAN/BGP first', c:'#00BFB3'},
    {label:'P2', sub:'escalate', c:'#6ee7c7'},
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
    bottom="Harden instructions: summarize Elastic first · then run the <strong>A2A workflow</strong> · never invent Splunk telemetry.",
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
    <div class="eyebrow fade-up-1">Workshop story arc · Challenge 9</div>
    <h1 class="headline fade-up-2">Find → Federate → Act in <strong>90 seconds</strong></h1>
    <p class="sub fade-up-3">Practice this close-out out loud — same prompt the lab agent writes for you.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="beats">
      <div class="beat fade-up-4"><div class="n">1</div><div><h3>Find</h3><p>“Cisco NOC Copilot pulled Meraki + BGP runbooks from Search.”</p></div></div>
      <div class="beat fade-up-5"><div class="n">2</div><div><h3>Federate</h3><p>“Four indices + connectors — systems stay authoritative; Search queries them.”</p></div></div>
      <div class="beat fade-up-6"><div class="n">3</div><div><h3>Act + A2A</h3><p>“Workflow stubbed Splunk O11Y — WAN/BGP first; AP RMA is secondary.”</p></div></div>
    </div>
  </div>
""",
    bottom="If the room only hears one story, make it <strong>Branch 4471 + A2A augment</strong>.",
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
    <div class="eyebrow fade-up-1">Outcomes · what buyers hear</div>
    <h1 class="headline fade-up-2">What you can <strong>say after the lab</strong></h1>
    <p class="sub fade-up-3">Mapped 1:1 to the Instruqt success criteria — not a roadmap wishlist.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="grid2">
      <div class="card fade-up-4"><div class="label">Find</div><h3>Cisco NOC Copilot</h3><p>Agent Builder grounded in Search indices — Meraki + BGP runbooks in minutes, not portal hops.</p></div>
      <div class="card fade-up-4"><div class="label">Augment</div><h3>Workflows + A2A</h3><p>Peer-platform evidence (Splunk O11Y) without rip-and-replace — lab stub today, real bridge tomorrow.</p></div>
      <div class="card fade-up-5"><div class="label">Federate</div><h3>Connectors + indices</h3><p>Keep Meraki/ITSM authoritative. Elastic is the query/augment layer for NOC copilots.</p></div>
      <div class="card fade-up-5"><div class="label">Pace</div><h3>AI time compression</h3><p>~60–90 minutes with Agent + Workflows vs hours of manual RCA and peer write-ups.</p></div>
    </div>
  </div>
""",
    bottom="Leave them with: <strong>Agent for Elastic · A2A for Splunk · connectors for federation</strong>.",
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
    <p class="sub fade-up-3">When Kibana opens, Challenge 1 starts in Agent Builder — not raw Discover.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="steps">
      <div class="step fade-up-4"><div class="n">1</div><p>Serverless Search project + seeded indices / dashboard / workflow</p></div>
      <div class="step fade-up-5"><div class="n">2</div><p>Select <strong>Cisco NOC Copilot</strong> in Agent Builder</p></div>
      <div class="step fade-up-6"><div class="n">3</div><p>If Discover/ES|QL is empty → time picker <strong>Last 24 hours</strong></p></div>
    </div>
  </div>
""",
    bottom="Track: <strong>cisco-serverless-workshop</strong> · Find → Federate → Act.",
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
    <div class="eyebrow fade-up-1">Close · Challenge 9</div>
    <h1 class="headline fade-up-2">Takeaways that match the <strong>lab</strong></h1>
    <p class="sub fade-up-3">Same five bullets the Cisco Agent helps you write in the close-out prompt.</p>
    <div class="header-divider fade-up-3"></div>
    <div class="take">
      <div class="card fade-up-4"><div class="icon">1</div><div><h3>Cisco NOC Copilot</h3><p>Agent Builder on Serverless Search — grounded Meraki + BGP + KB tools.</p></div></div>
      <div class="card fade-up-4"><div class="icon">2</div><div><h3>Workflows + A2A</h3><p>Augment Splunk O11Y evidence without rip-and-replace (stub → real bridge).</p></div></div>
      <div class="card fade-up-5"><div class="icon">3</div><div><h3>Federate in place</h3><p>Four indices + content connectors — systems stay authoritative.</p></div></div>
      <div class="card fade-up-5"><div class="icon">4</div><div><h3>Find → Federate → Act</h3><p>One Branch 4471 story across nine challenges.</p></div></div>
      <div class="card fade-up-6"><div class="icon">5</div><div><h3>AI time compression</h3><p>Paste prompts beat manual RCA write-ups — hours become minutes.</p></div></div>
    </div>
  </div>
""",
    bottom="Next experiment: connector POC, more agent tools, or a <strong>real A2A bridge URL</strong>.",
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
      <span class="pill hot">Cisco NOC Copilot</span>
      <span class="pill">Workflows + A2A</span>
      <span class="pill">Find → Federate → Act</span>
      <span class="pill hot">Branch 4471</span>
    </div>
  </div>
""",
    bottom="elastic.co · The Search AI Company",
)


NOTES = {
    "cover.html": "- Lead with Find → Federate → Act.\n- Cisco NOC Copilot + Workflows/A2A are the lab heroes.",
    "agenda.html": "- Three modules match Instruqt Challenges 1–9.\n- Search-only — Splunk via A2A, not a second Elastic product.",
    "pain.html": "- Meraki + BGP + Splunk silos. Bars = manual vs Agent+A2A pace.",
    "serverless.html": "- Seeded Copilot, A2A workflow, four indices. No O11Y/Sec projects.",
    "value.html": "- Three surfaces buyers remember: Agent Builder, Workflows/A2A, federation.",
    "ai-search.html": "- Challenge 1: don't start in Discover — select Cisco NOC Copilot.",
    "a2a.html": "- Challenge 2 hero slide. WAN/BGP first — do not RMA the AP.\n- Stub today → real A2A bridge later.",
    "foundations.html": "- Optional depth: KEYWORD → SEMANTIC → HYBRID. Supporting, not the lab hero.",
    "hybrid.html": "- Corpus + 24h tip. Keep short — A2A is the bigger claim.",
    "federated.html": "- Challenges 4–6. Four indices + content connectors. Federate don't rip.",
    "esql.html": "- Challenge 5 verify query. Agent correlates; ES|QL confirms.",
    "agents.html": "- Challenges 7–8: triage + harden instructions with A2A workflow name.",
    "noc-story.html": "- Challenge 9 90-second close-out. Practice out loud.",
    "outcomes.html": "- Buyer-ready outcomes mapped to lab success criteria.",
    "lab.html": "- While provisioning: Copilot first, Last 24 hours tip.",
    "close.html": "- Five takeaways = Challenge 9 bullets.",
    "thank-you.html": "- Point to cisco-serverless-workshop manage URL.",
    "future.html": "- Optional appendix: blob federation roadmap (not in lab path).",
    "architecture.html": "- Optional appendix: tiers diagram.",
}


def main() -> None:
    for name, html in SLIDES.items():
        write(name, html)
    (ROOT / "notes.json").write_text(json.dumps(NOTES, indent=2) + "\n", encoding="utf-8")
    print("  wrote notes.json")
    print(f"\n✓ Generated {len(SLIDES)} slides (+ foundations handcrafted)")


if __name__ == "__main__":
    main()
