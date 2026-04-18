# ══════════════════════════════════════════════════════════════
# PLAYBOOK AI — Tool Content (Deep copy for all 20 tools)
# ══════════════════════════════════════════════════════════════

# Each tool: dict with keys:
#   what_it_is, money_streams[], steps[], prompts[], stack[], insights[], facts{}, warnings[], tips[]

CONTENT = {}

# ─────────────────────────────────────────────
# 01. BASE44
# ─────────────────────────────────────────────
CONTENT['base44'] = {
  'what_it_is': "Base44 is a full-stack AI app builder that gives you a complete cloud backend — database, auth, file storage, automations, and a personal AI agent — out of the box. You describe what you want, and your agent builds it live. No DevOps. No boilerplate. No waiting for a developer.",
  'money_streams': [
    ("Build SaaS for Clients", "$3K–$15K per project", "Build custom internal tools, dashboards, and client portals for businesses. One week of work, professional invoice.", "14–30 days to first paid project"),
    ("Launch Your Own SaaS", "$500–$5K MRR", "Ship a niche SaaS product — job boards, CRM tools, booking systems — and charge monthly subscriptions.", "30–90 days to first subscriber"),
    ("Whop Community Tools", "$500–$3K/mo", "Build custom community dashboards and member portals for Whop creators. Recurring retainer model.", "7–14 days to deploy"),
    ("Rapid MVP Agency", "$2K–$8K per MVP", "Sell 'MVP in a Week' packages to founders and startups. They pay for speed. You deliver with Base44.", "1 week per client"),
  ],
  'steps': [
    ("Create Your Agent", "Go to app.base44.com, sign up, and create your first Superagent. Give it a name and personality. This is your builder.", ""),
    ("Define Your App", "Type your app idea in plain English. Be specific: 'A client CRM with a dashboard showing MRR, active clients, and invoice tracking.'", ""),
    ("Let It Build", "Watch your agent scaffold the full app — entities, pages, logic. It builds in real time. You review and steer.", ""),
    ("Add Integrations", "Connect Gmail, Slack, Stripe, Airtable, or any of the 30+ OAuth connectors. Your agent handles the auth flow.", ""),
    ("Deploy & Share", "Your app is live instantly on a Base44 URL. White-label with a custom domain. Share with clients or users immediately.", ""),
  ],
  'terminal': None,
  'prompts': [
    ("Client CRM Prompt", "Build me a CRM for a freelance agency. It needs: a Clients entity with name, email, project status, MRR, and last contact date. A Projects entity linked to clients with deadline, budget, and status. A dashboard page showing total MRR, active projects, overdue items. Row-level security so each client only sees their own data."),
    ("SaaS MVP Prompt", "Build a job board SaaS. Employers can post jobs (title, description, salary range, location, remote). Job seekers can apply with name, email, resume link. Admin dashboard shows all jobs and applications. Add email notification automation when a new application arrives."),
    ("Whop Tool Prompt", "Build a community analytics dashboard for a Whop creator. Pull in member data, show engagement scores, flag members who haven't posted in 14+ days. Generate a weekly owner brief with top performers and churn risks."),
  ],
  'stack': ["Stripe (payments)", "Gmail (notifications)", "Vercel (custom domain)", "Whop (community)", "Airtable (data sync)", "Slack (alerts)"],
  'insights': [
    ("lightning", "Speed Is Your Product", "Most clients don't care about the tech stack. They care that it works next week. Base44 makes that possible without a team."),
    ("currency-dollar", "Retainer Angle", "After building a client's tool, offer a $200–$500/mo retainer to 'maintain and improve' it. They almost always say yes."),
    ("storefront", "Niche + Niche + Niche", "The most profitable Base44 apps serve one specific industry with one specific problem. 'CRM for tattoo studios' beats 'general CRM' every time."),
  ],
  'facts': {"Pricing": "Free → $49/mo", "Context Window": "Full app memory", "Skill Level": "Beginner", "Deploy Time": "< 1 hour", "Time to Revenue": "1–3 days"},
  'warnings': ["Don't overbuild. Ship the MVP first, then add features based on real user feedback — not assumptions."],
  'tips': ["Use the agent's memory to store client preferences, recurring tasks, and project context so every session picks up where you left off."],
}

# ─────────────────────────────────────────────
# 02. CLAUDE CODE
# ─────────────────────────────────────────────
CONTENT['claudecode'] = {
  'what_it_is': "Claude Code is Anthropic's agentic coding tool that runs directly in your terminal. It doesn't just suggest code — it reads your entire codebase, writes files, runs commands, debugs errors, and ships features autonomously. It's the closest thing to having a senior engineer on call 24/7.",
  'money_streams': [
    ("Freelance Dev Agency", "$5K–$20K/mo", "Take on 3–5 client projects simultaneously. Claude Code does the heavy lifting — you QA, communicate, and invoice.", "2–4 weeks to first client"),
    ("Legacy Code Modernisation", "$8K–$40K per project", "Companies pay premium to modernise old codebases. Claude Code handles the refactor — you handle the contract.", "1 project = 1–3 weeks"),
    ("Open Source SaaS", "$2K–$15K MRR", "Build and ship a developer tool or SaaS product. Claude Code handles the full stack from Next.js to PostgreSQL.", "60–90 days to launch"),
    ("Bug Bounty & Audits", "$500–$5K per audit", "Use Claude Code to audit code for security issues, performance bottlenecks, and technical debt. Sell the report.", "Per engagement"),
  ],
  'steps': [
    ("Install Node & npm", "Make sure you have Node.js 18+ installed. Check with node --version.", "node --version\nnpm --version"),
    ("Install Claude Code", "Install globally via npm. You'll need an Anthropic API key from console.anthropic.com.", "npm install -g @anthropic-ai/claude-code"),
    ("Set Your API Key", "Export your key to your shell environment — add to .bashrc or .zshrc for persistence.", "export ANTHROPIC_API_KEY=sk-ant-your-key-here\necho 'export ANTHROPIC_API_KEY=sk-ant-...' >> ~/.zshrc"),
    ("Navigate to Your Project", "cd into any existing project or create a new directory. Claude Code reads your full file tree.", "mkdir my-saas && cd my-saas\nclaude"),
    ("Give It Context", "Type your first instruction. Be specific. The more context you give, the better the output.", "# Inside Claude Code:\n> Build a REST API with Express.js and PostgreSQL for a task management app with user auth"),
  ],
  'prompts': [
    ("Full SaaS Build", "I need a full-stack SaaS application. Tech stack: Next.js 14 (App Router), PostgreSQL, Prisma ORM, NextAuth.js for auth. Build: user registration/login, a dashboard with usage stats, a billing page integrated with Stripe (subscription plans: Free/$0, Pro/$29/mo, Agency/$99/mo), and an API with rate limiting per plan tier. Use TypeScript throughout. Set up the folder structure, all schema files, and seed data."),
    ("Codebase Audit Prompt", "Audit this entire codebase and produce a detailed technical report. Identify: 1) Security vulnerabilities (injection risks, exposed secrets, missing auth checks), 2) Performance bottlenecks (N+1 queries, missing indexes, heavy computations on main thread), 3) Code quality issues (dead code, duplicated logic, missing error handling), 4) Dependency vulnerabilities. Output a prioritised list with severity ratings and recommended fixes."),
    ("Legacy Modernisation", "This codebase is built in Python 2.7 with raw SQL queries and no tests. Modernise it: upgrade to Python 3.11, replace raw SQL with SQLAlchemy ORM, add pytest unit tests for all business logic functions, add type hints throughout, and set up a GitHub Actions CI pipeline. Maintain all existing functionality. Work file by file and confirm before each major change."),
  ],
  'terminal_steps': [
    ("Install", "npm install -g @anthropic-ai/claude-code", ""),
    ("API Key", "export ANTHROPIC_API_KEY=sk-ant-api03-...", ""),
    ("Launch", "cd your-project && claude", "Starts interactive session"),
    ("One-shot", 'claude -p "Add input validation to all API routes"', "Non-interactive mode"),
    ("With files", 'claude -p "Review this file" --file src/api/auth.ts', ""),
    ("Slash commands", "/clear — new context\n/model — switch model\n/compact — compress history", ""),
  ],
  'stack': ["Cursor (IDE layer)", "GitHub (version control)", "Vercel (deploy)", "Supabase (database)", "Stripe (billing)", "Railway (hosting)"],
  'insights': [
    ("git-branch", "Commit Often", "Run git commit after every meaningful Claude Code session. It can make sweeping changes — you want checkpoints."),
    ("file-text", "CLAUDE.md Is Gold", "Create a CLAUDE.md in your project root with architecture decisions, coding conventions, and business rules. Claude reads it on every session."),
    ("rocket", "The Compounding Edge", "As Claude builds your project, it learns your patterns. Session 10 is 3x faster than session 1. Stick with one project."),
  ],
  'facts': {"Pricing": "$20/mo (Pro) or API", "Model": "Claude Sonnet / Opus", "Skill Level": "Intermediate", "Context Window": "200K tokens", "Time to Revenue": "1–2 weeks"},
  'warnings': ["Always review diffs before committing. Claude Code can confidently write wrong code when given ambiguous instructions."],
  'tips': ["Put a CLAUDE.md file in your project root. Document your stack, conventions, and business rules. Claude reads it automatically every session."],
}

# ─────────────────────────────────────────────
# 03. CURSOR
# ─────────────────────────────────────────────
CONTENT['cursor'] = {
  'what_it_is': "Cursor is an AI-native code editor — a fork of VS Code that integrates Claude and GPT-4 directly into your workflow. Cmd+K edits code inline. Cmd+L chats with your codebase. Tab autocompletes entire functions. It doesn't replace your skills — it multiplies them by 3–5x.",
  'money_streams': [
    ("Senior Dev Freelancing", "$8K–$40K/mo", "Take on senior-level contracts at $100–$200/hr. Cursor closes the gap between your current skills and senior output.", "2–4 weeks to land clients"),
    ("SaaS Product Development", "$5K–$30K MRR", "Build production SaaS faster than anyone on your team. Ship features in hours that used to take days.", "60 days to launch"),
    ("Agency Overflow Work", "$3K–$15K/mo", "Partner with agencies as overflow dev. They have too much work — you have Cursor. White-label your services.", "1–2 weeks setup"),
    ("Technical Co-Founder for Hire", "$10K–$50K equity + salary", "Founders need builders. With Cursor you can build an entire MVP solo in 2–4 weeks. Negotiate equity + cash.", "Project-based"),
  ],
  'steps': [
    ("Download & Install", "Get Cursor at cursor.com. It installs like VS Code — takes 2 minutes. Import your VS Code settings instantly.", "# Download from cursor.com\n# Or via command line (macOS):\nbrew install --cask cursor"),
    ("Connect AI Models", "Go to Cursor Settings → Models. Add Claude Sonnet (best for code), GPT-4o (fastest), or your own API key for lower costs.", ""),
    ("Open Your Project", "Open any folder. Cursor indexes your entire codebase immediately — every file, every function is searchable by AI.", "cursor /path/to/your/project"),
    ("Master the 3 Core Shortcuts", "Cmd+K: Edit code inline. Cmd+L: Chat with your codebase. Tab: Accept AI autocomplete. These 3 = 80% of the value.", ""),
    ("Set Up Rules for AI", "Create a .cursorrules file in your project root. Define coding style, patterns, and constraints. Cursor follows them on every generation.", '# .cursorrules example:\n"Always use TypeScript. Prefer functional components.\nUse Tailwind for styling. Add JSDoc comments.\nNever use any type."'),
  ],
  'prompts': [
    ("Codebase Chat", "@codebase How does authentication work in this project? List all the files involved and explain the flow from login form to JWT issuance."),
    ("Inline Edit (Cmd+K)", "Refactor this function to handle edge cases: empty input, null values, and arrays longer than 1000 items. Add TypeScript types. Maintain the same return signature."),
    (".cursorrules Template", "You are an expert TypeScript/React developer. Rules: 1) Always use strict TypeScript — no 'any' types. 2) Use React Query for all data fetching. 3) All components must be under 150 lines — split if larger. 4) Use Zod for all form validation. 5) Write JSDoc for all exported functions. 6) Prefer early returns over nested conditionals."),
  ],
  'terminal_steps': [
    ("Install (macOS)", "brew install --cask cursor", "Or download from cursor.com"),
    ("Open project", "cursor .", "From any directory"),
    ("Key: inline edit", "Cmd+K (Mac) / Ctrl+K (Win)", "Edit selected code with AI"),
    ("Key: chat", "Cmd+L (Mac) / Ctrl+L (Win)", "Chat with your codebase"),
    ("Key: composer", "Cmd+I (Mac) / Ctrl+I (Win)", "Multi-file AI editing"),
    ("Key: tab complete", "Tab", "Accept AI suggestion"),
  ],
  'stack': ["Claude Code (terminal agent)", "GitHub Copilot (comparison)", "Vercel (deploy)", "Supabase (backend)", "Tailwind (styling)", "Stripe (billing)"],
  'insights': [
    ("target", "Composer Is the Power Move", "Cursor Composer (Cmd+I) lets AI edit multiple files at once. Use it for feature additions, refactors, and migrations."),
    ("files", ".cursorrules = Your Style Guide", "A well-written .cursorrules file makes every AI generation match your codebase's patterns perfectly. Invest 30 minutes once, save hours every week."),
    ("chart-line-up", "The 10x Myth Is Real", "Developers with Cursor consistently ship 3–5x faster than those without. At freelance rates, that's 3–5x more revenue per hour."),
  ],
  'facts': {"Pricing": "$20/mo Pro", "Model Options": "Claude, GPT-4o, Gemini", "Skill Level": "Intermediate", "IDE Base": "VS Code fork", "Time to Revenue": "1–2 weeks"},
  'warnings': ["Don't blindly accept Cursor's suggestions for security-sensitive code like auth, payments, and database queries. Always review those manually."],
  'tips': ["Use @codebase in chat to reference your entire project. Ask it 'where is X implemented' before building — prevents duplicating logic."],
}

# ─────────────────────────────────────────────
# 04. LOVABLE
# ─────────────────────────────────────────────
CONTENT['lovable'] = {
  'what_it_is': "Lovable (formerly GPT Engineer) turns plain English descriptions into fully deployed React applications. You describe the UI, the logic, the pages — and Lovable generates the full codebase and deploys it live. Non-technical founders use it to validate ideas before hiring a developer.",
  'money_streams': [
    ("Startup MVP Service", "$2K–$8K per project", "Build and deploy working MVPs for non-technical founders in 24–48 hours. They pay for speed and working code.", "1 week to first client"),
    ("Landing Page Agency", "$500–$2K per site", "Build high-converting landing pages in hours. Stack 10–15 clients per month.", "3–5 days to first delivery"),
    ("Prototype-to-Pitch Decks", "$1K–$5K per project", "Founders need working prototypes for investor demos. Lovable builds them fast.", "24–48 hours per project"),
    ("SaaS Side Projects", "$500–$5K MRR", "Launch niche SaaS products with zero coding. Validate with real users before investing in a full build.", "1–2 weeks"),
  ],
  'steps': [
    ("Sign Up & Start", "Go to lovable.dev. Sign up with GitHub. Your first project is free — start immediately, no setup required.", ""),
    ("Describe Your App", "Type what you want built. Be as specific as possible: 'A React dashboard for freelancers with a project tracker, time logger, and invoice generator. Use a dark theme with purple accents.'", ""),
    ("Iterate in Chat", "Lovable shows a live preview. Click 'Edit' to chat with it directly. Type changes like a conversation: 'Make the sidebar collapsible. Add a dark mode toggle. Change the button colour to #6C63FF.'", ""),
    ("Connect Supabase", "Click the Supabase integration button. Lovable auto-generates tables, auth, and API calls. Your app gets a real backend in minutes.", ""),
    ("Deploy to Custom Domain", "Hit Deploy. Your app is live on a Lovable URL instantly. Connect a custom domain via the settings panel.", ""),
  ],
  'prompts': [
    ("Full App Prompt", "Build a SaaS dashboard for social media managers. Features: 1) A content calendar with drag-and-drop scheduling. 2) Analytics page showing follower growth, top posts, engagement rate (use mock data). 3) Client workspace with separate views per client. 4) A simple onboarding flow with a 3-step wizard. Dark theme, modern design, sidebar navigation. Use Tailwind and shadcn/ui components."),
    ("Landing Page Prompt", "Build a high-converting landing page for an AI writing tool called 'Scribe'. Include: hero section with a bold headline and email capture form, features section (3 features with icons), social proof section with 3 testimonials, pricing section (Free / Pro $19/mo / Team $49/mo), and a final CTA. Modern, clean design with a green accent colour."),
    ("Iteration Prompt", "The current design looks too generic. Make it more premium: 1) Replace all rounded corners with sharp edges. 2) Add subtle grid background to the hero. 3) Make the typography larger and bolder. 4) Add a subtle glow effect to the primary CTA button. 5) Replace the stock icons with Phosphor icons."),
  ],
  'stack': ["Supabase (backend)", "Stripe (payments)", "Resend (email)", "Vercel (custom deploy)", "GitHub (code export)", "Tailwind (styling)"],
  'insights': [
    ("lightning", "Sell the Speed", "Your pitch is simple: 'Working app in 48 hours, guaranteed.' Most devs quote 3–4 weeks for the same thing. That gap is your business."),
    ("export", "Always Export the Code", "Lovable lets you export the full React codebase. Do this after every project. You own the code — it becomes your portfolio."),
    ("users", "Non-Tech Founders Are Your Market", "Target startup founders on Twitter/X and LinkedIn who are posting about their idea but can't build. They're everywhere and they have budget."),
  ],
  'facts': {"Pricing": "Free → $25/mo", "Output": "React + Tailwind", "Skill Level": "Beginner", "Backend": "Supabase", "Time to Revenue": "24–48 hours"},
  'warnings': ["Lovable is for MVPs and prototypes. For production apps with complex business logic, you'll need to export the code and continue in Cursor."],
  'tips': ["Be brutally specific in your initial prompt. The more detail you give — colours, layout, features, user flows — the less back-and-forth you'll need."],
}

# ─────────────────────────────────────────────
# 05. WINDSURF
# ─────────────────────────────────────────────
CONTENT['windsurf'] = {
  'what_it_is': "Windsurf by Codeium is an agentic IDE that goes further than Cursor — its 'Cascade' agent can reason across your entire codebase, plan multi-step changes, and execute them across dozens of files simultaneously. It's purpose-built for developers who want an AI that thinks before it codes.",
  'money_streams': [
    ("Enterprise Dev Contracts", "$10K–$40K/mo", "Target companies migrating from legacy systems. Windsurf's codebase reasoning makes large-scale refactors tractable.", "3–6 weeks to land"),
    ("Full-Stack Freelancing", "$5K–$20K/mo", "Take on complex full-stack projects with confidence. Windsurf handles architecture planning + execution.", "2–3 weeks"),
    ("Developer Tooling SaaS", "$3K–$20K MRR", "Build niche dev tools: CI/CD dashboards, monitoring tools, internal platforms. Developers pay well for tools.", "60–90 days"),
    ("Code Migration Service", "$5K–$30K per project", "Migrate React class components to hooks, Redux to Zustand, REST to GraphQL. Companies pay for expertise.", "Per project"),
  ],
  'steps': [
    ("Download Windsurf", "Get it at codeium.com/windsurf. Free tier available. Installs in under 3 minutes.", "# macOS\nbrew install --cask windsurf\n\n# Or download installer from codeium.com/windsurf"),
    ("Import VS Code Config", "On first launch, import your VS Code settings, keybindings, and extensions in one click. No reconfiguration.", ""),
    ("Open Cascade (the Agent)", "Click the Cascade icon or press Cmd+L. This is the agent panel — not just chat, but a full reasoning engine.", ""),
    ("Give It a Task", "Describe a feature or refactor in plain English. Cascade will read relevant files, plan its approach, then execute. Watch it work.", ""),
    ("Review the Flow", "Windsurf shows you exactly what it read, what it changed, and why. Review the diff. Approve and commit.", ""),
  ],
  'terminal_steps': [
    ("Install (macOS)", "brew install --cask windsurf", "Or download from codeium.com"),
    ("Open project", "windsurf .", ""),
    ("Cascade (agent)", "Cmd+L", "Full agentic mode"),
    ("Inline edit", "Cmd+K", "Edit selected code"),
    ("Autocomplete", "Tab", "Accept suggestion"),
    ("Search codebase", "Cmd+Shift+F", "AI-powered search"),
  ],
  'prompts': [
    ("Multi-File Refactor", "Refactor the entire authentication system. Current state: raw JWT handling in each route file with duplicated validation logic. Goal: centralise into a single auth middleware. Create an authMiddleware.ts file, extract all JWT logic into it, update all routes to use it, and add proper TypeScript types throughout. Show me your plan before executing."),
    ("Feature Addition", "Add a complete notification system to this app. Requirements: 1) NotificationProvider wrapping the app with context, 2) useNotifications hook for adding/removing/reading notifications, 3) A NotificationCenter UI component (bell icon with badge), 4) Support for 4 types: success, error, warning, info. 5) Auto-dismiss after 5 seconds. 6) Persist to localStorage. Integrate it with all existing API error handlers."),
  ],
  'stack': ["Claude Code (terminal)", "GitHub Actions (CI/CD)", "Docker (containerisation)", "PostgreSQL (database)", "Redis (caching)", "Datadog (monitoring)"],
  'insights': [
    ("brain", "Cascade Reads Context First", "Unlike other tools that jump straight to coding, Cascade reads all relevant files first and explains its plan. This leads to dramatically fewer bugs."),
    ("tree-structure", "Perfect for Monorepos", "Windsurf handles monorepos better than any other AI IDE. If your client has a large shared codebase, this is your tool."),
    ("currency-dollar", "Target Mid-Market Companies", "Small startups use Lovable/Base44. Enterprise uses consultancies. The mid-market (20–200 employees) pays for Windsurf-powered contract work."),
  ],
  'facts': {"Pricing": "Free → $15/mo Pro", "Agent": "Cascade (multi-file)", "Skill Level": "Intermediate", "Context": "Full codebase", "Time to Revenue": "1 week"},
  'warnings': ["Cascade can make sweeping changes across many files. Always use git and commit before letting it run on large refactors."],
  'tips': ["Ask Cascade to 'explain your plan before executing' on complex tasks. This surfaces misunderstandings before they become bugs."],
}

# ─────────────────────────────────────────────
# 06. MIDJOURNEY
# ─────────────────────────────────────────────
CONTENT['midjourney'] = {
  'what_it_is': "Midjourney is the industry standard for AI image generation. It consistently produces the highest aesthetic quality images of any tool — cinematic, painterly, architectural, product photography. The Discord-based workflow and web interface are used by designers, marketers, and creators to generate professional assets at scale.",
  'money_streams': [
    ("Print-on-Demand Store", "$1K–$8K/mo", "Generate art prints, posters, and designs. Sell on Etsy, Redbubble, Society6. A well-niched store runs passively.", "2–4 weeks to first sale"),
    ("Brand Asset Packages", "$500–$3K per client", "Create logo concepts, brand mood boards, social media graphics packs. Sell to small businesses and startups.", "1 week to first client"),
    ("Licensing & Stock", "$200–$2K/mo passive", "Upload generated images to Adobe Stock, Shutterstock, Pond5. Earn royalties every time they're licensed.", "3–6 months to build up"),
    ("Children's Book Illustration", "$2K–$10K per book", "Self-publish illustrated children's books on Amazon KDP. Midjourney handles all illustrations. You write the story.", "2–4 weeks per book"),
  ],
  'steps': [
    ("Join Midjourney", "Go to midjourney.com. Subscribe to Basic ($10/mo) or Standard ($30/mo). Join the Discord server to use /imagine commands.", ""),
    ("Use the Web Interface", "Go to midjourney.com/imagine for the cleaner web UI. Type your prompt, adjust settings, generate.", ""),
    ("Master the Prompt Formula", "Structure: [subject] [style] [lighting] [mood] [technical params]. Add --ar for aspect ratio, --v 6 for latest model, --style raw for realistic.", "/imagine prompt: editorial product photography, luxury perfume bottle, black marble background, dramatic side lighting, commercial studio quality --ar 3:4 --v 6"),
    ("Upscale & Vary", "After generation, upscale your best variant (U1–U4). Use Vary(Subtle) for small tweaks, Vary(Strong) for different interpretations.", ""),
    ("Export for Commercial Use", "Midjourney's paid plans include commercial usage rights. Export at full resolution. Use in your products, for clients, or on print platforms.", ""),
  ],
  'prompts': [
    ("Product Photo", "/imagine prompt: luxury skincare product photography, amber glass serum bottle, white marble surface, eucalyptus sprigs, soft diffused natural light, minimalist spa aesthetic, editorial magazine quality, 8K detail --ar 4:5 --v 6 --style raw"),
    ("Print Art", "/imagine prompt: abstract geometric art print, overlapping circles and triangles, muted earth tones terracotta sage cream charcoal, Bauhaus design school influence, high contrast, framed poster aesthetic, clean white margins --ar 2:3 --v 6"),
    ("Brand Mood Board", "/imagine prompt: brand identity mood board for a luxury sustainable fashion label, neutral palette sand ecru forest green, editorial photography collage, minimalist typography, natural textures linen cotton paper, aspirational lifestyle, flat lay --ar 16:9 --v 6"),
  ],
  'stack': ["Canva (post-process)", "Etsy (sell prints)", "Printify (print-on-demand)", "Adobe Firefly (variations)", "ChatGPT (prompt ideas)", "Adobe Stock (licensing)"],
  'insights': [
    ("image-square", "Niche Your Store Hard", "The top Etsy sellers aren't selling 'AI art' — they're selling 'vintage botanical prints for bathroom walls' or 'moody dark academia bookshelf art'. Niche wins."),
    ("package", "Batching Is the Business", "Generate 50+ variations in one session. The cost is pennies per image. One winning design can earn for years."),
    ("star", "Style Consistency = Brand", "Save your best prompts and parameters. Consistent style across your store builds brand recognition and repeat buyers."),
  ],
  'facts': {"Pricing": "$10–$60/mo", "Commercial Rights": "All paid plans", "Skill Level": "Beginner", "Output": "PNG up to 4K", "Time to Revenue": "48 hours"},
  'warnings': ["Midjourney v6 generates realistic faces that can resemble real people. Avoid generating portraits of named individuals for commercial use."],
  'tips': ["Use --style raw for the most realistic, unprocessed output. Add 'award-winning photography' or 'published in Architectural Digest' to push quality higher."],
}

# ─────────────────────────────────────────────
# 07. RUNWAY ML
# ─────────────────────────────────────────────
CONTENT['runway'] = {
  'what_it_is': "Runway is a professional AI video creation suite used by film studios, agencies, and content creators. Gen-3 Alpha generates high-quality video from text or images. Its editing tools — inpainting, motion brush, background removal — make it a full post-production studio in a browser tab.",
  'money_streams': [
    ("AI Video Content Studio", "$3K–$15K/mo", "Run a faceless content agency producing 30–60 second videos for brands, coaches, and creators. Sell packages monthly.", "2–3 weeks to launch"),
    ("Ad Creative Agency", "$2K–$8K per client/mo", "Brands need constant video ads for Meta, TikTok, YouTube. Generate 5–10 variations per week per client.", "2 weeks to first client"),
    ("Music Visualiser Service", "$500–$2K per video", "Musicians and labels need music video content. Runway generates stunning sync'd visuals in hours.", "1 week"),
    ("Film & TV Pre-Production", "$5K–$20K per project", "Create animatics, concept visualisations, and storyboards for film and TV pitches.", "Project-based"),
  ],
  'steps': [
    ("Create Account", "Go to runwayml.com. Free plan gives 125 credits to start. Subscribe to Standard ($15/mo) for serious work.", ""),
    ("Use Gen-3 Alpha", "Navigate to Generate → Video. Select 'Text to Video' for fresh generations or 'Image to Video' for controlled output.", ""),
    ("Write a Strong Video Prompt", "Include: camera motion (slow push in, tracking shot), subject, action, environment, lighting, cinematic style.", ""),
    ("Use Motion Brush", "For image-to-video, use the Motion Brush tool to draw where you want motion. Control exactly which elements move.", ""),
    ("Combine Clips in Multi-Track", "Use Runway's timeline editor to string clips together, add audio, and export. Full video production without leaving the browser.", ""),
  ],
  'prompts': [
    ("Brand Film Shot", "Cinematic slow push-in on a luxury watch resting on dark wet stone, water droplets forming on the surface, deep moody lighting, blue and amber colour grade, shallow depth of field, 24fps film grain, product commercial aesthetic"),
    ("Social Ad Creative", "A confident woman walks through a sunlit city street, slow motion hair movement, golden hour light, she glances at camera with subtle smile, aspirational lifestyle, warm colour palette, Instagram Reels vertical format aesthetic"),
    ("Abstract Opener", "Abstract liquid metal morphing into brand logo shape, chrome and gold tones, dramatic studio lighting with caustic reflections, luxury brand reveal opener, 4 seconds, holds on final logo frame"),
  ],
  'stack': ["ElevenLabs (voiceover)", "Sora (longer clips)", "Adobe Premiere (final edit)", "CapCut (social format)", "Midjourney (source images)", "Descript (captions)"],
  'insights': [
    ("video-camera", "Image-to-Video Is More Controllable", "Generate your perfect frame in Midjourney first, then animate it in Runway. This gives you far more control than text-to-video alone."),
    ("briefcase", "Brand Retainers Are the Model", "One brand client at $2K/mo for weekly ad variations is better than 10 one-off projects. Pitch a monthly 'creative subscription'."),
    ("sparkle", "Gen-3 vs. Gen-2 Quality Gap", "Always use Gen-3 Alpha for client work. The quality jump is enormous. Never show clients Gen-2 output."),
  ],
  'facts': {"Pricing": "Free → $35/mo", "Model": "Gen-3 Alpha", "Skill Level": "Beginner", "Max Length": "10 seconds/clip", "Time to Revenue": "1 week"},
  'warnings': ["Runway's free tier has limited credits. For client work, go Standard or Pro — you'll burn through free credits in one serious session."],
  'tips': ["Use 'cinematic', 'shallow depth of field', and a specific film stock name like 'Kodak Vision3 500T' to dramatically increase visual quality."],
}

# ─────────────────────────────────────────────
# 08. KLING AI
# ─────────────────────────────────────────────
CONTENT['kling'] = {
  'what_it_is': "Kling AI (by Kuaishou) is China's answer to Sora — and it frequently outperforms it for social content. Kling 3.0 generates hyper-realistic motion, expressive characters, and smooth physics that other models can't match. It's the tool for TikTok and Instagram Reels creators who need thumb-stopping video.",
  'money_streams': [
    ("Faceless TikTok Channels", "$1K–$10K/mo", "Run multiple AI-generated content channels on TikTok. Monetise via TikTok Creator Fund, brand deals, and affiliate links.", "3–6 weeks to monetise"),
    ("UGC Content Agency", "$2K–$8K/mo", "Brands pay $200–$500 per UGC-style video. Generate 10–20 per month per client on retainer.", "1–2 weeks"),
    ("Viral Social Content", "$1K–$5K/mo", "Manage social media for local businesses. Kling generates all video content. You do strategy and posting.", "2 weeks"),
    ("AI Film Shorts", "$500–$5K per short", "Produce 60–90 second AI film shorts for brands, musicians, and events.", "Per project"),
  ],
  'steps': [
    ("Create Account", "Go to klingai.com. Sign in with Google. Free tier gives daily credits — enough to test. Subscribe for $10/mo for serious volume.", ""),
    ("Choose Generation Mode", "Text to Video for concept-first creation. Image to Video for controlled character/scene animation. Video to Video for style transfer.", ""),
    ("Write Motion-Focused Prompts", "Kling excels at motion. Describe movement explicitly: 'camera slowly orbits', 'hair flowing in wind', 'crowd erupts with energy'.", ""),
    ("Use the Pro Camera Controls", "Kling offers camera control presets: push in, pull out, pan left, tilt up, orbit. These dramatically improve consistency.", ""),
    ("Export & Post-Process", "Download at full quality. Bring into CapCut for captions, music sync, and format adjustment for each platform.", ""),
  ],
  'prompts': [
    ("Viral Hook Shot", "Extreme close-up on human eye, pupil dilating slowly as lights flicker on, macro lens with intense shallow depth of field, photorealistic, golden hour light catching iris, mysterious and cinematic opening shot, smooth slow motion"),
    ("Product Showcase", "Luxury sneaker rotates on pedestal, dramatic studio spotlight, shadows sweeping across shoe, camera slowly orbits 360 degrees, smoke effects, dark background, commercial product launch aesthetic, hyper-detailed materials"),
    ("Lifestyle/Fashion", "Young woman in minimalist white outfit walks through Japanese cherry blossom park, petals falling in slow motion, golden hour backlight, hair gently moving, confident natural stride, cinematic widescreen, film grain"),
  ],
  'stack': ["CapCut (editing)", "ElevenLabs (voiceover)", "Midjourney (source images)", "Upload-Post (scheduling)", "Canva (thumbnails)", "TikTok Analytics (tracking)"],
  'insights': [
    ("trend-up", "The 3-Second Hook Rule", "For TikTok, your first 3 seconds determine everything. Generate 5 different openings for every piece of content and A/B test them."),
    ("palette", "Character Consistency", "Use Image-to-Video with a reference face image to maintain character consistency across a series. This is critical for brand mascots and recurring characters."),
    ("clock", "Volume Is the Strategy", "Post 2–3 times per day. One in ten videos will catch the algorithm. With Kling, that volume is achievable solo."),
  ],
  'facts': {"Pricing": "Free → ~$10/mo", "Model": "Kling 3.0", "Skill Level": "Beginner", "Max Length": "3 min (Pro)", "Time to Revenue": "3–5 days"},
  'warnings': ["Kling's interface is primarily in Chinese — use the English version at klingai.com, not the native Chinese app, for the international feature set."],
  'tips': ["For the most realistic human motion, use 'photorealistic, 8K, shot on Sony FX3, natural movement' in your prompt — Kling responds exceptionally well."],
}

# ─────────────────────────────────────────────
# 09. SORA
# ─────────────────────────────────────────────
CONTENT['sora'] = {
  'what_it_is': "Sora is OpenAI's text-to-video model, available to ChatGPT Plus and Pro subscribers. It's the strongest model for long-form, narrative, and cinematic content — generating coherent clips up to 20 seconds with exceptional temporal consistency. It's built for storytelling, not just eye-candy clips.",
  'money_streams': [
    ("Cinematic Short Films", "$2K–$10K per short", "Produce branded short films, festival submissions, and commercial showcases. Directors pay for Sora-assisted production.", "Project-based"),
    ("YouTube AI Film Channel", "$1K–$8K/mo", "Build a long-form AI film channel. Sora produces the visual narrative. Monetise via AdSense and brand deals.", "3–6 months to monetise"),
    ("Corporate Training Videos", "$3K–$15K per project", "Companies need internal training content. Sora generates professional scenarios that cost $20K+ with traditional production.", "1 project at a time"),
    ("Real Estate Visual Tours", "$500–$2K per property", "Animate still property renderings into cinematic walkthroughs for real estate agents and developers.", "Per project"),
  ],
  'steps': [
    ("Access via ChatGPT Plus/Pro", "Log in to chatgpt.com. Navigate to the Sora tab in the left sidebar. Plus plan gets standard quality; Pro gets 1080p and priority.", ""),
    ("Start with a Story Beat", "Sora performs best with narrative prompts. Think in shots: establishing shot → medium shot → close-up. Write each as a separate generation.", ""),
    ("Use Storyboard Mode", "In Sora's UI, upload a sequence of images or prompts as a storyboard. Sora tries to maintain continuity across them.", ""),
    ("Remix Existing Clips", "Upload a video and Sora can remix it — changing the style, weather, time of day, or characters while keeping the motion.", ""),
    ("Export & Sequence", "Download your clips. Import into DaVinci Resolve or Premiere for sequencing, colour grading, and audio sync.", ""),
  ],
  'prompts': [
    ("Cinematic Establishing Shot", "Aerial drone shot slowly descending over a neon-lit Tokyo street at 2am, rain-slicked streets reflecting neon signs, pedestrians with umbrellas, ultra-cinematic, anamorphic lens flare, Blade Runner 2049 colour palette, photorealistic, 24fps"),
    ("Character Drama", "A weathered astronaut in a worn spacesuit sits alone in a dimly lit module, staring at a photograph in their hand, a single tear forms, the camera slowly pushes in on their face, no dialogue, melancholic score implied, cinematic close-up, IMAX quality"),
    ("Nature Documentary", "A pack of silver wolves moves through a dense pine forest in heavy snowfall, slow motion, BBC Planet Earth production quality, golden hour breaks through the canopy, breath misting in cold air, majestic and silent"),
  ],
  'stack': ["DaVinci Resolve (editing)", "ElevenLabs (narration)", "Runway (short clips)", "Kling (social cuts)", "Suno (background score)", "YouTube (distribution)"],
  'insights': [
    ("film-slate", "Sora Is About Narrative", "Other tools do eye-candy. Sora does story. If your project needs a beginning, middle, and end, Sora's temporal consistency is unmatched."),
    ("megaphone", "Horizontal Content Strategy", "Generate one long-form Sora piece, then cut it into Kling/Runway-style clips for TikTok and Reels. One input, 10 outputs."),
    ("buildings", "B2B Is Underserved", "Corporate training, real estate, and internal communications are completely underserved by AI video. These clients have budget and urgency."),
  ],
  'facts': {"Pricing": "$20/mo (Plus), $200/mo (Pro)", "Max Length": "20 seconds", "Skill Level": "Beginner", "Resolution": "1080p (Pro)", "Time to Revenue": "1 week"},
  'warnings': ["Sora has strict content policies. Anything that could be construed as depicting real people, violence, or political content will be blocked."],
  'tips': ["Write prompts like a film director giving instructions to a cinematographer. 'Camera slowly pushes in', 'rack focus from foreground to background', 'dolly shot left' all improve output."],
}

# ─────────────────────────────────────────────
# 10. SEEDANCE
# ─────────────────────────────────────────────
CONTENT['seedance'] = {
  'what_it_is': "Seedance (by ByteDance) is the most underrated AI video model right now. Its free tier is exceptionally generous, and its motion quality for social-format content consistently beats Sora and rivals Kling. For content creators on a budget, this is the highest-ROI video tool available.",
  'money_streams': [
    ("Free Tool Arbitrage", "$500–$3K/mo", "Use Seedance's generous free tier to produce client content at zero cost. Charge market rates. Pure margin.", "First week"),
    ("Faceless Social Content", "$1K–$8K/mo", "Build AI lifestyle, motivation, and entertainment channels using Seedance. The free tier sustains a serious content schedule.", "3–4 weeks"),
    ("Low-Cost Ad Creative", "$1K–$5K/mo", "Sell affordable video ad packages ($200–$500/video) to small businesses. Seedance keeps your costs near zero.", "1–2 weeks"),
    ("AI Motion Art", "$200–$2K per piece", "Create and sell AI motion art loops for digital displays, screensavers, and NFT marketplaces.", "1 week"),
  ],
  'steps': [
    ("Access Seedance", "Go to seedance.ai (or via Dreamina app). Create a free account — no credit card required. ByteDance gives generous daily free credits.", ""),
    ("Select Model Version", "Choose Seedance 2.0 for the best quality. The 5-second and 10-second options cover most social content needs.", ""),
    ("Optimise for Motion", "Seedance excels at fluid motion. Use verbs heavily in your prompt: swirling, cascading, exploding, drifting, pulsating.", ""),
    ("Use Reference Images", "Upload a reference image for style or subject consistency. Seedance respects composition and colour palette from reference images.", ""),
    ("Batch Generation", "Generate 5–10 variations of the same prompt. Pick the best 2–3. Seedance's free daily credits allow serious batching.", ""),
  ],
  'prompts': [
    ("High-Motion Social", "Vibrant liquid paint explosions colliding in slow motion, neon magenta, electric blue and gold, macro photography, high speed camera, splashing droplets catching studio light, abstract art, hypnotic loop-friendly ending"),
    ("Motivation Content", "First-person perspective sprinting through a dark tunnel toward a bright light that grows larger, cinematic, motivational, camera shake, determination energy, dramatic building score implied, 9:16 vertical format"),
    ("Product Tease", "Luxury watch materialises from golden particles swirling in darkness, particles gather and crystallise into the product, dramatic reveal, particle physics, studio lighting, premium brand aesthetic"),
  ],
  'stack': ["CapCut (editing)", "Canva (thumbnails)", "ElevenLabs (voiceover)", "Midjourney (source images)", "Upload-Post (scheduling)", "Buffer (analytics)"],
  'insights': [
    ("currency-dollar", "Free Tier Business Model", "Many creators build entire income streams on Seedance's free tier. ByteDance is subsidising your content business. Use it aggressively while it lasts."),
    ("chart-bar", "Test Everything", "Generate 10 versions of every important clip. The difference between a 1M view video and a 5K view video is often the first 2 seconds."),
    ("clock", "Speed to Market Wins", "Seedance's fast generation speed means you can produce a full week of content in one afternoon. Consistency beats perfection on social."),
  ],
  'facts': {"Pricing": "Free (very generous)", "Company": "ByteDance", "Skill Level": "Beginner", "Format": "9:16 and 16:9", "Time to Revenue": "3 days"},
  'warnings': ["ByteDance is a Chinese company subject to shifting data and content policies. Avoid generating politically sensitive content to prevent account suspension."],
  'tips': ["Seedance's free tier refreshes daily — check in every morning and generate your batch before the day's work. Build a library of clips over time."],
}

# ─────────────────────────────────────────────
# 11. ELEVENLABS
# ─────────────────────────────────────────────
CONTENT['elevenlabs'] = {
  'what_it_is': "ElevenLabs is the most realistic AI voice platform on the market. It clones voices from a 1-minute sample, generates natural-sounding speech in 30+ languages, and lets you earn royalties by licensing your voice to other creators. It's both a production tool and a passive income engine.",
  'money_streams': [
    ("Voice Royalties (Passive)", "$200–$2K/mo passive", "Clone your voice and add it to ElevenLabs' Voice Library. Earn royalties every time it's used by a paid subscriber. Zero ongoing work.", "Setup: 1 day. Income: ongoing"),
    ("Voiceover Service", "$500–$5K/mo", "Offer professional voiceover services for YouTube, ads, podcasts, and audiobooks. Deliver in hours. Charge professional rates.", "1 week to first client"),
    ("Audiobook Production", "$1K–$5K per book", "Convert existing books or original content into full audiobooks. Sell on ACX/Audible, Findaway, and direct.", "2–4 weeks per book"),
    ("Faceless YouTube Automation", "$1K–$10K/mo", "ElevenLabs voices narrate AI-generated or stock video content. Build channels that grow while you sleep.", "4–8 weeks to monetise"),
  ],
  'steps': [
    ("Create Account", "Go to elevenlabs.io. Free plan gives 10,000 characters/mo — enough to test every feature. Starter plan ($5/mo) unlocks commercial use and voice cloning.", ""),
    ("Clone Your Voice", "Go to Voices → Add Voice → Instant Clone. Record 1–2 minutes of clean audio (no background noise, consistent mic). Upload. Your clone is ready in 60 seconds.", ""),
    ("Join the Voice Library", "Go to Voices → Voice Library. Add your cloned voice. Set it as available for other users. Royalties accrue when paid users select it.", ""),
    ("Use the API", "For automation and bulk generation, use the ElevenLabs API. $0.0001 per character at scale — pennies for full audiobooks.", "curl https://api.elevenlabs.io/v1/text-to-speech/{voice_id}\\\n  -H 'xi-api-key: YOUR_API_KEY'\\\n  -H 'Content-Type: application/json'\\\n  -d '{\"text\": \"Your script here\", \"model_id\": \"eleven_multilingual_v2\"}'"),
    ("Integrate with Video Tools", "Pair ElevenLabs with Runway or HeyGen. ElevenLabs generates the voice track; the video tool lip-syncs it to an avatar.", ""),
  ],
  'prompts': [
    ("High-Converting Ad Script", "Write a 30-second voiceover script for a [product] ad. Voice should be warm but authoritative. Structure: hook (problem), agitate (cost of inaction), solution (product), CTA. No filler words. Maximum impact per word. Format for ElevenLabs: no punctuation clutter, natural pause markers with [pause]."),
    ("Audiobook Chapter Opener", "Write the opening 3 paragraphs of Chapter 1 of a business audiobook called 'The Revenue Engine'. Conversational but intelligent tone. Draw the listener in with a story — not a lecture. Write for the ear, not the eye: short sentences, vivid imagery, natural rhythm."),
  ],
  'stack': ["HeyGen (lip-sync avatar)", "Runway (video)", "Descript (editing)", "Adobe Audition (audio polish)", "ACX (audiobook distribution)", "Spotify for Podcasters"],
  'insights': [
    ("microphone", "Record Your Voice Now", "Voice cloning technology will only get better. Record a high-quality voice dataset now — even if you're not sure what to do with it yet. Future you will thank you."),
    ("coins", "Royalties Compound", "Adding your voice to the library is a one-time 15-minute setup. Every month, that decision pays you. That's the definition of passive income."),
    ("globe", "Multilingual = Market Multiplier", "ElevenLabs supports 30+ languages with your cloned voice. One piece of content → 5 language versions → 5x the potential audience."),
  ],
  'facts': {"Pricing": "Free → $22/mo", "Voice Clone": "From 1 min audio", "Skill Level": "Beginner", "Languages": "30+", "Time to Revenue": "1–3 days"},
  'warnings': ["ElevenLabs strictly prohibits cloning voices of real people without consent. Only clone your own voice or voices you have explicit rights to."],
  'tips': ["For the most natural output, add stage directions in brackets: '[excited] This is the best part [pause] because it changes everything.' ElevenLabs reads them as emotion cues."],
}

# ─────────────────────────────────────────────
# 12. HEYGEN
# ─────────────────────────────────────────────
CONTENT['heygen'] = {
  'what_it_is': "HeyGen creates AI video avatars that look and sound exactly like you — or a custom avatar — speaking any script you type. One 2-minute video recording creates your digital twin. It then generates unlimited videos where your avatar presents, teaches, sells, or entertains. The ultimate tool for faceless or face-forward video at scale.",
  'money_streams': [
    ("Video Course Creation", "$2K–$20K per course", "Record yourself once. HeyGen handles all course lesson updates and variations. Sell on Teachable, Gumroad, or Kajabi.", "2–4 weeks per course"),
    ("Corporate Training Videos", "$5K–$25K/mo", "Companies need internal training content constantly. Your avatar presents in their brand style. Charge per video or retainer.", "2–3 weeks to land clients"),
    ("Personalized Outbound Sales", "$1K–$5K/mo", "Generate personalised 30-second video messages for each prospect. Proven to 10x reply rates vs text emails.", "1 week setup"),
    ("Faceless AI Channel", "$2K–$15K/mo", "Your avatar hosts a YouTube or TikTok channel. Type scripts, generate videos, upload. No camera, no lights, no studio.", "4–8 weeks to monetise"),
  ],
  'steps': [
    ("Create Your Avatar", "Go to app.heygen.com → Avatars → Create Avatar. Record a 2-minute talking video (good lighting, neutral background, clear audio). Your avatar is ready in ~24 hours.", ""),
    ("Clone Your Voice", "Under Voices, upload 2–5 minutes of clear audio. HeyGen clones your voice for use with your avatar. Combine both for maximum realism.", ""),
    ("Create Your First Video", "New Video → Select your avatar → Type or paste your script → Select voice → Generate. A professional video renders in minutes.", ""),
    ("Use Talking Photo for Rapid Content", "Talking Photo lets any still image speak. Upload a brand photo and a script. No avatar setup required. Perfect for client demos.", ""),
    ("Translate & Localise", "HeyGen's Video Translation feature automatically translates your video into 30+ languages with lip-sync. One video → 30 markets.", ""),
  ],
  'prompts': [
    ("Sales Outreach Script", "Write a 30-second personalised video script for outreach to [Company Name]. The person watching is [Name], their role is [Role]. We are reaching out because [specific reason]. Structure: 1) Name personalisation hook, 2) specific relevant insight about their company, 3) our value proposition in one sentence, 4) low-friction CTA. No corporate language. Sound human."),
    ("Course Intro Script", "Write the opening 90-second script for an online course about [topic]. The student just purchased. Make them feel they made the right decision. Build excitement for what they're about to learn. Make a bold promise about the transformation. Transition naturally into the first lesson overview."),
  ],
  'stack': ["ElevenLabs (voice quality)", "ChatGPT (script writing)", "Canva (video thumbnails)", "Zapier (automation)", "Teachable (course hosting)", "LinkedIn (outreach)"],
  'insights': [
    ("user-circle", "The Avatar Moat", "Once you have a professional avatar and cloned voice, you have a permanent content asset. It gets better over time, not worse."),
    ("translate", "Translation Is a Growth Hack", "Your English content might reach 1M people. The Spanish, Portuguese, and Hindi versions of the same content reach 3 billion more."),
    ("envelope", "Video Outreach ROI", "Personalised video outreach from HeyGen has a 40–60% open rate vs 5–10% for text emails. For B2B sales, this alone justifies the subscription."),
  ],
  'facts': {"Pricing": "Free → $29/mo", "Avatar Quality": "Photorealistic", "Skill Level": "Beginner", "Languages": "40+", "Time to Revenue": "1 week"},
  'warnings': ["HeyGen avatars are detectable by AI content detection tools. For platforms that prohibit AI avatars (e.g., some LinkedIn outreach limits), disclose appropriately."],
  'tips': ["Light your 2-minute avatar training video perfectly. Use a ring light, neutral background, and speak at your natural pace. The quality of your training clip determines your avatar quality forever."],
}

# ─────────────────────────────────────────────
# 13. CHATGPT
# ─────────────────────────────────────────────
CONTENT['chatgpt'] = {
  'what_it_is': "ChatGPT is the default AI for billions of people — which makes it your most accessible path to your first AI-powered dollar. With GPT-4o, deep research mode, custom GPTs, and the operator API, it's both a client-facing product and an internal force multiplier. Your first AI income almost certainly runs through here.",
  'money_streams': [
    ("Content Agency", "$3K–$15K/mo", "Write SEO articles, email sequences, social media content, and ad copy for businesses. ChatGPT does the drafts. You do QA and delivery.", "1 week to first client"),
    ("Custom GPT Products", "$500–$5K/mo", "Build niche Custom GPTs (for fitness, law, real estate, etc.) and sell access or subscription. GPT Store earns per interaction.", "1–2 weeks to build"),
    ("Ghostwriting Service", "$2K–$10K/mo", "Write LinkedIn posts, Twitter threads, blog articles, and books for executives and founders. $0.01/word at volume = serious money.", "1 week to first client"),
    ("Prompt Engineering Consulting", "$150–$400/hr", "Teach businesses how to use ChatGPT effectively. Run workshops, build internal playbooks, optimise workflows.", "1 week to first client"),
  ],
  'steps': [
    ("Go Plus or Use API", "Free tier is too limited for business use. ChatGPT Plus ($20/mo) unlocks GPT-4o, deep research, and Custom GPTs. For automation, use the OpenAI API directly.", "pip install openai"),
    ("Build a Custom GPT", "Go to ChatGPT → Explore GPTs → Create. Give it a persona, instructions, and knowledge files. This becomes your AI product.", "# System prompt structure for Custom GPT:\n# 1. Role definition\n# 2. Core task description\n# 3. Formatting rules\n# 4. Tone and persona\n# 5. What to avoid"),
    ("Use GPT-4o for Production", "Always use GPT-4o for client-facing output. It's multimodal, fast, and produces the most commercially usable text.", ""),
    ("Set Up the API", "For automation, content pipelines, and your own products, use the OpenAI API. Python SDK is the fastest start.", "from openai import OpenAI\nclient = OpenAI(api_key='sk-...')\nresponse = client.chat.completions.create(\n  model='gpt-4o',\n  messages=[{\"role\": \"user\", \"content\": \"Your prompt\"}]\n)\nprint(response.choices[0].message.content)"),
    ("Build Content Pipelines", "Combine the API with Google Sheets (for inputs) and email automation (for delivery). One system serves 10+ clients simultaneously.", ""),
  ],
  'prompts': [
    ("SEO Article System Prompt", "You are a world-class SEO content writer. When given a keyword, you write a 1,500-word article that: 1) Opens with a hook that addresses the reader's problem, 2) Uses the keyword naturally in H1, first paragraph, 2 H2s, and conclusion, 3) Includes a TL;DR summary box, 4) Uses short paragraphs (max 3 sentences), 5) Ends with 3 actionable takeaways, 6) Avoids all AI-sounding filler phrases. Output in Markdown."),
    ("LinkedIn Ghostwriting", "I need a LinkedIn post for [person's name], a [their role] at [company]. Topic: [topic]. Their writing style is [describe style — e.g. direct, data-driven, occasionally vulnerable]. Their audience is [audience]. Rules: no emojis, no hashtag spam, max 3 hashtags only if relevant, hook in first line must provoke curiosity or challenge an assumption, end with a genuine question. 150–250 words."),
    ("Email Sequence", "Write a 5-email welcome sequence for a new subscriber to [newsletter name] about [topic]. Each email: subject line (A/B test 2 options), preview text, body (200–300 words), one clear CTA. Sequence arc: Email 1 — warm welcome + deliver lead magnet. Email 2 — founder story + mission. Email 3 — big idea/contrarian take. Email 4 — social proof + case study. Email 5 — product offer. Tone: smart, direct, non-salesy."),
  ],
  'stack': ["Claude (long-form)", "Perplexity (research)", "Make/Zapier (automation)", "Notion (content calendar)", "Beehiiv (newsletter)", "Stripe (billing)"],
  'insights': [
    ("book-open", "The First Dollar Rule", "ChatGPT is the fastest tool to your first AI-earned dollar. Don't overthink it. Write 10 sample pieces tonight. Post them. DM 20 potential clients tomorrow."),
    ("robot", "Custom GPTs = Products", "A well-built Custom GPT for a specific niche (e.g., 'Real Estate Listing Writer' or 'Therapist Session Notes Generator') is a real product. 1,000 users × $5/mo = $5K MRR."),
    ("arrow-up-right", "Rate Compression Strategy", "Start at $30/hour. Build case studies. Raise to $75. Build more. Raise to $150. The market for expert AI-augmented writers pays $200+/hr."),
  ],
  'facts': {"Pricing": "Free → $20/mo", "Model": "GPT-4o", "Skill Level": "Beginner", "Context Window": "128K tokens", "Time to Revenue": "24 hours"},
  'warnings': ["Don't submit AI-generated content without editing. Clients who get caught publishing unedited AI slop blame the writer. Your reputation is the product."],
  'tips': ["Use a detailed system prompt for every project — not just one-off prompts. System prompts make your outputs consistent, branded, and repeatable across clients."],
}

# ─────────────────────────────────────────────
# 14. CLAUDE
# ─────────────────────────────────────────────
CONTENT['claude'] = {
  'what_it_is': "Claude (by Anthropic) is the AI that professionals reach for when quality matters over speed. With a 200K token context window, exceptional writing ability, strong reasoning, and the most nuanced understanding of tone and voice of any model, it's the tool for serious content, analysis, legal work, and anything where 'good enough' isn't enough.",
  'money_streams': [
    ("Executive Ghostwriting", "$5K–$25K/mo", "Write books, white papers, and thought-leadership content for C-suite executives. Claude handles voice matching and long-form coherence.", "2–4 weeks to first client"),
    ("Research & Analysis Reports", "$1K–$10K per report", "Produce market research, competitive analysis, and investment theses. Sell to funds, consultancies, and corporates.", "1 report at a time"),
    ("Legal & Compliance Drafting", "$3K–$20K/mo", "Draft contracts, policies, compliance documents, and memos for law firms and corporations. Claude's precision is unmatched.", "Requires domain knowledge"),
    ("Technical Documentation", "$2K–$8K/mo", "Write API docs, developer guides, and product specs for tech companies. Claude reads code and explains it clearly.", "2 weeks to first client"),
  ],
  'steps': [
    ("Subscribe to Claude.ai", "Go to claude.ai. Free tier gives access to Claude Haiku. Claude.ai Pro ($20/mo) unlocks Claude Sonnet and Opus — use Opus for your best work.", ""),
    ("Use Projects", "Projects give Claude persistent memory across sessions. Create one project per client. Claude remembers their style, preferences, and context.", ""),
    ("Upload Documents", "Claude can read entire books, codebases, legal documents, financial reports. Upload up to 200K tokens and ask questions across the full document.", ""),
    ("Set Up Claude API", "For production pipelines, use the Anthropic API. Claude 3 Opus is the best model for anything requiring deep reasoning.", "pip install anthropic\n\nimport anthropic\nclient = anthropic.Anthropic(api_key='sk-ant-...')\nmessage = client.messages.create(\n  model='claude-opus-4-5',\n  max_tokens=4096,\n  messages=[{\"role\": \"user\", \"content\": \"Your prompt\"}]\n)\nprint(message.content[0].text)"),
    ("Master XML Prompting", "Claude responds best to XML-structured prompts. Use <context>, <task>, <format>, <examples> tags for complex instructions.", ""),
  ],
  'prompts': [
    ("Executive Book Chapter", "<context>You are ghostwriting a business book for [name], CEO of [company]. Their core argument is [thesis]. Their writing voice is [description — e.g. direct, data-driven, occasionally uses personal stories, avoids jargon]. Their audience is senior executives with 15+ years experience.</context>\n<task>Write Chapter 3 on [topic]. 2,500 words. Include: an opening story from their career, the central framework (name it and make it memorable), 3 case studies, and a closing challenge to the reader.</task>\n<format>Narrative non-fiction. Short punchy sentences. No bullet points except for the framework. Use 'you' and 'we' language.</format>"),
    ("Document Analysis", "<task>Analyse the following 200-page financial report and produce: 1) An executive summary (300 words), 2) Top 5 risks identified with severity rating (1-5), 3) Top 3 opportunities, 4) Key financial metrics table, 5) Recommended questions for management. Be precise. Flag any numbers that appear inconsistent.</task>\n<document>[paste document]</document>"),
  ],
  'stack': ["ChatGPT (ideation)", "Claude Code (coding)", "Notion (content delivery)", "Beehiiv (publishing)", "Stripe (billing)", "Calendly (client booking)"],
  'insights': [
    ("feather", "Claude Writes Like a Human", "Claude's writing is the least detectable as AI. For executive ghostwriting and professional content, this is the single most important quality you can offer clients."),
    ("file-doc", "200K Context Is a Superpower", "Upload an entire company's documents — strategy decks, annual reports, product roadmaps — and ask Claude to synthesise insights. No other model does this as reliably."),
    ("crown", "Opus for Critical Work", "Use Claude Haiku for speed, Sonnet for balance, Opus for the work that your client is paying a premium for. Never use Haiku for deliverables you charge $500+ for."),
  ],
  'facts': {"Pricing": "Free → $20/mo", "Best Model": "Claude Opus", "Skill Level": "Beginner", "Context Window": "200K tokens", "Time to Revenue": "48 hours"},
  'warnings': ["Claude has strong safety guardrails. For legal or medical content, always tell it you are a professional in the field and the content is for professional use only."],
  'tips': ["Use XML tags to structure complex prompts: <context>, <task>, <format>, <examples>. Claude follows structured instructions more accurately than any other model."],
}

# ─────────────────────────────────────────────
# 15. PERPLEXITY
# ─────────────────────────────────────────────
CONTENT['perplexity'] = {
  'what_it_is': "Perplexity is the AI answer engine — it searches the web in real time, cites its sources, and synthesises answers with the accuracy of a research team. It's not just for asking questions; it's a professional research machine that can produce sourced reports in minutes that would take analysts days.",
  'money_streams': [
    ("Research-as-a-Service", "$500–$5K per report", "Produce sourced competitive analysis, market research, and industry reports for businesses and investors. Sell individual reports or subscriptions.", "1 week to first client"),
    ("SEO Content Research", "$1K–$5K/mo", "Use Perplexity to research every article before writing. Charge clients for thoroughly researched, up-to-date content that ranks.", "1 week"),
    ("Investment Research", "$2K–$10K/mo", "Produce sector overviews, company due diligence, and news briefings for investors and family offices.", "Requires finance knowledge"),
    ("Newsletter Intelligence", "$500–$3K/mo", "Use Perplexity to research and write niche newsletters with real-time news. Monetise with paid subscriptions.", "4–6 weeks to build audience"),
  ],
  'steps': [
    ("Sign Up for Pro", "Go to perplexity.ai. Free tier works for testing. Pro ($20/mo) unlocks more searches, Claude/GPT-4o models, and unlimited file uploads.", ""),
    ("Master Spaces", "Perplexity Spaces let you create focused research environments with uploaded documents. Create one Space per client or project.", ""),
    ("Use Deep Research Mode", "Click 'Deep Research' before your query. It spends 3–5 minutes running dozens of searches and producing a comprehensive cited report.", ""),
    ("Cite and Verify", "Every Perplexity answer includes citations. Always click through the top 3 sources to verify key claims before putting them in a client deliverable.", ""),
    ("Use the API", "For automated research pipelines, use the Perplexity API with the sonar-pro model — it does real-time web search programmatically.", "curl https://api.perplexity.ai/chat/completions \\\n  -H 'Authorization: Bearer YOUR_KEY' \\\n  -H 'Content-Type: application/json' \\\n  -d '{\"model\": \"sonar-pro\", \"messages\": [{\"role\": \"user\", \"content\": \"Your research query\"}]}'"),
  ],
  'prompts': [
    ("Market Research Report", "Conduct a comprehensive market analysis of the [industry] market. Cover: 1) Current market size and 5-year growth projections with sources, 2) Top 5 players with market share estimates, 3) Key trends disrupting the space in 2025, 4) Biggest pain points for customers (cite Reddit, forums, reviews), 5) White space opportunities for a new entrant. Cite all figures. Flag where data is estimated vs confirmed."),
    ("Competitor Intelligence", "Analyse [Competitor Name] as if you're preparing a competitor brief for their main rival. Cover: pricing model and recent changes, product roadmap signals (from job postings, blog posts, announcements), customer complaints (from G2, Trustpilot, Reddit), recent hires that signal strategic direction, and any financial signals (funding rounds, revenue estimates). Include URLs for all major claims."),
  ],
  'stack': ["Claude (report writing)", "ChatGPT (summarisation)", "Notion (report delivery)", "Beehiiv (newsletter)", "Gumroad (sell reports)", "Stripe (subscriptions)"],
  'insights': [
    ("magnifying-glass", "Deep Research is Your Analyst", "One Deep Research session can replace 4 hours of manual research. At $150/hr consulting rates, that's $600 of value per query."),
    ("newspaper", "Newsletter Moat", "A Perplexity-powered niche newsletter with daily sourced intelligence builds a durable, monetisable audience. Choose a niche no one else covers."),
    ("building-office", "Sell to Companies Not Individuals", "Companies pay $2K–$10K for a market research report. The same content that would earn $5 on Medium earns $5,000 as a consulting deliverable."),
  ],
  'facts': {"Pricing": "Free → $20/mo", "Model Options": "Claude, GPT-4o, Sonar", "Skill Level": "Beginner", "Search": "Real-time web", "Time to Revenue": "3 days"},
  'warnings': ["Always verify Perplexity citations. It occasionally cites real URLs for claims that aren't actually in the source. Check before including in client deliverables."],
  'tips': ["Start every research query with 'Conduct a comprehensive analysis of...' rather than a question. This triggers longer, more structured outputs."],
}

# ─────────────────────────────────────────────
# 16. GEMINI
# ─────────────────────────────────────────────
CONTENT['gemini'] = {
  'what_it_is': "Gemini (by Google DeepMind) is the AI most deeply embedded in the world's most-used software — Gmail, Docs, Sheets, Meet, and Search. Its 1-million-token context window handles entire codebases and book-length documents. For anyone operating in the Google ecosystem, it's the highest-leverage AI available.",
  'money_streams': [
    ("Google Workspace Automation", "$2K–$10K per setup", "Automate client workflows in Gmail, Docs, and Sheets using Gemini + Apps Script. Charge for setup and maintenance.", "2 weeks per client"),
    ("Deep Research Services", "$1K–$8K per report", "Gemini's Deep Research produces multi-source, cited reports that rival consulting-grade output. Sell to businesses.", "1 week"),
    ("YouTube SEO Content", "$1K–$5K/mo", "Gemini integrates with YouTube Studio. Use it to optimise titles, descriptions, chapters, and audience targeting at scale.", "1 week"),
    ("Enterprise AI Consulting", "$5K–$25K/mo", "Help companies deploy Google AI in their existing Workspace environment. The fastest AI adoption path for Google shops.", "3–6 weeks to engage"),
  ],
  'steps': [
    ("Access Gemini Advanced", "Go to gemini.google.com. Google One AI Premium ($20/mo) gives Gemini Ultra — the most powerful version. Free tier gives Gemini Pro.", ""),
    ("Use Gems (Custom Agents)", "Gems are like Custom GPTs. Go to 'My Gems' → Create a Gem. Define a persona, instructions, and tool access. These become your AI products.", ""),
    ("Connect Google Workspace", "In Gmail, Docs, or Sheets, click the Gemini icon. It reads your documents and workspace context natively — no copy-pasting.", ""),
    ("Deep Research Mode", "Click the graduation cap icon in Gemini for Deep Research. It runs multi-source web searches and produces a comprehensive cited report.", ""),
    ("Use the Gemini API", "For developers and automation builders, the Gemini API is generous on the free tier. Access via Google AI Studio.", "pip install google-generativeai\n\nimport google.generativeai as genai\ngenai.configure(api_key='YOUR_API_KEY')\nmodel = genai.GenerativeModel('gemini-2.0-flash-exp')\nresponse = model.generate_content('Your prompt')\nprint(response.text)"),
  ],
  'prompts': [
    ("Workspace Automation Prompt", "I manage a [type] business using Google Workspace. Analyse my Gmail inbox patterns and create: 1) An email triage system that labels emails by priority (urgent/important/FYI/promotional), 2) Template responses for my 10 most common email types, 3) A weekly summary of unresolved action items. Also create a Sheets formula dashboard that tracks my response time and email volume by day."),
    ("Long Document Analysis", "I'm uploading a 500-page industry report. After reading the full document: 1) Write a 1-page executive summary, 2) Extract all specific data points with their page numbers, 3) Identify the 3 most actionable insights for a startup in this space, 4) List any claims that seem contradicted by other parts of the document, 5) Suggest 5 follow-up research questions this report raises but doesn't answer."),
  ],
  'stack': ["ChatGPT (creative tasks)", "Perplexity (web research)", "Google AppScript (automation)", "Looker Studio (dashboards)", "BigQuery (data analysis)", "Google Ads (marketing)"],
  'insights': [
    ("google-logo", "The Workspace Moat", "If a client already pays for Google Workspace, they have Gemini and don't know it yet. You can charge $2K–$5K to unlock that value for them."),
    ("file-doc", "1M Context Is Unprecedented", "No other model comes close to Gemini's context window for production use. For legal due diligence, academic research, and enterprise document analysis, this is the only tool."),
    ("chart-pie", "Google Stack Clients Pay Premium", "Companies built on Google Workspace (most SMBs and enterprises) will pay premium for Gemini-native workflows. They don't want to migrate tools — they want their existing tools to work smarter."),
  ],
  'facts': {"Pricing": "Free → $20/mo", "Best Model": "Gemini 2.0 Ultra", "Skill Level": "Beginner", "Context Window": "1M tokens", "Time to Revenue": "3 days"},
  'warnings': ["Gemini's creative writing quality lags behind Claude for nuanced, long-form content. Use Gemini for research, analysis, and structured tasks; use Claude for writing."],
  'tips': ["Upload documents directly in Gemini rather than copy-pasting. It processes the full document structure, including tables and charts, far better than pasted text."],
}

# ─────────────────────────────────────────────
# 17. MAKE
# ─────────────────────────────────────────────
CONTENT['make'] = {
  'what_it_is': "Make (formerly Integromat) is a visual automation platform that connects apps and automates workflows with a drag-and-drop interface. It handles 1,000+ app integrations, complex multi-step logic, and runs 24/7. The business model: build automation systems for clients and charge monthly retainers. The market is enormous and most businesses have zero automation.",
  'money_streams': [
    ("Client Automation Retainers", "$500–$3K/mo per client", "Build one automation system per client, then charge monthly to 'maintain and optimise' it. 5 clients = $2.5K–$15K MRR.", "2 weeks to first client"),
    ("Lead Generation Automations", "$1K–$5K per build", "Build lead gen pipelines: scrape leads → enrich → personalise email → send → log to CRM. One-time setup fee + retainer.", "1–2 weeks per build"),
    ("E-commerce Automation", "$1K–$4K per build", "Connect Shopify/WooCommerce to inventory, accounting, shipping, and customer service. Every e-commerce store needs this.", "1–2 weeks"),
    ("Make Template Store", "$100–$2K/mo passive", "Build reusable automation templates and sell them on Make's marketplace or Gumroad.", "1 month to build catalogue"),
  ],
  'steps': [
    ("Sign Up", "Go to make.com. Free plan gives 1,000 ops/mo — enough to build and demo. Core plan ($10/mo) for client work.", ""),
    ("Understand Scenarios", "In Make, automations are called 'Scenarios'. Each Scenario has a trigger (what starts it) and actions (what it does). Think of it as an automated assembly line.", ""),
    ("Build Your First Scenario", "Click 'Create a new scenario'. Pick a trigger app (e.g. Gmail — new email). Add an action module (e.g. Slack — send message). Connect them. Test.", ""),
    ("Add Filters & Logic", "Between modules, add filters (only proceed if email is from domain X), routers (split workflow based on conditions), and iterators (process lists).", ""),
    ("Use the AI Module", "Make has a native AI module. Drop it in any scenario to add intelligent processing: classify emails, extract data from unstructured text, generate responses.", ""),
  ],
  'prompts': [
    ("Client Pitch Template", "You are selling automation services to small businesses. Write a 3-paragraph email pitch for [business type] explaining: 1) The specific manual tasks they are wasting 5–10 hours/week on (be specific to their industry), 2) How an automation system eliminates those tasks permanently, 3) Your offer: a 30-minute audit call where you identify their top 3 automation opportunities at no cost. Subject line options (give 3). Tone: direct, peer-to-peer, not salesy."),
    ("Automation Spec Brief", "I need to document this automation for a client proposal. The automation: [describe what it does]. Please write: 1) A plain-English description (non-technical), 2) Step-by-step flow diagram in text format, 3) Business value statement (time saved, errors eliminated, revenue impact), 4) Implementation timeline estimate, 5) Monthly maintenance tasks that justify a $500/mo retainer."),
  ],
  'stack': ["Airtable (data layer)", "OpenAI API (intelligence)", "Slack (notifications)", "Google Sheets (reporting)", "Stripe (billing)", "Notion (documentation)"],
  'insights': [
    ("infinity", "The Retainer Is the Business", "One well-built automation for a client creates a dependency. They can't easily turn it off — and they don't want to. That's your retainer for life."),
    ("wrench", "Start With Pain, Not Features", "The best automations solve something that annoys a business owner every single day. Ask: 'What do you do manually that you hate?' That's your first scenario."),
    ("chart-line-up", "Stack Clients in the Same Niche", "Build the same automation for 5 restaurants or 5 real estate agents. You do the work once (with variations) and charge 5 separate retainers."),
  ],
  'facts': {"Pricing": "Free → $16/mo+", "Integrations": "1,000+ apps", "Skill Level": "Intermediate", "Logic": "Visual drag-and-drop", "Time to Revenue": "2 weeks"},
  'warnings': ["Make scenarios can fail silently if not monitored. Always set up error handlers and Slack/email alerts for client automations — downtime damages your retainer relationship."],
  'tips': ["Use Make's 'Templates' section for inspiration on every new client. There's almost certainly a pre-built template for their industry that you can customise in 30 minutes."],
}

# ─────────────────────────────────────────────
# 18. N8N
# ─────────────────────────────────────────────
CONTENT['n8n'] = {
  'what_it_is': "n8n is the open-source, self-hostable automation platform that developer-minded builders use instead of Make or Zapier. Self-hosting means zero per-run costs at scale, full data privacy, and the ability to write custom JavaScript/Python nodes. The developer market pays premium for this — because they trust it.",
  'money_streams': [
    ("Self-Hosted Automation Service", "$3K–$15K/mo", "Host n8n for clients on their own servers or your VPS. They pay for setup + monthly management. Data stays in their environment.", "2–3 weeks to set up"),
    ("AI Agent Pipelines", "$2K–$8K per build", "Build autonomous AI agents using n8n's AI nodes — multi-step reasoning, tool use, memory. Sell to tech-savvy companies.", "1–2 weeks per build"),
    ("Developer Tool Integrations", "$5K–$20K per project", "Companies need n8n to integrate internal tools, databases, and custom APIs. This is high-value consultant work.", "Per project"),
    ("n8n Template Marketplace", "$500–$3K/mo passive", "Sell n8n workflow templates to the community. Complex AI workflows with 50+ nodes sell for $50–$200 each.", "1 month to catalogue"),
  ],
  'steps': [
    ("Self-Host on a VPS", "Get a $6/mo Hetzner or DigitalOcean VPS. Install n8n via Docker. Own your infrastructure. Client trust goes up, your costs go down.", "# Install Docker\ncurl -fsSL https://get.docker.com | sh\n\n# Run n8n with Docker\ndocker run -it --rm \\\n  --name n8n \\\n  -p 5678:5678 \\\n  -v ~/.n8n:/home/node/.n8n \\\n  n8nio/n8n\n\n# Access at http://localhost:5678"),
    ("Set Up with Docker Compose (Production)", "For production, use Docker Compose with Postgres, proper volumes, and nginx reverse proxy.", "# docker-compose.yml\nversion: '3.8'\nservices:\n  n8n:\n    image: n8nio/n8n\n    restart: always\n    ports:\n      - '5678:5678'\n    environment:\n      - N8N_HOST=your-domain.com\n      - N8N_PORT=5678\n      - WEBHOOK_URL=https://your-domain.com/\n      - DB_TYPE=postgresdb\n      - DB_POSTGRESDB_HOST=postgres\n    volumes:\n      - n8n_data:/home/node/.n8n\n  postgres:\n    image: postgres:15\n    restart: always\n    environment:\n      - POSTGRES_USER=n8n\n      - POSTGRES_PASSWORD=your-password\n      - POSTGRES_DB=n8n"),
    ("Build Your First AI Agent", "Use n8n's AI Agent node with an OpenAI or Anthropic model. Add tools (web search, database queries, email send). Connect memory. You have a working AI agent.", ""),
    ("Connect Custom APIs", "n8n has an HTTP Request node that connects to any API — even undocumented ones. Pair it with the Code node for custom JavaScript logic.", ""),
    ("Export & Share Workflows", "Export workflows as JSON. Share on the n8n community forum or sell on Gumroad. Complex multi-agent workflows sell for $50–$300.", ""),
  ],
  'prompts': [
    ("AI Agent Brief", "Design an n8n workflow for an AI email assistant. Requirements: 1) Trigger: new Gmail email arrives, 2) AI reads and classifies email (urgent/standard/promotional/spam), 3) For urgent: draft a reply using company context from Notion, send for human approval via Slack, 4) For standard: draft reply, auto-send after 30-min delay if no human edit, 5) Log all interactions to Airtable. Give me the complete node list and connections."),
  ],
  'stack': ["Docker (deployment)", "PostgreSQL (persistence)", "OpenAI API (intelligence)", "GitHub (workflow backup)", "Nginx (proxy)", "Cloudflare (SSL/DNS)"],
  'insights': [
    ("shield-check", "Self-Hosting Is Your Differentiator", "Most competitors use Make's cloud. You host n8n on client infrastructure. Data privacy sells itself to any company with compliance requirements."),
    ("code-block", "The Code Node Is Unlimited Power", "n8n's Code node lets you write any JavaScript or Python. There is no automation you cannot build. This is why developers choose n8n over everything else."),
    ("currency-dollar", "Scale Pricing With Infrastructure", "Start with shared hosting at $200/mo. As clients grow, upsell to dedicated instances at $500/mo. The infrastructure scales, so does your recurring revenue."),
  ],
  'facts': {"Pricing": "Free (self-host) / $24/mo cloud", "Language": "JavaScript/Python nodes", "Skill Level": "Intermediate", "Deploy": "Docker/VPS", "Time to Revenue": "2–3 weeks"},
  'warnings': ["Self-hosting means you are responsible for uptime, backups, and security. Set up automated daily backups and monitoring (UptimeRobot is free) before taking on clients."],
  'tips': ["The n8n community forum (community.n8n.io) has thousands of pre-built workflows. Search there before building from scratch — someone has almost certainly solved your problem."],
}

# ─────────────────────────────────────────────
# 19. ZAPIER
# ─────────────────────────────────────────────
CONTENT['zapier'] = {
  'what_it_is': "Zapier is the most widely-adopted automation tool in the world — over 7,000 app integrations and a non-technical interface that any business owner can understand. For automation service providers, this is your gateway to the SMB market. Clients trust the name, can see what it does, and will pay for someone to set it up right.",
  'money_streams': [
    ("Zapier Setup Service", "$500–$3K per setup", "Build Zap systems for small businesses — CRM to email, form to Slack, Stripe to Google Sheets. One-time setup fee.", "1 week to first client"),
    ("Retainer Management", "$200–$1K/mo per client", "Manage a client's Zapier account: troubleshoot, optimise, add new Zaps monthly. 10 clients = $2K–$10K MRR.", "Recurring from setup clients"),
    ("Zapier + AI Workflows", "$1K–$5K per build", "Integrate ChatGPT or Claude into Zapier workflows. Build smart automations that think — not just route data.", "1–2 weeks"),
    ("Templates & Playbooks", "$100–$1K per package", "Package your best Zapier setups as templates with documentation. Sell on Gumroad or Etsy.", "1 month to build"),
  ],
  'steps': [
    ("Create Zapier Account", "Go to zapier.com. Free tier gives 5 Zaps with 100 tasks/mo — enough to demo. Starter plan ($20/mo) for client work.", ""),
    ("Understand the Zap Structure", "Every Zap has a Trigger (something happens in App A) and one or more Actions (do something in App B). That's the entire model.", ""),
    ("Build a High-Value Demo Zap", "Build this Zap to demonstrate value: New Typeform submission → Enrich with Clearbit → Add to HubSpot CRM → Send personalised email via Gmail → Notify team in Slack. That's 5 actions from one trigger.", ""),
    ("Add ChatGPT to Zaps", "Add the 'ChatGPT' action anywhere in your Zap. Pass data to it, get intelligent output back, use that output in the next step.", ""),
    ("Use Tables & Interfaces", "Zapier Tables is a database. Interfaces is a form builder. Together with Zaps, they form a complete no-code platform — not just automation.", ""),
  ],
  'prompts': [
    ("Zapier Audit Script", "I'm auditing a small business's Zapier setup. They currently have [number] Zaps doing [describe current automations]. Their business type is [type]. Identify: 1) Likely inefficiencies in their current setup, 2) Top 5 additional Zaps they should have based on their industry, 3) Any Zaps that could be combined to save on task usage, 4) AI-powered Zap ideas using ChatGPT integration that would give them a competitive edge. Output as a structured audit report I can present to the client."),
  ],
  'stack': ["Make (complex logic)", "Airtable (database)", "HubSpot (CRM)", "Gmail (email)", "Slack (team)", "Stripe (payments)"],
  'insights': [
    ("users-three", "SMBs Are Underserved", "Every small business owner knows Zapier exists. Almost none have it set up properly. You are solving a known problem. That makes selling easy."),
    ("briefcase", "Package Your Service", "Don't sell hours. Sell 'The Ecommerce Automation Pack' for $1,500 or 'The Real Estate Lead Machine' for $2,000. Named packages close faster than hourly quotes."),
    ("arrow-up-right", "Start With Typeform to CRM", "The most common, highest-value Zap: new lead form submission → personalised email → CRM → Slack alert. This one workflow justifies your entire fee for most clients."),
  ],
  'facts': {"Pricing": "Free → $29/mo+", "Integrations": "7,000+ apps", "Skill Level": "Beginner", "Logic": "Visual no-code", "Time to Revenue": "1 week"},
  'warnings': ["Zapier's task-based pricing means costs scale with volume. For high-volume automations (10,000+ tasks/mo), Make or n8n become significantly cheaper."],
  'tips': ["Always turn on error notifications for client Zaps. When something breaks, you want to know before they do. Being proactive keeps retainers alive."],
}

# ─────────────────────────────────────────────
# 20. NOTEBOOKLM
# ─────────────────────────────────────────────
CONTENT['notebooklm'] = {
  'what_it_is': "NotebookLM is Google's AI research assistant that reads your documents and becomes an expert on them. Upload PDFs, Google Docs, URLs, and YouTube videos — NotebookLM synthesises, answers questions, and most uniquely, generates lifelike podcast-style audio discussions of your content. It's the fastest way to turn raw documents into monetisable products.",
  'money_streams': [
    ("Research Product Service", "$500–$3K per product", "Transform dense reports, books, or data into NotebookLM-powered interactive briefs. Sell to professionals who need fast insight.", "1 week to first product"),
    ("AI Podcast Production", "$500–$2K per episode", "Use NotebookLM's audio overview to generate two-host podcast conversations about any topic. Edit and publish. Zero recording required.", "3–5 days to first episode"),
    ("Corporate Knowledge Tools", "$2K–$8K per setup", "Upload a company's entire knowledge base into NotebookLM. Give teams an AI expert on company policy, products, and processes.", "2 weeks per client"),
    ("Study Materials Business", "$100–$500/mo", "Create NotebookLM notebooks from textbooks and course materials. Sell study memberships to students preparing for exams.", "2–4 weeks"),
  ],
  'steps': [
    ("Create a Notebook", "Go to notebooklm.google.com. Create a new notebook. Upload your sources — PDF, Google Doc, URL, YouTube video, or paste text. Up to 50 sources.", ""),
    ("Ask Research Questions", "In the chat panel, ask anything about your sources. NotebookLM cites the exact location in the source for every claim. Trust but verify.", ""),
    ("Generate Audio Overview", "Click 'Audio Overview' in the sidebar. Two AI hosts discuss your sources in a natural, engaging 8–15 minute podcast conversation. Download the MP3.", ""),
    ("Use the Study Guide Feature", "Ask NotebookLM to 'generate a study guide', 'create a FAQ', or 'list the key arguments'. These outputs are the raw material for your sellable products.", ""),
    ("Share Notebooks", "NotebookLM notebooks can be shared with a link. Recipients interact with your curated source material. This is your product delivery mechanism.", ""),
  ],
  'prompts': [
    ("Research Product Creation", "I've uploaded [document type] about [topic]. Based only on these sources: 1) Write a 500-word executive brief for a senior business audience (no jargon), 2) Create a 10-question FAQ with precise answers, 3) Identify the 5 most counterintuitive findings, 4) Generate 3 discussion questions suitable for a board-level meeting, 5) Write a one-paragraph summary I could send as a text message. For each section, cite the specific source document and location."),
    ("Podcast Script Direction", "Generate an Audio Overview of these sources. Frame the discussion as two analysts debating: one optimistic about the opportunities, one sceptical about the risks. Make it conversational and energetic, suitable for a business podcast audience. Ensure specific data points from the documents are referenced naturally in conversation."),
  ],
  'stack': ["Descript (audio editing)", "Beehiiv (newsletter)", "Gumroad (sell notebooks)", "Claude (expand briefs)", "Riverside.fm (podcast host)", "Canva (cover art)"],
  'insights': [
    ("microphone-stage", "Audio Overview Is Unique", "No other tool generates a two-host podcast discussion of your documents. This is a genuinely unique output that clients can't easily replicate themselves."),
    ("building-library", "Knowledge Products Are Scalable", "Create one NotebookLM notebook from a valuable source. Share it 1,000 times. The marginal cost is zero. That's the business model."),
    ("graduation-cap", "The Education Market Pays", "Students preparing for the CPA, bar exam, GMAT, or professional certifications will pay for well-organised AI study tools. NotebookLM is the perfect production engine."),
  ],
  'facts': {"Pricing": "Free (Google account)", "Sources": "Up to 50 per notebook", "Skill Level": "Beginner", "Audio": "Yes — podcast format", "Time to Revenue": "3 days"},
  'warnings': ["NotebookLM only synthesises what you give it — it doesn't search the web. For current events or real-time data, always supplement with Perplexity."],
  'tips': ["Upload the most authoritative, dense documents you can find (annual reports, academic papers, official whitepapers). NotebookLM's quality directly reflects the quality of your sources."],
}
