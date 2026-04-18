
# ══════════════════════════════════════════════════════════════
# PLAYBOOK AI — Build Script
# Generates the full index.html from component parts
# ══════════════════════════════════════════════════════════════

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Playbook AI — Master Every AI Tool. Make Real Money.</title>
<meta name="description" content="The definitive guide to 20 AI tools that generate real income. Step-by-step playbooks for builders, creators, writers, and operators."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1/src/index.js"></script>
<style>
'''

CSS = '''
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  background:#080808;
  color:#E8E4DE;
  font-family:'Inter',system-ui,sans-serif;
  font-weight:400;
  line-height:1.7;
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}
:root{
  --bg:   #080808;
  --bg2:  #0D0D0D;
  --bg3:  #111111;
  --bg4:  #161616;
  --bg5:  #1C1C1C;
  --cream:#E8E4DE;
  --muted:#888;
  --dim:  #555;
  --border:rgba(255,255,255,0.06);
  --border2:rgba(255,255,255,0.1);
  --accent:#00FF94;
  --accent-dim:rgba(0,255,148,0.08);
  --accent-mid:rgba(0,255,148,0.15);
  --display:'Syne',system-ui,sans-serif;
  --mono:'JetBrains Mono','Fira Code',monospace;
  --ease:cubic-bezier(0.16,1,0.3,1);
  --sidebar-w:280px;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:3px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:#333}

/* ── TYPOGRAPHY ── */
h1,h2,h3,h4,h5{font-family:var(--display);font-weight:700;line-height:1.1;letter-spacing:-0.02em;color:var(--cream)}
p{color:var(--muted);line-height:1.85}
strong{color:var(--cream);font-weight:600}
em{font-style:italic}
a{color:inherit;text-decoration:none}
ul,ol{list-style:none}

/* ── CODE ── */
code{
  font-family:var(--mono);font-size:.82em;
  background:rgba(255,255,255,.05);
  color:var(--accent);
  padding:2px 8px;border-radius:3px;
  border:1px solid rgba(255,255,255,.08);
}

/* ── SIDEBAR ── */
#sidebar{
  position:fixed;top:0;left:0;height:100vh;
  width:var(--sidebar-w);
  background:var(--bg2);
  border-right:1px solid var(--border);
  overflow-y:auto;
  overflow-x:hidden;
  padding:0 0 40px;
  z-index:300;
  transition:transform .35s var(--ease);
  scrollbar-width:thin;
  scrollbar-color:#222 transparent;
}
#sidebar::-webkit-scrollbar{width:2px}
#sidebar::-webkit-scrollbar-thumb{background:#222}
.sidebar-closed #sidebar{transform:translateX(calc(-1 * var(--sidebar-w)))}

.sidebar-header{
  padding:28px 24px 22px;
  border-bottom:1px solid var(--border);
  position:sticky;top:0;
  background:var(--bg2);
  z-index:2;
}
.sidebar-logo{
  display:flex;align-items:center;gap:10px;
}
.logo-mark{
  width:32px;height:32px;
  background:var(--accent);
  border-radius:6px;
  display:flex;align-items:center;justify-content:center;
  flex-shrink:0;
}
.logo-mark i{font-size:17px;color:#080808}
.logo-text{font-family:var(--display);font-size:1.1rem;font-weight:800;color:var(--cream);letter-spacing:-.02em}
.logo-text span{color:var(--accent)}

.sidebar-section-label{
  padding:20px 24px 8px;
  font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--dim);font-weight:600;
}
.nav-item{
  display:flex;align-items:center;gap:10px;
  padding:9px 24px;
  cursor:pointer;
  border-left:2px solid transparent;
  transition:all .2s;
  position:relative;
}
.nav-item:hover{
  background:rgba(255,255,255,.03);
  color:var(--cream);
}
.nav-item.active{
  border-left-color:var(--tool-accent,var(--accent));
  background:rgba(255,255,255,.03);
}
.nav-item.active .nav-label{color:var(--tool-accent,var(--accent))}
.nav-num{
  font-family:var(--mono);font-size:.65rem;
  color:var(--dim);min-width:22px;
}
.nav-label{font-size:.82rem;color:var(--muted);transition:color .2s}
.nav-item:hover .nav-label{color:var(--cream)}
.nav-item.cat-header{
  padding:18px 24px 6px;cursor:default;
  border-left:none;background:none;
}
.nav-item.cat-header:hover{background:none}
.nav-cat-label{
  font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--dim);font-weight:700;
}
.nav-dot{
  width:6px;height:6px;border-radius:50%;
  background:var(--tool-accent,var(--dim));
  flex-shrink:0;opacity:.5;
  transition:opacity .2s;
}
.nav-item.active .nav-dot,.nav-item:hover .nav-dot{opacity:1}

/* ── MAIN ── */
#main{
  margin-left:var(--sidebar-w);
  min-height:100vh;
  transition:margin .35s var(--ease);
}
.sidebar-closed #main{margin-left:0}

/* ── TOPBAR ── */
#topbar{
  position:fixed;top:0;
  left:var(--sidebar-w);right:0;
  height:56px;
  background:rgba(8,8,8,.9);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;
  padding:0 40px;
  z-index:200;
  transition:left .35s var(--ease);
  gap:16px;
}
.sidebar-closed #topbar{left:0}
#sidebar-toggle{
  background:none;border:none;cursor:pointer;
  padding:6px;color:var(--muted);
  display:flex;align-items:center;
  transition:color .2s;
}
#sidebar-toggle:hover{color:var(--cream)}
#sidebar-toggle i{font-size:20px}
.topbar-breadcrumb{
  font-size:.78rem;color:var(--dim);
  display:flex;align-items:center;gap:8px;
  margin-left:4px;
}
.topbar-breadcrumb span{color:var(--muted)}
.topbar-breadcrumb .sep{color:var(--dim)}
.topbar-pill{
  margin-left:auto;
  background:var(--accent-dim);
  border:1px solid var(--accent-mid);
  color:var(--accent);
  font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;
  padding:4px 12px;border-radius:20px;
  font-family:var(--mono);
}

/* ── PAGE ── */
.page{display:none;padding-top:56px}
.page.active{display:block}

/* ══════════════════════════════════
   LANDING PAGE
══════════════════════════════════ */
#landing{background:var(--bg)}

/* HERO */
.hero{
  min-height:100vh;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  text-align:center;
  padding:120px 40px 80px;
  position:relative;
  overflow:hidden;
}
.hero-grid-bg{
  position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(0,255,148,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,148,.03) 1px, transparent 1px);
  background-size:60px 60px;
  mask-image:radial-gradient(ellipse at center, black 30%, transparent 80%);
}
.hero-glow{
  position:absolute;
  top:30%;left:50%;transform:translate(-50%,-50%);
  width:600px;height:400px;
  background:radial-gradient(ellipse, rgba(0,255,148,.06) 0%, transparent 70%);
  pointer-events:none;
}
.hero-badge{
  display:inline-flex;align-items:center;gap:8px;
  background:var(--bg3);
  border:1px solid var(--border2);
  border-radius:20px;
  padding:6px 16px;
  font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);
  margin-bottom:36px;
}
.hero-badge-dot{
  width:6px;height:6px;border-radius:50%;
  background:var(--accent);
  box-shadow:0 0 8px var(--accent);
}
.hero-title{
  font-family:var(--display);
  font-size:clamp(52px,9vw,120px);
  font-weight:800;
  line-height:.92;
  letter-spacing:-.04em;
  color:var(--cream);
  margin-bottom:28px;
}
.hero-title .line2{
  color:transparent;
  -webkit-text-stroke:1px rgba(232,228,222,.3);
}
.hero-title .accent{color:var(--accent)}
.hero-sub{
  max-width:540px;
  font-size:1.05rem;
  color:var(--muted);
  line-height:1.8;
  margin-bottom:52px;
}
.hero-ctas{
  display:flex;align-items:center;gap:16px;
  flex-wrap:wrap;justify-content:center;
}
.btn-primary{
  background:var(--accent);
  color:#080808;
  border:none;
  padding:14px 32px;
  font-family:var(--display);
  font-size:.85rem;font-weight:700;
  letter-spacing:.04em;text-transform:uppercase;
  cursor:pointer;
  border-radius:4px;
  transition:transform .2s var(--ease),box-shadow .2s;
  display:inline-flex;align-items:center;gap:8px;
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,255,148,.25)}
.btn-primary i{font-size:17px}
.btn-ghost-hero{
  background:transparent;
  border:1px solid var(--border2);
  color:var(--cream);
  padding:14px 28px;
  font-family:var(--display);
  font-size:.85rem;font-weight:600;
  cursor:pointer;
  border-radius:4px;
  transition:border-color .2s,background .2s;
  display:inline-flex;align-items:center;gap:8px;
}
.btn-ghost-hero:hover{border-color:rgba(255,255,255,.25);background:rgba(255,255,255,.04)}
.btn-ghost-hero i{font-size:17px;color:var(--muted)}

/* TOOL GRID ON LANDING */
.landing-grid-section{
  padding:80px 40px 120px;
  max-width:1200px;margin:0 auto;
}
.section-eyebrow{
  font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);
  margin-bottom:14px;
  display:flex;align-items:center;gap:10px;
}
.section-eyebrow::before{
  content:'';display:block;
  width:24px;height:1px;background:var(--accent);flex-shrink:0;
}
.section-title{
  font-family:var(--display);
  font-size:clamp(32px,4vw,52px);
  font-weight:800;
  color:var(--cream);
  margin-bottom:16px;
}
.section-sub{font-size:.95rem;color:var(--muted);max-width:520px;margin-bottom:52px}

.tools-grid{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(200px,1fr));
  gap:2px;
  background:var(--border);
  border:1px solid var(--border);
}
.tool-card{
  background:var(--bg2);
  padding:28px 24px;
  cursor:pointer;
  transition:background .25s;
  position:relative;
  overflow:hidden;
}
.tool-card::before{
  content:'';
  position:absolute;
  top:0;left:0;right:0;height:2px;
  background:var(--tool-accent,var(--accent));
  transform:scaleX(0);
  transform-origin:left;
  transition:transform .35s var(--ease);
}
.tool-card:hover{background:var(--bg3)}
.tool-card:hover::before{transform:scaleX(1)}
.tool-card-num{
  font-family:var(--mono);font-size:.62rem;
  color:var(--dim);
  margin-bottom:14px;
}
.tool-card-name{
  font-family:var(--display);font-size:1rem;font-weight:700;
  color:var(--cream);margin-bottom:6px;
  line-height:1.2;
}
.tool-card-cat{
  font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;
  margin-bottom:14px;
}
.tool-card-income{
  font-family:var(--mono);font-size:.72rem;
  padding:4px 10px;
  border-radius:3px;
  display:inline-block;
  margin-bottom:10px;
}
.tool-card-tagline{
  font-size:.78rem;color:var(--dim);line-height:1.5;
}

/* STATS BAND */
.stats-band{
  border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);
  display:grid;
  grid-template-columns:repeat(4,1fr);
}
.stat-block{
  padding:48px 40px;
  border-right:1px solid var(--border);
  text-align:center;
}
.stat-block:last-child{border-right:none}
.stat-num{
  font-family:var(--display);font-size:3rem;font-weight:800;
  color:var(--cream);line-height:1;
  margin-bottom:8px;
}
.stat-num span{color:var(--accent)}
.stat-label{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}

/* HOW IT WORKS */
.how-section{
  padding:100px 40px;
  max-width:1100px;margin:0 auto;
}
.how-grid{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:2px;
  background:var(--border);
  border:1px solid var(--border);
  margin-top:52px;
}
.how-block{
  background:var(--bg2);
  padding:40px 36px;
}
.how-num{
  font-family:var(--mono);
  font-size:2.5rem;
  color:rgba(255,255,255,.04);
  line-height:1;
  margin-bottom:20px;
  font-weight:700;
}
.how-title{
  font-family:var(--display);
  font-size:1.1rem;font-weight:700;
  color:var(--cream);margin-bottom:10px;
}
.how-text{font-size:.85rem;color:var(--muted);line-height:1.75}

/* CATEGORIES ON LANDING */
.cats-section{padding:0 40px 100px;max-width:1100px;margin:0 auto}
.cat-row{
  display:flex;align-items:stretch;
  gap:2px;
  margin-bottom:2px;
}
.cat-label-block{
  min-width:180px;
  background:var(--bg3);
  border:1px solid var(--border);
  padding:24px;
  display:flex;flex-direction:column;justify-content:center;
}
.cat-name{
  font-family:var(--display);font-size:.9rem;font-weight:700;
  color:var(--cream);margin-bottom:4px;
}
.cat-count{font-size:.7rem;color:var(--dim)}
.cat-tools-row{
  flex:1;display:flex;gap:2px;
  background:var(--border);
}
.cat-tool-chip{
  flex:1;background:var(--bg2);
  padding:18px 20px;
  cursor:pointer;
  transition:background .2s;
  display:flex;flex-direction:column;
  gap:4px;
}
.cat-tool-chip:hover{background:var(--bg4)}
.chip-name{
  font-family:var(--display);font-size:.82rem;font-weight:700;
  color:var(--cream);
}
.chip-income{
  font-family:var(--mono);font-size:.68rem;
}

/* ══════════════════════════════════
   TOOL PLAYBOOK PAGE
══════════════════════════════════ */
.tool-page{padding-top:56px}

.tool-hero{
  padding:72px 56px 64px;
  border-bottom:1px solid var(--border);
  position:relative;
  overflow:hidden;
}
.tool-hero::before{
  content:'';
  position:absolute;inset:0;
  background:radial-gradient(ellipse at 0% 50%, var(--tool-hero-glow,rgba(0,255,148,.04)) 0%, transparent 60%);
  pointer-events:none;
}
.tool-hero-top{
  display:flex;align-items:flex-start;
  justify-content:space-between;
  gap:40px;
  margin-bottom:40px;
}
.tool-hero-left{flex:1}
.tool-number{
  font-family:var(--mono);font-size:.68rem;letter-spacing:.15em;
  color:var(--dim);text-transform:uppercase;
  margin-bottom:16px;
  display:flex;align-items:center;gap:10px;
}
.tool-number::before{
  content:'';display:block;width:20px;height:1px;
  background:var(--tool-accent,var(--accent));
}
.tool-name{
  font-family:var(--display);
  font-size:clamp(42px,6vw,80px);
  font-weight:800;
  color:var(--cream);
  line-height:.9;
  letter-spacing:-.03em;
  margin-bottom:20px;
}
.tool-category-badge{
  display:inline-flex;align-items:center;gap:6px;
  border:1px solid var(--tool-accent,var(--accent));
  color:var(--tool-accent,var(--accent));
  font-size:.63rem;letter-spacing:.15em;text-transform:uppercase;
  padding:5px 14px;border-radius:2px;
  margin-bottom:24px;
}
.tool-tagline{
  font-size:1.1rem;color:var(--muted);
  line-height:1.7;max-width:580px;
}
.tool-meta-grid{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:1px;
  background:var(--border);
  border:1px solid var(--border);
}
.tool-meta-cell{
  background:var(--bg3);
  padding:20px 24px;
}
.tool-meta-label{
  font-size:.6rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--dim);margin-bottom:6px;
}
.tool-meta-value{
  font-family:var(--display);font-size:1.1rem;font-weight:700;
  color:var(--cream);
}
.tool-meta-value.income{color:var(--accent)}
.tool-meta-sub{font-size:.7rem;color:var(--dim);margin-top:2px}

/* TOOL SECTIONS */
.tool-content{
  display:grid;
  grid-template-columns:1fr 340px;
  gap:0;
  max-width:1300px;
}
.tool-main{
  padding:56px;
  border-right:1px solid var(--border);
}
.tool-sidebar-panel{
  padding:40px 32px;
  position:sticky;
  top:56px;
  height:calc(100vh - 56px);
  overflow-y:auto;
}

/* SECTION HEADERS */
.section-h{
  display:flex;align-items:center;gap:14px;
  margin-bottom:28px;
  padding-bottom:16px;
  border-bottom:1px solid var(--border);
}
.section-h i{
  font-size:20px;
  color:var(--tool-accent,var(--accent));
}
.section-h h2{
  font-family:var(--display);
  font-size:1.5rem;font-weight:800;
  color:var(--cream);
}

/* MONEY MAP */
.money-map{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:2px;
  background:var(--border);
  border:1px solid var(--border);
  margin-bottom:48px;
}
.money-stream{
  background:var(--bg3);
  padding:24px;
  position:relative;
  overflow:hidden;
  transition:background .25s;
}
.money-stream:hover{background:var(--bg4)}
.money-stream::before{
  content:'';
  position:absolute;left:0;top:0;bottom:0;
  width:3px;
  background:var(--tool-accent,var(--accent));
}
.stream-name{
  font-family:var(--display);font-size:.95rem;font-weight:700;
  color:var(--cream);margin-bottom:6px;
}
.stream-range{
  font-family:var(--mono);font-size:.82rem;
  color:var(--accent);
  margin-bottom:8px;
}
.stream-desc{font-size:.78rem;color:var(--dim);line-height:1.6}
.stream-time{
  font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--dim);margin-top:10px;
  display:flex;align-items:center;gap:6px;
}
.stream-time i{font-size:12px}

/* STEPS */
.steps-list{
  display:flex;flex-direction:column;
  gap:2px;margin-bottom:48px;
}
.step-block{
  display:flex;gap:20px;
  background:var(--bg3);
  padding:24px 28px;
  border:1px solid var(--border);
  border-top:none;
  transition:border-color .2s,background .2s;
}
.step-block:first-child{border-top:1px solid var(--border)}
.step-block:hover{background:var(--bg4);border-color:var(--border2)}
.step-num{
  font-family:var(--mono);font-size:1.6rem;font-weight:700;
  color:rgba(255,255,255,.05);
  flex-shrink:0;line-height:1;
  width:36px;
  transition:color .2s;
}
.step-block:hover .step-num{color:var(--tool-accent,var(--accent))}
.step-title{
  font-family:var(--display);font-size:1rem;font-weight:700;
  color:var(--cream);margin-bottom:8px;
}
.step-desc{font-size:.82rem;color:var(--muted);line-height:1.75;margin-bottom:12px}

/* TERMINAL */
.terminal{
  background:#0D1117;
  border:1px solid rgba(255,255,255,.08);
  border-radius:6px;
  overflow:hidden;
  margin:16px 0;
  font-family:var(--mono);
}
.terminal-bar{
  background:#161B22;
  padding:10px 16px;
  display:flex;align-items:center;gap:8px;
  border-bottom:1px solid rgba(255,255,255,.06);
}
.term-dot{width:10px;height:10px;border-radius:50%}
.term-dot.r{background:#FF5F56}
.term-dot.y{background:#FFBD2E}
.term-dot.g{background:#27C93F}
.term-title{font-size:.68rem;color:#4D5566;margin-left:8px;letter-spacing:.05em}
.terminal-body{
  padding:18px 20px;
  font-size:.8rem;
  line-height:1.8;
  overflow-x:auto;
}
.term-line{display:flex;gap:12px;align-items:flex-start}
.term-prompt{color:#4D5566;flex-shrink:0}
.term-cmd{color:#E6EDF3}
.term-comment{color:#4D5566;font-size:.75rem}
.term-out{color:#3FB950;padding-left:20px;font-size:.75rem}
.term-out.dim{color:#4D5566}
.term-out.warn{color:#F0883E}
.term-out.err{color:#FF7B72}

/* PROMPT BLOCKS */
.prompt-block{
  background:var(--bg3);
  border:1px solid var(--border);
  border-left:3px solid var(--tool-accent,var(--accent));
  padding:20px 24px;
  margin:12px 0;
  border-radius:0 4px 4px 0;
}
.prompt-label{
  font-size:.6rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--tool-accent,var(--accent));
  margin-bottom:10px;
  display:flex;align-items:center;gap:8px;
}
.prompt-label i{font-size:13px}
.prompt-text{
  font-family:var(--mono);font-size:.78rem;
  color:var(--cream);line-height:1.7;
  white-space:pre-wrap;
}

/* STACK */
.stack-items{
  display:flex;flex-wrap:wrap;gap:8px;
  margin-bottom:32px;
}
.stack-chip{
  display:flex;align-items:center;gap:8px;
  background:var(--bg3);
  border:1px solid var(--border2);
  padding:8px 16px;border-radius:3px;
  font-size:.78rem;color:var(--cream);
  transition:border-color .2s,background .2s;
}
.stack-chip:hover{border-color:var(--tool-accent,var(--accent));background:var(--bg4)}
.stack-chip i{font-size:14px;color:var(--tool-accent,var(--accent))}

/* INSIGHT CARDS */
.insight-card{
  background:var(--bg3);
  border:1px solid var(--border);
  padding:24px;
  margin-bottom:12px;
  display:flex;gap:16px;
  transition:border-color .2s;
}
.insight-card:hover{border-color:var(--border2)}
.insight-card i{font-size:20px;color:var(--tool-accent,var(--accent));flex-shrink:0;margin-top:2px}
.insight-title{
  font-family:var(--display);font-size:.9rem;font-weight:700;
  color:var(--cream);margin-bottom:4px;
}
.insight-text{font-size:.8rem;color:var(--muted);line-height:1.7}

/* INCOME BADGE */
.income-badge{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(0,255,148,.08);
  border:1px solid rgba(0,255,148,.2);
  color:var(--accent);
  font-family:var(--mono);font-size:.78rem;
  padding:8px 16px;border-radius:3px;
  margin-bottom:32px;
}
.income-badge i{font-size:14px}

/* SKILL METER */
.skill-meter{
  background:var(--bg3);
  border:1px solid var(--border);
  padding:20px 24px;
  margin-bottom:12px;
}
.skill-meter-label{
  display:flex;justify-content:space-between;
  margin-bottom:10px;
}
.skill-name{font-size:.78rem;color:var(--cream)}
.skill-val{font-family:var(--mono);font-size:.72rem;color:var(--tool-accent,var(--accent))}
.skill-bar-track{
  height:3px;background:rgba(255,255,255,.06);
  border-radius:2px;
}
.skill-bar-fill{
  height:100%;border-radius:2px;
  background:var(--tool-accent,var(--accent));
  transition:width .8s var(--ease);
}

/* SIDEBAR PANEL */
.panel-title{
  font-family:var(--display);font-size:.8rem;font-weight:700;
  color:var(--cream);
  letter-spacing:.05em;text-transform:uppercase;
  margin-bottom:16px;
  padding-bottom:10px;
  border-bottom:1px solid var(--border);
}
.quick-facts{
  display:flex;flex-direction:column;gap:1px;
  background:var(--border);
  margin-bottom:28px;
}
.fact-row{
  display:flex;justify-content:space-between;align-items:center;
  background:var(--bg3);
  padding:12px 16px;
  gap:12px;
}
.fact-key{font-size:.72rem;color:var(--dim)}
.fact-val{font-size:.78rem;color:var(--cream);font-weight:500;text-align:right}
.fact-val.green{color:#22C55E}
.fact-val.amber{color:#F59E0B}
.fact-val.accent{color:var(--tool-accent,var(--accent))}

.warning-box{
  background:rgba(245,158,11,.06);
  border:1px solid rgba(245,158,11,.2);
  padding:16px 20px;border-radius:3px;
  margin-bottom:20px;
  display:flex;gap:12px;
}
.warning-box i{font-size:16px;color:#F59E0B;flex-shrink:0;margin-top:2px}
.warning-text{font-size:.78rem;color:#A89860;line-height:1.65}

.tip-box{
  background:rgba(0,255,148,.05);
  border:1px solid rgba(0,255,148,.15);
  padding:16px 20px;border-radius:3px;
  margin-bottom:20px;
  display:flex;gap:12px;
}
.tip-box i{font-size:16px;color:var(--accent);flex-shrink:0;margin-top:2px}
.tip-text{font-size:.78rem;color:#80AA90;line-height:1.65}

/* DIVIDER */
.section-divider{
  height:1px;background:var(--border);
  margin:48px 0;
}

/* FOOTER */
.site-footer{
  border-top:1px solid var(--border);
  padding:40px 56px;
  display:flex;align-items:center;justify-content:space-between;
  gap:20px;
}
.footer-logo{
  font-family:var(--display);font-size:1rem;font-weight:800;
  color:var(--cream);
}
.footer-logo span{color:var(--accent)}
.footer-note{font-size:.75rem;color:var(--dim)}

/* MOBILE */
@media(max-width:1100px){
  #sidebar{transform:translateX(calc(-1 * var(--sidebar-w)))}
  #main{margin-left:0}
  #topbar{left:0}
  .sidebar-open #sidebar{transform:translateX(0)}
  .sidebar-open #sidebar-overlay{display:block}
  #sidebar-overlay{
    display:none;
    position:fixed;inset:0;
    background:rgba(0,0,0,.7);
    z-index:299;
  }
}
@media(max-width:900px){
  .tool-content{grid-template-columns:1fr}
  .tool-sidebar-panel{position:static;height:auto;border-left:none;border-top:1px solid var(--border)}
  .tool-meta-grid{grid-template-columns:repeat(2,1fr)}
  .tool-hero{padding:40px 24px}
  .tool-main{padding:36px 24px}
  .hero{padding:100px 24px 60px}
  .landing-grid-section,.how-section,.cats-section{padding-left:24px;padding-right:24px}
  .stats-band{grid-template-columns:repeat(2,1fr)}
  .money-map{grid-template-columns:1fr}
  .how-grid{grid-template-columns:1fr}
}
@media(max-width:600px){
  .tools-grid{grid-template-columns:1fr 1fr}
  .hero-title{font-size:42px}
  .tool-name{font-size:40px}
  .site-footer{flex-direction:column;text-align:center;padding:32px 24px}
  #topbar{padding:0 20px}
}
'''

TOOLS_DATA = [
  # (id, num, name, category, cat_short, accent, income_range, skill_level, time_to_dollar, pricing, tagline)
  ('base44',     '01', 'Base44',       'Builders',    'BUILD', '#6C63FF', '$2K–$15K/mo', 'Beginner',      '1–3 days',  'Free → $49/mo', 'The no-code SaaS factory. Build real apps with your own AI agent.'),
  ('claudecode', '02', 'Claude Code',  'Builders',    'BUILD', '#CC785C', '$5K–$30K/mo', 'Intermediate',  '1–2 weeks', '$20/mo (Pro)',   'An AI that lives in your terminal and actually ships code end-to-end.'),
  ('cursor',     '03', 'Cursor',       'Builders',    'BUILD', '#00D4FF', '$8K–$40K/mo', 'Intermediate',  '1–2 weeks', '$20/mo',        'The IDE that makes senior engineers twice as fast and juniors dangerous.'),
  ('lovable',    '04', 'Lovable',      'Builders',    'BUILD', '#FF6B6B', '$1K–$10K/mo', 'Beginner',      '24 hours',  'Free → $25/mo', 'Describe your app in plain English. Ship it before lunch.'),
  ('windsurf',   '05', 'Windsurf',     'Builders',    'BUILD', '#00C896', '$5K–$25K/mo', 'Intermediate',  '1 week',    'Free → $15/mo', 'The agentic IDE that refactors entire codebases while you think.'),
  ('midjourney', '06', 'Midjourney',   'Creators',    'CREATE','#7B68EE', '$1K–$12K/mo', 'Beginner',      '48 hours',  '$10–$60/mo',    'Turn text into sellable art, brand kits, print products, and design assets.'),
  ('runway',     '07', 'Runway ML',    'Creators',    'CREATE','#FF4B6E', '$3K–$20K/mo', 'Beginner',      '1 week',    'Free → $35/mo', 'Hollywood-grade video AI. Build a content studio from a laptop.'),
  ('kling',      '08', 'Kling AI',     'Creators',    'CREATE','#FF8C42', '$2K–$15K/mo', 'Beginner',      '3–5 days',  'Free → $10/mo', 'The viral video engine. High-motion AI clips that stop thumbs cold.'),
  ('sora',       '09', 'Sora',         'Creators',    'CREATE','#10B981', '$2K–$18K/mo', 'Beginner',      '1 week',    '$20/mo (Plus)', 'OpenAI\'s cinematic video model. Long-form storytelling at scale.'),
  ('seedance',   '10', 'Seedance',     'Creators',    'CREATE','#F59E0B', '$1K–$10K/mo', 'Beginner',      '3 days',    'Free tier',     'ByteDance\'s secret weapon. Ultra-realistic motion for social content.'),
  ('elevenlabs', '11', 'ElevenLabs',   'Voice',       'VOICE', '#3B82F6', '$500–$8K/mo', 'Beginner',      '1–3 days',  'Free → $22/mo', 'Clone voices, earn royalties, build audio products that run 24/7.'),
  ('heygen',     '12', 'HeyGen',       'Voice',       'VOICE', '#8B5CF6', '$2K–$25K/mo', 'Beginner',      '1 week',    'Free → $29/mo', 'Your face, your voice, your AI double — making content while you sleep.'),
  ('chatgpt',    '13', 'ChatGPT',      'Intelligence','LLM',   '#10B981', '$2K–$20K/mo', 'Beginner',      '24 hours',  'Free → $20/mo', 'The world\'s default AI. Still the fastest path from zero to first client.'),
  ('claude',     '14', 'Claude',       'Intelligence','LLM',   '#CC785C', '$3K–$25K/mo', 'Beginner',      '48 hours',  'Free → $20/mo', 'The best writer in any room. Built for long-form, analysis, and nuance.'),
  ('perplexity', '15', 'Perplexity',   'Intelligence','LLM',   '#6366F1', '$1K–$10K/mo', 'Beginner',      '3 days',    'Free → $20/mo', 'The research engine. Sell deep reports, SEO packs, and competitive intel.'),
  ('gemini',     '16', 'Gemini',       'Intelligence','LLM',   '#4285F4', '$2K–$15K/mo', 'Beginner',      '3 days',    'Free → $20/mo', 'Google\'s AI. 1M token context. Deepest Google Workspace integration alive.'),
  ('make',       '17', 'Make',         'Automation',  'AUTO',  '#6B21A8', '$2K–$12K/mo', 'Intermediate',  '2 weeks',   'Free → $16/mo', 'Build automation systems for clients and charge $500–$2K/mo retainers.'),
  ('n8n',        '18', 'n8n',          'Automation',  'AUTO',  '#FF6B35', '$3K–$20K/mo', 'Intermediate',  '2–3 weeks', 'Free (self-host)','Self-hosted automation goldmine. Developer clients pay premium for this.'),
  ('zapier',     '19', 'Zapier',       'Automation',  'AUTO',  '#FF4A00', '$1K–$8K/mo',  'Beginner',      '1 week',    'Free → $29/mo', 'The gateway drug to automation revenue. Non-technical clients love it.'),
  ('notebooklm', '20', 'NotebookLM',   'Research',    'RSRCH', '#1DB954', '$500–$6K/mo', 'Beginner',      '3 days',    'Free',          'Google\'s research AI. Turn any document into a podcast, brief, or product.'),
]

def accent_var(accent):
    return f"--tool-accent:{accent}; --tool-hero-glow:rgba({int(accent[1:3],16)},{int(accent[3:5],16)},{int(accent[5:7],16)},0.06)"

def tool_css_class(tool_id, accent):
    r,g,b = int(accent[1:3],16), int(accent[3:5],16), int(accent[5:7],16)
    return f"[data-tool='{tool_id}']{{--tool-accent:{accent};--tool-hero-glow:rgba({r},{g},{b},0.05)}}"

TOOL_CSS_OVERRIDES = '\n'.join(tool_css_class(t[0], t[5]) for t in TOOLS_DATA)

print("plan computed, writing CSS done")
print(f"Total tools: {len(TOOLS_DATA)}")
