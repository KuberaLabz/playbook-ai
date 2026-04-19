# Extensions batch 4: tools 22-28 (elicit, tavily, superagent, openaiagents, nemoclaw, dify, crewai)

EXT = {}

EXT['elicit'] = {
  'use_cases': [
    ("Systematic Review Contractor", "Runs systematic literature reviews for pharmaceutical companies, public health organisations, and think tanks. One 50-paper review takes 6 hours with Elicit vs 3 weeks manually. Charges $5,000–$15,000 per review. Takes 2 projects/month."),
    ("Grant Writing Partner", "Partners with independent researchers applying for NIH, NSF, and Wellcome Trust grants. Does the literature review and evidence synthesis sections. Charges $2,000–$4,000 per grant section. Researchers win more grants with better-supported proposals."),
    ("Clinical Evidence Agency", "Produces clinical evidence briefs for medical device and pharmaceutical companies pre-launch. Every product needs evidence documentation for regulatory submission and sales team education. Charges $3,000–$10,000 per brief."),
    ("Academic Consulting Business", "Markets directly to PhD students and early-career researchers who need to conduct literature reviews for their thesis or publications. Offers a 'Thesis Literature Review' service for $1,500–$3,000. This niche has steady demand year-round."),
    ("Think Tank Research Associate", "Works with policy think tanks producing evidence reviews on education, healthcare, and economic policy. These organisations have research budgets but limited staff. Charges $2,000–$6,000 per review. Builds long-term relationships."),
  ],
  'more_streams': [
    ("Research Training Workshops", "$500–$2K/workshop", "Teach researchers, journalists, and analysts how to use Elicit for rapid literature reviews. Academic libraries and journalism schools are ideal clients. Run online or in-person."),
    ("Meta-Analysis Support", "$3K–$15K/project", "Help researchers prepare the data extraction tables and PRISMA flowcharts required for published meta-analyses. These are essential for publication and extremely time-consuming to prepare manually."),
  ],
  'niche_table': [
    ("Pharmaceutical Companies", "Clinical evidence, regulatory support", "$5K–$20K/project"),
    ("Public Health Organisations", "Systematic reviews, policy evidence", "$5K–$15K/review"),
    ("PhD Students / Researchers", "Thesis literature reviews, paper research", "$1.5K–$3K/project"),
    ("Journalism (investigative)", "Evidence synthesis for data journalism", "$500–$2K/article"),
    ("Policy Think Tanks", "Evidence briefs, systematic reviews", "$2K–$8K/brief"),
  ],
  'pricing_tiers': [
    ("Quick Literature Scan", "$500–$1,000", "Top 20 papers on one question. Summary table + key findings. 24 hours."),
    ("Literature Review", "$2,000–$5,000", "Comprehensive review — 50+ papers, data extraction table, synthesis. 1 week."),
    ("Systematic Review", "$5,000–$15,000", "Full PRISMA-standard systematic review. Publication-ready. 2–4 weeks."),
    ("Ongoing Research Support", "$1,500–$4,000/mo", "Monthly literature monitoring — new papers on your topics, monthly synthesis."),
  ],
  'client_script': "LinkedIn message to a PhD student:\n\nHey [Name] — I saw you're working on your thesis in [field]. How far along are you with the literature review chapter?\n\nI help researchers get through the literature review stage in days instead of months using AI research tools. I produce the full structured review — papers identified, screened, extracted into tables, and synthesised — and you write the narrative on top.\n\nI've helped [number] researchers at [institution types] clear this bottleneck. If you're stuck on the lit review, I'd love to help. Free 20-minute call to scope the project?",
  'extra_prompts': [
    ("PRISMA Data Extraction Table", "I'm conducting a systematic review on [topic]. Using the uploaded papers, extract the following data from each study into a structured table: Study ID (Author, Year), Design (RCT/cohort/cross-sectional/etc.), Sample Size (N), Population (key characteristics), Intervention/Exposure, Comparison/Control, Primary Outcome Measure, Primary Result (effect size, confidence interval, p-value), Follow-up Duration, Risk of Bias Assessment (high/moderate/low), Key Limitations. Flag any papers where critical information is missing from the abstract — these will require full-text retrieval."),
    ("Evidence Synthesis Narrative", "Based on the data extraction table for my systematic review on [topic], write the Results and Discussion sections. Results: 1) Overview of included studies (how many, study designs, total participants), 2) Primary outcomes — what did most studies find? Where was there consensus? 3) Heterogeneity — where did results differ and why might that be? 4) Subgroup findings if relevant. Discussion: 1) What this evidence means in plain terms, 2) Strengths and limitations of this body of evidence, 3) Comparison to existing reviews on this topic, 4) Implications for practice and policy, 5) Gaps that future research should address. Write at postgraduate academic level. Cite studies by Author (Year)."),
    ("Rapid Literature Scan Report", "Conduct a rapid evidence scan on [topic] using Elicit. I need this for [purpose — e.g. a pitch, a grant application, a client brief]. Produce a 2-page rapid evidence summary: 1) What does the research say? (3–4 key findings, each cited), 2) How strong is the evidence? (brief quality assessment), 3) What is contested or unclear? 4) What do the most recent studies (last 2 years) add? 5) Bottom line — one sentence summary. Use plain language — this is for a non-academic audience."),
  ],
  'advanced_steps': [
    ("PRISMA Compliance from Day One", "For any systematic review that might be published, use Elicit's screening tools in a PRISMA-compliant way from the start: document your search terms, record how many papers were identified/screened/excluded at each stage, note exclusion reasons. Doing this retroactively is painful. Doing it in Elicit as you go takes 10 extra minutes per review and makes the difference between a publishable and unpublishable product."),
    ("Build a Reusable Column Set Library", "In Elicit's column builder, save column sets for your most common review types: Clinical Trials columns (PICO format), Market Research columns, Policy Evidence columns. A saved column set means every new review project starts with the right data structure in 2 clicks rather than 20."),
    ("The Elicit + Consensus + Claude Pipeline", "Three tools, one pipeline: 1) Consensus — quick scan to confirm strong evidence exists and find the landmark studies, 2) Elicit — deep extraction of the best 20–50 papers into a structured table, 3) Claude (200K context) — paste the full table and synthesise it into a polished report. This pipeline reliably produces research products worth $2K–$10K per engagement in 4–8 hours of focused work."),
  ],
}

EXT['tavily'] = {
  'use_cases': [
    ("Real-Time News Intelligence Agent", "Builds an AI agent for a hedge fund that monitors news across 50 companies in their portfolio. Every morning at 6am the agent runs, flags material news, and delivers a briefing to the investment team. Charges $3,000/mo. Runs on n8n + Tavily + Claude."),
    ("Lead Enrichment Pipeline", "Builds a B2B lead enrichment service: upload a CSV of company names → Tavily researches each company → Claude extracts key signals → output is a fully enriched CRM-ready lead list. Charges $0.50–$1.00 per lead. Processes 1,000 leads/day. Revenue: $500–$1K/day."),
    ("Competitor Monitoring SaaS", "Builds a micro-SaaS that monitors competitors for any company. Users enter their competitors, Tavily checks them daily, and the product sends a weekly digest of changes. Charges $49–$149/mo. 100 subscribers = $4,900–$14,900 MRR."),
    ("AI Research Agent for Consultancies", "Builds a custom research agent for management consultancies. Consultants describe their research question in plain English; the agent uses Tavily to gather current data, Claude to synthesise, and delivers a sourced 2-page brief in 10 minutes. Charges $8,000 setup + $1,500/mo."),
    ("Content Freshness Service", "Audits clients' existing blog content and identifies articles with outdated statistics. Uses Tavily to find current data. Charges $1,500 per content audit + $500/mo to keep articles updated. Every SEO-focused company needs this."),
  ],
  'more_streams': [
    ("Developer Tool Integration", "$2K–$8K/integration", "Integrate Tavily into existing developer tools, internal portals, and AI assistants. Many companies have AI chatbots that lack real-time web access — Tavily fixes this."),
    ("Real-Time Data API Reselling", "$500–$3K/mo", "Build a niche data product on top of Tavily — e.g. 'Daily AI Funding Monitor' or 'Retail Price Tracker'. Sell access to the processed data via a simple API or dashboard."),
  ],
  'niche_table': [
    ("Investment / Finance", "News monitoring, earnings intelligence, market signals", "$3K–$10K/mo"),
    ("B2B Sales Teams", "Lead enrichment, prospect research, trigger events", "$1K–$5K/mo"),
    ("Marketing Agencies", "Content freshness, competitive monitoring, trend tracking", "$1.5K–$4K/mo"),
    ("Management Consultancies", "Rapid research, landscape scanning, due diligence", "$5K–$15K/engagement"),
    ("SaaS Companies", "Real-time data for AI features, competitive intel for product", "$2K–$8K/mo"),
  ],
  'pricing_tiers': [
    ("Research Agent Setup", "$2,000–$5,000", "One-off research agent build with Tavily backend. 1 week. Delivered with documentation."),
    ("Intelligence Service", "$1,500–$5,000/mo", "Ongoing automated research: daily/weekly briefings on topics you define."),
    ("Lead Enrichment", "$0.25–$1.00/lead", "Per-lead pricing for enrichment pipelines. Volume discounts from 1,000+/mo."),
    ("Custom SaaS Product", "$8,000–$25,000", "Full micro-SaaS with Tavily backend — dashboard, user auth, subscriptions."),
  ],
  'client_script': "Email to a VP of Sales:\n\nSubject: Your reps are researching prospects manually — quick question\n\nHi [Name],\n\nHow long does it take your reps to research a new account before a cold call? If it's more than 5 minutes, you're losing productivity that compounds across your entire team.\n\nI build AI research tools that enrich your lead list automatically — company news, funding rounds, hiring signals, recent product changes — all surfaced before your rep picks up the phone.\n\nI set this up for [similar company type] and their reps went from 8 calls/day to 14 calls/day with better open rates because they knew their prospect before dialling.\n\nWorth a 20-minute demo?",
  'extra_prompts': [
    ("Lead Enrichment Agent Prompt", "You are a B2B lead intelligence agent. For each company in the list provided: 1) Search for their latest news (last 30 days) — funding rounds, product launches, leadership changes, layoffs, 2) Find their estimated employee count and recent hiring signals (what departments are they building?), 3) Identify the most relevant trigger event that makes them a potential buyer for [product/service], 4) Research their current technology stack if detectable, 5) Find the best contact point — a specific person's name and LinkedIn URL if possible. Return results in JSON with keys: company_name, latest_news, employee_count, hiring_signals, trigger_event, tech_stack, best_contact. Cite your search sources."),
    ("News Monitoring System Prompt", "You are a news monitoring agent for [company/investor]. Your job runs every morning at 6am. Monitor these topics: [list topics/companies]. For each item monitored, determine if the news is: MATERIAL (requires immediate action or awareness), NOTABLE (worth including in the weekly digest), or NOISE (not relevant). For MATERIAL items, send an immediate alert with: what happened, why it matters, and recommended action. For the weekly digest, produce a clean briefing with NOTABLE items grouped by topic. Ignore NOISE. Today's search results: [Tavily output]. Process and deliver appropriately."),
    ("Competitive Intelligence Pipeline", "Design a complete competitive intelligence pipeline using Tavily as the data source. The pipeline monitors [X competitors] for [company]. Weekly automated workflow: 1) Tavily searches each competitor for: new features (check their changelog/blog), pricing changes (check pricing page), job postings that signal strategic direction (check LinkedIn/jobs page), press coverage (check news), customer complaints (check G2/Reddit/Twitter), 2) Claude analyses changes and rates them by threat level (High/Medium/Low), 3) Report is formatted and emailed to [stakeholders] every Monday at 8am. Map this as a Make or n8n workflow with every step specified."),
  ],
  'advanced_steps': [
    ("Cache Expensive Searches", "For research that repeats on the same topics (competitor monitoring, recurring client briefs), implement a simple cache: store Tavily results in a database (Supabase or Airtable) with a timestamp. Before making a new API call, check if you searched this query in the last 24 hours. For static information (company descriptions, product details), cache for 7 days. This can cut your Tavily API costs by 40–60% on recurring workflows."),
    ("Search Depth Strategy", "Use search_depth='basic' for high-volume, low-stakes lookups (lead enrichment at scale). Use search_depth='advanced' for client-facing research products where accuracy matters. Advanced uses 2 credits vs 1 for basic but retrieves significantly more content per URL. The rule: if the output is a deliverable you're charging for, use advanced. If it's a filter/triage step, use basic."),
    ("Build a Search Query Library", "Great Tavily results start with great queries. Build a library of high-performing search templates: '[Company] product launch OR new feature 2025', '[Company] CEO site:linkedin.com OR site:twitter.com', '[Company] pricing OR plans site:[competitor.com]'. Test and refine over 30 days. Your query library becomes a proprietary research asset."),
  ],
}

EXT['superagent'] = {
  'use_cases': [
    ("Whop Community AI Manager", "Deploys a Superagent for a fitness coach's Whop community with 500+ members. The agent onboards new members, answers FAQ questions 24/7, flags members who've been inactive for 14 days, and sends a weekly engagement brief to the coach. Charges $299/mo. Signs 8 Whop creators = $2,392 MRR."),
    ("Personal AI Business Operator", "Builds a Superagent that manages their own freelance business: tracks clients and projects in entities, sends weekly status updates, monitors overdue invoices, and drafts proposals. Frees up 10+ hours/week. The agent pays for itself in recovered time on day one."),
    ("AI Sales Agent", "Deploys a Superagent connected to Gmail and a CRM entity. The agent monitors the inbox, qualifies inbound leads, sends personalised responses, and books discovery calls via Calendly link. Charges clients $800/mo for the managed service. Runs 5 clients simultaneously."),
    ("Knowledge Base Agent as Product", "Builds a Superagent trained on a company's entire documentation and sells it as a 'Product Expert' for their customer support team. The agent answers internal questions with sources. Charges $500/mo per company. Runs 10 companies = $5K MRR."),
    ("Automated Research Agent", "Sets up a Superagent that every morning runs a Perplexity search on their client's competitors, formats the findings, and emails a briefing — automatically, every weekday at 8am via a scheduled automation. Charges $400/mo per client. 12 clients = $4,800 MRR."),
  ],
  'more_streams': [
    ("Agent White-Label Platform", "$2K–$10K setup + $200/mo", "Build a branded AI agent for a company and license it to their customers. The company resells it as their own AI assistant. You manage the infrastructure."),
    ("Multi-Agent System for Enterprise", "$10K–$40K/project", "Build an interconnected system of specialised Superagents for enterprise: one for sales, one for support, one for operations, one for reporting. All sharing a central data entity layer."),
  ],
  'niche_table': [
    ("Whop Community Creators", "Member management, engagement, onboarding", "$200–$500/mo per community"),
    ("Freelancers / Solopreneurs", "Business operations, client management", "$100–$300/mo"),
    ("SMB Sales Teams", "Lead qualification, inbox management, CRM", "$500–$1.5K/mo"),
    ("Online Coaches", "Client check-ins, progress tracking, FAQ", "$200–$500/mo"),
    ("SaaS Companies", "Customer onboarding, support, feature adoption", "$1K–$5K/mo"),
  ],
  'pricing_tiers': [
    ("Personal Agent Setup", "$500–$1,500", "Custom Superagent with identity, memory, 3 entities, 2 automations. 3-day delivery."),
    ("Business Agent", "$2,000–$5,000", "Full business agent — integrations, entities, automations, Telegram deployment. 1 week."),
    ("Agent as a Service", "$300–$1,000/mo", "You manage and maintain a deployed agent for a client. Includes updates and monitoring."),
    ("Enterprise Agent System", "$10,000–$40,000", "Multi-agent architecture for enterprise. Discovery → design → build → deploy → train."),
  ],
  'client_script': "DM to a Whop creator:\n\nHey [Name] — I've been in your community for a while. Love the content.\n\nQuick question: how are you currently handling new member onboarding and keeping members engaged between your posts? I know that's a huge time drain for most creators.\n\nI deploy AI agents specifically for Whop communities — they handle onboarding automatically, answer member questions 24/7, and flag anyone who's going quiet before they cancel. A few creators I work with have seen their member retention improve by 20–30% in the first month.\n\nWant me to show you what it would look like for [Community Name]? 15 minutes.",
  'extra_prompts': [
    ("Agent SOUL Design", "Help me design the soul and identity for a Base44 Superagent named [Agent Name] for [use case]. Create: 1) IDENTITY.md — name, personality description (3 adjectives), what makes this agent unique, how it introduces itself, 2) SOUL.md — its core values (5), how it makes decisions when instructions conflict, what it will never do, how it handles errors, its communication style, 3) USER.md template — what information should this agent collect about each user it serves? 4) memory.md template — what ongoing facts should it track per user? Write these as actual markdown files I can use directly."),
    ("Automation Architecture", "Design the complete automation system for a Superagent serving [use case]. For each automation: 1) Type (scheduled / entity trigger / connector), 2) Trigger specification (exact schedule or entity event), 3) What the agent should do when triggered (step by step), 4) What data it needs access to (entity names and fields), 5) What external actions it takes (email, Slack, calendar, etc.), 6) Success confirmation — how do I know it ran correctly? Design 5 automations that together create a complete autonomous operation loop for this use case."),
    ("Client Onboarding Agent Prompt", "You are ATLAS, the AI business agent for [Client Company]. You have been given access to their client database, email (Gmail), and project management system. Your daily operations: 1) Every morning at 9am: check for new clients added yesterday, send each a personalised welcome email with their onboarding checklist, 2) Every Monday: generate a client health report showing each client's project status, last contact date, and any overdue items. Send to [owner's email], 3) When any project entity is updated to status 'at_risk': immediately notify the owner via Slack with the client name, project details, and recommended action. Always be professional, specific, and proactive. If you're unsure about a decision, flag it to the owner rather than acting."),
  ],
  'advanced_steps': [
    ("Memory Architecture Matters", "Design your agent's memory.md file as a structured document from day one. Create clear sections: [CLIENT_PROFILES], [ONGOING_PROJECTS], [PREFERENCES_AND_RULES], [IMPORTANT_DECISIONS]. An agent with well-organised memory is dramatically more capable than one with a dump of unstructured notes. Review and clean memory.md monthly — stale memory is worse than no memory."),
    ("Test Automations With Low-Stakes Data First", "Before enabling any automation that sends external messages (emails, Slack, SMS), test it 5 times with dummy data. Check: does it run at the right time? Does it use the right data? Does the message sound right? Is the recipient correct? One automation that emails the wrong person or sends an embarrassing message destroys client trust instantly. Test in dev mode first."),
    ("Build a Skill Library", "For any operation your agent does more than 3 times, write it as a reusable skill in .agents/skills/. Skills are callable scripts that your agent can invoke reliably. A library of 20 skills makes your agent dramatically more capable and consistent than inline instructions. Share your best skills between client agents — you build it once, it serves many."),
  ],
}

EXT['openaiagents'] = {
  'use_cases': [
    ("Enterprise Customer Service Agent", "Builds a multi-agent customer service system for a 500-person company. Triage agent routes tickets → Product Expert agent answers product questions → Billing agent handles billing disputes → Escalation agent flags complex cases for humans. Charges $30,000 build + $3,000/mo managed service."),
    ("Autonomous Research & Report System", "Builds a research pipeline for a management consultancy: Research Agent searches web (Tavily) + databases → Analysis Agent identifies patterns → Writing Agent drafts report → QA Agent checks for hallucinations → delivery to client. Charges $12,000 build. Replicates in 3 hours what consultants bill $8,000 for."),
    ("Document Processing Agent", "Processes insurance claims, loan applications, or contract reviews using a multi-agent pipeline: Extraction Agent pulls data from PDFs → Validation Agent checks against rules → Decision Agent recommends approve/review/reject → Reporting Agent logs everything. Charges $20K–$60K per enterprise deployment."),
    ("AI Sales Development Agent", "Builds a sales agent that operates in background: researches leads with Tavily, drafts personalised outreach via Gmail, logs all activity to CRM, flags replies for human follow-up. One SDR agent replaces $4K–$6K/mo of human SDR cost. Charges $8K build + $1K/mo managed."),
    ("Compliance Monitoring Agent", "Monitors regulatory publications, contract databases, and internal policy docs for compliance risks. Agents run on schedule, compare new regulations to internal policies, flag gaps, and produce monthly compliance briefings. Charges $15K–$50K per enterprise engagement."),
  ],
  'more_streams': [
    ("Agent Framework Training", "$2K–$8K/workshop", "Teach enterprise development teams to build with the OpenAI Agents SDK. 2-day workshop. Companies pay well for internal capability building."),
    ("Agent Architecture Consulting", "$5K–$20K/engagement", "Design the architecture for a company's multi-agent system before their team builds it. Blueprint, not implementation. High-value, low-time-intensity work."),
  ],
  'niche_table': [
    ("Insurance / Claims Processing", "Document extraction, decision support", "$30K–$100K/deployment"),
    ("Financial Services", "Compliance monitoring, report generation", "$20K–$80K/project"),
    ("Legal / Contracts", "Document review, clause extraction, risk flagging", "$15K–$50K/project"),
    ("Sales / Revenue Teams", "SDR automation, lead research, outreach", "$8K–$20K build + $1K/mo"),
    ("Management Consultancies", "Research automation, report generation", "$10K–$30K/build"),
  ],
  'pricing_tiers': [
    ("Architecture Blueprint", "$3,000–$8,000", "Design the agent system — roles, handoffs, guardrails, tools — without building it. Delivered as technical spec + diagram."),
    ("Single Agent Build", "$5,000–$15,000", "One production agent with tools, guardrails, and tracing. Fully documented. 2 weeks."),
    ("Multi-Agent System", "$15,000–$60,000", "3–8 specialist agents with orchestration layer. Enterprise production-grade. 4–8 weeks."),
    ("Managed Agent Service", "$2,000–$8,000/mo", "Host, monitor, maintain, and improve the agent system. Monthly SLA."),
  ],
  'client_script': "Email to a VP of Operations at a financial services firm:\n\nSubject: Your document processing team — a question\n\nHi [Name],\n\nI'm curious: how many FTEs do you currently have processing [loan applications / insurance claims / contracts] that follow the same review criteria every time?\n\nI've been building AI agent systems that handle this kind of structured document processing with 95%+ accuracy — reviewing documents, extracting data, checking against rules, and flagging exceptions for human review. The system documents every decision with a full audit trail, which your compliance team will appreciate.\n\nI recently deployed a similar system for [similar company type] that processes 500 documents/day that previously required 6 reviewers.\n\nWould a 30-minute technical overview be worthwhile? I'll come with a working demo specific to your document type.",
  'extra_prompts': [
    ("Multi-Agent System Design", "Design a complete multi-agent system using the OpenAI Agents SDK for [business problem]. Specify: 1) Orchestrator agent — its role, instructions, and handoff decision logic, 2) Each specialist agent — name, role, system prompt (50+ words each), tools needed, typical inputs and outputs, 3) Handoff conditions — when does the orchestrator pass to each specialist? What data is passed in the handoff? 4) Input guardrails — what inputs should trigger an immediate stop? 5) Output guardrails — what outputs need validation before leaving the system? 6) Tracing strategy — what should be logged for each agent interaction? 7) Estimated token cost per end-to-end run using GPT-4o. Output as a complete technical specification."),
    ("Guardrail Design Framework", "Design a comprehensive guardrail system for an AI agent deployed in [context — e.g. customer service / financial advice / healthcare]. Input guardrails to implement: 1) PII detection and blocking (what counts as PII in this context?), 2) Off-topic request filtering (what is out of scope for this agent?), 3) Jailbreak attempt detection (what patterns indicate manipulation?), 4) Competitor mention handling. Output guardrails to implement: 1) Hallucination risk signals (when should output be flagged for review?), 2) Regulatory compliance check (what phrases or claims are prohibited in this industry?), 3) Tone and brand voice validation. For each guardrail, specify: the check logic, the action taken on trigger (block/warn/log), and the user-facing message."),
    ("Tracing and Observability Setup", "Set up a complete observability system for a multi-agent deployment. For each agent run, log: 1) Input received (sanitised — no PII), 2) Which agent handled it, 3) Tools called with inputs and outputs, 4) Handoffs made and reasons, 5) Final output, 6) Token usage and cost, 7) Latency per agent and total, 8) Any guardrail triggers. Build a Supabase table schema to store this data. Then write a weekly analytics query that produces: average cost per run, most common failure points, agent utilisation rates, and top reasons for human escalation. This data justifies your managed service retainer and shows clients ROI."),
  ],
  'advanced_steps': [
    ("Start With the Simplest Agent That Works", "The temptation in multi-agent design is to build the full architecture immediately. Resist it. Build one agent that does the core task well first. Then identify the one thing it can't handle — that becomes your second agent. Grow the crew organically from real failure points, not imagined ones. Systems that start simple and grow real are 10x more robust than systems designed comprehensively upfront."),
    ("The Handoff Context Protocol", "Every handoff between agents should include: 1) What the previous agent did, 2) What it found, 3) Why it's handing off, 4) What the receiving agent needs to do, 5) Any relevant constraints. A sloppy handoff loses context and produces bad output. Template: 'The Research Agent found [X]. It is handing off to the Writing Agent because [Y]. The Writing Agent should [Z] and must not [constraint].'"),
    ("Cost Engineering for Enterprise", "Enterprise clients ask: 'What does it cost per run?' Know your numbers. Profile your agent system: how many tokens per agent? How many tool calls? Use GPT-4o-mini for simple routing agents (10x cheaper than GPT-4o) and GPT-4o only for agents that need reasoning. A well-architected system can often cut runtime cost by 60–80% vs a naive implementation — and that's a compelling business case."),
  ],
}

EXT['nemoclaw'] = {
  'use_cases': [
    ("AI Security Auditor", "Conducts AI security audits for companies deploying chatbots and AI agents. Systematically tests for prompt injection, data leakage, PII exposure, and jailbreaks. Delivers a risk report with severity ratings. Charges $5,000–$15,000 per audit. Every company deploying AI is a potential client."),
    ("Compliance Consultant (EU AI Act)", "Helps European companies document their AI systems for EU AI Act compliance. NemoClaw's NeMo Guardrails provides the technical documentation required for 'high-risk AI' classification. Charges $10,000–$40,000 per engagement. Timeline: 2025–2026 compliance deadline creates urgency."),
    ("NVIDIA NIM Deployment Partner", "Certified partner for deploying NVIDIA NIM inference infrastructure on-premise. Targets enterprises that need to run LLMs locally for data sovereignty. Charges $20K–$80K per deployment. Positions as 'the only way to run AI without your data leaving your building'."),
    ("Red Team AI Service", "Runs 'red team' exercises against a company's AI deployments — adversarial testing, jailbreak attempts, data extraction tests, model inversion attacks. Delivers a penetration test report. Charges $8K–$25K per engagement. Growing demand as AI failures become newsworthy."),
    ("Healthcare AI Compliance", "Specialises in helping healthcare companies deploy HIPAA-compliant AI. NeMo Guardrails provides PII detection and output filtering. NIM enables on-premise deployment. Charges $30K–$100K+ per enterprise engagement. Healthcare has budget, urgency, and compliance requirements."),
  ],
  'more_streams': [
    ("AI Security Training", "$2K–$8K/workshop", "Train development teams on AI security — prompt injection defence, guardrail implementation, adversarial testing. Growing demand from security teams trying to understand AI risk."),
    ("AI Security Retainer", "$2K–$8K/mo", "Ongoing monitoring of a client's AI deployments. Monthly security briefing, new vulnerability testing, guardrail updates as new attack patterns emerge."),
  ],
  'niche_table': [
    ("Healthcare / HIPAA", "On-premise LLM, PII protection, compliance docs", "$30K–$100K+ project"),
    ("Financial Services", "AI compliance, data sovereignty, audit trails", "$20K–$80K project"),
    ("Legal / Law Firms", "Client confidentiality, on-premise deployment", "$15K–$50K project"),
    ("Enterprise SaaS (EU)", "EU AI Act compliance documentation", "$10K–$40K engagement"),
    ("Government / Defence", "Secure AI deployment, classified data handling", "$50K–$500K+ contract"),
  ],
  'pricing_tiers': [
    ("AI Security Audit", "$5,000–$15,000", "Systematic testing of one AI deployment. Report with findings, risk ratings, remediation plan. 2 weeks."),
    ("Guardrail Implementation", "$10,000–$30,000", "Design and deploy NeMo Guardrails for an existing AI system. Includes documentation. 3–4 weeks."),
    ("NIM Deployment", "$20,000–$80,000", "Full on-premise NVIDIA NIM infrastructure deployment. GPU provisioning, model deployment, monitoring."),
    ("Compliance Package", "$15,000–$50,000", "Full AI compliance documentation for EU AI Act / HIPAA / SOC2. Audit trail + attestation."),
  ],
  'client_script': "Email to a CISO or CTO at a company using AI in production:\n\nSubject: Your AI deployment — a compliance question\n\nHi [Name],\n\nI noticed [Company] is using [AI product/chatbot/agent] in production. Quick question: do you have documentation of what guardrails are in place and what happens when the system encounters adversarial inputs?\n\nThe EU AI Act, FTC enforcement actions, and sector-specific regulations (HIPAA, SOX) are increasingly requiring companies to document and test their AI deployments. Undocumented AI deployments are becoming a legal liability.\n\nI specialise in AI security audits and compliance documentation for companies exactly like yours. I'll identify your current exposure and deliver a remediation roadmap.\n\nI can scope the engagement for your specific deployment in a 30-minute call. Worth the conversation?",
  'extra_prompts': [
    ("AI Security Test Plan", "Create a comprehensive security test plan for auditing [type of AI deployment — e.g. a customer service chatbot / an internal knowledge base agent / a document processing system]. The test plan should cover: 1) Prompt injection attacks — 10 specific test inputs designed to override system instructions, 2) Data exfiltration attempts — prompts designed to extract training data, system prompts, or other users' data, 3) Jailbreak techniques — role-play, hypothetical framing, gradual escalation, token smuggling, 4) PII extraction tests — attempts to get the system to reveal or generate personally identifiable information, 5) Business logic attacks — inputs designed to exploit the specific use case (e.g. get a billing agent to issue refunds it shouldn't). For each test category: expected safe response, signs of vulnerability, severity rating if vulnerable."),
    ("NeMo Guardrails Config", "Write a complete NeMo Guardrails configuration (config.yml + Colang files) for a [type of AI assistant — e.g. customer service bot / HR assistant / financial advisor assistant] deployed by [company type]. The guardrails should: 1) Block all off-topic requests (define what's in-scope vs out-of-scope), 2) Detect and block attempts to extract system instructions, 3) Filter PII from both inputs and outputs (define what counts as PII in this context), 4) Block competitor comparisons, 5) Ensure regulatory compliance (list 3 specific things this assistant must never say in [industry]). Write production-ready Colang with realistic user utterance examples for each rule."),
    ("EU AI Act Compliance Report", "Write an AI system compliance assessment template for the EU AI Act for a [system type] classified as [risk level — limited/high]. Include: 1) System description and intended purpose, 2) Risk classification justification (why this risk level applies), 3) Technical documentation requirements — list all 15 items required under Article 11, 4) Conformity assessment procedure for this risk class, 5) Human oversight measures in place, 6) Data governance documentation required, 7) Ongoing monitoring obligations post-deployment, 8) Incident reporting requirements. Flag every section where legal review is essential before filing."),
  ],
  'advanced_steps': [
    ("Lead With the Regulation", "Security is abstract. Fines are concrete. Always open conversations with: 'The EU AI Act Article 10 requires companies to document [specific requirement]. Your current deployment doesn't have that documentation.' Lead with the legal obligation, not the technical risk. CISOs and Legal teams respond to regulatory exposure — they budget for it. They don't budget for 'AI security best practices'."),
    ("Build a Repeatable Audit Framework", "Create a standardised 50-point AI security checklist that you run on every engagement. Automate as much of it as possible using scripts that test prompts systematically. A repeatable framework means each audit takes less time while the invoice stays the same. Over 10 audits, your effective hourly rate doubles."),
    ("Get NVIDIA Partner Certified", "Apply for NVIDIA's Partner Network as an NIM deployment partner. Certified partners get referrals from NVIDIA's sales team, access to pre-sales support, and co-marketing opportunities. Enterprise clients trust certified partners more than independents. The certification process takes 4–6 weeks and unlocks a deal flow you can't get any other way."),
  ],
}

EXT['dify'] = {
  'use_cases': [
    ("White-Label AI Product Studio", "Builds white-label AI assistants for 6 SaaS companies. Each company gets a branded AI assistant embedded in their product — trained on their docs, their product knowledge, their brand voice. Charges $3,000 setup + $500/mo. Revenue: $3,000 MRR + steady setup fees."),
    ("RAG Knowledge Base Agency", "Builds internal knowledge base AI tools for companies with large documentation libraries. One enterprise client has 10,000 internal documents. Dify's RAG pipeline makes them all searchable by natural language. Charges $8,000 build + $1,000/mo. Becomes mission-critical infrastructure."),
    ("No-Code AI Product Launcher", "Launches niche AI micro-SaaS products on Dify without heavy coding: a 'Legal Contract Reviewer', a 'Job Description Writer', a 'SEO Brief Generator'. Each product is a Dify workflow with a Stripe paywall. 3 products × 100 subscribers × $19/mo = $5,700 MRR."),
    ("Customer Support AI Consultant", "Replaces expensive live chat support for e-commerce and SaaS companies with Dify-powered AI. Trained on their FAQ, product docs, and past support tickets. Resolves 70% of tickets without human intervention. Charges $5,000 setup + $800/mo. Clients save $2K–$5K/mo in support costs."),
    ("Developer Tool Builder", "Uses Dify's API to build developer-facing AI tools with a clean interface. Charges other developers for access. Focuses on niche developer pain points: 'Code Review API', 'Commit Message Generator', 'Test Case Writer'. Sells B2D (business-to-developer) at $29–$99/mo."),
  ],
  'more_streams': [
    ("Dify Plugin Development", "$2K–$10K/plugin", "Build custom Dify plugins (tools that agents can call) for enterprise clients. Custom integrations with proprietary systems that don't have off-the-shelf connectors."),
    ("Open-Source Contribution + Consulting", "$5K–$20K/engagement", "Contribute to Dify's open-source codebase, build a reputation in the community, then convert community visibility into enterprise consulting engagements."),
  ],
  'niche_table': [
    ("SaaS Companies", "In-product AI assistant, onboarding bot", "$3K–$8K setup + $500/mo"),
    ("E-commerce / DTC", "Customer support AI, product recommendation", "$2K–$5K setup + $400/mo"),
    ("Legal / Finance", "Document Q&A, compliance assistant", "$5K–$15K setup + $1K/mo"),
    ("Internal Tools / HR", "Policy assistant, onboarding helper", "$3K–$8K setup + $500/mo"),
    ("Developers / Dev Tools", "Code helpers, workflow automation", "$29–$99/mo per user"),
  ],
  'pricing_tiers': [
    ("Starter App", "$1,500–$3,000", "Simple Dify chatbot or workflow. RAG on up to 50 documents. 1-week delivery."),
    ("Production AI Tool", "$4,000–$10,000", "Full Dify deployment — RAG pipeline, multi-model support, API access, user auth. 2–3 weeks."),
    ("Enterprise Knowledge Base", "$10,000–$30,000", "Large-scale RAG on 1,000+ documents. Custom chunking strategy. Integration with existing systems."),
    ("Monthly Managed Service", "$500–$2,000/mo", "Model updates, knowledge base updates, usage monitoring, performance optimisation."),
  ],
  'client_script': "Email to a SaaS founder:\n\nSubject: Your docs — do users actually find answers there?\n\nHi [Name],\n\nI've used [Product] and noticed the help docs are thorough — but they're designed to be searched, not answered. Most users give up and email support instead.\n\nI build AI assistants that sit on top of existing documentation and answer questions instantly with specific, sourced answers. Setup takes 1–2 weeks. For [Product], it would handle the top 80% of support tickets automatically.\n\nOne of my clients reduced their support volume by 65% in the first month after deployment.\n\nI can show you a working demo on your actual docs in 48 hours — no commitment. Interested?",
  'extra_prompts': [
    ("RAG Knowledge Base Design", "I'm building a Dify RAG application for [company type] with approximately [number] documents covering [topics]. Design the optimal knowledge base architecture: 1) Document segmentation strategy — what chunk size and overlap is appropriate for this content type? 2) Embedding model recommendation — which Dify-supported embedding model best suits this use case? 3) Retrieval strategy — top-k retrieval, similarity threshold recommendations, reranking configuration, 4) Metadata strategy — what metadata should be stored with each chunk to improve filtering? 5) Update strategy — how often should the knowledge base be reindexed and how should we handle document versioning? 6) Testing plan — how do I evaluate retrieval quality before launching to users?"),
    ("Workflow Agent Design", "Design a Dify workflow for [specific automated task]. The workflow should: 1) Start with [trigger — user input / scheduled / webhook], 2) Process through these nodes in order: [describe each step], 3) Use [model name] for [reasoning/generation steps] and [different model] for [simpler steps — cost optimisation], 4) Include an error handling branch that [describes fallback behaviour], 5) Output [describe final output format and destination]. Draw this as a node-by-node spec I can build directly in Dify's visual editor. Note which nodes are LLM nodes vs tool nodes vs condition nodes."),
    ("Customer Support Agent System Prompt", "You are [Company]'s AI support assistant. You have access to [Company]'s complete knowledge base including product documentation, FAQ, pricing, and policies. Your guidelines: 1) Answer questions using only information in your knowledge base — never make up features, prices, or policies, 2) If you're not certain, say 'Let me check our documentation' and retrieve the answer rather than guessing, 3) For billing issues, always offer to escalate to a human: 'I'd like to connect you with our billing team for this', 4) Match the user's tone — if they're frustrated, be extra patient; if they're casual, be friendly, 5) End every resolved conversation with 'Is there anything else I can help you with?' 6) Log any question you can't answer in a feedback tag for the team to review. Never say 'I don't know' without offering a next step."),
  ],
  'advanced_steps': [
    ("Chunking Strategy Is Everything in RAG", "The most common RAG failure is poor chunking. Rules: 1) Chunk by logical unit (paragraph or section), not by character count, 2) Include the parent heading in every chunk for context, 3) For structured docs (FAQs, product specs), chunk by question/answer pair, 4) Set overlap to 10–15% of chunk size so concepts at boundaries aren't split, 5) Test retrieval quality by asking 20 questions you know the answer to and checking if the right chunks are retrieved. Fix chunking before anything else."),
    ("Multi-Model Cost Strategy", "Dify lets you use different models for different nodes. Use this strategically: GPT-4o or Claude for nodes requiring complex reasoning (answer generation, analysis), GPT-4o-mini or Gemini Flash for simpler nodes (classification, keyword extraction, reformatting). A production application can reduce inference costs by 50–70% with thoughtful model assignment without sacrificing output quality."),
    ("Build a Feedback Loop", "Add a thumbs up/down rating to every Dify chatbot output. Connect this to a Notion or Airtable database. Review the thumbs-down responses weekly. These are your knowledge base gaps. For every 5 thumbs-down on the same question type, add a dedicated document addressing it. After 30 days, your retrieval accuracy will be measurably better than a static deployment."),
  ],
}

EXT['crewai'] = {
  'use_cases': [
    ("Content Production Machine", "Builds a CrewAI content crew for a marketing agency: Research Agent finds trending topics + competitor content → Writer Agent drafts the article → SEO Agent optimises → Editor Agent polishes → Publisher Agent formats for CMS. Produces 20 articles/day. Agency charges clients $100/article = $2K/day revenue. Build cost: $8,000. Runs continuously."),
    ("Market Intelligence Service", "Deploys a CrewAI crew that monitors 10 companies for a private equity firm: News Agent monitors press releases → Data Agent pulls financial signals → Analyst Agent identifies patterns → Report Agent writes the weekly brief. Charges $5,000/mo. 3 clients = $15K MRR."),
    ("Autonomous Sales Prospector", "Builds a CrewAI prospecting crew: Research Agent finds leads matching ICP → Enrichment Agent gathers context → Personalisation Agent writes custom intros → Outreach Agent drafts emails → CRM Agent logs everything. Replaces one full-time SDR at $60K/yr. Charges $10K build + $1,500/mo managed."),
    ("Product Research Crew", "Runs product research for e-commerce brands: Trend Agent monitors TikTok/Amazon trends → Competition Agent analyses competitor products → Pricing Agent analyses margin opportunity → Report Agent delivers weekly product opportunity brief. Charges $3,000/mo per brand."),
    ("Technical Documentation Crew", "Builds a documentation crew for software companies: Code Reader Agent parses the codebase → API Doc Agent writes API reference → Tutorial Agent writes quickstart guides → Reviewer Agent checks accuracy. Documentation that takes a dev team months is complete in days. Charges $15K–$40K per documentation project."),
  ],
  'more_streams': [
    ("CrewAI Training & Consulting", "$3K–$10K/engagement", "Teach data science and engineering teams at companies to build their own CrewAI systems. 3-day workshops. High demand as companies try to build in-house AI capability."),
    ("Productised Crew Templates", "$200–$1,000/template", "Package well-built CrewAI crews as Python repositories with documentation and sell on GitHub or Gumroad. A 'Market Research Crew' template with 15 stars sells itself."),
  ],
  'niche_table': [
    ("Marketing Agencies", "Content production, competitive monitoring", "$3K–$10K build + $500/mo"),
    ("Private Equity / VC", "Portfolio monitoring, deal flow research", "$5K–$15K/mo retainer"),
    ("SaaS / Product Companies", "User research, competitor analysis, feature research", "$5K–$15K build"),
    ("Sales Teams / RevOps", "Prospecting, enrichment, outreach automation", "$8K–$20K build + $1K/mo"),
    ("Software Development", "Documentation, code review, test generation", "$10K–$40K/project"),
  ],
  'pricing_tiers': [
    ("Single-Agent Script", "$1,500–$3,000", "One specialist agent as a standalone Python script. Documented and tested. 1 week."),
    ("Two-Agent Crew", "$3,000–$6,000", "Orchestrator + one specialist. One clear workflow. Documented. 1–2 weeks."),
    ("Production Crew", "$8,000–$20,000", "Full multi-agent crew — 3–6 agents, tools, memory, error handling, API wrapper. 3–4 weeks."),
    ("Managed Crew Service", "$1,000–$5,000/mo", "You host, monitor, and maintain the crew. Handle model upgrades, tool failures, output quality."),
  ],
  'client_script': "LinkedIn DM to a content marketing manager:\n\nHey [Name] — I saw [Company] is producing [frequency] content pieces per [week/month]. Quick question: what does your content production process look like end-to-end — from research to publish?\n\nI build AI agent systems that automate content production pipelines. Not just AI writing — the full workflow: research, drafting, SEO optimisation, editing, and formatting. One of my clients went from 4 articles/week to 20 with the same team size.\n\nI'll map out what that looks like specifically for [Company]'s content workflow — free — on a 20-minute call. Worth it?",
  'extra_prompts': [
    ("Content Crew Architecture", "Design a complete CrewAI content production system for a [type] company publishing [frequency] pieces per [week/month]. Specify every agent: 1) Role title and specific focus (not generic — 'B2B SaaS SEO Strategist' not 'SEO Agent'), 2) Goal (one specific, measurable objective), 3) Backstory (3–4 sentences establishing expertise and working style), 4) Tools needed (web search, file writer, SEO API, etc.), 5) Typical inputs and outputs. Then specify: the task sequence, expected output of each task, how tasks connect, the final deliverable format. Include the Python code structure (agents + tasks + crew setup) as a working template."),
    ("Crew Debugging Guide", "My CrewAI crew for [task] is producing [describe the problem — e.g. repetitive content / hallucinated facts / agents not using tools / slow performance]. Diagnose the likely root cause and provide fixes: 1) Is this a role definition problem? (vague backstory, conflicting goals), 2) Is this a task specification problem? (unclear expected_output, missing context), 3) Is this a tool configuration problem? (tool not being called, wrong parameters), 4) Is this a model problem? (temperature too high, wrong model for the task), 5) Is this an orchestration problem? (wrong process type, missing context between tasks). For each diagnosis, provide the specific code change to fix it."),
    ("ROI Pitch for Crew System", "Write a compelling ROI analysis for selling a CrewAI [type of crew] system to [target buyer role]. The system replaces [describe the manual process]. Current state: [X people doing Y hours/week at $Z/hour]. With the crew: [describe the automation and what humans still do]. Calculate: 1) Current annual labour cost, 2) Annual cost of the crew system (build amortised over 2 years + monthly operating cost), 3) Net annual savings, 4) ROI percentage, 5) Payback period in months. Then write the one-page business case I can present to [CFO / VP Operations / CEO]. Lead with the financial outcome, not the technology."),
  ],
  'advanced_steps': [
    ("The Backstory Is the System Prompt", "In CrewAI, the agent's backstory is functionally its system prompt. A generic backstory like 'You are a researcher' produces generic research. A specific backstory like 'You are a former Goldman Sachs equity analyst with 12 years covering the technology sector. You never cite a claim without a source. You prioritise primary data over secondary analysis. You flag uncertainty explicitly.' produces dramatically better output. Spend 30 minutes per agent on the backstory — it's the highest-leverage tuning you can do."),
    ("Use Process.hierarchical for Complex Tasks", "For tasks with dynamic, unpredictable workflows, switch from Process.sequential to Process.hierarchical. This adds a manager LLM that decides which agent to call based on the current state of the task — not a fixed sequence. Use sequential for predictable pipelines (research → write → edit). Use hierarchical for complex tasks where the path depends on what's discovered along the way."),
    ("Deploy as a REST API", "Wrap your CrewAI crew in a FastAPI endpoint so it's callable from anywhere: your n8n automation, your Make scenario, your client's dashboard. The endpoint receives inputs, kicks off the crew, and returns the output. A deployed crew API is a product — you can charge per API call, per month, or as part of a managed service. Without the API wrapper, it's just a script."),
  ],
}
