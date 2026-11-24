"""Content for the Meta_001 site. Edit here, then run gen/build.py."""

NAME = 'Kiprop Haggai'
PHONE_DISPLAY = '0716 494 214'
PHONE_TEL = '+254716494214'
WA = '254716494214'
EMAIL = 'kiprophaggai01@gmail.com'
SITE_URL = 'https://kip-01.github.io/Meta_001/'

# Only handles that are filled in are shown on the site.
HANDLES = [
    ('whatsapp', 'WhatsApp', '0716 494 214', 'https://wa.me/254716494214'),
    ('phone', 'Phone', '0716 494 214', 'tel:+254716494214'),
    ('email', 'Email', EMAIL, 'mailto:' + EMAIL),
    ('medium', 'Medium', '@kiprop', 'https://medium.com/@kiprop'),
    ('github', 'GitHub', 'kip-01', 'https://github.com/kip-01'),
    ('youtube', 'YouTube', '@japhreys', 'https://www.youtube.com/@japhreys'),
    # Add more here, for example:
    # ('linkedin', 'LinkedIn', 'your-handle', 'https://www.linkedin.com/in/your-handle'),
    # ('instagram', 'Instagram', '@your-handle', 'https://www.instagram.com/your-handle'),
    # ('x', 'X', '@your-handle', 'https://x.com/your-handle'),
    # ('facebook', 'Facebook', 'Your Name', 'https://www.facebook.com/your-handle'),
    # ('tiktok', 'TikTok', '@your-handle', 'https://www.tiktok.com/@your-handle'),
]

FIELDS = [
    ('climate', 'Climate and livelihoods'),
    ('peace', 'Peace and cohesion'),
    ('wash', 'WASH and inclusion'),
    ('compliance', 'Compliance and CSR'),
    ('enterprise', 'Enterprise and health'),
]

# ------------------------------------------------------------------ projects
PROJECTS = [
 dict(id='k4rc', name='Kenya4Resilience Consortium (K4RC)', short='K4RC', kind='Delivered', fields=['climate', 'peace'],
  place='Wamba, Samburu County', when='Jul 2020 to May 2024', role='Project Coordinator',
  hook='Farming and peace-making, run as one programme.',
  summary='In Wamba, drought, thinning pasture and disputes between neighbouring communities were piling onto pastoral households. The consortium worked on both fronts at once: new ways to earn from the land, and structured dialogue to keep the peace.',
  metrics=[('400', 'farmers trained'), ('450+', 'at dialogue forums'), ('45%', 'fewer conflict incidents'), ('317', 'weapons surrendered')],
  points=[
   ('Farming from scratch', 'About 400 pastoralists were trained and given starter inputs. Six groups, including women, youth and people with disabilities, now grow maize, beans, carrots, groundnuts, sweet potatoes, cowpeas and capsicum.'),
   ('Seeing is believing', 'Exchange trips to working farms in Maralal and Thika, plus on-site coaching with the sub-county agriculture office.'),
   ('Gardens that spread', 'Sack gardens and small plots were copied well beyond the project\'s own participants.'),
   ('Pests, handled on the spot', 'When caterpillars from the maize fields moved onto vegetables, the team added pest-management training.'),
   ('Talking it through', 'Eighteen cross-border dialogue forums brought together Morans, community members and security agencies. Incidents fell by 45% and 317 weapons were handed in.'),
   ('A hub that outlasts the project', 'The Samburu K4R Hub (20 members) links the Kenya Forest Service, schools, ward administration and chiefs.'),
  ],
  mine=['Coordinated the field programme, the partners and the county links.', 'Set up demonstration plots and trained grazing committees in pasture regeneration and fodder banking.', 'Connected 800+ smallholders to input suppliers, buyers and traders.', 'Led 7 health outreaches with Wamba Level IV Hospital and AMREF, reaching about 300 households.', 'Tracked results with KoboCollect and Power BI. Wrote donor reports and 17 impact stories, and produced 15+ infographics and videos.'],
  facts=[('Partners', 'Children\'s Mission Africa, The Salvation Army, Life and Peace Institute, International Aid Services'), ('Launched', '1 July 2021, Maralal')],
  photo=None),
 dict(id='mseto', name='Mseto Resilience: WASH and Food Security', short='Mseto', kind='Delivered', fields=['climate', 'wash'],
  place='Kitui, Machakos, Makueni, Samburu and Isiolo', when='Oct 2018 to Jun 2020', role='WASH and Livelihoods Project Officer',
  hook='Water, savings and a demonstration farm, in five counties.',
  summary='A Salvation Army Kenya East programme that tied water, sanitation, food security and rights together, using a faith-based facilitation process in which communities study their own problems and plan the fix.',
  metrics=[('1,200+', 'households reached'), ('20', 'savings groups and CBOs formed'), ('72.5%', 'harvest roof rainwater, vs 50% outside'), ('31,200', 'right-holders in the 2019-23 design')],
  points=[
   ('Community-led analysis', 'Faith-based facilitation put the problem-solving in residents\' hands rather than the project\'s.'),
   ('Money that stays local', 'Twenty village savings and loan groups, producer groups and community organisations were formed and trained.'),
   ('A farm that teaches', 'A commercial demonstration farm showed drip irrigation, soil-moisture conservation, pest management and mixed crop-livestock systems.'),
   ('Evidence', 'In Kilome-Sulutani 72.5% of households now harvest rainwater from their roofs, against 50% in areas the project had not reached.'),
   ('Next phase', 'The 2019-2023 design scales to 64 communities and 64 schools, with a research and demonstration centre at Thika.'),
  ],
  mine=['Coordinated WASH and livelihood work for 1,200+ agropastoral households.', 'Supported accessible water and sanitation at Joytown, Thika High School for the Blind and Variety Village.', 'Delivered child protection, safeguarding and health promotion training.', 'Ran gender-responsive work in poultry, kitchen gardens, beekeeping and basketry, and built conflict sensitivity into shared grazing and water.'],
  facts=[('Implementer', 'The Salvation Army Kenya East Territory'), ('Goals', 'SDG 2, 3, 5, 6, 13, 17')], photo=None),
 dict(id='joytown', name='Joytown Schools', short='Joytown', kind='Delivered', fields=['wash', 'climate'],
  place='Thika, Kiambu County', when='2018 to 2020, with reporting in 2025', role='Infrastructure support and partner reporting',
  hook='A school built so every learner can get around it.',
  summary='Salvation Army Joytown is a national secondary school for learners with physical impairments. Through Mseto I coordinated accessible washrooms, pathways, kitchens and water harvesting; later work covers partner reports and a needs assessment.',
  metrics=[('293', 'learners (2025)'), ('2.026 to 2.505', 'KCSE mean score'), ('25%', 'qualify for university'), ('86', 'eligible students turned away')],
  points=[
   ('Infrastructure people can use', 'Accessible ablution blocks, ramps and kitchens, with roofed and railed walkways so wheelchairs and crutches cope in the rains.'),
   ('A solar pump', 'Donor-funded solar pumping has cut the school\'s water costs.'),
   ('Plain about the gaps', 'The 2025 report sets three priorities: digital inclusion (20 adaptive laptops, 8 projectors), hygiene and dignity (a commercial washing machine), and capacity (a perimeter wall, dining hall and dormitories).'),
  ],
  mine=['Coordinated accessible WASH and water harvesting (2018 to 2020).', 'Helped prepare the 2025 annual report and a needs assessment for partners.'],
  facts=[('Motto', 'Najimudu: "I am able"')], photo='classroom.jpg', photo2='construction.jpg',
  caption='A new classroom block at Joytown, and the same block going up.'),
 dict(id='terraore', name='TerraOre: community and environmental compliance', short='TerraOre', kind='Delivered', fields=['compliance'],
  place='Ikolomani, Kakamega County', when='Jun 2024 to Nov 2025', role='CSR, Environmental and Community Relations Coordinator',
  hook='Making a plant\'s arrival fair, documented and licensed.',
  summary='A minerals leaching plant changes life for the households and groups around it. My job was to make that change fair, written down and compliant, and to keep local leaders and government offices in the loop from first contact to start-up.',
  metrics=[('7', 'households relocated and compensated'), ('1', 'NEMA EIA licence supported'), ('1', 'Ministry of Mining registration')],
  points=[
   ('Know who is affected', 'Mapped households, local leaders and community groups before any decision was announced.'),
   ('Relocation done properly', 'Built the phased relocation appraisal for seven households, with cash compensation and new houses on purchased, titled land.'),
   ('Licence and paperwork', 'Supported the Environmental Impact Assessment (NEMA/EIA/PSL/32674, issued 29 May 2024) and followed up its conditions.'),
   ('Government in the room', 'Registered the company with the Ministry of Mining and represented the Ikolomani Youth Cooperative at a Ministry stakeholders\' workshop in January 2025.'),
  ],
  mine=['Led community engagement end to end.', 'Reported progress to management and kept relationships open with host community members and offices.'],
  facts=[('Company', 'TerraOre Mineral Resources Ltd'), ('Site', 'Molowa plant')], photo=None),
 dict(id='jeep', name='Jibu Economic Empowerment Project (JEEP)', short='JEEP', kind='Proposal', fields=['climate'],
  place='Machakos, Makueni, Kitui and Embu', when='Prepared Nov 2026', role='Proposal author',
  hook='Savings groups, tougher value chains and kitchen gardens.',
  summary='A three-year proposal for The Salvation Army Kenya East Territory to lift incomes and nutrition for smallholder households whose harvests rise and fall with the rains.',
  metrics=[('3', 'outcomes'), ('27', 'activities'), ('30', 'savings groups'), ('600', 'kitchen-garden households')],
  points=[
   ('Why', 'Low, unstable income from rain-fed crops; little access to savings or credit; weak market links; narrow diets.'),
   ('Finance', '30 savings and loan groups formed or revived; about 700 members trained on seven modules.'),
   ('Income', '300 lead farmers trained in diversification and 300 in value-chain choice, with poultry, dairy goats, pigs and bees demonstrated at a Learning and Research Centre in Thika and a satellite site at Karurumo.'),
   ('Nutrition', '600 households get kitchen-garden starter inputs, Farming God\'s Way training and fruit trees.'),
   ('Stress-tested', 'The plan models cost inflation and a weaker shilling, and carries a register of nine risks with mitigations.'),
  ],
  mine=['Wrote the proposal end to end: context analysis, logframe-aligned design, SDG mapping, implementation plan, budget narrative and risk assessment.'],
  facts=[('Status', 'Proposal. Start date to be confirmed')], photo=None),
 dict(id='nursery', name='Resilient Nursery Schools Project', short='Nursery schools', kind='Proposal', fields=['wash', 'climate'],
  place='Five counties of western Kenya', when='3-year proposal', role='Proposal author',
  hook='A mobile health team for 13 nursery schools.',
  summary='Many early-childhood centres have no health or nutrition services and little funding. This proposal sends a fully equipped mobile outreach team, working with county health workers, to 13 schools and the homes around them.',
  metrics=[('13', 'nursery schools'), ('~1,000', 'children'), ('5', 'outcomes'), ('3', 'years')],
  points=[
   ('Health and nutrition', 'Growth monitoring, deworming, vitamin A, immunisation checks, referrals and school feeding.'),
   ('Safer schools', 'First aid, hazard assessments of classrooms and play areas, plus WASH: safe water, child-friendly latrines, handwashing.'),
   ('Rights', 'A birth certificate for every enrolled child, and rights training for parents and teachers.'),
   ('Honest scoping', 'The first draft covered 50 schools. Testing outcomes against time and money showed that would spread impact too thin, so it targets 13, with scale-up later.'),
  ],
  mine=['Authored the proposal and logframe, and made the call to narrow the scope.'],
  facts=[('Goals', 'SDG 3, 4, 6, 17'), ('Reach', '~1,000 children, 50 teachers, 60 support staff, 100 caregivers')], photo=None),
 dict(id='kujenga', name='Kujenga Amani Pamoja: youth-led peace proposals', short='Kujenga Amani', kind='Proposal', fields=['peace'],
  place='Kwale County', when='Sep to Oct 2024', role='Proposal development support',
  hook='Three coastal youth groups, three fundable peace plans.',
  summary='Young people aged 14 to 26 around Tsimba-Golini, Diani and Mazimalume were being pulled into gangs and neighbourhood rivalries. I helped three youth organisations turn their own conflict analysis into grant applications.',
  metrics=[('3', 'applications'), ('140 to 212', 'direct participants each'), ('3 to 4', 'months each')],
  points=[
   ('Tujuane straight talks', 'Youth and elders sit down together, with theatre skits and local radio carrying the message.'),
   ('Maskani dialogues', 'Conversations in the neighbourhood hangouts on problems first, then solutions, and an ideas competition linked to devolved funds.'),
   ('Culture as a peace tool', 'Shared meals, Swahili music, Kaya elders and a cultural day that creates "Amani Ambassadors".'),
  ],
  mine=['Problem statements, objectives, intervention logic, activity plans, beneficiary numbers, gender and conflict-sensitivity sections and communication plans.'],
  facts=[('Applicants', 'Youth Voice Matters Initiative, Kwale Youth for Peace and Cohesion, Young Generation Talents Nurture'), ('Status', 'Proposals. Funding outcomes not shown')], photo=None),
 dict(id='terraheal', name='TerraHeal Pharmaceuticals', short='TerraHeal', kind='Business', fields=['enterprise'],
  place='Kakamega, Kenya', when='Jun 2026 to now', role='Pharmacy Operations Manager',
  hook='A licensed pharmacy, set up from an empty room to daily trading.',
  summary='TerraHeal sells medicines, cosmetics and supplements, wholesale and retail, and offers counselling. I took it from premises hunt to a stocked, systemised shop and I run its operations.',
  metrics=[('800+', 'product lines tracked'), ('8am to 1am', 'open daily'), ('2', 'phone lines'), ('1', 'management dashboard')],
  points=[
   ('From empty room to open shop', 'Premises, interior layout, stocking and staff set-up.'),
   ('Inventory that watches itself', 'Stock, expiry dates and stock-outs tracked across 800+ lines.'),
   ('Institutional supply', 'Sales and supply to county hospitals, medicines for a church health outreach, quotations to health centres.'),
   ('Back office', 'Procurement from licensed distributors, payroll, banking authorisation and KRA documentation.'),
  ],
  mine=['Running day-to-day operations, supplier quotations, systems and records.'],
  facts=[('Public line', '0710 913 110'), ('Email', 'terrahealpharmaceuticals@gmail.com')], photo=None),
]

# ------------------------------------------------------------------ roles / timeline
ROLES = [
 dict(id='terraheal', fields=['enterprise'], start=(2026, 6), end=(2026, 11.5), when='Jun 2026 to now', title='Pharmacy Operations Manager', org='TerraHeal Pharmaceuticals Ltd', place='Kakamega',
  bullets=['Built the pharmacy from set-up to trading: premises, layout, stocking.', 'Inventory control for 800+ product lines, covering stock levels, expiry and stock-outs.', 'Sales and supply of medicines to county government hospitals; medicines for an Anglican Church of Kenya health outreach.', 'Procurement from licensed distributors, systems administration, payroll, banking authorisation and KRA documentation.']),
 dict(id='terraore', fields=['compliance'], start=(2024, 6), end=(2025, 11), when='Jun 2024 to Nov 2025', title='CSR, Environmental and Community Relations Coordinator', org='TerraOre Mineral Resources Ltd', place='Ikolomani, Kakamega County',
  bullets=['Led community engagement for a minerals leaching plant, first contact to start-up.', 'Relocation appraisal and compensation for seven households.', 'Supported the NEMA EIA (NEMA/EIA/PSL/32674, 29 May 2024) and its licence conditions; registered the company with the Ministry of Mining.']),
 dict(id='k4rc', fields=['climate', 'peace', 'compliance'], start=(2020, 7), end=(2024, 5), when='Jul 2020 to May 2024', title='Project Coordinator', org='Kenya4Resilience Consortium (K4RC)', place='Wamba, Samburu County',
  bullets=['Livelihood and resilience programmes reaching 5,000+ pastoralist and agropastoral households.', '18 dialogue forums, 450+ participants; conflict incidents down 45%; 317 weapons surrendered.', 'Women and youth above 60% of active participants and leaders.', '800+ smallholders linked to markets; 7 health outreaches (about 300 households); 17 impact stories; 15+ infographics and videos.']),
 dict(id='mseto', fields=['climate', 'wash', 'peace'], start=(2018, 10), end=(2020, 6), when='Oct 2018 to Jun 2020', title='WASH and Livelihoods Project Officer', org='Mseto Resilience WASH and Food Security Project, The Salvation Army', place='Nairobi, Kitui, Machakos, Isiolo, Makueni, Samburu',
  bullets=['1,200+ agropastoral households reached.', 'Disability inclusion at Joytown, Thika High School for the Blind and Variety Village.', '20 savings and loan groups, producer groups and CBOs formed and trained; demonstration farm managed.']),
 dict(id='kmfri', fields=['climate'], start=(2016, 4), end=(2016, 8), when='Apr to Aug 2016', title='Extension Officer', org='Kenya Marine and Fisheries Research Institute', place='Sagana, Kirinyaga County',
  bullets=['Fish farmer groups mobilised KES 500,000+ and financed 7 micro-enterprises.', '6 incubation workshops for 80+ farmers; group income up 45%; production efficiency up 30%.']),
]

# ------------------------------------------------------------------ expertise
EXPERTISE = [
 dict(id='climate', name='Climate resilience and adaptation', tag='core', blurb='Helping households keep earning and eating through droughts and erratic rain.',
  proof=['K4RC: pastoralists moved into climate-smart agropastoralism.', 'Mseto: rainwater harvesting, drip irrigation, soil-moisture conservation.', 'Writing: "Resilience: climate change" on Medium.'], tools=['Demonstration plots', 'Fodder banks', 'Rainwater harvesting', 'Integrated pest management']),
 dict(id='livelihoods', name='Livelihoods and savings groups', tag='core', blurb='Savings, enterprise and market links that survive the end of a project.',
  proof=['20 savings and loan groups formed (Mseto).', '800+ smallholders linked to buyers (K4RC).', 'JEEP: 30 groups and two value-chain tracks designed.'], tools=['VSLA methodology', 'Value-chain selection', 'Farmer-to-farmer learning']),
 dict(id='peace', name='Peacebuilding and conflict sensitivity', tag='core', blurb='Dialogue that shifts behaviour, and programmes designed so they do not feed conflict.',
  proof=['18 forums, 450+ participants, incidents down 45%.', 'Three Kwale youth peace proposals.', 'Diploma in Conflict Sensitivity in Community Development, in progress.'], tools=['Conflict analysis', 'Dialogue forums', 'Do-no-harm checks']),
 dict(id='wash', name='WASH and disability inclusion', tag='core', blurb='Water, sanitation and buildings that work for learners who use wheelchairs and crutches.',
  proof=['Accessible blocks and walkways at three special-needs institutions.', 'Joytown annual report and needs assessment.'], tools=['Accessible design', 'Water harvesting', 'Child protection training']),
 dict(id='proposals', name='Proposal and grant development', tag='core', blurb='From context analysis to logframe, SDG mapping, risk register and budget narrative.',
  proof=['JEEP, Resilient Nursery Schools, Kujenga Amani (three applications).', 'Scope tested against time and money before submission.'], tools=['Logframes', 'Theory of change', 'Cost-indexation scenarios', 'Risk registers']),
 dict(id='mel', name='Monitoring, evaluation and learning', tag='core', blurb='Tracking what changed, and writing it down so others can reuse it.',
  proof=['Dashboards and donor reports for a consortium.', '17 impact stories.', 'Trained in outcome mapping, outcome harvesting and adaptive management.'], tools=['KoboCollect', 'Power BI', 'Outcome mapping', 'Baseline and endline design']),
 dict(id='eia', name='Environmental and social compliance', tag='other', blurb='Impact assessments, licence conditions and the paperwork that keeps projects legal.',
  proof=['NEMA-registered Associate Expert, EIA-MP/153/2018.', 'Diploma in Social and Environmental Impact Assessment (2018).', 'Supported a NEMA EIA licence at TerraOre.'], tools=['EIA and ESIA', 'Licence follow-up', 'Stakeholder registers']),
 dict(id='csr', name='CSR and community relations', tag='other', blurb='Engagement, relocation and compensation handled with documents and dignity.',
  proof=['Seven households relocated and compensated.', 'Ministry of Mining registration and workshop representation.'], tools=['Stakeholder mapping', 'Relocation appraisal', 'Grievance handling']),
 dict(id='pharmacy', name='Pharmacy and health-supply operations', tag='other', blurb='Stocking, procurement, records and supply to institutions.',
  proof=['TerraHeal: 800+ product lines, supplier quotations, institutional supply.', 'Prequalification and screening bids for a church-run child development centre.'], tools=['Inventory control', 'Quotations and LPOs', 'Payroll', 'Statutory filings']),
 dict(id='aqua', name='Aquaculture and fisheries extension', tag='other', blurb='Pond management, fish health and farmer business groups.',
  proof=['Extension officer at KMFRI (2016): production efficiency up 30%.', 'BSc Aquatic Resources Conservation and Development with IT, Maseno University (2017).'], tools=['Pond management', 'Value addition', 'Business incubation']),
 dict(id='story', name='Storytelling and field media', tag='other', blurb='Turning field results into stories, infographics and short films.',
  proof=['8 stories on Medium (2019 to 2022).', '15+ infographics and videos reused by other chapters.', 'Two Kenya4Resilience films.'], tools=['Impact stories', 'Infographics', 'Video', 'Long-form writing']),
 dict(id='faith', name='Faith-based partnership and facilitation', tag='other', blurb='Working through churches and faith institutions as trusted community platforms.',
  proof=['Mseto used a faith-based facilitation process.', 'Salvation Army and Anglican Church of Kenya partnerships.'], tools=['Church partnerships', 'Community facilitation']),
 dict(id='web', name='Web and data tools', tag='other', blurb='Small, practical tools: dashboards, storefronts and sites.',
  proof=['TerraHeal management dashboard and storefront prototype.', 'This portfolio, designed in Figma and published on GitHub Pages.'], tools=['HTML, CSS, JavaScript', 'Spreadsheets', 'Figma']),
]

METHOD = [
 ('Listen and map', 'Who is affected, who decides, who has been left out. I start with people and records, not assumptions.'),
 ('Frame with evidence', 'Use local data and the community\'s own analysis to define one problem worth solving.'),
 ('Design the smallest thing that works', 'Cut scope until time and money match the ambition, as with the 13-school nursery project.'),
 ('Build with the people affected', 'Farmers, elders, teachers, youth groups and county staff share the work, and the credit.'),
 ('Measure, then adjust', 'Short feedback loops, field dashboards, honest reports, and changes when the data says so.'),
 ('Hand over', 'Groups, hubs and county teams that can carry on after the project steps back.'),
]

SERVICES = [
 ('Proposal and concept-note development', 'Context analysis, logframe, risk register, budget narrative, SDG mapping.'),
 ('Resilience programme design', 'Livelihoods, savings groups and climate-smart farming for dryland counties.'),
 ('Community engagement and CSR planning', 'Stakeholder mapping, relocation appraisal, grievance handling and reporting.'),
 ('Environmental compliance support', 'EIA and ESIA support and follow-up of licence conditions.'),
 ('M&E set-up', 'Kobo forms, Power BI dashboards, outcome mapping and learning reports.'),
 ('Pharmacy and small-business operations', 'Stocking, inventory, supplier quotations, records and payroll set-up.'),
 ('Writing and field storytelling', 'Impact stories, articles, infographics and short films.'),
]

EDU = [
 ('Diploma in Conflict Sensitivity in Community Development', 'Campus Køge, Denmark', '2025 to 2027, in progress'),
 ('Diploma in Social and Environmental Impact Assessment', 'Africa Waste Management Company Ltd', '2018'),
 ('BSc Aquatic Resources Conservation and Development with IT', 'Maseno University', '2017'),
]
TRAINING = [
 ('NEMA Associate Expert (EIA-MP/153/2018)', 'Environmental Institute of Kenya'),
 ('Peacebuilding, Conflict Analysis and Disaster Risk Reduction', '2024'),
 ('Conflict Sensitivity', '2023'),
 ('Adaptive Management', '2022'),
 ('Outcome Mapping and Outcome Harvesting', '2021'),
 ('Child Protection, Safeguarding and PSEA', 'Salvation Army and K4RC, 2020'),
]

FAQ = [
 ('What is the quickest way to reach you?', 'Call or send a WhatsApp message to 0716 494 214. Say who you are, where the work is and what you need by when, and I will reply with next steps.'),
 ('Where are you based?', 'Kakamega, Kenya. Field work has taken me through Samburu, Kitui, Machakos, Makueni, Isiolo, Embu and Kakamega counties.'),
 ('Which projects are delivered and which are proposals?', 'Each project carries a status tag. Proposals are written pieces of work; funding outcomes are not shown here.'),
 ('Why are there no budgets or personal details?', 'Source proposals contain budgets and names of private individuals. I leave those out of a public site.'),
 ('Is TerraHeal your own business?', 'I am its Pharmacy Operations Manager and run it day to day. For ownership, shareholding and licence questions, please contact the business directly.'),
 ('How is this site built?', 'Plain HTML, CSS and JavaScript, no tracking and no cookies. The flows and layouts were designed in Figma, and the code is on GitHub.'),
]

# ------------------------------------------------------------------ business
BUSINESS = dict(
 terraheal=dict(
  name='TerraHeal Pharmaceuticals', tagline='Wholesale and retail medicines, cosmetics, supplements and counselling in Kakamega.',
  role='Pharmacy Operations Manager, Jun 2026 to now',
  stats=[('800+', 'product lines tracked'), ('8am to 1am', 'open daily'), ('4,300+', 'sales transactions logged, Jun to early Aug 2026'), ('3', 'institutional bids prepared')],
  services=[('Retail pharmacy', 'Prescription and over-the-counter medicines, cosmetics and supplements.'), ('Wholesale supply', 'Medicines and consumables for clinics, health centres and hospitals, with quotations.'), ('Counselling', 'A private counselling service alongside the dispensary.'), ('Institutional health work', 'Prequalification to supply a church-run child development centre, and a bid to run health screening for its 301 participants.')],
  flow=[('Source', 'Compare supplier quotations and buy only from licensed distributors.'), ('Receive and check', 'Verify batch numbers, expiry dates and quantities against the order.'), ('Stock', 'Log each line in the inventory sheet; flag low stock and stock-outs.'), ('Sell', 'Retail at the counter or wholesale on invoice and local purchase order.'), ('Reconcile', 'Match cash, till and M-Pesa daily against expenses.'), ('Report', 'A management dashboard summarises sales, stock and cash for decisions.')],
  built=['Premises, interior layout and stocking.', 'Inventory for 800+ product lines with expiry and stock-out tracking.', 'Templates for invoices and purchase orders; a sales, income and expenditure tracker; a management dashboard.', 'Payroll, banking authorisation and KRA filing.', 'Planned: an installable pharmacy app with M-Pesa payments.'],
  contact=[('Business line 1', '0716 494 214', 'tel:+254716494214'), ('Business line 2', '0710 913 110', 'tel:+254710913110'), ('Email', 'terrahealpharmaceuticals@gmail.com', 'mailto:terrahealpharmaceuticals@gmail.com')]),
 terraore=dict(
  name='TerraOre Mineral Resources', tagline='Community engagement, relocation and licensing for a minerals leaching plant at Molowa, Ikolomani.',
  role='CSR, Environmental and Community Relations Coordinator, Jun 2024 to Nov 2025',
  stats=[('7', 'households relocated'), ('1', 'NEMA EIA licence supported'), ('18', 'months on the ground'), ('1', 'Ministry of Mining registration')],
  services=[('Community engagement', 'Mapping, meetings and a clear line to local leaders and county offices.'), ('Relocation and compensation', 'Phased appraisal, cash compensation and houses on titled land.'), ('Environmental licensing', 'Support to the EIA and follow-up of its conditions.'), ('Government liaison', 'Company registration and stakeholder workshops.')],
  flow=[('Map', 'Identify affected households, leaders and groups.'), ('Engage', 'Open meetings, questions answered in the open, records kept.'), ('Appraise', 'Value land, homes and livelihoods for each household.'), ('Relocate', 'Cash and new houses on purchased, titled land.'), ('License', 'Support the NEMA EIA and track every condition.'), ('Operate', 'Keep relationships with host community and offices open.')],
  built=['Phased relocation appraisal for seven households.', 'Stakeholder register and engagement log.', 'Progress reporting to company management.', 'Ministry of Mining registration and January 2025 workshop representation.'],
  contact=[]),
)

# ------------------------------------------------------------------ articles
ARTICLES = [
 dict(id='salmaletu', title='Salmaletu Women Group', date='2022-07-16', topics=['Resilience', 'Women and leadership'], url='https://medium.com/@kiprop/salmaletu-women-group-70bdb4bff598', img='https://cdn-images-1.medium.com/max/1024/1*Jbt0da2Q3fJ5xJDSgKlySw.jpeg',
  blurb='A former rescue centre in Wamba is now a 20-member group mixing farming with savings and loans, and wrestling with water shortages.'),
 dict(id='asal', title='Farming in ASAL areas.', date='2021-07-15', topics=['Resilience', 'Climate'], url='https://medium.com/@kiprop/farming-in-asal-areas-79c49dda4558', img='https://cdn-images-1.medium.com/max/1024/1*4e3lsPieMQpi0ccJB4diiQ.jpeg',
  blurb='A teacher in Embakasi village keeps soil moist with polythene-lined sunken beds, and uses elephant dung as manure and fuel.'),
 dict(id='leadership', title='Leadership under women', date='2020-04-27', topics=['Women and leadership', 'Faith'], url='https://medium.com/@kiprop/leadership-under-women-5071c7bc4f08', img='https://cdn-images-1.medium.com/max/1024/0*VkRDSYffjWelqckx',
  blurb='Why women struggle to lead, from weak solidarity to cultural norms, and what changes when leadership is shared.'),
 dict(id='peace', title='Peace.', date='2020-04-22', topics=['Peace', 'Faith'], url='https://medium.com/@kiprop/peace-e9fe059a5e71', img='https://cdn-images-1.medium.com/max/640/0*dItc1qsB8YCHBgU5',
  blurb='Peace as wholeness and justice, not only the absence of war, and why inner peace and world peace feed each other.'),
 dict(id='gcc', title='Global Climate Change', date='2020-04-13', topics=['Climate'], url='https://medium.com/@kiprop/global-climate-change-aa4de63f6795', img='https://cdn-images-1.medium.com/max/803/1*J74woD-jXewsEHGgzHZIeg.png',
  blurb='A reprint of a 2008 climate speech on cap-and-trade and clean-energy investment, with a promised follow-up on progress since.', reprint=True),
 dict(id='abandoned', title='Abandoned children.', date='2019-09-19', topics=['Family'], url='https://medium.com/@kiprop/abandoned-children-fa8c9563573b', img=None,
  blurb='What drives child abandonment, how it marks children, and how families and communities can step in.'),
 dict(id='resilience', title='Resilience: climate change.', date='2019-09-18', topics=['Climate', 'Resilience'], url='https://medium.com/@kiprop/climate-resilience-c240b1e41553', img='https://cdn-images-1.medium.com/max/1024/0*BxJk0H4ZSBuNZYL3',
  blurb='Hazard, exposure and vulnerability explained, and why adaptation and mitigation need each other.'),
 dict(id='youth', title='Youth are the present.', date='2019-09-05', topics=['Youth', 'Faith'], url='https://medium.com/@kiprop/youth-are-the-present-8920faa3d497', img='https://cdn-images-1.medium.com/max/800/1*dLfhhL9aqNAxUEKTdgCt-g.png',
  blurb='Young people are stakeholders today, not only the future. A case for real inclusion in policy, decisions and jobs.'),
]
TOPICS = ['Resilience', 'Climate', 'Peace', 'Women and leadership', 'Youth', 'Family', 'Faith']
PATHS = [
 ('Climate and resilience', 'From definitions to a farm in Wamba.', ['resilience', 'gcc', 'asal', 'salmaletu']),
 ('People and leadership', 'Who gets to lead, and who gets left behind.', ['leadership', 'youth', 'abandoned']),
 ('Peace', 'What wholeness looks like.', ['peace']),
]
MEDIUM_AVATAR = 'https://cdn-images-1.medium.com/fit/c/150/150/1*iU0Ss0bH7uK4OobOLi9KgQ.jpeg'

VIDEOS = [
 dict(id='I3XqEDcZWGo', title='Consortium Project', channel='Kenya4Resilience', dur='15:57', date='28 Mar 2024',
  blurb='The Kenya4Resilience Consortium explained: a rights-based approach to cut disaster risk and build the capacity to absorb, adapt and transform.'),
 dict(id='ghBy5MKxOOc', title='Community of Practice', channel='Kenya4Resilience', dur='12:33', date='28 Mar 2024',
  blurb='How ten funded CSOs formed a community of practice to share lessons and build communities that bend but do not break.'),
]
