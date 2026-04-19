#!/usr/bin/env python3
"""PLAYBOOK AI v3 — Full assembler with extended content"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from build import HEAD, CSS, TOOLS_DATA
from content import CONTENT
from content_v2 import CONTENT_V2
from extensions.ext_01_07 import EXT as E1
from extensions.ext_08_14 import EXT as E2
from extensions.ext_15_21 import EXT as E3
from extensions.ext_22_28 import EXT as E4
from assemble_v2 import ALL_TOOLS, ALL_TOOL_CSS, tool_style, render_terminal, render_sidebar, TOPBAR, JS

ALL_CONTENT = {**CONTENT, **CONTENT_V2}
ALL_EXT = {}
for d in [E1, E2, E3, E4]:
    ALL_EXT.update(d)

# ── Render landing (reuse from v2) ────────────────────────────────────────
from assemble_v2 import render_landing

# ── Extended Tool Page ────────────────────────────────────────────────────
def render_ext_tool_page(t, c, ext):
    tid, num, name, cat, catshort, accent, income, skill, ttd, price, tagline = t
    r,g,b = int(accent[1:3],16), int(accent[3:5],16), int(accent[5:7],16)

    # ── What it is ──
    what_html = f'<p class="what-text">{c["what_it_is"]}</p>'

    # ── Money map (original 4 + 2 more from ext) ──
    all_streams = list(c['money_streams']) + list(ext.get('more_streams', []))
    streams_html = '<div class="money-map">'
    for i, stream in enumerate(all_streams):
        if len(stream) == 4:
            sname, srange, sdesc, stime = stream
        else:
            sname, srange, sdesc = stream; stime = ""
        badge = ' new-stream' if i >= 4 else ''
        streams_html += f'''<div class="money-stream{badge}">
          <div class="stream-name">{sname}</div>
          <div class="stream-range">{srange}</div>
          <div class="stream-desc">{sdesc}</div>
          <div class="stream-time"><i class="ph ph-clock"></i>{stime}</div>
        </div>'''
    streams_html += '</div>'

    # ── Use Cases ──
    use_cases_html = '<div class="use-cases-grid">'
    for uc_title, uc_body in ext.get('use_cases', []):
        use_cases_html += f'''<div class="use-case-card">
          <div class="uc-title">{uc_title}</div>
          <p class="uc-body">{uc_body}</p>
        </div>'''
    use_cases_html += '</div>'

    # ── Niche table ──
    niche_rows = ''
    for niche, workflow, rate in ext.get('niche_table', []):
        niche_rows += f'''<tr>
          <td class="niche-name">{niche}</td>
          <td class="niche-workflow">{workflow}</td>
          <td class="niche-rate" style="color:{accent}">{rate}</td>
        </tr>'''
    niche_html = f'''<div class="niche-table-wrap">
      <table class="niche-table">
        <thead><tr><th>Niche</th><th>What You Build / Deliver</th><th>Rate Card</th></tr></thead>
        <tbody>{niche_rows}</tbody>
      </table>
    </div>''' if niche_rows else ''

    # ── Pricing tiers ──
    pricing_html = '<div class="pricing-tiers">'
    for pt_name, pt_price, pt_desc in ext.get('pricing_tiers', []):
        pricing_html += f'''<div class="pricing-tier">
          <div class="pt-name">{pt_name}</div>
          <div class="pt-price" style="color:{accent}">{pt_price}</div>
          <p class="pt-desc">{pt_desc}</p>
        </div>'''
    pricing_html += '</div>'

    # ── Client script ──
    script_raw = ext.get('client_script', '')
    script_html = ''
    if script_raw:
        lines = script_raw.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        script_html = f'''<div class="client-script-box">
          <div class="cs-label"><i class="ph ph-chat-teardrop-dots"></i> Client Acquisition Script</div>
          <pre class="cs-text">{lines}</pre>
        </div>'''

    # ── Setup steps (original) ──
    steps_html = '<div class="steps-list">'
    for i, step in enumerate(c['steps']):
        step_title, step_desc, step_cmd = step
        term = ''
        if step_cmd:
            lines = step_cmd.strip().split('\n')
            term_steps = [(ln.rstrip(), '') for ln in lines if ln.strip()]
            term = render_terminal(term_steps)
        steps_html += f'''<div class="step-block">
          <div class="step-num">{str(i+1).zfill(2)}</div>
          <div>
            <div class="step-title">{step_title}</div>
            <p class="step-desc">{step_desc}</p>
            {term}
          </div>
        </div>'''

    # ── Advanced steps (ext) ──
    adv_start = len(c['steps']) + 1
    for i, adv in enumerate(ext.get('advanced_steps', [])):
        adv_title, adv_desc = adv[0], adv[1]
        steps_html += f'''<div class="step-block advanced-step">
          <div class="step-num" style="background:rgba({r},{g},{b},0.15);color:{accent}">{str(adv_start+i).zfill(2)}</div>
          <div>
            <div class="step-title">{adv_title} <span class="adv-badge">Advanced</span></div>
            <p class="step-desc">{adv_desc}</p>
          </div>
        </div>'''
    steps_html += '</div>'

    # ── CLI reference ──
    cli_html = ''
    if c.get('terminal_steps'):
        cli_html = render_terminal([(cmd, cmt) for cmd, cmt, *_ in c['terminal_steps']])

    # ── All prompts (original + extra) ──
    all_prompts = list(c.get('prompts', [])) + list(ext.get('extra_prompts', []))
    prompts_html = ''
    for j, (plabel, ptext) in enumerate(all_prompts):
        ptext_e = ptext.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        badge = ' <span class="new-badge">+NEW</span>' if j >= len(c.get('prompts',[])) else ''
        prompts_html += f'''<div class="prompt-block">
          <div class="prompt-label"><i class="ph ph-copy"></i>{plabel}{badge}</div>
          <pre class="prompt-text">{ptext_e}</pre>
        </div>'''

    # ── Insights ──
    insights_html = ''
    for icon, ititle, itext in c.get('insights', []):
        insights_html += f'''<div class="insight-card">
          <i class="ph-fill ph-{icon}"></i>
          <div><div class="insight-title">{ititle}</div><div class="insight-text">{itext}</div></div>
        </div>'''

    # ── Stack ──
    stack_html = '<div class="stack-items">'
    for item in c.get('stack', []):
        n = item.split('(')[0].strip()
        d = item.split('(')[1].rstrip(')') if '(' in item else ''
        stack_html += f'<div class="stack-chip"><i class="ph ph-plugs-connected"></i><span><strong>{n}</strong>{" — "+d if d else ""}</span></div>'
    stack_html += '</div>'

    # ── Sidebar ──
    skill_map = {'Beginner': 30, 'Intermediate': 65, 'Advanced': 90}
    skill_pct = skill_map.get(skill.split()[0], 50)
    facts_html = '<div class="quick-facts">'
    for k, v in c.get('facts', {}).items():
        cc = 'green' if any(x in v for x in ['Free','Beginner']) else ''
        facts_html += f'<div class="fact-row"><span class="fact-key">{k}</span><span class="fact-val {cc}">{v}</span></div>'
    facts_html += '</div>'
    warn_html = ''.join(f'<div class="warning-box"><i class="ph ph-warning"></i><p class="warning-text">{w}</p></div>' for w in c.get('warnings',[]))
    tip_html  = ''.join(f'<div class="tip-box"><i class="ph ph-lightbulb"></i><p class="tip-text">{tip}</p></div>' for tip in c.get('tips',[]))
    income_badge = f'<div class="income-badge"><i class="ph ph-currency-dollar"></i><span>{income} estimated monthly income</span></div>'

    return f'''
<div id="tool-{tid}" class="page tool-page" data-tool="{tid}" style="--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)">
  <div class="tool-hero">
    <div class="tool-hero-top">
      <div class="tool-hero-left">
        <div class="tool-number">{num} / 28 — {cat}</div>
        <h1 class="tool-name">{name}</h1>
        <div class="tool-category-badge"><i class="ph ph-tag"></i>{catshort}</div>
        <p class="tool-tagline">{tagline}</p>
      </div>
    </div>
    <div class="tool-meta-grid">
      <div class="tool-meta-cell"><div class="tool-meta-label">Monthly Income</div><div class="tool-meta-value income">{income}</div><div class="tool-meta-sub">Estimated range</div></div>
      <div class="tool-meta-cell"><div class="tool-meta-label">Skill Level</div><div class="tool-meta-value">{skill}</div><div class="tool-meta-sub">To get started</div></div>
      <div class="tool-meta-cell"><div class="tool-meta-label">Time to First Dollar</div><div class="tool-meta-value">{ttd}</div><div class="tool-meta-sub">If you start today</div></div>
      <div class="tool-meta-cell"><div class="tool-meta-label">Pricing</div><div class="tool-meta-value">{price}</div><div class="tool-meta-sub">Entry cost</div></div>
    </div>
  </div>

  <div class="tool-content">
    <div class="tool-main">

      <div class="section-h"><i class="ph-fill ph-info"></i><h2>What It Is</h2></div>
      {what_html}

      <div class="section-h" style="margin-top:48px"><i class="ph-fill ph-users-three"></i><h2>Real Use Cases</h2></div>
      <p class="section-label-sub">Specific ways people are making money with {name} right now.</p>
      {use_cases_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-currency-dollar"></i><h2>The Money Map</h2></div>
      {income_badge}
      {streams_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-table"></i><h2>Niche Breakdown</h2></div>
      <p class="section-label-sub">The highest-paying niches for {name} and realistic rate cards.</p>
      {niche_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-tag"></i><h2>Pricing Templates</h2></div>
      <p class="section-label-sub">Exact packages and prices to charge. Copy these directly.</p>
      {pricing_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-steps"></i><h2>Setup Guide</h2></div>
      {steps_html}
      {f'<div class="section-h" style="margin-top:40px"><i class="ph-fill ph-terminal-window"></i><h2>CLI Quick Reference</h2></div>{cli_html}' if cli_html else ''}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-chat-teardrop-text"></i><h2>Copy-Paste Prompts</h2></div>
      <p class="section-label-sub">Use these directly. Modify the bracketed sections for your context.</p>
      {prompts_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-megaphone"></i><h2>Client Acquisition Script</h2></div>
      <p class="section-label-sub">Proven outreach copy to land your first paying client with {name}.</p>
      {script_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-brain"></i><h2>Operator Insights</h2></div>
      {insights_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-stack"></i><h2>The Stack</h2></div>
      <p class="section-label-sub">Tools that pair with {name} to unlock more income streams.</p>
      {stack_html}

    </div>

    <div class="tool-sidebar-panel">
      <div class="panel-title">Quick Facts</div>
      {facts_html}
      <div class="section-divider" style="margin:20px 0"></div>
      <div class="panel-title">Skill Level</div>
      <div class="skill-meter">
        <div class="skill-meter-label"><span class="skill-name">Entry Barrier</span><span class="skill-val">{skill}</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{skill_pct}%"></div></div>
      </div>
      <div class="skill-meter">
        <div class="skill-meter-label"><span class="skill-name">Income Potential</span><span class="skill-val">High</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:85%"></div></div>
      </div>
      <div class="skill-meter" style="margin-bottom:28px">
        <div class="skill-meter-label"><span class="skill-name">Speed to Revenue</span><span class="skill-val">{ttd}</span></div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{max(15, 90 - skill_pct)}%"></div></div>
      </div>
      <div class="section-divider" style="margin:0 0 20px"></div>
      <div class="panel-title">Watch Out For</div>
      {warn_html}
      <div class="panel-title" style="margin-top:20px">Pro Tips</div>
      {tip_html}
    </div>
  </div>

  <div class="site-footer" style="justify-content:space-between">
    <div class="footer-logo">PLAYBOOK<span style="color:var(--accent)">AI</span></div>
    <button class="btn-ghost-hero" onclick="showPage('landing')" style="padding:10px 20px;font-size:.75rem">
      <i class="ph ph-house"></i> Home
    </button>
  </div>
</div>'''

# ── Extra CSS for new sections ─────────────────────────────────────────────
EXTRA_CSS = """
/* Use Cases */
.use-cases-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin-bottom:40px}
.use-case-card{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;transition:border-color .2s}
.use-case-card:hover{border-color:var(--tool-accent)}
.uc-title{font-size:.8rem;font-weight:700;color:var(--tool-accent);text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px}
.uc-body{font-size:.82rem;line-height:1.7;color:var(--muted);margin:0}

/* Niche table */
.niche-table-wrap{overflow-x:auto;margin-bottom:40px}
.niche-table{width:100%;border-collapse:collapse;font-size:.82rem}
.niche-table thead tr{border-bottom:1px solid var(--border)}
.niche-table th{padding:10px 14px;text-align:left;font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);font-weight:600}
.niche-table td{padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.04)}
.niche-table tbody tr:hover{background:var(--surface2)}
.niche-name{font-weight:600;color:var(--text)}
.niche-workflow{color:var(--muted)}
.niche-rate{font-weight:700;white-space:nowrap}

/* Pricing tiers */
.pricing-tiers{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin-bottom:40px}
.pricing-tier{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:20px;transition:border-color .2s}
.pricing-tier:hover{border-color:var(--tool-accent)}
.pt-name{font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:6px}
.pt-price{font-size:1.1rem;font-weight:800;margin-bottom:8px}
.pt-desc{font-size:.78rem;line-height:1.6;color:var(--muted);margin:0}

/* Client script */
.client-script-box{background:rgba(0,255,148,.04);border:1px solid rgba(0,255,148,.15);border-radius:12px;padding:24px;margin-bottom:40px}
.cs-label{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin-bottom:14px;display:flex;align-items:center;gap:8px}
.cs-text{font-size:.8rem;line-height:1.8;color:var(--muted);white-space:pre-wrap;font-family:inherit;margin:0}

/* Extended money streams */
.money-stream.new-stream{border-color:rgba(0,255,148,.2);background:rgba(0,255,148,.03)}
.money-stream.new-stream .stream-name::after{content:' +';color:var(--accent);font-size:.65rem;font-weight:700}

/* Advanced steps */
.advanced-step .step-title{color:var(--tool-accent)}
.adv-badge{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;background:rgba(var(--tool-accent-rgb),.12);color:var(--tool-accent);padding:2px 7px;border-radius:20px;margin-left:8px;vertical-align:middle}

/* New prompt badge */
.new-badge{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;background:rgba(0,255,148,.15);color:var(--accent);padding:2px 7px;border-radius:20px;margin-left:8px}

/* Section sub-label */
.section-label-sub{font-size:.8rem;color:var(--dim);margin-bottom:20px;margin-top:-8px}
"""

# ── Build ──────────────────────────────────────────────────────────────────
def build():
    parts = [HEAD, '<style>', CSS, '\n', ALL_TOOL_CSS, '\n', EXTRA_CSS, '\n</style>\n</head>\n<body>']
    parts.append(render_sidebar())
    parts.append('<div id="main">')
    parts.append(TOPBAR)
    parts.append(render_landing())

    ok = 0
    for t in ALL_TOOLS:
        tid = t[0]
        c = ALL_CONTENT.get(tid)
        ext = ALL_EXT.get(tid)
        if not c:
            print(f"  SKIP: no base content for {tid}")
            continue
        if not ext:
            print(f"  SKIP: no extension for {tid}")
            continue
        parts.append(render_ext_tool_page(t, c, ext))
        print(f"  ✓ {t[1]}. {t[2]}")
        ok += 1

    parts.append('</div>')
    parts.append(JS)
    parts.append('</body>\n</html>')

    html = '\n'.join(parts)
    out = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(out, 'w') as f:
        f.write(html)

    kb = len(html) // 1024
    print(f"\n✅ PLAYBOOK AI v3 — {ok} tools | {len(html):,} chars ({kb}KB)")
    return html

if __name__ == '__main__':
    build()
