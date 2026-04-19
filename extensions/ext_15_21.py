# Extensions batch 3: tools 15-21 (perplexity, gemini, make, n8n, zapier, notebooklm, consensus)

EXT = {}

EXT['perplexity'] = {
  'use_cases': [
    ("Niche Newsletter Publisher", "Builds a paid Substack newsletter covering AI investment signals using Perplexity Deep Research daily. 500 paid subscribers at $15/mo = $7,500 MRR. Research time: 45 minutes/day. Writing time: 60 minutes/day."),
    ("Market Research Consultant", "Produces competitive intelligence reports for VC-backed startups before fundraising rounds. Charges $3,000–$8,000 per report. Uses Perplexity to source and verify 50+ data points in 2 hours."),
    ("SEO Content Researcher", "Runs a content agency where every article starts with a Perplexity Deep Research session. Quality and accuracy are noticeably better than competitors. Charges a 30% premium and keeps clients longer."),
    ("Investor Brief Service", "Produces weekly sector briefings for angel investors and family offices — 3 pages, fully sourced, covering funding rounds, M&A activity, and emerging players. Charges $2,000/mo per subscriber. Runs 8 subscribers."),
    ("Competitive Intelligence Retainer", "Monitors 3 competitors per client every week — new features, pricing changes, job postings, press coverage, review sentiment. Delivers a Friday briefing. Charges $1,500/mo per client. Manages 6 clients."),
  ],
  'more_streams': [
    ("Due Diligence Research", "$2K–$10K/report", "Produce startup due diligence research for angel investors. Perplexity sources public information on team background, market size, competitors, and risks. One report = one investment decision."),
    ("Trend Report Products", "$50–$500/report", "Produce and sell annual/quarterly trend reports for specific industries. Sell on Gumroad. 100 downloads × $99 = $9,900 from one report."),
  ],
  'niche_table': [
    ("Venture Capital / Angel Investing", "Deal flow research, due diligence, sector briefs", "$2K–$10K/report"),
    ("SaaS / Tech Companies", "Competitive intel, market sizing, trend reports", "$1K–$5K/mo retainer"),
    ("Law Firms", "Case research, precedent finding, regulatory updates", "$150–$300/hr"),
    ("Marketing Agencies", "Campaign research, audience insights, industry data", "$500–$2K/project"),
    ("Consultancies", "Client background research, industry landscape", "$1K–$5K/engagement"),
  ],
  'pricing_tiers': [
    ("Research Flash", "$200–$500", "Quick-turn research brief on one specific question. 4-hour delivery. 3–5 pages."),
    ("Sector Report", "$1,500–$5,000", "Comprehensive industry analysis. 15–30 pages, fully sourced. 3-day delivery."),
    ("Monthly Intelligence", "$1,500–$4,000/mo", "Ongoing research: weekly briefs + monthly deep report. Always current."),
    ("Custom Deep Research", "$3,000–$10,000", "Multi-week research project. Investment thesis, market entry, M&A target analysis."),
  ],
  'client_script': "Cold email to a VC associate:\n\nSubject: [Sector] deal flow intelligence — quick question\n\nHi [Name],\n\nI produce weekly intelligence briefs for investors in [sector] — funding rounds, new entrants, pricing shifts, and technology signals. Fully sourced, 3 pages, every Friday.\n\nI have one slot open. The first brief is free — I'll cover [specific sector topic relevant to their portfolio] this week so you can judge the quality.\n\nWorth 10 minutes to look at it?",
  'extra_prompts': [
    ("Competitive Intelligence Brief", "Conduct a comprehensive competitive intelligence report on [Company Name] as of today. Cover: 1) Business model and revenue streams (cite sources), 2) Pricing — current plans, recent changes, and any public pricing signals, 3) Product roadmap signals — announced features, job postings that reveal direction, recent changelog entries, 4) Customer sentiment — summarise the last 30 days of reviews on G2, Trustpilot, Reddit, and App Store. Flag specific complaints that appear multiple times, 5) Team and hiring signals — key hires in the last 6 months and what they indicate strategically, 6) Financial signals — last funding round, estimated ARR if available, burn signals from layoffs or hiring freezes. Include the URL source for every factual claim."),
    ("Investment Sector Brief", "Produce a current-state briefing on the [sector] market for an angel investor considering their first investment. Cover: 1) Market size (TAM/SAM/SOM) with current sources, 2) Top 10 funded companies — stage, total raised, last round date, lead investor, 3) Emerging players under $5M raised that are getting traction, 4) 3 macro trends reshaping the space in 2025, 5) The 2 most recent notable exits or acquisitions and what they reveal about the market, 6) Key risks — regulatory, technology, or competitive threats. Keep it under 1,500 words. Every statistic must be cited."),
    ("Weekly Monitoring Prompt", "You are a competitive intelligence analyst. Today is [date]. Conduct a thorough search for the following updates about [Company]: 1) Any product announcements or feature launches in the last 7 days, 2) Any pricing changes announced or leaked, 3) Press coverage — major articles or mentions, 4) Social media signals — significant posts from founders or executives, 5) Job postings added or removed in the last week (what does this signal?), 6) Any negative news — lawsuits, outages, customer complaints trending. Deliver as a structured 1-page brief with source links for every item."),
  ],
  'advanced_steps': [
    ("Build a Perplexity Spaces Library", "Create a permanent Perplexity Space for every client and major research area. Upload their core documents (annual reports, product docs, strategy decks) to the Space. Now every research session starts with company-specific context plus live web search. Your research is 10x more targeted than a generic web search."),
    ("Pair with Claude for Report Assembly", "The workflow: 1) Perplexity Deep Research generates sourced raw intelligence, 2) Export the full output, 3) Paste into Claude with a report-writing prompt and your house style guide, 4) Claude assembles it into a polished deliverable. This two-tool pipeline produces reports that typically cost $5K–$20K from traditional research firms — in 3–4 hours."),
    ("Source Verification Protocol", "Before delivering any report: 1) Click every linked source, 2) Verify the statistic is in the source — not just close to it, 3) Check the publication date — is it current enough for your client's needs? 4) For market size numbers specifically, note the methodology (bottom-up vs top-down). Sourcing errors in research products destroy credibility immediately."),
  ],
}

EXT['gemini'] = {
  'use_cases': [
    ("Google Workspace Integrator", "Targets SMBs already paying for Google Workspace. Charges $2,000–$5,000 to set up Gemini-powered workflows across Gmail, Docs, and Sheets. Clients see immediate ROI. No new software needed — just unlock what they already pay for."),
    ("YouTube Channel Strategist", "Uses Gemini's YouTube Studio integration to optimise titles, descriptions, and chapters for creators. Charges $500–$1,500/mo per channel. 10 channels = $5K–$15K/mo."),
    ("1M Context Research Analyst", "Takes on complex research projects that require ingesting entire codebases, annual reports, or book-length documents. The 1M token context window makes Gemini the only viable tool. Charges $3K–$15K per engagement."),
    ("Google Ads AI Consultant", "Uses Gemini to analyse ad performance data, write ad copy variants, and generate keyword strategies. Integrates with Google Ads API directly. Charges $2K–$5K/mo per client."),
    ("Enterprise AI Adoption Consultant", "Helps Google Workspace enterprise clients ($12/user/month Business Plus) activate Gemini across their 500–5,000 seat organisation. Charges $20K–$80K for the implementation project. Google's own partner referral programme pays commissions."),
  ],
  'more_streams': [
    ("Google AppScript Automation", "$1K–$5K/setup", "Build Gemini-powered Google AppScript automations for Sheets, Gmail, and Docs. Every Google Workspace user is a potential client. The TAM is enormous."),
    ("BigQuery AI Analytics", "$5K–$25K/project", "Use Gemini's BigQuery integration to build AI-powered analytics dashboards for data-driven companies. Enterprise-tier work with enterprise-tier rates."),
  ],
  'niche_table': [
    ("SMBs on Google Workspace", "Workspace automation, AI workflows", "$2K–$5K setup + $500/mo"),
    ("YouTube Creators", "Channel optimisation, content strategy", "$500–$2K/mo per channel"),
    ("Enterprise (500+ seats)", "Gemini AI adoption, training, setup", "$20K–$80K/project"),
    ("Marketing Teams", "Ads copy, campaign analysis, briefs", "$2K–$5K/mo"),
    ("Data Teams", "BigQuery AI, analytics dashboards", "$5K–$25K/project"),
  ],
  'pricing_tiers': [
    ("Workspace Audit", "$500–$1,500", "Identify top 5 Gemini automation opportunities in a company's Workspace setup. Delivered as an action plan."),
    ("Workflow Setup", "$2,000–$5,000", "Build and deploy 3–5 Gemini automations across Gmail, Docs, Sheets. 2-week delivery."),
    ("Enterprise Rollout", "$20,000–$80,000", "Full Gemini adoption for 100+ seat organisations. Training, customisation, governance."),
    ("Monthly Optimisation", "$500–$2,000/mo", "Monthly refinement of Gemini workflows. New automations, performance review."),
  ],
  'client_script': "Email to an office manager or COO:\n\nSubject: Your Google Workspace — hidden time savings\n\nHi [Name],\n\nYour company pays for Google Workspace. Most companies use about 20% of what it can do — especially now that Gemini AI is built in.\n\nI help [company size] businesses like yours set up Gemini across Gmail, Docs, and Sheets to eliminate the manual work that's eating 5–10 hours per employee per week.\n\nI've done this for [similar company type] and they cut their admin time by [specific result]. I'll do a free 30-minute audit call to show you exactly where the savings are in your setup.\n\nWorth a look?",
  'extra_prompts': [
    ("Workspace Automation Design", "Design a complete Gemini-powered workflow for a [business type] using Google Workspace. For each of these tools — Gmail, Google Docs, Google Sheets, Google Calendar, Google Meet — identify: 1) The most time-consuming manual task their team currently does in that tool, 2) Exactly how Gemini can automate or assist with it, 3) The AppScript or Gemini prompt needed to implement it, 4) Estimated hours saved per week per employee. Output as an implementation roadmap with effort estimates (hours to set up) and ROI estimates (hours saved per month)."),
    ("YouTube Channel Optimisation", "I'm optimising a YouTube channel about [topic] for maximum discoverability. Using current YouTube search data: 1) Generate 10 video title options for [video topic] — each using a different angle (curiosity gap, how-to, list, controversial, SEO-primary), 2) Write the full video description (500 words) with natural keyword integration, timestamps placeholder, and CTA, 3) Suggest 5 relevant tags, 4) Write 3 community post options to promote this video, 5) Suggest the ideal thumbnail concept based on what's currently getting clicks in this niche."),
    ("1M Context Document Analysis", "I am uploading [number] documents totalling approximately [size]. These cover [topic]. After reading all documents: 1) Build a master index of all key entities mentioned (people, companies, technologies, dates) across all documents, 2) Identify the top 5 themes that appear across multiple documents, 3) Find any contradictions or conflicts between documents, 4) Extract all specific data points (numbers, statistics, percentages) with their document source, 5) Produce a synthesis that no single document contains — patterns only visible across the full corpus. This is the analysis no human researcher could complete in under a week."),
  ],
  'advanced_steps': [
    ("Build a Gem for Every Client", "Create a dedicated Gemini Gem (custom AI persona) for each client. Upload their company documents, brand guidelines, and communication style. Every piece of work for that client starts from their Gem. This is the equivalent of Claude's Projects but natively inside Google's ecosystem — critical for clients who won't leave the Google stack."),
    ("Gemini API Free Tier Arbitrage", "The Gemini API's free tier is extremely generous (1,500 requests/day on Gemini 1.5 Flash). For automation projects, build on the free tier during development and testing. For production, Gemini 1.5 Flash is the cheapest capable model at $0.075/1M input tokens — use it for high-volume automation tasks where Claude and GPT-4o would be too expensive."),
    ("Deep Research as a Product", "Gemini's Deep Research feature (available in Advanced) runs 30+ search queries and produces a cited, multi-section report. Position this as a product: 'AI Research Brief' for $200–$500 per question. Target questions that professionals currently spend hours researching manually: 'What is the regulatory landscape for [industry] in [market]?' — one Deep Research session, one polished deliverable."),
  ],
}

EXT['make'] = {
  'use_cases': [
    ("Lead Gen Machine Builder", "Builds end-to-end lead generation systems for B2B companies: LinkedIn scrape → enrich with Clay → personalise with ChatGPT → send via Lemlist → log to HubSpot → alert on reply. Charges $3,000 setup + $500/mo. Has 8 clients = $4K MRR + $24K in setup fees."),
    ("E-commerce Ops Automator", "Builds full e-commerce back-office automation for Shopify stores: new order → inventory update → accounting entry → shipping label → customer notification → review request at day 7. Charges $2,500 setup. 4 clients/month = $10K/mo."),
    ("Agency White-Label Partner", "Partners with 3 marketing agencies as their automation arm. Agencies sell automation to their clients and pass the builds to him. Gets $1,500–$3,000 per build. Agencies mark it up. No client acquisition cost."),
    ("Make Template Creator", "Builds and sells Make workflow templates on Gumroad and the Make marketplace. A 'Real Estate Lead Machine' template sells for $97. 100 sales = $9,700. One build, infinite sales."),
    ("SaaS Integration Specialist", "Specialises in connecting SaaS tools that don't have native integrations. Every SaaS company has clients who need their tool connected to something it doesn't support. Charges $1K–$3K per custom integration."),
  ],
  'more_streams': [
    ("Make Partner Programme", "$500–$3K/mo referral", "Join Make's official partner programme. Refer clients to Make subscriptions and earn referral commissions. Every client you onboard earns you recurring commission."),
    ("Automation Audit Service", "$500–$1,500/audit", "Audit a company's existing Make setup for inefficiencies, broken scenarios, and missing opportunities. Deliver a report + implementation plan. Fast to do, high perceived value."),
  ],
  'niche_table': [
    ("Real Estate Agencies", "Lead routing, CRM sync, follow-up sequences", "$2K–$5K setup + $400/mo"),
    ("E-commerce / Shopify", "Order ops, inventory, customer journey", "$2K–$4K setup + $300/mo"),
    ("Marketing Agencies", "Client reporting, lead delivery, campaign ops", "$1.5K–$3K setup + $300/mo"),
    ("SaaS Companies", "Onboarding automation, churn prevention", "$2K–$5K setup + $500/mo"),
    ("Coaches / Course Creators", "Student onboarding, progress tracking, upsells", "$1K–$2.5K setup + $200/mo"),
  ],
  'pricing_tiers': [
    ("Starter Automation", "$800–$1,500", "1–3 connected scenarios solving one workflow problem. Delivered in 3 days."),
    ("Business Automation Pack", "$2,500–$4,000", "Full workflow automation for one business function (sales, ops, marketing). 1 week."),
    ("Automation OS", "$5,000–$10,000", "Complete business automation — all major workflows connected. 2–3 weeks."),
    ("Retainer", "$300–$800/mo", "Monthly maintenance, new scenarios, optimisation, priority support."),
  ],
  'client_script': "DM to a Shopify store owner:\n\nHey [Name] — I was browsing [Store Name] and noticed you're doing [X] orders. Quick question: how are you currently handling the post-purchase workflow — inventory updates, accounting, review requests?\n\nI build automated systems for Shopify stores that handle all of that without any manual work. One of my clients went from spending 3 hours/day on order ops to zero.\n\nI'll map out exactly what that system would look like for your store — free — on a 20-minute call. Worth it?",
  'extra_prompts': [
    ("Automation Scope Document", "I'm building a Make automation for a [business type] client. Their current manual process: [describe step by step]. Design the complete Make scenario: 1) The trigger — what event starts the automation and in which app? 2) All modules in sequence with the app name and action for each, 3) Data mapping — what specific fields are passed between modules? 4) Filter conditions — when should the scenario proceed vs stop? 5) Error handling — what happens if module 3 fails? 6) Testing plan — how do I validate each step before going live? Output as a technical spec I can build from directly."),
    ("Client ROI Calculator", "My Make automation for [client type] saves them: [hours saved per week]. They currently pay a [employee type] [hourly rate] to do this manually. Calculate: 1) Monthly labour cost saved, 2) Annual labour cost saved, 3) ROI on my $[setup fee] + $[monthly retainer] in months to break even, 4) Total value delivered in year 1, 5) Write a one-paragraph ROI statement I can use in my proposal that makes the financial case compellingly but conservatively."),
    ("Niche Automation Research", "I want to build a productised automation service for [specific industry — e.g. dental practices / real estate agencies / law firms]. Research: 1) What are the top 5 most painful manual workflows in this industry? 2) What software tools do they commonly use (CRM, scheduling, accounting, communication)? 3) Which of their workflows are most frequently automated by their competitors (showing proven demand)? 4) What's a realistic price point for automation services in this niche? 5) How would I find 10 potential clients in this niche in the next 2 weeks?"),
  ],
  'advanced_steps': [
    ("Build Your Client Onboarding Scenario", "Meta-automation: build a Make scenario that onboards your own new automation clients automatically. Trigger: new client added to your Airtable. Actions: send welcome email → create Notion project → send Slack notification to yourself → schedule kickoff meeting via Calendly → add to invoice system. Every new client gets a consistent, professional experience from day one."),
    ("Error Handling Is Non-Negotiable", "Every client scenario needs: 1) Error handlers on every module (set to 'Resume' for non-critical, 'Break' for critical), 2) An error notification scenario that alerts you on Slack/email immediately when something breaks, 3) A retry logic for API rate limits (add a sleep module + router). Clients don't cancel retainers when things break — they cancel when they find out things broke and you didn't tell them."),
    ("Build a Scenario Library", "After every client project, export the scenario as a blueprint (right-click → Export Blueprint). Store in a GitHub repo organised by industry and function. Within 6 months you'll have 50+ blueprints. New client projects become 80% copy-paste from existing blueprints. Your hourly effective rate doubles."),
  ],
}

EXT['n8n'] = {
  'use_cases': [
    ("Self-Hosted AI Agency", "Hosts n8n on a $12/mo Hetzner VPS. Builds AI agent workflows for 6 clients at $500/mo each. Total infra cost: $12/mo. Revenue: $3,000/mo. Every dollar above $12 is margin. No per-operation pricing like Make or Zapier."),
    ("Privacy-First Automation", "Targets healthcare, legal, and finance clients who can't send data to third-party cloud automation tools. Self-hosted n8n keeps everything on-premise. Charges a 50% premium for data sovereignty. Wins clients that Make and Zapier can't touch."),
    ("AI Agent Pipeline Builder", "Builds multi-step AI agent pipelines: research agent → analysis agent → report writer → email sender. All orchestrated in n8n. Charges $5K–$15K per pipeline. Targets marketing agencies and consulting firms."),
    ("n8n Template Seller", "Builds complex n8n workflows (50+ nodes) and sells as JSON templates on the n8n community forum and Gumroad. Detailed AI agent workflows sell for $50–$200 each. Portfolio of 30 templates earns $500–$3K/mo passively."),
    ("Developer Tool Integrator", "Specialises in connecting internal developer tools — GitHub, Jira, Slack, Datadog, PagerDuty — into automated incident response and deployment pipelines. Charges $150/hr. Engineering teams at Series A+ startups pay immediately."),
  ],
  'more_streams': [
    ("n8n Hosting Service", "$100–$500/mo per client", "Host and manage n8n instances for clients who want self-hosted automation but don't have DevOps skills. White-label the service under your agency name."),
    ("Enterprise Integration Consulting", "$10K–$40K/engagement", "Design and implement n8n-based integration architectures for enterprise clients replacing legacy middleware. Long engagements, high value."),
  ],
  'niche_table': [
    ("Healthcare / HIPAA", "On-premise patient workflow automation", "$5K–$20K setup + $1K/mo"),
    ("Legal / Finance", "Compliant document processing, reporting", "$5K–$15K setup + $800/mo"),
    ("Developer Teams", "CI/CD, incident response, DevOps automation", "$150–$250/hr"),
    ("Marketing Agencies", "AI content pipelines, reporting automation", "$3K–$8K setup + $500/mo"),
    ("SaaS Companies", "Customer onboarding, data sync pipelines", "$5K–$15K setup + $800/mo"),
  ],
  'pricing_tiers': [
    ("Hosted Setup", "$500–$1,500", "n8n deployed on client's server + 2 starter workflows. Delivered in 3 days."),
    ("Workflow Build", "$2,000–$6,000", "Complex multi-step workflow with AI nodes, error handling, monitoring. 1 week."),
    ("AI Agent Pipeline", "$5,000–$15,000", "Full multi-agent automation system. Architecture + build + documentation. 2–3 weeks."),
    ("Managed Service", "$500–$2,000/mo", "You host, maintain, monitor, and expand their n8n instance. Pure recurring revenue."),
  ],
  'client_script': "Cold email to a marketing agency:\n\nSubject: Your content team — a question about volume\n\nHi [Name],\n\nI saw [Agency] is producing content for [X] clients. Quick question: how much of your team's time goes into tasks that are identical every week — pulling reports, formatting briefs, posting content, sending client updates?\n\nI build private AI automation systems for agencies that eliminate that repetitive work. Unlike tools like Zapier or Make, mine run on your own servers — so your client data never leaves your infrastructure.\n\nOne of my clients cut 15 hours of weekly admin across their team of 8 in the first month.\n\nWorth 20 minutes to show you what that looks like for your setup?",
  'extra_prompts': [
    ("AI Agent Workflow Design", "Design a complete n8n AI agent workflow for [specific use case]. Specify: 1) Trigger node — what starts this workflow (webhook, schedule, email, etc.)? 2) All nodes in order — node type, app/service, specific action, and what data it processes, 3) The AI Agent node configuration — which model, what system prompt, which tools it has access to, 4) Memory strategy — how does the agent maintain context across runs? 5) Output node — where does the final result go? 6) Error handling node placement, 7) Estimated monthly API cost at [expected volume] runs/day. Draw this as a numbered node list I can build step-by-step."),
    ("Self-Host Sales Pitch", "Write a 200-word pitch for selling self-hosted n8n automation to a [healthcare / legal / financial] company that is currently using a cloud automation tool. Key argument: their client data currently passes through [cloud tool]'s servers in [country], which creates [specific compliance risk — HIPAA / GDPR / attorney-client privilege]. Self-hosted n8n eliminates this risk entirely. Price the solution at [$X setup + $Y/mo] and explain the ROI. Avoid technical jargon — this is for a compliance officer or COO, not a developer."),
    ("Workflow Documentation Template", "Generate complete technical documentation for this n8n workflow: [describe workflow]. Include: 1) Purpose and business value statement, 2) Architecture diagram (text-based node map), 3) Node-by-node description — what each does, what data goes in, what comes out, 4) Required credentials and where to obtain them, 5) Environment variables needed, 6) Testing procedure — how to verify each node is working correctly, 7) Common failure points and how to debug them, 8) Maintenance schedule recommendation. Format as a technical runbook a non-developer could follow."),
  ],
  'advanced_steps': [
    ("Set Up Monitoring from Day One", "Every production n8n deployment needs: 1) UptimeRobot (free) pinging your n8n URL every 5 minutes, 2) n8n's built-in error workflow — create a catch-all error handler that sends a Slack/Telegram message with the workflow name and error details, 3) Weekly automated backup of n8n's database to S3 or Google Drive. These 3 steps prevent the 3 most common client-relationship-destroying incidents."),
    ("The Code Node as a Superpower", "n8n's Code node runs arbitrary JavaScript or Python. Use it for: data transformation that no native node handles, calling any API with custom auth, parsing complex JSON structures, running regex on messy data. Learn to use it fluently and no automation task is out of reach. It's the difference between 'n8n can't do that' and 'n8n can do anything'."),
    ("Version Control Your Workflows", "Export every production workflow as JSON and commit to a private GitHub repo. Folder structure: /workflows/client-name/workflow-name.json. Tag releases. When a workflow breaks after an edit, you have a 30-second rollback. Clients who learn you have version control on their automations trust you more."),
  ],
}

EXT['zapier'] = {
  'use_cases': [
    ("Real Estate Lead Machine", "Builds a Zapier system for real estate agencies: new Zillow lead → enriched with Clearbit → personalised email via Gmail → added to HubSpot → agent notified on Slack → follow-up scheduled in 24 hours if no reply. Charges $1,500 setup + $300/mo. Signs 5 agencies. Revenue: $1,500 MRR + $7,500 upfront."),
    ("Coaching Business Automator", "Automates the entire back-office of coaching businesses: new Typeform intake → create client record in Notion → send onboarding email sequence → schedule discovery call via Calendly → add to Stripe subscription → add to private Slack community. Charges $1,200 setup. Closes 4 coaches/month."),
    ("Agency Client Reporting", "Builds automated weekly client reports for marketing agencies: pull Google Analytics data → pull Meta Ads data → format in Google Sheets template → send as PDF to client every Friday. Charges $800/mo per client. Agency has 12 clients = $9,600/mo just for reporting."),
    ("Zapier Trainer", "Runs online workshops teaching small business owners to use Zapier. Charges $197/workshop. 20 attendees/session × 2 sessions/month = $7,880/mo. Also sells a 'Zapier Starter Pack' of 10 templates for $47."),
    ("E-commerce After-Purchase Sequence", "Builds post-purchase automation for Shopify stores: order placed → 24hr follow-up email → 7-day review request → 30-day repurchase offer → tag as VIP if 3+ purchases. Charges $1,500 setup. Every e-commerce store needs this."),
  ],
  'more_streams': [
    ("Zapier Tables + Interfaces", "$1K–$3K/build", "Build lightweight apps using Zapier Tables (database) and Interfaces (forms/dashboards) as a no-code alternative to Airtable. Faster to build, easier for non-technical clients to maintain."),
    ("Automation Maintenance Plans", "$150–$500/mo", "Offer monthly maintenance for any client's Zapier account — fix broken Zaps, monitor task usage, add new Zaps as their business grows. 15 clients × $250/mo = $3,750 MRR."),
  ],
  'niche_table': [
    ("Real Estate Agencies", "Lead routing, follow-up, CRM sync", "$1.5K–$3K setup + $300/mo"),
    ("Coaches / Consultants", "Client onboarding, scheduling, billing", "$1K–$2.5K setup + $200/mo"),
    ("E-commerce / DTC", "Post-purchase, review requests, VIP tagging", "$1K–$2K setup + $200/mo"),
    ("Marketing Agencies", "Client reporting, lead delivery, campaign ops", "$800–$2K setup + $300/mo"),
    ("Non-Profits", "Donor management, volunteer onboarding, events", "$800–$2K setup + $150/mo"),
  ],
  'pricing_tiers': [
    ("Quick Win Zap", "$500–$800", "1–2 Zaps solving one specific problem. Same-day delivery."),
    ("Workflow Bundle", "$1,200–$2,500", "5–8 Zaps covering one business function. 3-day delivery."),
    ("Full Automation Setup", "$3,000–$6,000", "Complete business automation — sales, ops, marketing. 1–2 weeks."),
    ("Monthly Care Plan", "$200–$500/mo", "Monitoring, fixes, new Zaps, quarterly review. Retainer."),
  ],
  'client_script': "DM to a business owner you find on Twitter/X:\n\nHey [Name] — love what you're building with [their business]. Quick question: do you use any tools to automate your client intake or follow-up process?\n\nI build Zapier systems that handle the admin work that bogs most [their industry] businesses down — from first lead to paid client, fully automated.\n\nI'll map out exactly what that looks like for [Business Name] on a free 20-minute call. Not a pitch — just a mapping session. You'll walk away with a clear picture of what could be automated even if we don't work together.\n\nCalendar link: [Calendly]",
  'extra_prompts': [
    ("Zapier Proposal Writer", "Write a professional proposal for a Zapier automation project for [client type]. The automation I'm building: [describe the workflow in plain terms]. Structure the proposal as: 1) Executive Summary — the problem I'm solving and the business impact (no tech jargon), 2) Scope of Work — each Zap described in plain English, 3) Implementation Timeline — day-by-day for a 1-week build, 4) Investment — [setup fee] + [monthly retainer] with clear payment terms, 5) ROI Calculation — time saved per week × their hourly value, 6) What happens if something breaks — my maintenance commitment, 7) Next steps — what they sign, what I start, when it goes live. Tone: confident and professional but warm."),
    ("Zap Architecture Design", "Design a complete Zapier automation system for [business type]. Map every Zap: Trigger app + event → Action app + action → any filters or conditions. For each Zap include: 1) Business purpose (why it exists), 2) Data passed between apps, 3) Any conditional logic, 4) Estimated monthly task usage. Then calculate the total monthly Zapier task usage and recommend the right Zapier plan tier. Finally, flag any Zaps that would be better built in Make or n8n due to complexity."),
    ("Niche Automation Package Name", "I'm productising my Zapier automation service for [specific niche — e.g. fitness coaches / mortgage brokers / wedding planners]. Create: 1) A compelling package name (e.g. 'The Revenue Engine', 'The Client Machine'), 2) The exact 5–7 Zaps included in the package (specific to their industry workflows), 3) A one-page sales description of the package, 4) The price point and justification, 5) 3 objection responses for the most common pushbacks (too expensive, I can do it myself, I don't need it yet). Make the package feel like a product, not a custom service."),
  ],
  'advanced_steps': [
    ("The Productised Service Model", "Stop quoting custom work hourly. Build 3 packaged Zapier products for one niche (e.g. 'The Real Estate Lead Machine' at $1,500, 'The Real Estate Follow-Up Engine' at $1,000, 'The Real Estate Reporting Stack' at $800). Each is pre-built, pre-tested, and takes you 1 hour to customise for a new client. You sell the outcome, not your time. Margin goes from 40% to 80%+."),
    ("Task Usage Optimisation", "Zapier bills per task. Audit every client's Zap for task waste: multi-step Zaps where early steps filter out most records (move the filter earlier), loops running more iterations than needed, polling triggers that fire too frequently. Optimising task usage keeps clients on lower plans — which they appreciate — and prevents unexpected billing surprises that kill retainers."),
    ("Build a Referral Machine", "Your best Zapier clients know other business owners with the same problems. After a successful delivery, send: 'I'm glad this is saving you time. If you know anyone else in [their industry] who's drowning in manual work, I'd love an introduction. I give a $200 Amazon voucher for every referral that becomes a client.' One client can generate 3–5 referrals. This is the fastest growth channel for local service businesses."),
  ],
}

EXT['notebooklm'] = {
  'use_cases': [
    ("Paid Study Community", "Uploads medical licensing exam content (USMLE, NCLEX) into NotebookLM notebooks. Sells access to a study community at $29/mo. 200 members = $5,800 MRR. Content is free (public domain textbooks + official prep materials). Margin: near 100%."),
    ("Conference Intelligence Service", "Attends major industry conferences (virtually), uploads all speaker presentations and session recordings into NotebookLM. Sells a 'Conference Intelligence Brief' to professionals who couldn't attend. Charges $97 per brief. 50 buyers per conference = $4,850 per event."),
    ("AI Podcast Network", "Creates a podcast network where every episode is an AI-generated NotebookLM Audio Overview of industry documents. Topics: 'The Weekly VC Report', 'This Week in AI Policy', 'The Founders Briefing'. Monetises via Spotify, Apple Podcasts, and sponsorships."),
    ("Legal Research Assistant", "Uploads case law, statutes, and legal briefs into NotebookLM for law firms. Lawyers can query the case law and get sourced answers instantly. Charges $500–$2,000/mo per firm. 8 firms = $4K–$16K MRR."),
    ("Book Summary Service", "Creates NotebookLM notebooks from business books and sells 'Smart Book Summaries' — interactive notebooks where buyers can ask questions about the book. Charges $9–$19 per book. Portfolio of 50 books earns passive income as buyers discover them."),
  ],
  'more_streams': [
    ("Corporate Knowledge Base", "$2K–$8K/setup", "Upload a company's entire documentation — policies, products, processes — into NotebookLM and train their team to use it. Every employee gets instant access to company knowledge. Charge for setup + quarterly updates."),
    ("Podcast Repurposing Service", "$200–$500/episode", "Take existing podcast episodes, upload transcripts to NotebookLM, generate comprehensive show notes, chapter markers, key insights, and an Audio Overview for each episode. Sell to podcasters wanting to maximise content reach."),
  ],
  'niche_table': [
    ("Students (Licensing Exams)", "USMLE, Bar, CPA, GMAT study tools", "$20–$50/mo subscription"),
    ("Legal Professionals", "Case law research, contract analysis", "$500–$2K/mo per firm"),
    ("Investors / Analysts", "Earnings calls, annual reports, filings", "$500–$3K/mo subscription"),
    ("Podcast Creators", "Episode repurposing, show notes, summaries", "$200–$500/episode"),
    ("Corporate L&D", "Internal knowledge base, training materials", "$2K–$8K/setup + $500/mo"),
  ],
  'pricing_tiers': [
    ("Study Notebook", "$15–$50 one-time", "Single-topic study notebook with FAQ, study guide, and audio overview. Sold as digital product."),
    ("Research Brief", "$100–$500", "Document analysis + executive summary + FAQ + audio overview. Delivered in 24 hours."),
    ("Knowledge Base Setup", "$2,000–$8,000", "Full company knowledge base in NotebookLM. Setup + training + 3 months support."),
    ("Subscription Community", "$15–$50/mo", "Access to ongoing updated notebooks in a specific domain. Recurring membership."),
  ],
  'client_script': "Email to a law firm partner:\n\nSubject: Your associates' research time — a question\n\nHi [Name],\n\nA partner at a [similar firm type] firm told me their associates were spending 4–6 hours per case doing initial legal research that a tool I set up now handles in 15 minutes.\n\nI build AI research systems for law firms using Google's NotebookLM — uploaded with your relevant case law, statutes, and firm knowledge. Associates get sourced, accurate answers instantly. Nothing leaves your environment.\n\nI'd like to show you a 10-minute demo using a sample from [their practice area]. Would Thursday work?",
  'extra_prompts': [
    ("Study Guide Generation", "Based on all uploaded sources, create a comprehensive study guide for [exam/topic]. Include: 1) Master concept list — every key term defined in plain language, 2) 50 practice questions at exam difficulty with detailed answer explanations, 3) Common mistake patterns — the top 10 errors students make on this topic, 4) Memory aids — mnemonics, frameworks, and visual descriptions for the hardest concepts, 5) A 7-day study schedule covering all material. Cite the specific notebook source for every fact."),
    ("Podcast Episode Generation", "Based on the uploaded sources about [topic], create a NotebookLM Audio Overview script. Format: 1) Two-host dialogue, 2) Host A is analytical and data-focused; Host B is more narrative and asks clarifying questions, 3) Cold open — start with the most surprising or counterintuitive finding, 4) Cover the 5 most important insights from the sources, 5) One moment of genuine disagreement or debate between hosts, 6) Close with 3 actionable takeaways for the listener. Total length: 12–15 minutes at normal speaking pace (~1,800 words)."),
    ("Executive Knowledge Brief", "From the uploaded company documents, generate a complete executive knowledge brief for a new senior hire joining [company/department]. Include: 1) The company's strategic priorities in plain English (not jargon), 2) The 10 things they most need to know in their first 30 days, 3) Key processes and who owns them, 4) The questions they're likely to be asked and the answers, 5) Red flags — things that could go wrong if they don't know them, 6) The 5 most important people they need to build relationships with and why. Cite document sources for every claim."),
  ],
  'advanced_steps': [
    ("The Source Curation Advantage", "The quality of a NotebookLM product is entirely determined by the quality of sources uploaded. For any paid product: 1) Use primary sources only (official docs, academic papers, original reports), 2) Upload the full document not excerpts — NotebookLM needs context, 3) Include at least 5 sources that represent different perspectives, 4) Update sources quarterly for subscription products. Source curation is your competitive moat — anyone can create a notebook, not everyone knows what to put in it."),
    ("Audio Overview Post-Production", "NotebookLM's Audio Overview is excellent but needs finishing: 1) Download the MP3, 2) Import to Descript — clean up any dead air, 3) Add an intro and outro music bed (use Suno to generate royalty-free music), 4) Add a chapter marker at every major topic shift, 5) Export as MP3 for podcast or MP4 with static image for YouTube. This post-production step takes 20 minutes and elevates the product from 'AI tool output' to 'professional podcast episode'."),
    ("Build a Notebook Update System", "For subscription products, set up a monthly update workflow: 1) Google Alert for your source topics → new articles collected in a Google Doc, 2) At month end, review and select the 5–10 most important updates, 3) Upload to the existing notebook, 4) Send subscribers a 'What's New' email listing the updates. Subscribers who see consistent updates renew. Subscribers who see a stale notebook cancel."),
  ],
}

EXT['consensus'] = {
  'use_cases': [
    ("Health Brand Science Partner", "Partners with 3 health supplement brands as their science content partner. Sources peer-reviewed evidence for every product claim. Charges $2,000/mo per brand. Delivers: 2 evidence briefs, 10 social claims with citations, 1 long-form science article. Revenue: $6K/mo."),
    ("Evidence-Based Newsletter", "Runs a paid newsletter that debunks health myths using actual research. 'What the science actually says about [trending topic]'. 1,000 paid subscribers at $12/mo = $12,000 MRR. Sources all claims via Consensus in under 2 hours per issue."),
    ("Grant Writer for Researchers", "Helps independent researchers write evidence-backed grant proposals. Consensus makes the literature review section fast and bulletproof. Charges $1,500–$3,000 per proposal section. Works with 4–6 researchers simultaneously."),
    ("Expert Witness Research", "Produces scientific literature reviews for lawyers preparing expert witness testimony in medical, environmental, or pharmaceutical cases. Charges $2,000–$8,000 per research package. Law firms have budget and urgency."),
    ("Wellness Platform Content Director", "Runs all content strategy and production for a wellness app or platform. Every article, email, and social post is evidence-grounded. Charges $3,000–$6,000/mo as a content director on retainer."),
  ],
  'more_streams': [
    ("Scientific Fact-Checking Service", "$500–$2K/project", "Companies making health, environmental, or scientific claims hire you to verify their content against peer-reviewed evidence before publishing. One legal challenge from a false claim costs far more than your fee."),
    ("University Research Support", "$1K–$5K/project", "Help graduate students and independent researchers conduct rapid literature reviews using Consensus + Elicit. Academic consulting is a large, underserved market."),
  ],
  'niche_table': [
    ("Health & Supplement Brands", "Evidence-backed marketing claims", "$2K–$5K/mo retainer"),
    ("Wellness Apps & Platforms", "Science-grounded content strategy", "$3K–$8K/mo"),
    ("Law Firms (medical/pharma)", "Expert witness research, case support", "$2K–$8K/project"),
    ("Academic Researchers", "Literature review support, grant writing", "$1K–$3K/project"),
    ("Healthcare Companies", "Clinical evidence briefs, patient education", "$2K–$6K/project"),
  ],
  'pricing_tiers': [
    ("Evidence Brief", "$300–$800", "One research question → sourced answer with top 5 studies cited. 24-hour delivery."),
    ("Content Science Audit", "$1,000–$3,000", "Audit existing content for scientific accuracy. Flag unsupported claims, recommend evidence. Delivered as a report."),
    ("Monthly Science Partner", "$2,000–$5,000/mo", "Ongoing evidence sourcing for all content. 10–20 briefs/month. 2 long-form articles."),
    ("Research Report", "$1,500–$6,000", "Comprehensive literature review on one topic. 15–30 pages. Fully cited. 1 week."),
  ],
  'client_script': "Email to a health brand's content director:\n\nSubject: Your content — a compliance question\n\nHi [Name],\n\nI was reading [Brand]'s blog and noticed [specific claim — e.g. 'boosts collagen by 40%' / 'clinically proven to improve sleep']. Quick question: do you have peer-reviewed citations backing that specific claim?\n\nThe FTC has escalated enforcement against unsubstantiated health claims significantly in 2024–2025. One complaint can trigger a multi-thousand-dollar investigation.\n\nI help health brands build an evidence library — every marketing claim backed by peer-reviewed science, cited and documented. It protects your brand legally and makes your content more persuasive.\n\nI'll audit one page of your website for free this week and show you which claims need stronger evidence. Interested?",
  'extra_prompts': [
    ("Evidence Content Brief", "I found the following peer-reviewed evidence on [topic] using Consensus: [paste top 5 results with key findings]. Now create a content brief for a 1,200-word science-backed article for [brand's] audience of [describe audience]. Include: 1) Headline options (give 3 — one curiosity-driven, one SEO-primary, one authority-led), 2) Article structure with every H2 and H3 mapped, 3) The specific study to cite at each section, 4) One key quote from a lead researcher to feature, 5) Claims to avoid — anything the evidence doesn't clearly support, 6) CTA that connects the science to [brand's product/service] without overclaiming."),
    ("Scientific Claim Verification", "I need to verify the following marketing claims for a [health/wellness/supplement] brand before they publish: [list 10 claims]. For each claim: 1) Search Consensus for supporting peer-reviewed evidence, 2) Rate the evidence quality: Strong (multiple RCTs or meta-analyses), Moderate (some RCTs or systematic reviews), Weak (observational studies only), or Unsupported (no peer-reviewed evidence found), 3) Suggest a compliant rewrite if the original claim is overstated, 4) Flag any claims that could attract regulatory attention from the FTC or relevant health authority."),
    ("Grant Literature Review", "I'm writing a grant application for a study on [research topic]. Using peer-reviewed evidence, write the Background and Significance section (800 words). Structure: 1) Establish the public health / scientific importance of the topic, 2) Summarise the current state of evidence (what we know, citing key studies), 3) Identify the specific gap this study will address (what we don't know), 4) Explain why this gap matters and why now is the time to address it, 5) Briefly preview how the proposed study design addresses the gap. Cite all studies in APA format. Flag where the evidence base is particularly strong vs thin."),
  ],
  'advanced_steps': [
    ("Build a Citation-First Content Process", "For every piece of content: 1) Search Consensus first — before writing a single word, 2) Collect the top 10 most relevant studies, 3) Classify each as primary (directly addresses your claim) or supporting, 4) Build your content around what the evidence actually shows — not the claim you want to make. This inverted process produces content that is both more accurate and more persuasive, because readers can see you're grounded in real research."),
    ("Create a Brand Evidence Library", "For each brand client, build a shared Notion database of all claims they make, their supporting studies, and the strength of evidence. Update it monthly as new research publishes. When their marketing team wants to make a new claim, they check the library first. You become their scientific infrastructure — not just a content vendor. This creates deep client lock-in."),
    ("Consensus + Elicit Pipeline", "Use both tools together: Consensus for breadth (quick scan of 200M papers to find the relevant ones) → Elicit for depth (extract specific methodology, sample size, and effect size from the top 10 papers) → Claude to synthesise into a report. This three-tool pipeline produces research quality that costs $10K+ from a traditional research firm in 4–6 hours."),
  ],
}
