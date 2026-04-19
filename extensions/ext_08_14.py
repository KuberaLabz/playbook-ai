# Extensions batch 2: tools 08-14 (kling, sora, seedance, elevenlabs, heygen, chatgpt, claude)

EXT = {}

EXT['kling'] = {
  'use_cases': [
    ("Faceless TikTok Empire", "Runs 4 faceless TikTok channels simultaneously — motivation, luxury lifestyle, AI art, and travel. Posts 2x/day per channel using Kling-generated clips + ElevenLabs voiceover. After 3 months: 2 channels hit 50K followers and start earning from TikTok Creator Fund + brand deals. Revenue: $3K–$8K/mo."),
    ("UGC Content Agency", "Signs 5 DTC brands at $800/mo each for weekly UGC-style video content. Kling generates the clips, CapCut adds captions and music. Delivers 4–6 videos per brand per month. Revenue: $4K/mo from 5 clients."),
    ("AI Product Launch Videos", "Creates cinematic product reveal videos for Kickstarter and Indiegogo campaigns. Charges $1,500–$3,000 per campaign video. Product creators pay because great video is proven to increase funding by 30–50%."),
    ("Social Media Manager 2.0", "Offers full social media management for local businesses — strategy, content creation, posting, and reporting. Kling handles all video production. Charges $1,200/mo per client. Manages 6 clients."),
    ("Viral Clip Consultant", "Analyses trending TikTok content, reverse-engineers what makes clips go viral (first 3 seconds, motion patterns, colour), then replicates the formula for brands. Charges $2,500/mo retainer for 'viral strategy + content'."),
  ],
  'more_streams': [
    ("YouTube Shorts Channel", "$500–$5K/mo", "Post Kling-generated YouTube Shorts daily. Monetise via YouTube Partner Program (1,000 subscribers + 4,000 hours). Shorts bonus program pays per million views."),
    ("AI Video Course", "$197–$997", "Teach content creators to use Kling for their channels. Bundle with prompt templates and a 30-day content calendar. Sell on Gumroad."),
  ],
  'niche_table': [
    ("Motivation / Mindset", "TikTok/YouTube Shorts, Creator Fund", "$500–$3K/mo per channel"),
    ("Luxury Lifestyle", "Brand deals, affiliate links", "$1K–$10K/mo"),
    ("AI & Tech", "Sponsor deals, newsletter, course", "$2K–$8K/mo"),
    ("Local Business", "Social media management retainer", "$800–$2K/mo per client"),
    ("E-commerce/DTC Brands", "UGC content, product ads", "$500–$2K/mo per brand"),
  ],
  'pricing_tiers': [
    ("Single Video", "$200–$500", "One polished 15–60 second clip. Delivered in 24 hours."),
    ("Content Pack", "$800–$1,500", "8 videos — 4 formats (TikTok, Reels, Shorts, Stories). 3-day delivery."),
    ("Monthly Content", "$1,200–$3,000/mo", "20–30 videos/month. Full social media content calendar covered."),
    ("Channel Management", "$1,500–$4,000/mo", "Content + posting + community management. Full-service social."),
  ],
  'client_script': "Instagram DM to local business:\n\nHey [Business name]! Love your [product/service]. Quick question — are you posting video content on TikTok or Instagram Reels?\n\nI create short-form video content for [industry] businesses. I handled content for [similar business type] last month and they got [specific result — e.g. 200% more profile visits / their first viral post].\n\nI'll create 3 free sample videos for your business this week — no commitment, just want to show you the quality. Can I grab your menu/product photos to work from?",
  'extra_prompts': [
    ("Viral Hook Formula", "Extreme close-up of [visually striking subject — e.g. luxury watch face, coffee being poured, neon sign reflection in rain], macro lens, shallow depth of field, slow motion, [dominant colour — e.g. deep gold and black], [sound-implied action — e.g. dripping, crackling, ticking], photorealistic, cinematic, ASMR-adjacent visual quality, designed to stop scrolling in first 2 seconds"),
    ("Brand Story Sequence", "Create a 5-prompt sequence for a 30-second brand story about [brand/product]. Prompt 1: [establishing wide shot concept]. Prompt 2: [product hero shot]. Prompt 3: [human connection moment]. Prompt 4: [transformation or result]. Prompt 5: [logo/CTA frame]. Each prompt should specify camera movement, subject, environment, lighting, and connect visually to the next scene through colour or composition."),
    ("Trend Replication Prompt", "Analyse this TikTok trend: [describe the trend — visual style, motion pattern, colour palette, pacing]. Now write a Kling prompt that replicates the core viral elements of this trend but applies them to [brand/product]. The first 2 seconds must have [specific hook element]. Maintain the trend's energy while making it brand-appropriate."),
  ],
  'advanced_steps': [
    ("The 3-Account Test Strategy", "Never launch one channel — launch three simultaneously with different angles on the same niche. Run them for 30 days. The one with the highest organic reach gets all your focus and the other two get repurposed content. This surfaces what resonates with the algorithm 3x faster."),
    ("Build a Prompt Database", "After every session, save your best-performing Kling prompts with their output quality rating (1–5), the clip's view count if posted, and what made it work. After 100 prompts, you have a pattern library that makes every future session 3x faster."),
    ("Repurpose Across All Platforms", "One Kling clip → 5 platforms: TikTok (9:16), Instagram Reels (9:16), YouTube Shorts (9:16), Twitter/X (16:9 cropped), LinkedIn (1:1 square). Use CapCut's auto-reformat. One generation session = a week of content across every platform."),
  ],
}

EXT['sora'] = {
  'use_cases': [
    ("Corporate Video Producer", "Produces internal training videos, onboarding films, and executive communications for corporations. Sora handles the visual storytelling. Charges $5K–$15K per video. Companies that used to pay $30K for a video shoot now pay $8K."),
    ("Documentary Pre-Viz Studio", "Creates documentary-style pre-visualisation reels for production companies pitching to Netflix and HBO. Directors use them to secure commissions. Charges $10K–$25K per pitch reel."),
    ("Real Estate Developer Content", "Animates architectural concept art into cinematic development showcases for luxury real estate developers. Charges $2K–$5K per development. Developers use them for pre-sales before a brick is laid."),
    ("YouTube Long-Form AI Channel", "Builds a YouTube channel with Sora-generated cinematic content — documentary-style AI films, nature series, and sci-fi shorts. Monetises via AdSense ($3–$10 RPM) and Patreon. 100K subscribers earns $3K–$8K/mo."),
    ("Agency Showreel Production", "Produces cinematic showreels and capabilities films for creative agencies, PR firms, and consultancies. These companies need premium video but rarely have internal production capacity. Charges $8K–$20K."),
  ],
  'more_streams': [
    ("Educational Video Production", "$2K–$10K/project", "Create professional educational content for e-learning platforms, universities, and corporate L&D. Sora's narrative consistency makes it ideal for structured educational storytelling."),
    ("Event Highlight Films", "$1K–$5K/event", "Create cinematic highlight films for conferences, product launches, and brand events using Sora to fill gaps where footage is missing or low quality."),
  ],
  'niche_table': [
    ("Corporate / B2B", "Training, onboarding, executive comms", "$5K–$20K/video"),
    ("Film / TV Production", "Pre-viz, animatics, pitch reels", "$10K–$30K/project"),
    ("Real Estate Development", "Concept-to-cinematic visualisation", "$2K–$8K/property"),
    ("YouTube/Streaming", "AI documentary series, sci-fi shorts", "$1K–$5K/mo monetised"),
    ("Events & Conferences", "Highlight films, recap videos", "$1K–$5K/event"),
  ],
  'pricing_tiers': [
    ("Concept Reel", "$2,000–$5,000", "60–90 second cinematic concept video. 5 business days."),
    ("Short Film", "$5,000–$15,000", "2–4 minute produced short. Script, generate, edit, deliver."),
    ("Corporate Package", "$8,000–$25,000", "Full corporate video production — multiple videos, edits, formats."),
    ("Monthly Retainer", "$3,000–$8,000/mo", "Ongoing video production — 2–4 pieces per month."),
  ],
  'client_script': "LinkedIn outreach to real estate developers:\n\nHi [Name] — I saw [Development Name] is in pre-sale. Congratulations on the project.\n\nI create cinematic showcase videos for luxury developments that convert pre-sales before construction begins. Using AI production tools, I deliver full-quality videos at a fraction of traditional production costs and timelines.\n\nI made a 30-second concept clip of what a video for [Development Name] could look like — using your existing renders. Can I send it over? No commitment, just want you to see the quality.",
  'extra_prompts': [
    ("Narrative Short Film Shot", "Write a 6-prompt sequence for a 90-second cinematic short about [theme/story]. Each prompt is one scene. For each scene specify: 1) Exact camera movement and framing, 2) Subject and action, 3) Environment and time of day, 4) Lighting setup, 5) Colour grade reference, 6) How this scene connects emotionally to the previous and next. Write for Sora — prioritise temporal consistency and narrative momentum over visual spectacle."),
    ("Corporate Training Scene", "Professional corporate environment, [specific scenario — e.g. new employee onboarding meeting, product training session, safety briefing]. Realistic office setting, diverse team of professionals, natural workplace lighting, genuine interaction energy, documentary-style medium shots, no obvious AI aesthetics, authentic and relatable, suitable for internal corporate training video. Cinematic but grounded."),
    ("Architectural Visualisation", "Cinematic aerial approach to [building/development description], starting from 500m altitude, slowly descending toward the entrance, [time of day — e.g. golden hour with long shadows], [weather — e.g. clear sky, dramatic clouds], architectural photography quality, [style — e.g. Herzog & de Meuron, Zaha Hadid], photorealistic materials and lighting, no people, pure architecture showcase"),
  ],
  'advanced_steps': [
    ("The Shot List Method", "Before generating a single clip, write a complete shot list like a film director: Scene 1 — Establishing shot (wide, aerial), Scene 2 — Medium establishing (street level), Scene 3 — Hero close-up, etc. Generate each shot separately. This produces a coherent film, not a collection of unrelated clips."),
    ("Use ChatGPT as Your Script Supervisor", "Paste your shot list into ChatGPT and ask it to check for: narrative continuity, lighting consistency (day vs night), colour palette conflicts, pacing (too many slow shots in a row). Fix the shot list before generating. Saves credits and produces better output."),
    ("Colour Grade in CapCut", "All Sora clips benefit from a consistent colour grade before delivery. In CapCut Pro, create one colour preset (LUT) for your brand/client's aesthetic. Apply it to every clip in the project. This professional finishing step makes AI footage indistinguishable from professional production."),
  ],
}

EXT['seedance'] = {
  'use_cases': [
    ("Zero-Cost Content Agency", "Builds an entire content agency on Seedance's free tier. Charges clients $800–$1,500/mo for social video content. Seedance costs nothing. Pure margin from day one."),
    ("Daily Posting System", "Posts 3x/day across TikTok, Instagram Reels, and YouTube Shorts using Seedance batches. Generates a full week of content every Monday in a 3-hour session. Account hits 10K followers in 6 weeks."),
    ("Abstract Art Seller", "Creates looping abstract motion art (liquid, particles, geometric) using Seedance's free tier. Sells as: digital downloads on Etsy, NFTs on OpenSea, and screensaver packs on Gumroad. Earns $500–$2K/mo passively."),
    ("Podcast Visual Producer", "Creates motion backgrounds and B-roll for podcast video content. Podcasters are hungry for visual content as they move to YouTube. Charges $200–$500/episode. Serves 5–10 podcasters/month."),
    ("Social Media Manager Upgrade", "An existing social media manager adds Seedance to their workflow. Upgrades every client from static images to short video clips at no additional tool cost. Raises prices 40% across their book of business."),
  ],
  'more_streams': [
    ("Digital Art Downloads", "$200–$2K/mo passive", "Package Seedance motion loops as digital downloads. 'Aesthetic desktop wallpaper packs', 'meditation background loops', 'stream overlay packs' all sell well on Etsy and Gumroad."),
    ("Twitch/YouTube Overlay Packs", "$50–$500/pack", "Streamers and YouTubers buy animated overlays, transitions, and background loops. Create themed packs and sell on Streamlabs Market or Gumroad."),
  ],
  'niche_table': [
    ("TikTok / Reels Creators", "Faceless channels, viral content", "$500–$5K/mo"),
    ("Podcasters (moving to video)", "B-roll, motion backgrounds", "$200–$500/episode"),
    ("Local Businesses", "Social media video content", "$500–$1,200/mo"),
    ("Digital Art / NFT", "Motion art, loop packs", "$200–$2K/mo passive"),
    ("Streamers / YouTubers", "Overlays, transitions, backgrounds", "$50–$500/pack"),
  ],
  'pricing_tiers': [
    ("Clip Pack", "$200–$400", "10 unique motion clips in one visual style. Delivered in 24 hours."),
    ("Weekly Content", "$500–$1,000/mo", "3 clips/week for one platform. Consistent aesthetic."),
    ("Full Social Package", "$1,200–$2,500/mo", "Daily content for 2 platforms. Strategy + creation + scheduling."),
    ("Digital Download Pack", "$15–$50", "Royalty-free motion loops for creators. Sell once, deliver forever."),
  ],
  'client_script': "DM to a podcaster you follow:\n\nHey [Name] — I've been listening to [Podcast] for a while. Quick observation: your audio quality is great but now that everyone's uploading to YouTube, static images don't cut it anymore.\n\nI create short motion video clips for podcast content — abstract backgrounds, episode teasers, audiogram-style clips. Completely free for this week as I'm testing a new workflow.\n\nWant me to make a 30-second clip for your latest episode? I just need the episode title and your brand colours.",
  'extra_prompts': [
    ("Abstract Loop", "Hypnotic [material — e.g. liquid mercury / molten gold / electric plasma] flowing in slow motion, [colour palette — e.g. deep midnight blue and electric violet], [camera — macro lens, extreme close-up], particle system with [behaviour — e.g. swirling vortex / expanding waves / fractal branching], seamlessly loop-friendly ending, 4K quality, suitable for meditation app background / desktop wallpaper"),
    ("High-Energy Social Hook", "[Action description — e.g. shattered glass reforms into a diamond / city skyline erupts in golden light / ocean wave crashes in ultra slow-mo], first-frame impact, extreme visual contrast, designed for maximum scroll-stop in first 1 second, [colour grade — e.g. high contrast black and gold], cinematic slow motion, 9:16 vertical format"),
    ("Brand Motion Identity", "[Brand aesthetic — e.g. minimalist tech startup / luxury fashion house / wellness brand] visual identity in motion: [primary colour] on [background colour], [texture — e.g. clean lines / organic shapes / geometric patterns] animating slowly, [brand feeling — e.g. precision and trust / warmth and care / energy and disruption], suitable as intro/outro for brand video content, 3-second seamless loop"),
  ],
  'advanced_steps': [
    ("The Daily Batch System", "Every morning: open Seedance, collect your daily free credits, generate your daily batch (5–8 clips), rename and categorise into folders by style and colour. After 30 days, you have 150–240 clips — a full content library that feeds your channels and client work for months."),
    ("Reference Image Stacking", "Upload 2–3 reference images simultaneously as style anchors. Seedance blends them. Use this to: replicate a specific brand aesthetic, hit a colour palette precisely, or create a visual style that's uniquely yours and hard for competitors to copy."),
    ("Transition Clip Strategy", "Generate 20–30 seamless transition clips (light leaks, ink splashes, geometric wipes) that work as cuts between other clips. These are the most reusable assets in any editor's library and the fastest way to add production value to client deliverables."),
  ],
}

EXT['elevenlabs'] = {
  'use_cases': [
    ("Passive Voice Royalty Income", "Records a 5-minute high-quality voice sample, clones it on ElevenLabs, lists it in the Voice Library, and earns $200–$800/mo in royalties with zero ongoing work. A professional voice with a distinctive accent earns more."),
    ("Audiobook Production Studio", "Converts public domain books (free on Project Gutenberg) into audiobooks using cloned premium voices. Uploads to ACX/Audible and earns royalties. A library of 20 audiobooks earns $1K–$5K/mo passively."),
    ("Podcast Production Service", "Offers podcast voiceover and production services to businesses. Uses ElevenLabs to generate narration from scripts. Delivers a polished podcast episode in 4 hours. Charges $300–$800/episode."),
    ("Faceless YouTube Narrator", "Runs a YouTube channel where a cloned AI voice narrates documentary-style content over Sora/Kling visuals. Posts 2x/week. At 100K subscribers: $3K–$8K/mo from AdSense + sponsorships."),
    ("Multilingual Content Agency", "Takes a client's English podcast or video, translates it with Claude, and regenerates the audio with ElevenLabs in Spanish, Portuguese, French, and German. Charges $200–$500/video per language. 4 languages per video = $800–$2K per video."),
  ],
  'more_streams': [
    ("IVR & Business Phone Systems", "$500–$3K/setup", "Record professional IVR (phone menu) systems for businesses using cloned or studio voices. Small businesses pay $500–$1,500 for a professional phone system voice package."),
    ("Character Voices for Games/Animation", "$500–$5K/project", "Indie game developers and animators need character voices. Clone or create unique character voices for their projects. One game can need 5–20 unique voices."),
  ],
  'niche_table': [
    ("Audiobooks", "ACX, Findaway, direct sales", "$1K–$5K/mo passive (portfolio)"),
    ("Podcast Narration", "Business podcasts, thought leadership", "$300–$800/episode"),
    ("YouTube Automation", "Faceless channels, documentary style", "$1K–$8K/mo"),
    ("Corporate Training", "E-learning modules, internal training", "$500–$3K/module"),
    ("Multilingual Localisation", "Video/podcast translation + revoice", "$200–$500/language/video"),
  ],
  'pricing_tiers': [
    ("Voiceover (per minute)", "$25–$50/min", "Professional narration. 200-word script = ~1 minute. Delivered same day."),
    ("Podcast Episode", "$300–$600", "Full episode narration, audio cleanup, delivered as MP3. 48-hour turnaround."),
    ("Audiobook Production", "$800–$3,000", "Full audiobook — narration, chapter markers, ACX-ready format. Per book."),
    ("Monthly Voice License", "$300–$1,000/mo", "Clients use your cloned voice for ongoing content. Monthly license fee."),
  ],
  'client_script': "LinkedIn DM to a podcast host:\n\nHey [Name] — I've been following [podcast name]. Your content is genuinely valuable and I noticed you're still audio-only.\n\nYouTube is where podcasts grow right now — but producing a video version of every episode is time-consuming. I create the full YouTube version: AI-generated visuals synced to your audio, chapter markers, thumbnail, and description. Done in 24 hours per episode.\n\nI'll produce your latest episode as a free sample this week. Want to see what it looks like?",
  'extra_prompts': [
    ("Voiceover Script Polish", "Rewrite this script for audio narration: [paste script]. Changes needed: 1) Shorten sentences — max 15 words per sentence for easy listening, 2) Remove all parenthetical information — if it's important, rewrite it into the main sentence, 3) Replace formal written language with natural spoken English, 4) Add [pause] markers where a 1-second pause would help comprehension, 5) Add [emphasis] markers on the 2–3 most important words per paragraph. Output the revised script ready to paste directly into ElevenLabs."),
    ("Character Voice Brief", "I need to create [number] distinct character voices for [project type — e.g. a children's audiobook / indie game / animated series]. For each character provide: 1) Age and gender, 2) Personality in 3 words, 3) Speech pattern (e.g. slow and deliberate, fast and excitable, formal and clipped), 4) Regional accent or dialect if relevant, 5) ElevenLabs voice settings recommendation (stability, similarity, style — give specific numbers). Make each voice clearly distinct from the others."),
    ("Multilingual Content Plan", "I have an English [podcast/video/course] about [topic]. Help me plan a multilingual expansion. For each of these 5 languages (Spanish, Portuguese, French, German, Hindi): 1) Estimated market size for [topic], 2) Best distribution platform in that market, 3) Cultural adaptations needed in the script (not just translation — actual content adjustments), 4) Estimated monthly revenue if I hit 10K views/listeners in that market. Prioritise the languages by ROI potential."),
  ],
  'advanced_steps': [
    ("Optimise Your Voice Settings", "For each voice you use regularly, test and save the optimal settings: Stability (0.5–0.75 for natural variation), Similarity Boost (0.75–0.85 for consistency), Style Exaggeration (0.1–0.3 unless you want dramatic effect). Save these as presets. The right settings can make a mediocre voice sound professional."),
    ("Build a Script-to-Audio Pipeline", "Automate with Make/n8n: Google Docs script → trigger → Claude cleans and formats for audio → ElevenLabs API generates MP3 → uploaded to Google Drive → notification sent. Your entire voiceover workflow runs in 5 minutes with no manual steps."),
    ("Create Your Voice Brand", "Your voice is a product. Give it a name, write a description highlighting its unique qualities, and add sample audio that showcases its range. The top voices in ElevenLabs' library earn $2K–$5K/mo in royalties. The difference between $200/mo and $2K/mo is professional positioning."),
  ],
}

EXT['heygen'] = {
  'use_cases': [
    ("Faceless Course Empire", "Creates a 10-module online course using their HeyGen avatar as the instructor. Never appears on camera personally. Sells on Teachable for $497. Avatar delivers every lesson. 50 students/month = $24,850/mo."),
    ("Personalised Outbound Agency", "Sends 500 personalised HeyGen video messages per week to B2B prospects. Each 30-second video mentions the prospect's name, company, and a specific detail. Booking rate: 8–12% vs 1–2% for text emails. Generates $30K–$60K/mo pipeline for clients."),
    ("Corporate Training Producer", "Creates employee onboarding and compliance training videos for mid-size companies. Avatar presents all material. 1 script = 1 video in 10 minutes. Charges $5K–$15K for a full training programme. Produces in 1 week."),
    ("Multilingual Brand Channel", "Creates one piece of content in English, then HeyGen translates and lip-syncs it into Spanish, Portuguese, French, and German. Four markets from one production. YouTube channels in each language grow simultaneously."),
    ("Real Estate Video Agent", "Real estate agents use their HeyGen avatar to create personalised video messages for every listing and every buyer inquiry. Avatar does open house walkthroughs, market update videos, and personalised follow-ups. Charges agents $500/mo for the service."),
  ],
  'more_streams': [
    ("Talking Head Content Service", "$500–$3K/mo per client", "Create regular 'talking head' style videos for thought leaders, coaches, and executives who don't want to be on camera but need video content. Your avatar presents their script."),
    ("Avatar Licensing", "$200–$1K/mo per client", "Create a custom avatar for a business and license it to them monthly. They use it for their own content. You maintain it and charge a monthly fee."),
  ],
  'niche_table': [
    ("Online Educators / Coaches", "Course content, video lessons, updates", "$2K–$10K/course"),
    ("B2B Sales Teams", "Personalised outbound, follow-ups", "$2K–$8K/mo setup + retainer"),
    ("Corporate L&D", "Training videos, onboarding, compliance", "$5K–$25K/programme"),
    ("Real Estate Agents", "Listing videos, market updates, follow-ups", "$300–$800/mo per agent"),
    ("Content Creators", "YouTube, TikTok, regular video content", "$500–$2K/mo"),
  ],
  'pricing_tiers': [
    ("Single Video", "$200–$500", "Script-to-video in 24 hours. Avatar presents, you script."),
    ("Video Package", "$800–$2,000", "5 videos — course module, ad, onboarding, etc. 3-day delivery."),
    ("Monthly Video Service", "$1,500–$5,000/mo", "8–15 videos/month. Avatar creation + ongoing production."),
    ("Custom Avatar Creation", "$500–$2,000 one-time", "Set up client's own avatar. Includes recording guide + avatar training."),
  ],
  'client_script': "Email to a course creator:\n\nSubject: Your course content — a question\n\nHi [Name],\n\nI bought [their course] last month. The content is excellent but I noticed the video lessons were filmed on [describe the setup — e.g. a phone / basic webcam / inconsistent lighting].\n\nI create professional video content for course creators using AI avatar technology — the production quality is indistinguishable from a studio setup. More importantly, updating or expanding your course content takes minutes instead of days.\n\nI'll remake one of your existing lessons as a free demo — same content, professional production. Would that be useful to see?",
  'extra_prompts': [
    ("Personalised Outreach Script", "Write 10 personalised 30-second video scripts for outreach to [specific role — e.g. VP of Marketing at SaaS companies]. Each script should: 1) Open with the person's first name + one specific company observation (leave [COMPANY_OBSERVATION] placeholder), 2) Reference a pain point relevant to their role, 3) Deliver one specific value statement about [your product/service], 4) End with a low-friction CTA (e.g. 'reply with a ✓ if you'd like to see how'). Keep each under 75 words — exactly 30 seconds at normal speaking pace."),
    ("Course Intro Script", "Write a 90-second welcome video script for a course called [Course Name] about [topic]. The avatar presents this to new students. Script structure: 1) Acknowledge they made a good decision and validate their goal, 2) Make a specific, concrete promise about what they'll be able to do after the course, 3) Quick preview of the 5 main modules in plain English, 4) One personal/origin story moment about why you created this course (30 seconds max), 5) Exciting close that builds anticipation for Module 1. Write for spoken delivery — short sentences, natural rhythm."),
    ("Market Update Template", "Write a 60-second weekly market update script template for a [real estate agent / financial advisor / industry expert] to record as a HeyGen avatar video. Include placeholders: [WEEK_DATE], [KEY_STAT_1], [KEY_STAT_2], [TREND], [LOCAL_OBSERVATION], [CTA]. The tone should be: authoritative but warm, data-informed but not overwhelming, locally relevant. This template should be reusable every week with only the placeholders swapped out."),
  ],
  'advanced_steps': [
    ("The Training Video Quality Formula", "For your avatar training recording: 1) Film against a plain wall (cream or grey — not white), 2) Ring light at 45° angle at eye level, 3) Camera at exact eye height, 4) Wear solid colours (no patterns, no logos), 5) Speak for exactly 2 minutes at your normal pace. These 5 rules produce an avatar that passes for professional studio production. Break any one and the quality drops significantly."),
    ("Build a Video Content Calendar", "Use ChatGPT to generate a 12-week content calendar for your avatar channel. Each week: one educational video, one case study, one FAQ response. Script all 36 videos in one ChatGPT session using a batch prompt. Generate all 36 HeyGen videos in one day. Schedule with Buffer or Upload-Post. 3 months of consistent content produced in 8 hours."),
    ("Lip-Sync Audit Process", "Before sending any HeyGen video to a client, run this 30-second check: 1) Play at 1.25x speed — does lip sync feel off? 2) Check the first and last 3 seconds where sync issues are most common, 3) Play with headphones — audio quality check, 4) Watch on mobile — does it look good at small size? Fix anything that fails before delivery."),
  ],
}

EXT['chatgpt'] = {
  'use_cases': [
    ("Content Agency at Scale", "Runs a 12-client content agency. Each client gets 16 SEO articles/month at $100/article = $1,600/mo per client. ChatGPT drafts, writer QAs and publishes. Revenue: $19,200/mo. Team: 1 writer + 1 editor. Net margin: 60%+."),
    ("LinkedIn Ghostwriter", "Manages LinkedIn content for 8 executives at $1,500/mo each. Posts 5x/week per client. ChatGPT writes every post in the client's voice. Revenue: $12K/mo. Time per client: 3 hours/month."),
    ("Custom GPT Product Launch", "Builds a 'Legal Contract Generator' Custom GPT for freelancers. Trains it on 50 contract templates. Sells access for $15/mo. 300 subscribers = $4,500 MRR. Total build time: 8 hours."),
    ("Prompt Engineering Consultant", "Charges $3,000 for a one-day workshop teaching marketing teams how to use ChatGPT for their specific workflows. Runs 2–3 workshops/month. Revenue: $6K–$9K/mo."),
    ("Email Marketing Agency", "Writes full email sequences, newsletters, and drip campaigns for e-commerce brands. Charges $500–$2,000 per sequence. ChatGPT handles drafts; agency refines and delivers. 10 sequences/month = $5K–$20K/mo."),
  ],
  'more_streams': [
    ("AI Workflow Consulting", "$2K–$8K/engagement", "Audit a company's workflows, identify where ChatGPT can save 10+ hours/week per employee, build a custom implementation plan. High ROI for clients — they see payback in 30 days."),
    ("Newsletter Monetisation", "$500–$5K/mo", "Build a niche newsletter powered by ChatGPT. Monetise via sponsorships ($50–$500/issue), paid tiers ($10–$30/mo), and affiliate links. Consistency is the competitive advantage."),
  ],
  'niche_table': [
    ("SaaS / Tech Companies", "Blog content, documentation, email", "$100–$300/article"),
    ("E-commerce Brands", "Product descriptions, email sequences, ads", "$50–$200/piece"),
    ("Law Firms / Finance", "Thought leadership, client newsletters", "$200–$500/article"),
    ("Coaches / Consultants", "LinkedIn ghostwriting, newsletter", "$1K–$3K/mo retainer"),
    ("Agencies (white-label)", "Blog, social, email at scale", "$500–$2K/mo per client"),
  ],
  'pricing_tiers': [
    ("Single Article", "$100–$300", "1,500-word SEO article. 24-hour delivery. Researched, formatted, images included."),
    ("Content Package", "$800–$1,500/mo", "8 articles + 4 email newsletters. Consistent publishing covered."),
    ("Ghostwriting Retainer", "$1,500–$3,000/mo", "LinkedIn + blog + newsletter. Full thought leadership content calendar."),
    ("Workshop / Training", "$2,000–$5,000", "1-day team workshop on ChatGPT workflows. Custom to their industry."),
  ],
  'client_script': "Cold email to a SaaS founder:\n\nSubject: [Company] content — noticed a gap\n\nHi [Name],\n\nI was reading [Company]'s blog. You published [X articles] last year — solid content. But I noticed the publishing cadence dropped off in [month].\n\nFor SaaS companies, consistent SEO content is compounding — every article keeps working for years. I run a content service specifically for [their category] SaaS companies: 4 SEO articles/month, $800 flat, 100% done-for-you.\n\nI'll write one article for [Company] this week at no charge to show you the quality and fit. Topic I'd suggest: [specific topic relevant to their product].\n\nInterested?",
  'extra_prompts': [
    ("SEO Content Brief System", "You are an SEO content strategist. For the keyword [keyword], produce a complete content brief: 1) Search intent analysis (what is the user actually trying to accomplish?), 2) Article structure — H1, all H2s, all H3s with a one-line description of each section, 3) Word count target and competitor benchmark, 4) 5 LSI/semantic keywords to include naturally, 5) Internal linking suggestions (3 existing pages to link to/from), 6) Featured snippet opportunity — what exact question should we answer in a box? 7) CTA recommendation — what should the reader do after finishing? Output as a complete brief I can give to a writer."),
    ("LinkedIn Ghostwriting System", "You are ghostwriting for [describe the person: role, company, expertise, audience]. Their content pillar for this week is: [topic]. Write 5 LinkedIn posts: Post 1 — Contrarian take (challenges a common belief in their industry). Post 2 — Framework post (a 3-5 step process they've developed). Post 3 — Story post (a specific moment from their career that taught them something). Post 4 — Data post (surprising statistic + their interpretation). Post 5 — Engagement post (a genuine question for their audience). Each post: 150–250 words, hook in the first line, no hashtag spam (max 2), ends with a question or CTA."),
    ("Custom GPT Design", "Help me design a Custom GPT for [specific professional role — e.g. freelance graphic designers]. The GPT should solve [specific pain point]. Design: 1) The name and tagline, 2) Full system prompt (500+ words) including role, capabilities, limitations, formatting rules, and personality, 3) 4 starter conversation prompts that demonstrate the value, 4) Knowledge files I should upload (list 5 specific document types), 5) Monetisation model — how should I price access and where should I sell it? 6) Marketing angle — one-sentence pitch for each potential buyer persona."),
  ],
  'advanced_steps': [
    ("Build a Client Voice Profile", "For every ghostwriting client, create a dedicated ChatGPT Project. Upload: 5 of their best existing posts, a voice description doc, their target audience profile, and 10 topics they care about. Every piece you write for them starts from this project. Quality and consistency go up dramatically — and onboarding new clients gets faster."),
    ("The Batch Prompt Method", "For content agencies, never prompt one piece at a time. Batch: 'Write 10 LinkedIn hooks for a SaaS founder in the HR tech space. Each hook should use a different emotional trigger: curiosity, fear, aspiration, controversy, surprise, nostalgia, authority, social proof, urgency, and humour.' Pick the best 3. Batch prompting produces better results and saves 80% of prompting time."),
    ("Add a QA Layer", "Before delivering any AI-generated content to clients: 1) Run through Grammarly for technical errors, 2) Check with a plagiarism tool (Copyscape or Originality.ai), 3) Read aloud once — catches unnatural AI phrasing, 4) Verify any statistics against their source. This QA layer is what separates professional content services from commodity ones."),
  ],
}

EXT['claude'] = {
  'use_cases': [
    ("Executive Ghostwriting Agency", "Writes books, white papers, and thought leadership articles for C-suite executives. Charges $5K–$15K per white paper, $25K–$80K per book. Claude handles voice matching across 100K+ words. 2–3 projects running simultaneously."),
    ("Legal Document Drafting", "Drafts contracts, NDAs, privacy policies, and terms of service for startups and small businesses. Charges $300–$1,500 per document. Law firms charge $300+/hr for the same work. 10 documents/week = $3K–$15K/mo."),
    ("Investment Research Service", "Produces sector deep-dive reports for angel investors, family offices, and VCs. Uploads 50+ documents per sector into Claude's 200K context window. Delivers a 30-page research report. Charges $2K–$8K per report."),
    ("Technical Documentation Studio", "Writes API docs, developer guides, and product specs for tech companies. Reads entire codebases via Claude Code integration, then writes documentation that's accurate to the actual implementation. Charges $150–$250/hr."),
    ("Long-Form Content Agency", "Specialises in 3,000–10,000 word cornerstone articles, ebooks, and reports for B2B companies. Claude's long context window handles entire books of research. Charges $500–$2,000 per piece. 10 pieces/month."),
  ],
  'more_streams': [
    ("Book Proposal Service", "$1K–$5K/proposal", "Write book proposals for non-fiction authors targeting traditional publishers. A strong proposal (20–40 pages) takes Claude 3 hours to draft. Authors pay well — a book deal is worth $50K–$500K."),
    ("Policy & Compliance Writing", "$2K–$10K/engagement", "Write internal policies, compliance manuals, and regulatory documentation for companies. Healthcare, finance, and tech all have constant policy writing needs."),
  ],
  'niche_table': [
    ("C-Suite / Executives", "Thought leadership, books, white papers", "$5K–$80K/project"),
    ("Law Firms / Startups", "Contracts, policies, legal drafts", "$300–$1,500/document"),
    ("Investment / Finance", "Research reports, due diligence, memos", "$2K–$10K/report"),
    ("Tech Companies", "API docs, developer guides, specs", "$150–$250/hr"),
    ("B2B Companies", "Long-form content, ebooks, reports", "$500–$2K/piece"),
  ],
  'pricing_tiers': [
    ("Document Drafting", "$300–$1,500", "Contracts, policies, one-off documents. 48-hour delivery."),
    ("Research Report", "$2,000–$8,000", "Deep research synthesis. 20–50 pages. 1-week delivery."),
    ("Ghostwriting Retainer", "$3,000–$10,000/mo", "Ongoing thought leadership — articles, white papers, book chapters."),
    ("Book Project", "$25,000–$80,000", "Full manuscript ghostwriting. 60K–80K words. 3–6 month engagement."),
  ],
  'client_script': "LinkedIn DM to a senior executive:\n\nHi [Name] — I've been following your work at [Company]. Your perspective on [topic they post about] is genuinely differentiated — most people in [their space] are saying the same things.\n\nI help senior leaders like you translate that differentiation into published work that reaches far beyond LinkedIn — white papers, keynote articles, and book projects that position you as the definitive voice in [their domain].\n\nI'm selective about who I work with. Would a 20-minute conversation be worth it to see if there's a fit?",
  'extra_prompts': [
    ("Voice Matching Analysis", "I'm ghostwriting for [describe the person]. Here are 5 examples of their authentic writing: [paste examples]. Analyse their voice: 1) Average sentence length and structure patterns, 2) Vocabulary level — do they favour Latinate or Anglo-Saxon words? Technical or plain language? 3) Paragraph length and rhythm, 4) Characteristic phrases or expressions they reuse, 5) What they never say — speech patterns they avoid, 6) Emotional register — are they analytical, inspirational, pragmatic, provocative? Create a voice style guide I can reference for every piece I write for them."),
    ("White Paper Structure", "Write the complete structure for a 6,000-word white paper titled '[Title]' for [company/author]. The audience is [describe]. The central argument is [thesis]. Structure: 1) Executive Summary (500 words — standalone document if needed), 2) The Problem (1,000 words — establish stakes and urgency), 3) Why Current Solutions Fail (1,000 words — position the gap), 4) The Framework/Solution (2,000 words — the core intellectual property), 5) Evidence and Case Studies (1,000 words), 6) Implementation Guide (500 words — practical next steps), 7) Conclusion and Call to Action (500 words). For each section, give me: the 3 key points to cover, the evidence to include, and the emotional job of that section."),
    ("Document Drafting System", "Draft a [document type — e.g. SaaS Terms of Service / NDA / Privacy Policy / Contractor Agreement] for a [company type] that [describe their business]. Requirements: 1) Jurisdiction: [country/state], 2) Specific clauses needed: [list any], 3) Specific concerns to address: [list any], 4) Language: clear and readable (not overly legalistic — this will be read by non-lawyers), 5) Format: clearly numbered sections with headings. Flag any clause where legal review is particularly important before signing."),
  ],
  'advanced_steps': [
    ("The Document Library Method", "For every client, build a Claude Project and upload their entire knowledge base: past publications, company background, product documentation, style guide, and audience research. Each new piece you write starts from this complete context. What took 2 hours of briefing calls now takes 10 minutes."),
    ("XML Structured Prompts for Consistency", "For production work, always use XML tags: <context>client background</context><task>specific deliverable</task><format>length, structure, style</format><examples>2–3 samples of their best work</examples>. This structured approach is Claude's native language — it follows complex, multi-part instructions more reliably than any other model."),
    ("Long Document Strategy", "When working with 200K+ token documents: 1) Upload all source material first, 2) Ask Claude to 'read all documents before answering', 3) Do a comprehension check ('summarise the 3 most important points across all documents'), 4) Then give your actual task. This priming step produces significantly more accurate and comprehensive outputs from large document sets."),
  ],
}
