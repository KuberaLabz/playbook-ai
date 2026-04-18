#!/usr/bin/env python3
"""PLAYBOOK AI v2 — Full Assembler with 28 tools"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build import HEAD, CSS, TOOLS_DATA
from content import CONTENT
from content_v2 import CONTENT_V2

# Merge content
ALL_CONTENT = {**CONTENT, **CONTENT_V2}

# ── New tools to add ────────────────────────────────────────────────────
NEW_TOOLS = [
  # Research additions
  ('consensus',    '21', 'Consensus',         'Research',   'RSRCH', '#06B6D4', '$1K–$8K/mo',  'Beginner',      '1 week',    'Free → $11/mo',    'The AI search engine for peer-reviewed science. Sell credible, sourced research products.'),
  ('elicit',       '22', 'Elicit',            'Research',   'RSRCH', '#8B5CF6', '$1K–$8K/mo',  'Beginner',      '1 week',    'Free → $12/mo',    'Automated literature review AI. Run systematic research reviews in hours, not weeks.'),
  ('tavily',       '23', 'Tavily',            'Research',   'RSRCH', '#F97316', '$3K–$15K/mo', 'Intermediate',  '2 weeks',   'Free → $35/mo',    'The search API built for AI agents. Powers real-time intelligence in any agent system.'),
  # AI Agents category
  ('superagent',   '24', 'Base44 Superagent', 'AI Agents',  'AGENT', '#00FF94', '$500–$5K/mo', 'Beginner',      '1–2 weeks', 'Free → $49/mo',    'Personal AI agents that remember, act, and run 24/7. Build, deploy, and sell agent products.'),
  ('openaiagents', '25', 'OpenAI Agents SDK', 'AI Agents',  'AGENT', '#10B981', '$15K–$80K/project','Intermediate','3–4 weeks','API usage-based',  'The official framework for production multi-agent systems. Enterprise-grade AI consulting.'),
  ('nemoclaw',     '26', 'NemoClaw',          'AI Agents',  'AGENT', '#EF4444', '$3K–$25K/mo', 'Advanced',      '3–6 weeks', 'NVIDIA NIM pricing','NVIDIA-backed security agent. AI security audits, guardrails, and compliance deployments.'),
  ('dify',         '27', 'Dify',              'AI Agents',  'AGENT', '#6366F1', '$1K–$10K/mo', 'Intermediate',  '2 weeks',   'Free (self-host)',  'Open-source LLM app builder. Ship AI SaaS products with RAG, tools, and one-click APIs.'),
  ('crewai',       '28', 'CrewAI',            'AI Agents',  'AGENT', '#F59E0B', '$5K–$25K/project','Intermediate','3–4 weeks','Open-source',      'Multi-agent orchestration framework. Build specialist agent crews that work while you sleep.'),
]

ALL_TOOLS = TOOLS_DATA + NEW_TOOLS

# ── Generate per-tool CSS overrides ─────────────────────────────────────
def tool_css_class(tool_id, accent):
    r,g,b = int(accent[1:3],16), int(accent[3:5],16), int(accent[5:7],16)
    return f"[data-tool='{tool_id}']{{--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)}}"

ALL_TOOL_CSS = '\n'.join(tool_css_class(t[0], t[5]) for t in ALL_TOOLS)

# ── Helpers ─────────────────────────────────────────────────────────────
def esc(s): return s.replace("'", "&#39;").replace('"', '&quot;')
def tool_style(accent):
    r,g,b = int(accent[1:3],16),int(accent[3:5],16),int(accent[5:7],16)
    return f"style='--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)'"

def render_terminal(steps):
    if not steps: return ''
    lines = ''
    for item in steps:
        cmd = item[0]; comment = item[1] if len(item) > 1 else ''
        if cmd.startswith('#'):
            lines += f'<div class="term-line"><span class="term-comment">{cmd}</span></div>'
        elif cmd.startswith('>>'):
            lines += f'<div class="term-line"><span class="term-out">{cmd[2:]}</span></div>'
        else:
            cmt_html = f'<span class="term-comment" style="margin-left:auto;padding-left:20px"># {comment}</span>' if comment else ''
            lines += f'<div class="term-line"><span class="term-prompt">$</span><span class="term-cmd">{cmd}</span>{cmt_html}</div>'
    return f'''<div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Terminal</span>
      </div>
      <div class="terminal-body">{lines}</div>
    </div>'''

# ── Landing Page ─────────────────────────────────────────────────────────
def render_landing():
    cards = ''
    for t in ALL_TOOLS:
        tid,num,name,cat,catshort,accent,income,skill,ttd,price,tagline = t
        cards += f"""
        <div class="tool-card" {tool_style(accent)} onclick="goToTool('{tid}')">
          <div class="tool-card-num">{num}</div>
          <div class="tool-card-name">{name}</div>
          <div class="tool-card-cat" style="color:{accent}">{cat}</div>
          <div class="tool-card-income" style="background:rgba({int(accent[1:3],16)},{int(accent[3:5],16)},{int(accent[5:7],16)},0.1);color:{accent}">{income}</div>
          <div class="tool-card-tagline">{tagline}</div>
        </div>"""

    cats_order = ['Builders','Creators','Voice','Intelligence','Automation','Research','AI Agents']
    cat_map = {}
    for t in ALL_TOOLS:
        cat_map.setdefault(t[3],[]).append(t)

    cat_html = ''
    cat_descs = {
        'Builders':     'Build real products',
        'Creators':     'Generate visual content',
        'Voice':        'Voice & avatar tools',
        'Intelligence': 'LLMs & reasoning',
        'Automation':   'Workflow automation',
        'Research':     'Deep research tools',
        'AI Agents':    'Deploy autonomous agents',
    }
    for cat in cats_order:
        tools = cat_map.get(cat, [])
        if not tools: continue
        chips = ''
        for t in tools:
            tid,num,name,_,catshort,accent,income,*_ = t
            chips += f"""<div class="cat-tool-chip" onclick="goToTool('{tid}')">
              <div class="chip-name">{name}</div>
              <div class="chip-income" style="color:{accent}">{income}</div>
            </div>"""
        cat_html += f"""<div class="cat-row">
          <div class="cat-label-block">
            <div class="cat-name">{cat}</div>
            <div class="cat-count">{len(tools)} tools · {cat_descs.get(cat,'')}</div>
          </div>
          <div class="cat-tools-row">{chips}</div>
        </div>"""

    return f"""
<div id="landing" class="page active">
  <section class="hero">
    <div class="hero-grid-bg"></div>
    <div class="hero-glow"></div>
    <div class="hero-badge"><div class="hero-badge-dot"></div>28 Tools · 7 Categories · Real Income Strategies</div>
    <h1 class="hero-title">
      <span class="line1">PLAYBOOK</span><br>
      <span class="line2">AI</span>
    </h1>
    <p class="hero-sub">The definitive guide to 28 AI tools that generate real income. Not theory. Not hype. Step-by-step playbooks with commands, prompts, and money maps for builders, creators, writers, operators, and agents.</p>
    <div class="hero-ctas">
      <button class="btn-primary" onclick="goToTool('base44')">
        <i class="ph-fill ph-rocket-launch"></i> Start With Tool 01
      </button>
      <button class="btn-ghost-hero" onclick="document.getElementById('tools-grid-section').scrollIntoView({{behavior:'smooth'}})">
        <i class="ph ph-grid-four"></i> Browse All Tools
      </button>
    </div>
  </section>

  <div class="stats-band">
    <div class="stat-block"><div class="stat-num">28<span>+</span></div><div class="stat-label">AI Tools Covered</div></div>
    <div class="stat-block"><div class="stat-num">7<span></span></div><div class="stat-label">Income Categories</div></div>
    <div class="stat-block"><div class="stat-num">$0<span></span></div><div class="stat-label">Cost to Access</div></div>
    <div class="stat-block"><div class="stat-num">&#8734;</div><div class="stat-label">Earning Potential</div></div>
  </div>

  <section class="how-section">
    <div class="section-eyebrow">How It Works</div>
    <h2 class="section-title">Pick a tool. Follow the playbook. Get paid.</h2>
    <div class="how-grid">
      <div class="how-block">
        <div class="how-num">01</div>
        <div class="how-title">Choose Your Tool</div>
        <p class="how-text">Each of the 28 tools has its own dedicated playbook. Start with the one that matches your current skills — or follow the recommended sequence from Builders to Agents.</p>
      </div>
      <div class="how-block">
        <div class="how-num">02</div>
        <div class="how-title">Follow the Playbook</div>
        <p class="how-text">Every playbook includes a full setup guide with real terminal commands, copy-paste prompts, a money map with income ranges, and a curated tool stack.</p>
      </div>
      <div class="how-block">
        <div class="how-num">03</div>
        <div class="how-title">Execute the Money Map</div>
        <p class="how-text">Each tool has 4 specific income streams with realistic revenue ranges and time-to-first-dollar estimates. Specific paths — not vague advice.</p>
      </div>
    </div>
  </section>

  <section id="tools-grid-section" class="landing-grid-section">
    <div class="section-eyebrow">The Full Arsenal</div>
    <h2 class="section-title">28 tools. Zero fluff.</h2>
    <p class="section-sub">Every tool chosen because it has a clear, proven path to income. Sorted by category.</p>
    <div class="tools-grid">{cards}</div>
  </section>

  <section class="cats-section">
    <div class="section-eyebrow">By Category</div>
    <h2 class="section-title">Every income category covered.</h2>
    <p class="section-sub" style="margin-bottom:40px">From building SaaS products to deploying autonomous AI agent systems — your path is in here.</p>
    {cat_html}
  </section>

  <footer class="site-footer">
    <div class="footer-logo">PLAYBOOK<span>AI</span></div>
    <div class="footer-note">Free forever. Built for people who execute, not spectate.</div>
    <div class="footer-note" style="color:var(--dim)">&#169; 2025 Playbook AI</div>
  </footer>
</div>"""

# ── Tool Page ─────────────────────────────────────────────────────────────
def render_tool_page(t, c):
    tid,num,name,cat,catshort,accent,income,skill,ttd,price,tagline = t
    r,g,b = int(accent[1:3],16),int(accent[3:5],16),int(accent[5:7],16)

    streams_html = '<div class="money-map">'
    for sname, srange, sdesc, stime in c['money_streams']:
        streams_html += f'''<div class="money-stream">
          <div class="stream-name">{sname}</div>
          <div class="stream-range">{srange}</div>
          <div class="stream-desc">{sdesc}</div>
          <div class="stream-time"><i class="ph ph-clock"></i>{stime}</div>
        </div>'''
    streams_html += '</div>'

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
    steps_html += '</div>'

    cli_html = ''
    if c.get('terminal_steps'):
        cli_html = render_terminal([(cmd, cmt) for cmd, cmt, *_ in c['terminal_steps']])

    prompts_html = ''
    for plabel, ptext in c.get('prompts', []):
        ptext_e = ptext.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        prompts_html += f'''<div class="prompt-block">
          <div class="prompt-label"><i class="ph ph-copy"></i>{plabel}</div>
          <pre class="prompt-text">{ptext_e}</pre>
        </div>'''

    stack_html = '<div class="stack-items">'
    for item in c.get('stack', []):
        n = item.split('(')[0].strip()
        d = item.split('(')[1].rstrip(')') if '(' in item else ''
        stack_html += f'<div class="stack-chip"><i class="ph ph-plugs-connected"></i><span><strong>{n}</strong>{" — "+d if d else ""}</span></div>'
    stack_html += '</div>'

    insights_html = ''
    for icon, ititle, itext in c.get('insights', []):
        insights_html += f'''<div class="insight-card">
          <i class="ph-fill ph-{icon}"></i>
          <div><div class="insight-title">{ititle}</div><div class="insight-text">{itext}</div></div>
        </div>'''

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
      <p style="font-size:.95rem;line-height:1.9;color:var(--muted);margin-bottom:48px">{c['what_it_is']}</p>

      <div class="section-h"><i class="ph-fill ph-currency-dollar"></i><h2>The Money Map</h2></div>
      {income_badge}
      {streams_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-steps"></i><h2>Setup Guide</h2></div>
      {steps_html}
      {f'<div class="section-h" style="margin-top:40px"><i class="ph-fill ph-terminal-window"></i><h2>CLI Quick Reference</h2></div>{cli_html}' if cli_html else ''}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-chat-teardrop-text"></i><h2>Copy-Paste Prompts</h2></div>
      <p style="font-size:.82rem;color:var(--dim);margin-bottom:20px">Use these directly. Modify the bracketed sections for your specific context.</p>
      {prompts_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-brain"></i><h2>Operator Insights</h2></div>
      {insights_html}
      <div class="section-divider"></div>

      <div class="section-h"><i class="ph-fill ph-stack"></i><h2>The Stack</h2></div>
      <p style="font-size:.82rem;color:var(--dim);margin-bottom:20px">Tools that pair with {name} to unlock more income streams.</p>
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

# ── Sidebar ───────────────────────────────────────────────────────────────
def render_sidebar():
    cats_order = ['Builders','Creators','Voice','Intelligence','Automation','Research','AI Agents']
    cat_icons  = {
        'Builders':    'hammer',
        'Creators':    'palette',
        'Voice':       'microphone',
        'Intelligence':'brain',
        'Automation':  'gear-six',
        'Research':    'magnifying-glass',
        'AI Agents':   'robot',
    }
    cat_map = {}
    for t in ALL_TOOLS:
        cat_map.setdefault(t[3],[]).append(t)

    nav = ''
    for cat in cats_order:
        tools = cat_map.get(cat, [])
        if not tools: continue
        icon = cat_icons.get(cat, 'circle')
        nav += f'''<div class="nav-item cat-header">
          <i class="ph ph-{icon}" style="font-size:13px;color:var(--dim);flex-shrink:0"></i>
          <span class="nav-cat-label">{cat}</span>
        </div>'''
        for t in tools:
            tid,num,name,_,_,accent,*_ = t
            nav += f'''<div class="nav-item" id="nav-{tid}" data-page="tool-{tid}" onclick="goToTool('{tid}')" style="--tool-accent:{accent}">
              <span class="nav-num">{num}</span>
              <div class="nav-dot" style="background:{accent}"></div>
              <span class="nav-label">{name}</span>
            </div>'''
    return f'''<div id="sidebar">
  <div class="sidebar-header">
    <div class="sidebar-logo">
      <div class="logo-mark"><i class="ph-fill ph-lightning"></i></div>
      <div class="logo-text">PLAYBOOK<span>AI</span></div>
    </div>
  </div>
  <div class="nav-item" id="nav-landing" data-page="landing" onclick="showPage('landing')" style="margin-top:8px">
    <i class="ph ph-house" style="font-size:14px;color:var(--muted);flex-shrink:0;width:22px"></i>
    <span class="nav-label">Overview</span>
  </div>
  <div style="height:1px;background:var(--border);margin:8px 0"></div>
  {nav}
</div>
<div id="sidebar-overlay" onclick="toggleSidebar()"></div>'''

# ── JS ─────────────────────────────────────────────────────────────────────
JS = """<script>
const pages = document.querySelectorAll('.page');
const navItems = document.querySelectorAll('.nav-item[data-page]');

function showPage(id) {
  pages.forEach(p => p.classList.remove('active'));
  navItems.forEach(n => n.classList.remove('active'));
  const page = document.getElementById(id);
  if (page) { page.classList.add('active'); window.scrollTo(0,0); }
  const navId = id === 'landing' ? 'nav-landing' : 'nav-' + id.replace('tool-','');
  const nav = document.getElementById(navId);
  if (nav) nav.classList.add('active');
  const name = (id === 'landing') ? 'Overview' : (page?.querySelector('.tool-name')?.textContent || '');
  document.getElementById('breadcrumb-current').textContent = name;
  const catEl = page?.querySelector('.tool-category-badge');
  document.getElementById('breadcrumb-cat').textContent = catEl ? catEl.textContent.replace(/[^a-zA-Z ]/g,'').trim() + ' /' : '';
  if (window.innerWidth < 1100) document.body.classList.remove('sidebar-open');
}

function goToTool(tid) { showPage('tool-' + tid); }
function toggleSidebar() {
  if (window.innerWidth >= 1100) document.body.classList.toggle('sidebar-closed');
  else document.body.classList.toggle('sidebar-open');
}

document.addEventListener('DOMContentLoaded', () => {
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('.skill-bar-fill').forEach(b => {
          const w = b.style.width; b.style.width='0';
          setTimeout(()=>{ b.style.width=w; }, 100);
        });
      }
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.tool-sidebar-panel').forEach(el => obs.observe(el));
  document.getElementById('nav-landing').classList.add('active');
});
</script>"""

TOPBAR = """<div id="topbar">
  <button id="sidebar-toggle" onclick="toggleSidebar()"><i class="ph ph-list"></i></button>
  <div class="topbar-breadcrumb">
    <span>Playbook AI</span><span class="sep">/</span>
    <span id="breadcrumb-cat"></span>
    <span id="breadcrumb-current">Overview</span>
  </div>
  <div class="topbar-pill">Free Edition</div>
</div>"""

# ── ASSEMBLE ──────────────────────────────────────────────────────────────
def build():
    parts = [HEAD, '<style>', CSS, '\n', ALL_TOOL_CSS, '\n</style>\n</head>\n<body>']
    parts.append(render_sidebar())
    parts.append('<div id="main">')
    parts.append(TOPBAR)
    parts.append(render_landing())

    for t in ALL_TOOLS:
        tid = t[0]
        c = ALL_CONTENT.get(tid)
        if not c:
            print(f"  WARNING: no content for {tid}")
            continue
        parts.append(render_tool_page(t, c))
        print(f"  ✓ {t[1]}. {t[2]} ({t[3]})")

    parts.append('</div>')
    parts.append(JS)
    parts.append('</body>\n</html>')

    html = '\n'.join(parts)
    out = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(out, 'w') as f:
        f.write(html)
    print(f"\n✅ PLAYBOOK AI v2 — {len(ALL_TOOLS)} tools | {len(html):,} chars | {html.count(chr(10)):,} lines")
    return html

if __name__ == '__main__':
    build()
