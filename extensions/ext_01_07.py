# Extensions batch 1: tools 01-07 (base44, claudecode, cursor, lovable, windsurf, midjourney, runway)
# Each tool gets: use_cases[], more_streams[], niche_table[], pricing_tiers[], client_script, extra_prompts[], advanced_steps[]

EXT = {}

EXT['base44'] = {
  'use_cases': [
    ("Freelance SaaS Builder", "A developer charges $5K to build a client portal for a marketing agency. Uses Base44 entities for campaigns, clients, and invoices. Delivered in 4 days. Client pays $300/mo retainer to maintain it. Total year-1 revenue: $8,600 from one client."),
    ("Whop Tool Creator", "A community operator builds a member analytics dashboard for a fitness coach's Whop community — engagement scores, churn alerts, weekly briefs. Sells access for $99/mo. Signs 12 Whop creators in 3 months = $1,188 MRR."),
    ("Internal Tool Agency", "Targets small law firms with a case management app built on Base44. Charges $3,500 setup + $250/mo. Closes 3 firms in month one = $750 MRR + $10,500 upfront."),
    ("No-Code Consultant", "Teaches non-technical founders to build their own MVPs on Base44. Runs a $497 workshop. 20 attendees/month = $9,940/mo from education alone."),
    ("Automation + App Bundle", "Pairs Base44 with Make automations. Sells 'AI Business OS' packages — a custom app + 5 automations — for $4,000 flat. Delivers in 1 week. Runs 2 projects/month."),
  ],
  'more_streams': [
    ("White-Label App Reselling", "$500–$2K/mo", "Build one app template (e.g. client portal), white-label it for multiple clients with minor customisation. Sell the same base 10x."),
    ("SaaS Product Launch", "$1K–$20K MRR", "Build your own product on Base44, launch on Product Hunt or AppSumo. Base44 handles auth, database, and hosting — you focus on the idea."),
  ],
  'niche_table': [
    ("Legal / Law Firms", "Case tracking, client portals", "$3K–$8K setup + $300/mo"),
    ("Real Estate Agents", "Lead CRM, deal pipeline", "$2K–$5K setup + $200/mo"),
    ("Fitness Coaches", "Client check-ins, program tracker", "$1K–$3K setup + $150/mo"),
    ("Marketing Agencies", "Campaign dashboards, client reports", "$3K–$6K setup + $250/mo"),
    ("E-commerce Stores", "Inventory + order management", "$2K–$5K setup + $200/mo"),
  ],
  'pricing_tiers': [
    ("Starter", "$1,500", "1 entity, 1 page dashboard, basic automations. Delivered in 3 days."),
    ("Business", "$3,500", "Full app (5+ entities, 5 pages, 3 automations, email integration). 1 week."),
    ("Agency OS", "$6,500", "Complete business OS (CRM + projects + invoicing + client portal + Slack alerts). 2 weeks."),
    ("Monthly Retainer", "$200–$500/mo", "Maintenance, new feature additions, bug fixes. Billed after initial project."),
  ],
  'client_script': "DM (Twitter/LinkedIn):\n\nHey [Name] — noticed you're running [their business type]. Quick question: how are you currently tracking [specific pain point — e.g. client projects / inventory / leads]?\n\nI build custom AI-powered dashboards that replace spreadsheets and Notion docs for [industry] businesses. Usually takes me 3-5 days to ship.\n\nWould a 15-min call be worth it to show you what I built for [similar business]?",
  'extra_prompts': [
    ("Advanced CRM Build", "Build a full CRM for a [industry] business. Entities needed: Contact (name, email, phone, company, status: lead/prospect/client/churned, lifetime_value, source), Deal (contact_id, title, value, stage: discovery/proposal/negotiation/closed_won/closed_lost, close_date, notes), Activity (contact_id, deal_id, type: call/email/meeting/demo, notes, date, outcome). Dashboard page: total pipeline value, deals by stage (kanban view), contacts added this week, overdue follow-ups. Add an automation: when a deal moves to closed_won, send a congratulations email to the contact and notify the team via Slack."),
    ("Client Reporting Automation", "Build a weekly report automation for an agency. Every Monday at 9am, the agent should: 1) Query all active client entities, 2) For each client, calculate their metrics for the past 7 days (tasks completed, hours logged, budget used), 3) Generate a personalised email summary for each client using their data, 4) Send each email via Gmail, 5) Log the send in a ReportLog entity. The agent should handle errors gracefully and notify me on Slack if any client email fails."),
    ("Pricing Page for Your App", "I've built a [describe app] on Base44 and want to monetise it. Design a 3-tier pricing structure: Free tier (limited features to drive signups), Pro tier ($X/mo — core value), Agency tier ($Y/mo — power users). For each tier list: feature inclusions, usage limits, target customer, and the psychological reason this tier exists in the funnel. Then write the pricing page copy for each tier (name, price, subtitle, 5 bullet features, CTA button text)."),
  ],
  'advanced_steps': [
    ("Set Up Row-Level Security", "Enable RLS on customer-facing entities so each user only sees their own data. Go to entity settings → enable RLS. Combine with the User entity for per-user data isolation — critical before going live with any paying customers."),
    ("Connect Stripe for Billing", "Use the Stripe backend function skill to add subscription billing. Deploy a checkout function, create a webhook handler for payment events, and update your User entity's subscription_status field automatically on successful payment."),
    ("Build an Onboarding Flow", "Add a multi-step onboarding wizard as your app's first page. New users complete it once — it populates their profile entity and triggers a welcome automation. Onboarded users convert to paying at 3–5x the rate of users who skip setup."),
  ],
}

EXT['claudecode'] = {
  'use_cases': [
    ("Legacy Modernisation Agency", "Targets companies with Python 2 or PHP 4/5 codebases. Charges $15K–$40K to modernise. Claude Code handles the refactor while you manage the client and do QA. 2–3 projects running simultaneously = $30K–$120K/quarter."),
    ("Freelance Full-Stack Dev", "Takes on Next.js + Supabase projects at $100–$150/hr. Claude Code makes them 4x faster than before. Effectively earning $400–$600/hr of value delivered per hour worked."),
    ("Open Source to SaaS", "Forks popular open-source tools, adds a premium hosted version with billing and auth. Claude Code builds the SaaS wrapper. Charges $19–$99/mo. 200 subscribers = $4K–$20K MRR."),
    ("Bug Bounty Hunter", "Uses Claude Code to systematically audit open source codebases for CVEs. Files responsible disclosures and collects bounties of $500–$10K per valid finding."),
    ("Internal Tools Contractor", "Works with companies that have growing engineering teams but no bandwidth for internal tooling. Builds admin dashboards, data pipelines, and developer tools at $150/hr using Claude Code."),
  ],
  'more_streams': [
    ("Code Review as a Service", "$500–$3K/review", "Audit a startup's codebase before a funding round or product launch. Claude Code spots every issue. You write the report and present findings."),
    ("Technical Co-Founder Placement", "$10K–$50K + equity", "Position yourself as a technical co-founder for non-technical founders. Claude Code lets you execute at senior engineer speed from day one."),
  ],
  'niche_table': [
    ("FinTech Startups", "Secure API integrations, trading logic", "$150–$250/hr"),
    ("SaaS Companies", "Feature builds, performance optimisation", "$100–$200/hr"),
    ("E-commerce", "Custom Shopify/WooCommerce integrations", "$80–$150/hr"),
    ("Healthcare Tech", "HIPAA-compliant data pipelines", "$150–$300/hr"),
    ("Agencies", "White-label app development", "$5K–$20K/project"),
  ],
  'pricing_tiers': [
    ("Code Review", "$500–$1,500", "Full codebase audit — security, performance, quality. Delivered as a report in 48 hours."),
    ("Feature Sprint", "$2,000–$5,000", "One focused feature built, tested, and deployed. Fixed price, 1-week delivery."),
    ("Monthly Retainer", "$5,000–$15,000/mo", "Dedicated development — 40–80 hours/month. Weekly check-ins, continuous delivery."),
    ("Project Build", "$10,000–$40,000", "Full product from spec to launch. Milestone-based payments."),
  ],
  'client_script': "Cold Email:\n\nSubject: [Company] — saw your [GitHub repo / job posting / product]\n\nHi [Name],\n\nI came across [specific thing about their company] and noticed [specific technical challenge — e.g. you're hiring 3 backend engineers / your checkout has a known performance issue / your API docs mention the migration you're planning].\n\nI'm a full-stack developer specialising in [their stack]. I've been using AI-assisted development tools that let me ship at 3–4x the normal pace — which means you get senior-quality code at a fraction of the timeline.\n\nI have capacity starting [date]. Worth a 20-minute call to see if there's a fit?\n\n[Your name]",
  'extra_prompts': [
    ("Full Project Brief", "I'm starting a new project. Here's the spec: [paste spec]. Before writing any code: 1) Review the spec and identify any ambiguities or missing requirements, 2) Propose the tech stack with justification for each choice, 3) Create the folder structure, 4) List the first 5 tasks in priority order, 5) Identify any security considerations I should address from day one. Then wait for my confirmation before proceeding."),
    ("Performance Audit", "Audit this codebase for performance issues. Check: 1) Database query patterns — N+1 queries, missing indexes, unoptimised joins, 2) API response times — unnecessary computation, missing caching, 3) Frontend bundle size — unused imports, missing code splitting, 4) Memory leaks — event listeners not cleaned up, large objects in closure scope, 5) Third-party dependency bloat. For each issue found, estimate the performance impact (ms saved, % improvement) and provide the fix."),
    ("Test Suite Generation", "Generate a comprehensive test suite for this codebase. Include: 1) Unit tests for all business logic functions (100% coverage target), 2) Integration tests for all API endpoints (happy path + error cases), 3) Edge case tests for any data validation functions, 4) A mock strategy for all external services (database, email, third-party APIs). Use [Jest/Pytest/whichever is appropriate]. Write tests that are readable as documentation — not just passing assertions."),
  ],
  'advanced_steps': [
    ("Master the CLAUDE.md File", "Create a CLAUDE.md in your project root. Include: tech stack, coding conventions, business domain glossary, architecture decisions, and things Claude should never do (e.g. 'never use any type', 'always add error handling'). This file is read every session — it's the difference between consistent quality and inconsistent output."),
    ("Use Parallel Workstreams", "For large projects, open multiple Claude Code sessions simultaneously in different terminals — one working on frontend, one on backend, one on tests. They work in parallel. Merge via git. This multiplies your throughput further."),
    ("Build a Cost Tracker", "Claude Code uses Anthropic API credits. For large projects, track your spend with: claude --print-cost. Set a daily budget. For client work, factor API costs into your project price (usually $5–$30/project at typical usage)."),
  ],
}

EXT['cursor'] = {
  'use_cases': [
    ("10x Freelancer", "A mid-level developer uses Cursor to take on senior-level contracts at $150/hr. Previously billed 20 hours/week at $75/hr ($6K/mo). Now bills 30 hours/week at $150/hr ($18K/mo) — same effort, 3x revenue."),
    ("SaaS Co-Founder", "A non-technical founder partners with a Cursor-powered developer. They ship an entire MVP — auth, dashboard, Stripe billing, email — in 2 weeks instead of 3 months. Raises a pre-seed round."),
    ("Refactor Specialist", "Targets companies with messy codebases that their team is afraid to touch. Charges $5K–$15K to clean up technical debt using Cursor's multi-file Composer. Delivers in 1–2 weeks."),
    ("Developer Educator", "Creates a 'Cursor Mastery' course teaching developers the keyboard shortcuts, .cursorrules patterns, and multi-file workflows. Sells for $197 on Gumroad. 500 students = $98,500."),
    ("Agency Tech Lead", "Joins a marketing agency as a part-time tech lead at $5K/mo. Uses Cursor to handle all their development needs — landing pages, integrations, custom tools — in 2–3 hours per day."),
  ],
  'more_streams': [
    ("Cursor Workflow Consulting", "$2K–$8K/engagement", "Teach development teams how to adopt AI-assisted workflows. Run 2-day workshops for engineering teams. High demand from companies trying to 'do more with less'."),
    (".cursorrules Marketplace", "$50–$500/template", "Create and sell battle-tested .cursorrules files for specific stacks (Next.js + Tailwind, Django + DRF, React Native). Developers pay for instant productivity gains."),
  ],
  'niche_table': [
    ("Next.js / React", "Frontend and full-stack web apps", "$100–$200/hr"),
    ("Python / Django", "Backend APIs, data pipelines", "$90–$180/hr"),
    ("React Native", "Mobile app development", "$120–$220/hr"),
    ("Solidity / Web3", "Smart contracts, dApps", "$150–$350/hr"),
    ("Data Engineering", "ETL pipelines, analytics", "$120–$200/hr"),
  ],
  'pricing_tiers': [
    ("Hourly Contract", "$100–$200/hr", "For ongoing clients who need flexible capacity. Bill in 2-hour minimum blocks."),
    ("Sprint Package", "$3,000–$8,000", "One focused sprint — one major feature or module. Fixed scope, fixed price, 1-week delivery."),
    ("Monthly Tech Partner", "$5,000–$15,000/mo", "Ongoing development partner. 40–80 hours/month, weekly calls, continuous delivery."),
    ("Workshop", "$2,000–$5,000", "2-day Cursor workflow workshop for dev teams. Includes .cursorrules templates and playbook."),
  ],
  'client_script': "LinkedIn DM:\n\nHey [Name] — I saw [Company] is hiring [X engineers]. Congrats on the growth.\n\nI work with engineering teams going through scaling phases — not as a full-time hire but as a development partner. I cover [their stack] and typically operate at 3–4x the output of a traditional contractor because of how I work.\n\nIf your team has a backlog of features that keeps slipping, worth 15 minutes?\n\nNo pitch deck, just a conversation.",
  'extra_prompts': [
    ("Codebase Onboarding", "@codebase I'm new to this project. Give me a complete onboarding document: 1) Architecture overview — what are the main modules and how do they relate? 2) Data flow — how does data move from the user to the database and back? 3) The 5 most important files I need to understand first and why, 4) Current known issues or TODOs in the codebase, 5) Development workflow — how do I run locally, run tests, and deploy? Write this as if you're a senior engineer handing off to a new team member."),
    ("Feature from Spec", "I need to implement [feature name]. Spec: [paste spec]. Before coding: 1) Identify which existing files will be modified, 2) List any new files to be created, 3) Flag any potential conflicts with existing code, 4) Estimate complexity (hours). Then implement the feature following the existing code patterns in this project. Add tests. Update any relevant documentation."),
    ("Composer Multi-File Refactor", "Using Composer: Refactor the authentication system across this entire codebase. Current state: [describe]. Target state: [describe]. Requirements: 1) Zero breaking changes to the public API, 2) All existing tests must pass after refactor, 3) Add new tests for any new logic, 4) Update all imports across all affected files, 5) Add a CHANGELOG entry documenting what changed and why. Show me the full plan before executing."),
  ],
  'advanced_steps': [
    ("Build a Personal .cursorrules Library", "Maintain a GitHub repo of your best .cursorrules files for each stack you work in. Start a new project by copying the relevant rules file. This gives you instant consistency and quality across all projects — and you can sell these files."),
    ("Use Cursor Notepads for Context", "Cursor's Notepads (Cmd+Shift+P → 'Open Notepad') let you store persistent context that you can reference in any chat with @notepad. Create notepads for: client requirements, API docs, business logic rules. Drop them into any conversation instantly."),
    ("Combine Cursor + Claude Code", "Use Cursor for visual, interactive development. Use Claude Code in a parallel terminal for longer, autonomous tasks. The combination: Cursor for features you're actively shaping, Claude Code for background tasks (test writing, documentation, refactors) running while you code."),
  ],
}

EXT['lovable'] = {
  'use_cases': [
    ("MVP Factory", "Runs a 'MVP in 48 Hours' service for non-technical founders. Charges $2,500 flat. Gets 4–6 clients/month from Twitter/X outreach. Revenue: $10K–$15K/mo. Uses the same Lovable + Supabase template each time with customisation."),
    ("Landing Page Sprint", "Builds high-converting landing pages for online course creators and coaches. Charges $800–$1,500. Delivers same day. Runs 8–12 projects/month. Revenue: $6.4K–$18K/mo."),
    ("SaaS Validator", "Builds a working demo of any SaaS idea in 4–8 hours. Sells 'Validation Packages' to founders: working app + 10 beta user signups + feedback report for $3,000. Accelerator cohorts are a prime market."),
    ("Investor Demo Builder", "Founders need working prototypes for Y Combinator and demo days, not wireframes. Charges $1,500–$5,000 for a polished Lovable app that they can demo live. 2–3 per month."),
    ("Non-Technical Co-Founder", "Uses Lovable to build the entire product solo while the other co-founder handles sales. Shipped a complete SaaS product, got first paying customers, before raising a seed round."),
  ],
  'more_streams': [
    ("Lovable Templates Marketplace", "$200–$1,500/template", "Build polished, reusable Lovable starter templates for specific industries (booking app, job board, feedback tool). Sell on Gumroad. Download once, sell infinitely."),
    ("No-Code Course", "$197–$997", "Teach non-technical founders how to build their own apps on Lovable. Bundle with a template library. Sell on Gumroad or Teachable."),
  ],
  'niche_table': [
    ("SaaS Founders", "MVPs, demo apps, investor prototypes", "$1,500–$5,000/project"),
    ("Coaches & Course Creators", "Booking pages, member portals, content hubs", "$800–$2,000/project"),
    ("Local Businesses", "Booking systems, customer portals", "$600–$1,500/project"),
    ("Agencies", "Client-facing portals, reporting dashboards", "$1,500–$4,000/project"),
    ("E-commerce", "Product showcases, pre-order pages", "$500–$1,500/project"),
  ],
  'pricing_tiers': [
    ("Landing Page", "$800", "Single-page site with email capture, features section, and CTA. Same day delivery."),
    ("MVP App", "$2,500", "Full working app — up to 5 pages, Supabase backend, auth, basic CRUD. 48-hour delivery."),
    ("Full Product", "$5,000", "Complete SaaS — multi-page, full auth, Stripe billing, custom domain. 1-week delivery."),
    ("Rush Fee", "+$500", "Same-day delivery guarantee. Applies to any tier."),
  ],
  'client_script': "Twitter/X DM:\n\nHey [Name] — saw your tweet about [their idea/problem]. That's actually very buildable.\n\nI ship working apps in 48 hours for founders who need to move fast. Not wireframes — actual live products with a database and login.\n\nIf you want to see what I could build for you specifically, I can mock it up today for free so you can decide. No strings.\n\nWant me to take a shot at it?",
  'extra_prompts': [
    ("SaaS Dashboard Build", "Build a complete SaaS application for [specific use case]. The app needs: 1) Authentication (sign up, login, password reset, email verification), 2) Onboarding wizard (3 steps collecting key user preferences stored in their profile), 3) Main dashboard with [specific metrics and widgets], 4) Settings page (profile, notifications, billing), 5) Usage/billing page showing current plan and a Stripe checkout button for upgrading. Use shadcn/ui components throughout. Dark mode by default. Mobile responsive. Include loading states and empty states for every data view."),
    ("Conversion-Optimised Landing Page", "Build a high-converting landing page for [product]. Structure: 1) Hero — bold headline addressing the core pain point, sub-headline with the solution, email capture form with 'Get Early Access' CTA, 3 social proof logos or numbers, 2) Problem section — 3 pain points with icons, 3) Solution section — product demo GIF placeholder + 3 key benefits, 4) Social proof — 3 testimonial cards with avatar, name, role, 5) Pricing — 3 tiers (Free/Pro/Team), 6) FAQ — 5 questions, 7) Final CTA. A/B test version: swap hero CTA text to 'Start Free'."),
    ("Iteration Speed Prompt", "I have this existing Lovable app [describe current state]. I need to make it feel more premium and production-ready. Specific changes: 1) Replace all placeholder content with realistic demo data, 2) Add micro-animations to all interactive elements (hover states, button clicks, page transitions), 3) Add proper error states and loading skeletons to all data-fetching components, 4) Improve the empty states — add illustrations and helpful CTAs instead of just 'No data', 5) Add a keyboard shortcut system (Cmd+K command palette). Maintain all existing functionality."),
  ],
  'advanced_steps': [
    ("Always Export to GitHub", "After every Lovable project, export the full React codebase to GitHub immediately. This is your portfolio, your backup, and your ability to continue in Cursor if the project outgrows Lovable. Go to Settings → Export to GitHub. Do this after every session."),
    ("Stack Lovable with Supabase Edge Functions", "For complex backend logic (payment webhooks, scheduled jobs, third-party API calls), write Supabase Edge Functions. Lovable handles the frontend and basic CRUD; Edge Functions handle everything that needs to run server-side. This unlocks production-grade capabilities without leaving the Lovable ecosystem."),
    ("Build a Reusable Starter", "Create your personal Lovable starter template with your preferred design system, component library, auth setup, and folder structure. Duplicate it as the base for every new project. What used to take 4 hours of setup now takes 10 minutes."),
  ],
}

EXT['windsurf'] = {
  'use_cases': [
    ("Enterprise Refactor Specialist", "Targets companies with large, aging React class component codebases. Charges $15K–$30K to migrate to hooks and modern patterns using Windsurf's Cascade agent. Completes in 2–3 weeks. Clients save months of internal developer time."),
    ("Monorepo Architect", "Specialises in companies building monorepos with shared packages. Windsurf handles the cross-package dependencies and shared logic far better than other AI IDEs. Charges $200/hr for this niche expertise."),
    ("Full-Stack Solo Founder", "Builds a developer tool SaaS using Windsurf. Ships a complete product — backend, frontend, docs, and tests — in 6 weeks solo. Lists on Product Hunt. Gets 500 paid users in 3 months."),
    ("Migration Expert", "Offers REST-to-GraphQL and Redux-to-Zustand migrations. Windsurf understands the full dependency graph. Charges $8K–$20K per migration project. Clients are mid-stage startups with technical debt."),
    ("Code Quality Consultant", "Uses Windsurf to bring legacy enterprise codebases up to modern standards — TypeScript migration, test coverage from 0% to 80%, ESLint/Prettier setup, CI/CD pipelines. Charges day rates of $1,200–$2,000."),
  ],
  'more_streams': [
    ("Windsurf Workflow Training", "$2K–$6K/workshop", "Run 2-day training workshops for development teams adopting AI-assisted workflows. Windsurf's Cascade is complex enough that teams pay for expert guidance."),
    ("Technical Debt Bounty", "$5K–$25K/engagement", "Position as a 'technical debt specialist'. Audit a codebase, price the cleanup, execute with Windsurf. Enterprises have budgets specifically for this."),
  ],
  'niche_table': [
    ("React/TypeScript", "Component migrations, performance optimisation", "$150–$250/hr"),
    ("Node.js/Express", "API modernisation, microservices", "$130–$220/hr"),
    ("Python/FastAPI", "Backend rebuilds, async migration", "$120–$200/hr"),
    ("Monorepos (Nx/Turborepo)", "Architecture setup, package management", "$180–$300/hr"),
    ("Enterprise Java", "Spring Boot migration, modernisation", "$200–$350/hr"),
  ],
  'pricing_tiers': [
    ("Code Audit", "$1,500–$3,000", "Full codebase review with Windsurf. Delivered as a prioritised report. 48-hour turnaround."),
    ("Sprint Retainer", "$4,000–$8,000/sprint", "2-week focused sprint on one major goal (migration, feature, refactor). Daily updates."),
    ("Monthly Partner", "$8,000–$20,000/mo", "Embedded developer for 40+ hours/month. Slack access, weekly calls, async support."),
    ("Project", "$15,000–$50,000", "Full project scope. Milestone payments. Windsurf executes, you manage and deliver."),
  ],
  'client_script': "LinkedIn outreach:\n\nHi [Name] — I noticed [Company] has a [React class components / large Redux store / aging API] mentioned in your [job posting / GitHub / blog post].\n\nI specialise in modernising exactly this kind of codebase — and I complete these projects in weeks, not quarters, using AI-assisted development tools.\n\nI've helped [similar company type] go from [old state] to [new state] without disrupting their release cycle.\n\nWould it be useful to do a free 30-minute architectural review? I'll identify the top 3 risks and the fastest path to modernisation.",
  'extra_prompts': [
    ("Cascade Architecture Review", "Use Cascade to analyse this entire codebase. Produce: 1) Architecture diagram description (modules, dependencies, data flow), 2) Top 5 architectural anti-patterns with specific file/line references, 3) Coupling analysis — which modules are most tightly coupled and what's the blast radius of changing them, 4) A modernisation roadmap in 3 phases: Quick Wins (< 1 week), Structural Improvements (1–4 weeks), Strategic Refactors (1–3 months). For each item, estimate developer-days and risk level."),
    ("TypeScript Migration Plan", "This codebase is currently in JavaScript with zero type safety. Plan and execute a TypeScript migration: 1) Start with the tsconfig.json setup (strict mode, incremental compilation), 2) Migrate the utility functions first (lowest risk), 3) Add types to all API response interfaces, 4) Migrate React components file by file, starting with leaf components, 5) Address all 'any' types before completion. Track progress in a MIGRATION.md file. Never break the running application — use // @ts-nocheck as a temporary escape hatch only."),
    ("Test Coverage Sprint", "This codebase has 0% test coverage. In one sprint, bring it to 70%+. Strategy: 1) Set up Jest/Vitest with the correct config for this stack, 2) Write tests for all pure utility functions first (highest ROI), 3) Write integration tests for all API endpoints, 4) Write component tests for the 10 most complex UI components, 5) Set up a coverage report in CI that fails if coverage drops below 70%. Prioritise tests by business risk — test payment logic before UI styling."),
  ],
  'advanced_steps': [
    ("Configure Windsurf Memories", "Windsurf's Memories feature lets Cascade remember facts about your project across sessions. Go to Settings → Memories. Add your architecture decisions, coding standards, and client preferences. Cascade references these automatically — no need to re-explain context every session."),
    ("Use Cascade in Plan Mode First", "Before any large change, switch Cascade to Plan mode (the toggle in the Cascade panel). It will describe exactly what it intends to do without making any changes. Review the plan, refine it, then execute. This prevents unexpected sweeping changes and builds your mental model of what's happening."),
    ("Pair with Linear for Client Work", "Connect your Windsurf workflow to Linear (issue tracker). Each Cascade session tackles one Linear ticket. Cascade references the ticket description for context. When done, it marks the ticket complete. Clients see a professional, tracked delivery process."),
  ],
}

EXT['midjourney'] = {
  'use_cases': [
    ("Etsy Print Shop", "Runs a themed Etsy store — 'Dark Academia Wall Art'. Uses Midjourney to generate 200+ print designs in a consistent aesthetic. Lists 150 products. Makes $3K–$8K/mo passively after 3 months of setup."),
    ("Brand Asset Studio", "Offers brand mood board packages to startups and e-commerce brands. Delivers: 10 logo concepts, 20 brand photography mockups, 5 social media templates. Charges $800–$2,500. Delivers in 2 days."),
    ("Children's Book Publisher", "Self-publishes illustrated children's books on Amazon KDP. Midjourney creates all illustrations in a consistent style (saved as a custom style code). Each book costs ~$20 to produce. Books sell for $8–$15 and earn 70% royalty. Portfolio of 10 books earns $2K–$5K/mo passively."),
    ("Interior Design Visualiser", "Offers room visualisation packages for interior designers and real estate developers. Takes a room photo, recreates it in different styles using Midjourney img2img. Charges $200–$500 per room. Works with 5–10 designers."),
    ("Fashion Concept Designer", "Creates AI fashion concept lookbooks for indie clothing brands. Designs entire collection concepts — colourways, silhouettes, editorial photography — before a single garment is made. Charges $1,500–$4,000 per lookbook."),
  ],
  'more_streams': [
    ("Stock Photo Licensing", "$500–$3K/mo passive", "Upload AI-generated images to Adobe Stock, Shutterstock, and Getty. Niche subjects (obscure architecture, rare scenes, abstract concepts) earn consistent royalties with zero ongoing work."),
    ("NFT Art Collections", "$2K–$50K per drop", "Create thematic NFT collections using Midjourney with consistent style codes. Deploy on OpenSea or Magic Eden. Revenue depends heavily on marketing and community building."),
  ],
  'niche_table': [
    ("Home Decor (Etsy)", "Prints, wall art, posters", "$500–$5K/mo passive"),
    ("Brand Identity", "Logo concepts, mood boards, photography", "$800–$3K/project"),
    ("Book Covers", "Fiction, self-help, children's books", "$200–$800/cover"),
    ("Social Media Content", "Post graphics, story templates, ads", "$500–$2K/mo retainer"),
    ("Architecture/Real Estate", "Renders, visualisations, concepts", "$500–$2K/project"),
  ],
  'pricing_tiers': [
    ("Single Image Pack", "$50–$200", "10 high-res images in a specific style. Delivered in 24 hours."),
    ("Brand Mood Board", "$400–$800", "30 curated images for brand direction. Delivered in 48 hours with usage rights."),
    ("Full Brand Package", "$1,500–$3,000", "Logo concepts + photography style + social media templates + colour palette. 3 days."),
    ("Monthly Content Pack", "$500–$1,500/mo", "50–100 images per month for social media and marketing use."),
  ],
  'client_script': "Instagram/LinkedIn DM:\n\nHey [Name] — love what you're building with [Brand]. Your visual content is solid but I noticed [specific gap — e.g. your product photography is inconsistent / you're using the same 3 stock photos everywhere].\n\nI create custom brand photography and concept art using AI tools — indistinguishable from premium studio photography. Turnaround is 24–48 hours and the images are entirely yours.\n\nI'll create 5 free sample images in your brand style today to show you what's possible. Want me to send them over?",
  'extra_prompts': [
    ("Consistent Product Style", "/imagine prompt: [product description] product photography, [specific background — e.g. white marble with gold accents], [lighting style — e.g. soft studio lighting with shadow detail], [camera — e.g. shot on Hasselblad], photorealistic, commercial quality, 8K --ar 1:1 --v 6 --style raw --sref [your style URL for consistency]"),
    ("Print-on-Demand Art Series", "/imagine prompt: [art style — e.g. vintage botanical illustration] of [subject], [colour palette — e.g. muted sage, cream, and rust], [medium — e.g. watercolour on textured paper], [mood — e.g. tranquil, academic], suitable for framed wall art, high detail, print quality --ar 2:3 --v 6\n\nThen run: /imagine prompt: [same prompt] --sref [URL of first image] --sw 100\nThis maintains visual consistency across your entire collection."),
    ("Brand Mood Board Direction", "/imagine prompt: brand identity mood board for a [industry] company called [name], target audience: [describe], values: [list 3], aesthetic: [describe style], photography collage layout, include: textures, typography hints, colour swatches, lifestyle imagery, aspirational tone, editorial magazine quality --ar 16:9 --v 6"),
  ],
  'advanced_steps': [
    ("Build and Save Style References", "After generating your best image, click the share button and copy the URL. Add --sref [URL] to any future prompt to maintain the exact same visual style across hundreds of images. This is how you build a coherent product line or brand package — style consistency is the professional standard."),
    ("Use --seed for Reproducibility", "Add --seed [number] to any prompt to make it reproducible. When a client loves an image and wants variations, use the same seed with slight prompt changes. Use /show [job ID] to retrieve and re-generate any past image."),
    ("Batch Prompting with Permutations", "Use {option1, option2, option3} in your prompt to generate multiple variations automatically: /imagine prompt: {minimal, maximalist, editorial} product photography of a luxury watch, dark background --v 6. Midjourney generates 3 separate images from one prompt. Batch test 10 styles in minutes."),
  ],
}

EXT['runway'] = {
  'use_cases': [
    ("Brand Video Studio", "Runs a monthly retainer service for DTC (direct-to-consumer) brands. Delivers 8–12 video assets per month — product demos, lifestyle clips, ad variants. Charges $2,500/mo. Has 4 clients = $10K MRR."),
    ("Music Video Director", "Creates AI music videos for independent artists. Charges $1,500–$5,000 per video. Uses Midjourney for key frames, Runway Gen-3 to animate them, ElevenLabs for audio sync. 2–4 projects/month."),
    ("Real Estate Video Agency", "Animates architectural renders and interior photos into cinematic walkthroughs for developers and agents. Charges $500–$1,500 per property. Property developers pay immediately — it sells their listings."),
    ("Ad Creative Factory", "Builds a service producing 10 ad creative variants per week for Meta and TikTok campaigns. Charges $1,500/mo. Clients A/B test constantly — they always need more variants."),
    ("Cinematic Stock Creator", "Creates premium AI video clips for Pond5, Shutterstock, and Adobe Stock. Focuses on hard-to-film scenarios (cinematic space, underwater, time-lapse cityscapes). Earns $1K–$4K/mo passive after building a catalogue."),
  ],
  'more_streams': [
    ("Film Pre-Production", "$3K–$15K/project", "Create animatics, mood videos, and concept reels for film/TV pitches. Directors and studios pay for visual development before green-lighting."),
    ("AI Stock Footage Library", "$500–$3K/mo passive", "Upload niche AI video clips to stock platforms. High-demand, hard-to-film scenarios earn the most: abstract data visualisations, medical animations, architectural fly-throughs."),
  ],
  'niche_table': [
    ("DTC/E-commerce Brands", "Product demos, lifestyle ads, UGC style", "$2K–$5K/mo retainer"),
    ("Real Estate", "Property walkthroughs, neighbourhood showcases", "$500–$1,500/property"),
    ("Music Artists", "Music videos, lyric videos, visualisers", "$1,500–$5,000/video"),
    ("Corporate/B2B", "Explainer videos, training content", "$2K–$8K/video"),
    ("Film/TV Pitch", "Animatics, mood reels, concept visualisation", "$3K–$15K/project"),
  ],
  'pricing_tiers': [
    ("Single Ad Creative", "$300–$600", "One 15–30 second video asset optimised for one platform. 48-hour delivery."),
    ("Ad Pack", "$1,200–$2,500", "5 video variants (different hooks, CTAs, formats). A/B test ready. 3-day delivery."),
    ("Monthly Retainer", "$2,000–$5,000/mo", "8–15 video assets per month. Dedicated creative strategy call monthly."),
    ("Custom Production", "$3,000–$15,000", "Full short-form video production — concept, generate, edit, deliver. Timeline varies."),
  ],
  'client_script': "Cold DM (Twitter/Instagram):\n\nHey [Brand name] — your product is visually stunning but I noticed your video ads are still using [static images / UGC only / same 2 clips everywhere].\n\nI run a video creative studio using next-generation AI production tools. I can produce 5 different ad variations for your [product] in 48 hours — for a fraction of what a traditional video shoot costs.\n\nWant me to create one free 15-second concept video for [specific product] so you can see the quality? No commitment — just want to show you what's possible.",
  'extra_prompts': [
    ("Product Hero Shot", "Cinematic slow push-in on [product description], [surface — e.g. black obsidian pedestal], [lighting — e.g. split dramatic studio lighting, one warm key light, one cool fill], [atmosphere — e.g. wisps of smoke], [detail — e.g. material texture visible, ultra sharp focus], commercial product launch quality, 24fps, [brand colour] colour grade"),
    ("Lifestyle Brand Film", "[Subject description] in [location], [time of day — e.g. golden hour, blue hour], [camera movement — e.g. tracking shot following subject], [atmosphere — e.g. warm summer afternoon, light haze], [mood — e.g. aspirational, free, confident], [film style — e.g. shot on 35mm, Kodak Vision3], cinematic widescreen, brand lifestyle aesthetic for [brand type]"),
    ("Gen-3 Storyboard Prompt Set", "For a 60-second brand film, write 8 sequential Gen-3 prompts — one per scene. Brand: [describe]. Story arc: [describe the narrative]. Each prompt should specify: camera movement, subject/action, environment, lighting, mood, and end on a frame that connects to the next scene. Make the sequence tell a coherent visual story without any text or narration."),
  ],
  'advanced_steps': [
    ("Image-to-Video Workflow", "The professional workflow: 1) Generate your perfect hero frame in Midjourney at 4K, 2) Import to Runway as the first frame of Image-to-Video, 3) Use Motion Brush to define exactly which parts move (product stays still, background shimmers), 4) Generate 3–5 variations, pick the best, 5) Extend the clip using Runway's Extend feature. This workflow gives you 10x more control than text-to-video alone."),
    ("Build a B-Roll Library", "Create a library of 50–100 generic brand-safe clips (abstract textures, environment shots, transition clips). Store them in a Google Drive folder organised by mood and colour. For every new client project, pull from this library for cutaways and transitions. Your per-project time drops dramatically once the library is built."),
    ("Combine with Descript for Delivery", "Export all Runway clips into Descript for final assembly. Descript handles captions, transcript-based editing, and multi-format export (16:9 for YouTube, 9:16 for TikTok, 1:1 for Instagram). One project → 3 platform formats in 20 minutes."),
  ],
}
