"""
SINGLE SOURCE OF TRUTH — C817 Gemini for Google Sheet (non-WSQ).

A beginner, one-day (7.5 hours), hands-on short course on using generative AI —
Google's Gemini — inside Google Sheets to generate and explain formulas, clean
and transform data, analyse datasets, and build tables, charts and visualisations,
while validating AI output and applying it safely to real work data. Every
artifact (PPT, LP, LG, LG.md) and every lab is generated from this module +
data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C817.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Gemini for Google Sheet (C817)"
SHORT_TITLE  = "Gemini for Google Sheet (C817)"   # used in output filenames
COURSE_CODE  = "C817"                                     # non-WSQ code — never a TGS- ref
VERSION      = "v1.1"
VERSION_DATE = "4 October 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain what generative AI and Gemini in Google Sheets are, and set up and access AI features inside a sheet.",
    "LO2: Generate spreadsheet formulas with AI and use AI to explain, step by step, what a formula does.",
    "LO3: Write clear, effective prompts that get accurate results for spreadsheet tasks.",
    "LO4: Use AI to clean, transform and organise messy spreadsheet data into a usable table.",
    "LO5: Summarise and analyse datasets with AI to surface useful, decision-ready insights.",
    "LO6: Create tables, charts and visualisations from your data using AI.",
    "LO7: Validate AI output for accuracy and apply AI safely and responsibly to real work data.",
]
LO_TITLES = [
    "Understand & access AI",
    "Generate & explain formulas",
    "Prompt effectively",
    "Clean & organise data",
    "Summarise & analyse",
    "Charts & visuals",
    "Validate & apply safely",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with AI in Google Sheets",
         subtitle="Generative AI & Gemini in Sheets · Setting up and accessing AI · Generating and explaining formulas · Effective prompting",
         weighting="50%",
         concepts=[
            "Generative AI — AI that creates new content (text, formulas, summaries) from a plain-language request, rather than only looking things up.",
            "Gemini in Google Sheets — Google's built-in AI that helps you build formulas, clean data, analyse and summarise, directly inside a spreadsheet.",
            "Where to find it — the Gemini side panel (\"Ask Gemini\") and AI-assisted menus let you work in plain English without leaving your sheet.",
            "The =AI() function — a Sheets function that sends your prompt to Gemini and returns the result straight into a cell, so AI output becomes spreadsheet data.",
            "Generating formulas — describe the calculation you want in words and let AI write the correct formula (SUM, IF, VLOOKUP, and more) for you.",
            "Explaining formulas — paste any formula and ask AI to explain, step by step, what it does — a fast way to learn and to check an inherited sheet.",
            "Effective prompting — a good spreadsheet prompt names the range, the goal, the output format and any conditions, so the AI has no room to guess.",
            "Human in the loop — AI drafts; you check. Always verify a formula or result against a value you can confirm before you rely on it.",
         ]),
    dict(num=2, code="02",
         title="Analysing and Automating Data with AI in Sheets",
         subtitle="Cleaning, transforming & organising data · Summarising and analysing datasets · Tables, charts & visualisations · Validating and applying AI safely",
         weighting="50%",
         concepts=[
            "Cleaning data — AI can standardise text, fix inconsistent formats, split or merge columns and flag blanks, turning a messy sheet into a usable one.",
            "Transforming data — reshape data with AI: extract fields, categorise rows, convert units or reformat dates without writing complex formulas by hand.",
            "Organising data — sort, group and label records so a raw export becomes a structured table you can analyse.",
            "Summarising datasets — ask AI for totals, averages, top and bottom performers and a plain-language summary of what the numbers say.",
            "Analysing datasets — AI can spot trends, compare segments and answer \"what\" and \"why\" questions about your data in seconds.",
            "Tables and pivots — turn a flat list into a summary table or pivot with AI, grouping and aggregating the figures that matter.",
            "Charts and visualisations — describe the story you want to tell and let AI suggest and build the right chart to show it.",
            "Validating and applying safely — AI can be confidently wrong; check outputs against known values, keep confidential data out of prompts, and stay accountable for the result.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Getting started with Gemini AI in Google Sheets, then analysing and visualising real data with AI",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The single training day totals exactly 480
# minutes excluding the 1-hour lunch — of which 30 minutes are tea breaks, so
# 450 minutes (7.5 hours) are instructional, matching the advertised duration.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ground rules, and confirming Gemini AI access in Google Sheets for the labs"),
        ("9:50","10:45",55,"topic","TOPIC 01 — Getting Started with AI in Google Sheets: generative AI and Gemini in Sheets; setting up and accessing AI; generating and explaining formulas; effective prompting for spreadsheet tasks (concepts + live demo)"),
        ("10:45","11:30",45,"lab","Hands-on: "+lab_titles([1,2])),
        ("11:30","11:45",15,"break","Tea break"),
        ("11:45","13:00",75,"lab","Hands-on: "+lab_titles([3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:50",50,"topic","TOPIC 02 — Analysing and Automating Data with AI in Sheets: cleaning, transforming and organising data; summarising and analysing datasets; creating tables, charts and visualisations; validating AI output and applying AI safely to work data (concepts + live demo)"),
        ("14:50","15:30",40,"lab","Hands-on: "+lab_titles([5])),
        ("15:30","15:45",15,"break","Tea break"),
        ("15:45","18:15",150,"lab","Hands-on: "+lab_titles([6,7,8])),
        ("18:15","18:30",15,"recap","Course wrap-up, your AI-in-Sheets checklist and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="How AI Works Inside Google Sheets",
    concepts=[
        "From typing formulas to describing results — you tell Gemini the outcome you want and it produces the formula or the data for you.",
        "It works where your data lives — Gemini runs inside the sheet, using the ranges and tabs you already have.",
        "Two ways in — the Gemini side panel for a conversation about your data, and the =AI() function for AI output right in a cell.",
        "You stay accountable — AI drafts and suggests; you verify every result before it informs a decision.",
    ],
    framework_title="The Ask–Check–Apply Loop",
    framework=[
        ("Prepare", "Know your data: which range, what each column means, and what a correct answer looks like."),
        ("Ask", "Write a clear prompt — the range, the goal, the output format and any conditions."),
        ("Check", "Verify the AI's formula or result against a value you can confirm yourself."),
        ("Apply", "Put the verified result to work in your sheet."),
        ("Refine", "Adjust the prompt and re-run until the output is right, then reuse it."),
    ],
    statement=dict(
        headline="AI in Sheets is fastest when your prompt is specific and your check is honest.",
        body="This course is hands-on: you clean, calculate, analyse and chart one real dataset with Gemini, verifying every result before you trust it.",
        kicker="THE WORKING RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A clean dataset", ["A messy orders sheet standardised and organised", "Consistent dates, text and categories", "Formulas generated and explained by AI"]),
        ("An analysis", ["Totals, averages and top performers", "A summary table / pivot", "A plain-language read of the numbers"]),
        ("A visual story, applied safely", ["The right chart for the message", "AI outputs checked against known values", "Your own safe-use checklist"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Riverside Supplies dataset.",
        "You do it yourself in Google Sheets — on the sample data, or on your own non-confidential data.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You compare the AI's output with a value you can confirm, and refine your prompt if it is off.",
        "You keep the working prompt or formula — it becomes part of your AI-in-Sheets toolkit.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Gemini for Google Sheet (C817) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 8 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build one connected result from a single dataset. You take a messy quarter of orders "
    "for a small retailer, 'Riverside Supplies', and use Gemini AI in Google Sheets to generate and "
    "explain formulas, clean and organise the data, analyse it, and turn it into charts you can trust. "
    "Wherever you can, use your own non-confidential data so you leave with skills applied to your own "
    "work; the supplied Riverside Supplies sample sheet is provided for everyone to follow along."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a current Chrome or Edge browser.",
        "A Google account with access to Google Sheets and Google Drive.",
        "Gemini in Google Sheets available and enabled on your account (the trainer confirms access at the start of the day).",
        "The sample 'Riverside Supplies — Q1 Orders' Google Sheet (the trainer shares a link; make your own copy with File > Make a copy) — or your own non-confidential dataset.",
    ],
    verify_text="Before Lab 1, confirm you can open Google Sheets, make your own copy of the sample sheet, and open the Gemini side panel (\"Ask Gemini\"). If Gemini is not visible on your account, tell the trainer.",
    verify_code="Open sheets.google.com  ·  open the sample sheet  ·  File > Make a copy  ·  open the Gemini / Ask Gemini panel",
    conventions=[
        "Placeholders such as <YOUR COPY> or <RANGE> are replaced with your own values.",
        "Prompts you give Gemini are shown in a shaded box — paste them into the side panel, or into an =AI() formula where a lab says so.",
        "Cell references (e.g., A2:I200) and menu paths (e.g., Insert > Chart) are written exactly as you will use them.",
        "Every lab ends with a 'Test it' step — verify the AI's result against a value you can confirm before you move on.",
    ],
)
LAB_NOTE = (
    "Use only data you are authorised to use. Never paste passwords, personal identifiers or "
    "confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if "
    "in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change "
    "over time; the trainer will point out the current location on the day."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="In one day you have taken a messy spreadsheet from raw export to a clean, analysed and charted dataset — using Gemini AI at every step, and checking its work before trusting it.",
    sections=[
        dict(title="What you built", bullets=[
            "Gemini AI set up and accessible in your own copy of the Riverside Supplies sheet.",
            "Formulas generated and explained by AI, including a multi-step formula you refined and verified.",
            "A reusable prompt pattern (range, goal, output, conditions) for spreadsheet tasks.",
            "A cleaned, transformed and organised dataset from a messy export.",
            "An analysis — totals, averages, top performers and a summary table — plus the right chart to tell the story.",
            "A personal checklist for validating AI output and applying AI safely to real work data.",
        ]),
        dict(title="What to do next", bullets=[
            "Point these techniques at one real, recurring spreadsheet task in your own week and measure the time saved.",
            "Keep verifying: check every AI formula or figure against a value you can confirm before you act on it.",
            "Save your best prompts so you and your team can reuse them.",
            "Keep confidential data out of prompts, and note where AI helped so your work stays accountable.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the clean-analyse-chart flow on the sample data from memory, writing your own prompts.",
    "Apply the techniques to a real, non-confidential spreadsheet from your own organisation.",
    "Review each lab's detailed steps in this guide and re-run the tasks on your own machine.",
]
LG_GLOSSARY = [
    ("Generative AI", "AI that creates new content — text, formulas, summaries — from a plain-language request, rather than only retrieving existing answers."),
    ("Gemini", "Google's AI assistant; inside Google Sheets it helps you build formulas, clean data, analyse and summarise."),
    ("Gemini side panel", "The \"Ask Gemini\" panel in Sheets where you have a conversation about the data in your spreadsheet."),
    ("=AI() function", "A Google Sheets function that sends a prompt to Gemini and returns the result into a cell."),
    ("Prompt", "The plain-language instruction you give the AI; a good one states the range, goal, output format and conditions."),
    ("Formula", "A spreadsheet instruction (such as =SUM or =IF) that calculates a result from your data."),
    ("Range", "A block of cells, written like A2:I200, that a formula or prompt applies to."),
    ("Data cleaning", "Standardising and correcting data — fixing formats, trimming spaces, filling or flagging blanks — so it can be used."),
    ("Transforming data", "Reshaping data: splitting or merging columns, extracting fields, categorising rows or reformatting values."),
    ("Pivot table", "A summary table that groups and aggregates a flat list, such as total sales by region."),
    ("Chart", "A visual representation of data — bar, line, pie — used to show a pattern or comparison at a glance."),
    ("Validation", "Checking that an AI result is correct by comparing it against a value you can confirm yourself."),
    ("Hallucination", "A confident but wrong AI output; the reason every AI result must be verified before use."),
    ("Human in the loop", "The practice of a person reviewing and approving AI output before it is relied upon."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", "27 July 2026", "Initial release — C817 AI Application for Google Sheet courseware.", TRAINER),
    ("1.1", VERSION_DATE, "Course retitled to Gemini for Google Sheet.", TRAINER),
]
