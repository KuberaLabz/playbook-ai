#!/usr/bin/env python3
"""PLAYBOOK AI — Final HTML Assembler"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build import HEAD, CSS, TOOL_CSS_OVERRIDES, TOOLS_DATA
from content import CONTENT

# ── Helpers ────────────────────────────────────────────────────────────
def esc(s): return s.replace("'", "&#39;").replace('"', '&quot;')
def tool_style(accent):
    r,g,b = int(accent[1:3],16),int(accent[3:5],16),int(accent[5:7],16)
    return f"style='--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)'"

# ── Landing Page ────────────────────────────────────────────────────────
def render_landing():
    # Build tool cards
    cards = ''
    for t in TOOLS_DATA:
        tid,num,name,cat,catshort,accent,income,skill,ttd,price,tagline = t
        cards += f"""
        <div class="tool-card" {tool_style(accent)} onclick="goToTool('{tid}')" title="{esc(name)}">
          <div class="tool-card-num">{num}</div>
          <div class="tool-card-name">{name}</div>
          <div class="tool-card-cat" style="color:{accent}">{cat}</div>
          <div class="tool-card-income" style="background:rgba({int(accent[1:3],16)},{int(accent[3:5],16)},{int(accent[5:7],16)},0.1);color:{accent}">{income}</div>
          <div class="tool-card-tagline">{tagline}</div>
        </div>"""

    # Category rows
    cats_order = ['Builders','Creators','Voice','Intelligence','Automation','Research']
    cat_map = {}
    for t in TOOLS_DATA:
        cat_map.setdefault(t[3],[]).append(t)

    cat_html = ''
    cat_descs = {
        'Builders':     'Build real products',
        'Creators':     'Generate visual content',
        'Voice':        'Voice & avatar tools',
        'Intelligence': 'LLMs & reasoning',
        'Automation':   'Workflow automation',
        'Research':     'Research & analysis',
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

  <!-- HERO -->
  <section class="hero">
    <div class="hero-grid-bg"></div>
    <div class="hero-glow"></div>
    <div class="hero-badge"><div class="hero-badge-dot"></div>20 Tools · 6 Categories · Real Income Strategies</div>
    <h1 class="hero-title">
      <span class="line1">PLAYBOOK</span><br>
      <span class="line2">AI</span>
    </h1>
    <p class="hero-sub">The definitive guide to 20 AI tools that generate real income. Not theory. Not hype. Step-by-step playbooks with commands, prompts, and money maps for builders, creators, writers, and operators.</p>
    <div class="hero-ctas">
      <button class="btn-primary" onclick="goToTool('base44')">
        <i class="ph-fill ph-rocket-launch"></i> Start With Tool 01
      </button>
      <button class="btn-ghost-hero" onclick="document.getElementById('tools-grid-section').scrollIntoView({{behavior:'smooth'}})">
        <i class="ph ph-grid-four"></i> Browse All Tools
      </button>
    </div>
  </section>

  <!-- STATS -->
  <div class="stats-band">
    <div class="stat-block"><div class="stat-num">20<span>+</span></div><div class="stat-label">AI Tools Covered</div></div>
    <div class="stat-block"><div class="stat-num">6<span></span></div><div class="stat-label">Income Categories</div></div>
    <div class="stat-block"><div class="stat-num">$0<span></span></div><div class="stat-label">Cost to Access</div></div>
    <div class="stat-block"><div class="stat-num">∞</div><div class="stat-label">Earning Potential</div></div>
  </div>

  <!-- HOW IT WORKS -->
  <section class="how-section">
    <div class="section-eyebrow">How It Works</div>
    <h2 class="section-title">Pick a tool. Follow the playbook. Get paid.</h2>
    <div class="how-grid">
      <div class="how-block">
        <div class="how-num">01</div>
        <div class="how-title">Choose Your Tool</div>
        <p class="how-text">Each of the 20 tools has its own dedicated playbook. Start with the one that matches your current skills and interests — or follow the recommended sequence.</p>
      </div>
      <div class="how-block">
        <div class="how-num">02</div>
        <div class="how-title">Follow the Playbook</div>
        <p class="how-text">Every playbook includes a full setup guide, real terminal commands, copy-paste prompts, a money map with income ranges, and a curated tool stack.</p>
      </div>
      <div class="how-block">
        <div class="how-num">03</div>
        <div class="how-title">Execute the Money Map</div>
        <p class="how-text">Each tool includes 4 specific income streams with realistic revenue ranges and time-to-first-dollar estimates. No vague advice — specific paths to income.</p>
      </div>
    </div>
  </section>

  <!-- TOOLS GRID -->
  <section id="tools-grid-section" class="landing-grid-section">
    <div class="section-eyebrow">The Full Arsenal</div>
    <h2 class="section-title">20 tools. Zero fluff.</h2>
    <p class="section-sub">Every tool is chosen because it has a clear, proven path to income. Sorted by category.</p>
    <div class="tools-grid">{cards}</div>
  </section>

  <!-- CATEGORY OVERVIEW -->
  <section class="cats-section">
    <div class="section-eyebrow">By Category</div>
    <h2 class="section-title">Every income category covered.</h2>
    <p class="section-sub" style="margin-bottom:40px">From building SaaS products to running faceless content channels — your income path is in here.</p>
    {cat_html}
  </section>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-logo">PLAYBOOK<span>AI</span></div>
    <div class="footer-note">Free forever. Built for people who execute, not spectate.</div>
    <div class="footer-note" style="color:var(--dim)">© 2025 Playbook AI</div>
  </footer>

</div>"""

# ── Tool Page ────────────────────────────────────────────────────────────
def render_terminal(steps):
    if not steps: return ''
    lines = ''
    for cmd, comment in steps:
        if cmd.startswith('#') or (cmd.strip().startswith('//') and not cmd.strip().startswith('///')):
            lines += f'<div class="term-line"><span class="term-comment">{cmd}</span></div>'
        elif cmd.startswith('---'):
            lines += f'<div class="term-line" style="margin-top:8px"><span class="term-out dim">{cmd[3:]}</span></div>'
        elif cmd.startswith('>>'):
            lines += f'<div class="term-line"><span class="term-out">{cmd[2:]}</span></div>'
        else:
            comment_html = f'<span class="term-comment" style="margin-left:auto;padding-left:20px"># {comment}</span>' if comment else ''
            lines += f'<div class="term-line"><span class="term-prompt">$</span><span class="term-cmd">{cmd}</span>{comment_html}</div>'
    return f'''<div class="terminal">
      <div class="terminal-bar">
        <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
        <span class="term-title">Terminal</span>
      </div>
      <div class="terminal-body">{lines}</div>
    </div>'''

def render_tool_page(t, c):
    tid,num,name,cat,catshort,accent,income,skill,ttd,price,tagline = t
    r,g,b = int(accent[1:3],16),int(accent[3:5],16),int(accent[5:7],16)

    # Money streams
    streams_html = '<div class="money-map">'
    for sname, srange, sdesc, stime in c['money_streams']:
        streams_html += f'''<div class="money-stream">
          <div class="stream-name">{sname}</div>
          <div class="stream-range">{srange}</div>
          <div class="stream-desc">{sdesc}</div>
          <div class="stream-time"><i class="ph ph-clock"></i>{stime}</div>
        </div>'''
    streams_html += '</div>'

    # Steps
    steps_html = '<div class="steps-list">'
    for i, step in enumerate(c['steps']):
        step_title, step_desc, step_cmd = step
        term = ''
        if step_cmd:
            cmd_lines = step_cmd.strip().split('\n')
            term_steps = []
            for ln in cmd_lines:
                ln = ln.rstrip()
                if not ln: continue
                if ln.startswith('#'):
                    term_steps.append((ln, ''))
                elif ln.startswith('>>'):
                    term_steps.append((ln, ''))
                else:
                    term_steps.append((ln, ''))
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

    # Terminal (separate CLI steps for tools that have them)
    cli_html = ''
    if c.get('terminal_steps'):
        cli_html = render_terminal([(cmd, cmt) for cmd, cmt, *_ in c['terminal_steps']])

    # Prompts
    prompts_html = ''
    for plabel, ptext in c.get('prompts', []):
        ptext_escaped = ptext.replace('<','&lt;').replace('>','&gt;')
        prompts_html += f'''<div class="prompt-block">
          <div class="prompt-label"><i class="ph ph-copy"></i>{plabel}</div>
          <pre class="prompt-text">{ptext_escaped}</pre>
        </div>'''

    # Stack
    stack_html = '<div class="stack-items">'
    for item in c.get('stack', []):
        name_part = item.split('(')[0].strip()
        desc_part = item.split('(')[1].rstrip(')') if '(' in item else ''
        stack_html += f'<div class="stack-chip"><i class="ph ph-plugs-connected"></i><span><strong>{name_part}</strong>{" — "+desc_part if desc_part else ""}</span></div>'
    stack_html += '</div>'

    # Insights
    insights_html = ''
    for icon, ititle, itext in c.get('insights', []):
        insights_html += f'''<div class="insight-card">
          <i class="ph-fill ph-{icon}"></i>
          <div><div class="insight-title">{ititle}</div><div class="insight-text">{itext}</div></div>
        </div>'''

    # Skill meters
    skill_map = {'Beginner': 30, 'Intermediate': 65, 'Advanced': 90}
    skill_pct = skill_map.get(skill.split()[0], 50)

    # Facts
    facts_html = '<div class="quick-facts">'
    for k, v in c.get('facts', {}).items():
        color_class = 'green' if any(x in v for x in ['Free','Beginner']) else ''
        facts_html += f'<div class="fact-row"><span class="fact-key">{k}</span><span class="fact-val {color_class}">{v}</span></div>'
    facts_html += '</div>'

    # Warnings
    warn_html = ''
    for w in c.get('warnings', []):
        warn_html += f'<div class="warning-box"><i class="ph ph-warning"></i><p class="warning-text">{w}</p></div>'

    # Tips
    tip_html = ''
    for tip in c.get('tips', []):
        tip_html += f'<div class="tip-box"><i class="ph ph-lightbulb"></i><p class="tip-text">{tip}</p></div>'

    # Income badge
    income_badge = f'<div class="income-badge"><i class="ph ph-currency-dollar"></i><span>{income} estimated monthly income</span></div>'

    return f'''
<div id="tool-{tid}" class="page tool-page" data-tool="{tid}" style="--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)">

  <!-- TOOL HERO -->
  <div class="tool-hero">
    <div class="tool-hero-top">
      <div class="tool-hero-left">
        <div class="tool-number">{num} / 20 — {cat}</div>
        <h1 class="tool-name">{name}</h1>
        <div class="tool-category-badge"><i class="ph ph-tag"></i>{catshort}</div>
        <p class="tool-tagline">{tagline}</p>
      </div>
    </div>
    <div class="tool-meta-grid">
      <div class="tool-meta-cell">
        <div class="tool-meta-label">Monthly Income</div>
        <div class="tool-meta-value income">{income}</div>
        <div class="tool-meta-sub">Estimated range</div>
      </div>
      <div class="tool-meta-cell">
        <div class="tool-meta-label">Skill Level</div>
        <div class="tool-meta-value">{skill}</div>
        <div class="tool-meta-sub">To get started</div>
      </div>
      <div class="tool-meta-cell">
        <div class="tool-meta-label">Time to First Dollar</div>
        <div class="tool-meta-value">{ttd}</div>
        <div class="tool-meta-sub">If you start today</div>
      </div>
      <div class="tool-meta-cell">
        <div class="tool-meta-label">Pricing</div>
        <div class="tool-meta-value">{price}</div>
        <div class="tool-meta-sub">Entry cost</div>
      </div>
    </div>
  </div>

  <!-- MAIN CONTENT + SIDEBAR -->
  <div class="tool-content">
    <div class="tool-main">

      <!-- WHAT IT IS -->
      <div class="section-h">
        <i class="ph-fill ph-info"></i>
        <h2>What It Is</h2>
      </div>
      <p style="font-size:.95rem;line-height:1.9;color:var(--muted);margin-bottom:48px">{c['what_it_is']}</p>

      <!-- MONEY MAP -->
      <div class="section-h">
        <i class="ph-fill ph-currency-dollar"></i>
        <h2>The Money Map</h2>
      </div>
      {income_badge}
      {streams_html}

      <div class="section-divider"></div>

      <!-- SETUP GUIDE -->
      <div class="section-h">
        <i class="ph-fill ph-steps"></i>
        <h2>Setup Guide</h2>
      </div>
      {steps_html}

      {f'<div class="section-h" style="margin-top:40px"><i class="ph-fill ph-terminal-window"></i><h2>CLI Quick Reference</h2></div>{cli_html}' if cli_html else ''}

      <div class="section-divider"></div>

      <!-- PROMPTS -->
      <div class="section-h">
        <i class="ph-fill ph-chat-teardrop-text"></i>
        <h2>Copy-Paste Prompts</h2>
      </div>
      <p style="font-size:.82rem;color:var(--dim);margin-bottom:20px">Use these directly. Modify the bracketed sections for your specific context.</p>
      {prompts_html}

      <div class="section-divider"></div>

      <!-- INSIGHTS -->
      <div class="section-h">
        <i class="ph-fill ph-brain"></i>
        <h2>Operator Insights</h2>
      </div>
      {insights_html}

      <div class="section-divider"></div>

      <!-- STACK -->
      <div class="section-h">
        <i class="ph-fill ph-stack"></i>
        <h2>The Stack</h2>
      </div>
      <p style="font-size:.82rem;color:var(--dim);margin-bottom:20px">Tools that pair with {name} to unlock more income streams.</p>
      {stack_html}

    </div>

    <!-- SIDEBAR PANEL -->
    <div class="tool-sidebar-panel">
      <div class="panel-title">Quick Facts</div>
      {facts_html}

      <div class="section-divider" style="margin:20px 0"></div>

      <div class="panel-title">Skill Level</div>
      <div class="skill-meter">
        <div class="skill-meter-label">
          <span class="skill-name">Entry Barrier</span>
          <span class="skill-val">{skill}</span>
        </div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{skill_pct}%"></div></div>
      </div>
      <div class="skill-meter">
        <div class="skill-meter-label">
          <span class="skill-name">Income Potential</span>
          <span class="skill-val">High</span>
        </div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:85%"></div></div>
      </div>
      <div class="skill-meter" style="margin-bottom:28px">
        <div class="skill-meter-label">
          <span class="skill-name">Speed to Revenue</span>
          <span class="skill-val">{ttd}</span>
        </div>
        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{max(15, 90 - skill_pct)}%"></div></div>
      </div>

      <div class="section-divider" style="margin:0 0 20px"></div>

      <div class="panel-title">Watch Out For</div>
      {warn_html}

      <div class="panel-title" style="margin-top:20px">Pro Tips</div>
      {tip_html}
    </div>
  </div>

  <!-- NEXT TOOL NAV -->
  <div id="next-nav-{tid}" class="site-footer" style="justify-content:space-between">
    <div class="footer-logo">PLAYBOOK<span style="color:var(--accent)">AI</span></div>
    <div style="display:flex;gap:12px;align-items:center">
      <button class="btn-ghost-hero" onclick="showPage('landing')" style="padding:10px 20px;font-size:.75rem">
        <i class="ph ph-house"></i> Home
      </button>
    </div>
  </div>

</div>'''

# ── Sidebar HTML ─────────────────────────────────────────────────────────
def render_sidebar():
    cats_order = ['Builders','Creators','Voice','Intelligence','Automation','Research']
    cat_icons = {
        'Builders':     'hammer',
        'Creators':     'palette',
        'Voice':        'microphone',
        'Intelligence': 'brain',
        'Automation':   'gear-six',
        'Research':     'magnifying-glass',
    }
    cat_map = {}
    for t in TOOLS_DATA:
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
            tid,num,name,_,_,accent,income,*_ = t
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

# ── JavaScript ───────────────────────────────────────────────────────────
JS = """
<script>
const pages = document.querySelectorAll('.page');
const navItems = document.querySelectorAll('.nav-item[data-page]');

function showPage(id) {
  pages.forEach(p => p.classList.remove('active'));
  navItems.forEach(n => n.classList.remove('active'));
  const page = document.getElementById(id);
  if (page) {
    page.classList.add('active');
    window.scrollTo(0,0);
  }
  const nav = document.getElementById('nav-' + id.replace('tool-',''));
  if (nav) nav.classList.add('active');

  // Update topbar breadcrumb
  const name = page ? (page.querySelector('.tool-name')?.textContent || 'Overview') : 'Overview';
  document.getElementById('breadcrumb-current').textContent = name;
  const catEl = page ? page.querySelector('.tool-category-badge') : null;
  const catText = catEl ? catEl.textContent.replace(/[^a-zA-Z ]/g,'').trim() : '';
  document.getElementById('breadcrumb-cat').textContent = catText ? catText + ' /' : '';

  // Close sidebar on mobile
  if (window.innerWidth < 1100) {
    document.body.classList.remove('sidebar-open');
  }
}

function goToTool(tid) { showPage('tool-' + tid); }

function toggleSidebar() {
  if (window.innerWidth >= 1100) {
    document.body.classList.toggle('sidebar-closed');
  } else {
    document.body.classList.toggle('sidebar-open');
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  // Animate skill bars on page
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('.skill-bar-fill').forEach(bar => {
          const w = bar.style.width;
          bar.style.width = '0';
          setTimeout(() => { bar.style.width = w; }, 100);
        });
      }
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.tool-sidebar-panel').forEach(el => observer.observe(el));

  // Active nav on load
  document.getElementById('nav-landing').classList.add('active');
});
</script>
"""

# ── Topbar ───────────────────────────────────────────────────────────────
TOPBAR = """<div id="topbar">
  <button id="sidebar-toggle" onclick="toggleSidebar()" title="Toggle sidebar">
    <i class="ph ph-list"></i>
  </button>
  <div class="topbar-breadcrumb">
    <span>Playbook AI</span>
    <span class="sep">/</span>
    <span id="breadcrumb-cat"></span>
    <span id="breadcrumb-current">Overview</span>
  </div>
  <div class="topbar-pill">Free Edition</div>
</div>"""

# ── ASSEMBLE ─────────────────────────────────────────────────────────────
def build():
    parts = [HEAD, '<style>', CSS, '\n', TOOL_CSS_OVERRIDES, '\n</style>\n</head>\n<body>']
    parts.append(render_sidebar())
    parts.append('<div id="main">')
    parts.append(TOPBAR)
    parts.append(render_landing())
    for t in TOOLS_DATA:
        tid = t[0]
        c = CONTENT.get(tid)
        if not c:
            print(f"  WARNING: no content for {tid}")
            continue
        parts.append(render_tool_page(t, c))
        print(f"  ✓ Rendered: {t[2]}")
    parts.append('</div>')  # end #main
    parts.append(JS)
    parts.append('</body>\n</html>')

    html = '\n'.join(parts)
    out_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(out_path, 'w') as f:
        f.write(html)
    print(f"\n✅ PLAYBOOK AI — Built: {len(html):,} chars | {html.count(chr(10)):,} lines")
    print(f"   Saved to: {out_path}")
    return html

if __name__ == '__main__':
    build()
