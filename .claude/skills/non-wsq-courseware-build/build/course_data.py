"""Single source of truth for the C817 non-WSQ courseware package (v2.0).

Gemini for Google Sheet: three topics and twelve connected labs, built on one
fictional HR scenario - Orchid Bay Talent Partners' Q3 2026 hiring drive - and
on Google's official guidance "Collaborate with Gemini in Google Sheets"
(support.google.com/docs/answer/14356410). Lab mock data comes from mock_data.py.

  Topic 1  Fundamentals of Google Sheet          Labs 1-4
  Topic 2  Data Analytics and Visualization      Labs 5-8
  Topic 3  Interactive Dashboard                 Labs 9-12

NON-WSQ RULES - the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference - this course carries the plain code C817.
"""

TITLE = "Gemini for Google Sheet"
SHORT_TITLE = "Gemini for Google Sheet (C817)"   # used in output filenames
COURSE_CODE = "C817"
COURSE_PAGE = "tertiarycourses.com.sg/gemini-for-google-sheet.html"
GITHUB_REPO = "tertiarycourses/C817-Gemini-for-Google-Sheet"
PROMPTS_PAGE = "https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/"
VERSION = "v2.0"
VERSION_DATE = "19 October 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Dr. Alfred Ang"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; 7.5 instructional hours)"
DARK_THEME = False
SHOT_CREDIT = "Screenshot: Google Docs Editors Help - Collaborate with Gemini in Google Sheets"

# ---------------------------------------------------------------- sources
_H = "https://support.google.com/docs/answer/"
S_SHEETS = _H + "14356410"      # Collaborate with Gemini in Google Sheets (the course's reference page)
S_AI = _H + "15877199"          # Use the AI function in Google Sheets
S_PROMPTS = _H + "15013615"     # Learn about prompts for Gemini in Docs, Sheets, Slides ...
S_PLANS = _H + "13952129"       # Get started with Google Workspace with Gemini
S_PIVOT = _H + "1272900"
S_CF = _H + "78413"
S_DROPDOWN = _H + "186103"
S_CHART = _H + "63824"
S_VLOOKUP = _H + "3093318"
S_COUNTIFS = _H + "3256550"
S_IF = _H + "3093364"
S_TABLES = _H + "14239833"
S_PROTECT = _H + "1218656"
S_GEMS = "https://support.google.com/gemini/answer/15146780"
S_BLOG = "https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/"

TRAINER_PROFILE = dict(
    name="Dr. Alfred Ang",
    role="AI Trainer & Engineer",
    points=[
        ("graduate", "PhD-qualified trainer specialising in AI, data and software engineering."),
        ("laptop", "Builds AI agents and Gemini and Google Workspace workflows for business teams."),
        ("teach", "Trains professionals across Singapore on practical, project-based AI skills."),
        ("badge", "Certifications: PMP, AWS, Microsoft, CompTIA, CKA, CKAD."),
    ],
    links=[("linkedin", "linkedin.com/in/angchewhoe"), ("github", "github.com/alfredang")],
)

ICE_BREAKER = [
    "Your name, organisation and role.",
    "One spreadsheet you rebuild or clean every week or month.",
    "A formula, chart or report you wish someone would just build for you.",
    "Whether you can see the Ask Gemini (spark) button in Google Sheets on your account.",
]

LEARNING_OUTCOMES = [
    "LO1: Use Gemini in Google Sheets - the side panel, actions and formula help - to summarise, quality-check and "
    "prepare HR data, and to generate, explain and fix formulas such as VLOOKUP, COUNTIF and nested IF.",
    "LO2: Create colour-coded tables, trackers and dropdowns, extract and categorise text with the AI function, and "
    "generate data analysis, insights, pivot tables and charts with Gemini, verifying every result.",
    "LO3: Build an interactive hiring dashboard, automate repeat screening with a custom Gem, and use Gemini's "
    "optimisation solver, reporting and sharing features responsibly.",
]
LO_TITLES = ["Sheets Fundamentals", "Analytics & Visualization", "Interactive Dashboard"]

TOPIC_RECAPS = {
    1: [
        ("LO1 · Side panel", "Summaries, questions across chosen tabs, Insert, Retry, Undo and Clear history."),
        ("LO1 · Data quality", "Duplicates, spelling variants, bad emails, text numbers and impossible values found and counted."),
        ("LO1 · Data prep", "Gemini actions - find and replace, number format, insert/delete, freeze, sort, filter - with counts before and after."),
        ("LO1 · Formulas", "VLOOKUP, IF, nested IF and COUNTIFS from plain English; explained, fixed and reconciled."),
    ],
    2: [
        ("LO2 · Tables and trackers", "Notes turned into a colour-coded tracker with dropdowns, checkboxes and editable rules."),
        ("LO2 · AI function", "=AI extracts, categorises and summarises text; accuracy measured against an answer key."),
        ("LO2 · Analysis", "Trends, rates and cost per hire with Analysis steps; pivot tables checked with COUNTIFS."),
        ("LO2 · Charts", "Inserted (static) and linked charts; titles that state the finding; alt text."),
    ],
    3: [
        ("LO3 · KPI formulas", "Dropdown selectors drive COUNTIFS and AVERAGEIFS KPIs and summary tables."),
        ("LO3 · Interactivity", "Linked charts, a metric switch, KPI alerts and protection - tested on three views."),
        ("LO3 · Gems", "A Candidate Screener Gem with instructions and knowledge files, used from the Sheets side panel."),
        ("LO3 · Decide and share", "Optimised hires within budget, proved with formulas, exported and shared minimally."),
    ],
}


# ---------------------------------------------------------------- section helper
def S(title, lab, definition, why, how, example, use_when, avoid_when, quality, sources, brief, **extra):
    d = dict(title=title, lab=lab, definition=definition, why=why, how=how, example=example, use_when=use_when,
             avoid_when=avoid_when, quality=quality, sources=sources, brief=brief)
    d.update(extra)
    return d


def B(what, why, check, prompts, verify, try_head="ASK GEMINI", try_title="Try It in Gemini", **extra):
    d = dict(what=what, why=why, check=check, prompts=prompts, verify=verify, try_head=try_head, try_title=try_title)
    d.update(extra)
    return d


TOPICS = [
    # ================================================================== TOPIC 1
    dict(
        num=1,
        code="01",
        title="Fundamentals of Google Sheet",
        subtitle=(
            "Gemini side panel and summaries · data quality checks · data prep with Gemini actions · generating, "
            "explaining and fixing formulas (VLOOKUP, COUNTIF, nested IF)"
        ),
        weighting="Labs 1-4",
        concepts=[
            ("Native Sheets first", "Gemini works best on a Google Sheets file - save an .xlsx as Google Sheets first."),
            ("Ask, then insert", "Answers stay in the side panel until you click Insert. Insert anything you want to keep."),
            ("Actions you approve", "For edits, Gemini shows an Action preview card. You click Apply - and can Undo."),
            ("Name the tab and column", "'Count Hired in the Stage column on Applications' beats 'analyse my data'."),
            ("Describe the formula", "Write the rule in plain English; Gemini writes VLOOKUP, IF or COUNTIFS and explains it."),
            ("Check every number", "Confirm Gemini's answers with your own COUNTIF, COUNTIFS or pivot-table total."),
        ],
        sections=[
            S("What Gemini in Google Sheets Can Do", 1,
              "Gemini in Google Sheets is Google's AI collaborator built into the spreadsheet. From the side panel you can "
              "create tables, create formulas, generate data analysis and insights, build charts and graphs, summarise "
              "files from Drive and emails from Gmail, and perform actions on the sheet - conditional formatting, pivot "
              "tables, dropdowns and checkboxes, sorting and filtering, find and replace, number formats, inserting, "
              "deleting or freezing rows and columns, filling ranges, formatting tables and solving optimisation tasks. "
              "Beside the panel, the AI function (=AI) brings Gemini into individual cells.",
              "It turns spreadsheet work you would normally look up or click through into a plain-English request. That "
              "saves time on routine work, but Gemini can be wrong, so its output stays a proposal until you check it. "
              "The feature needs an eligible Google Workspace or Google AI plan and works best on native Google Sheets "
              "files.",
              ["Open a spreadsheet in Google Sheets and click Ask Gemini (the spark icon) at the top right.",
               "Pick a suggested prompt or type your own in the prompt box and press Enter.",
               "Insert, Apply, Retry or Undo the result - then verify it against the data."],
              ["Orchid Bay's analyst opens the Q3 applications export and reads Gemini's automatic summary.",
               "She asks which positions received the most applications and inserts the table.",
               "A COUNTIF confirms the Rejected count Gemini reported."],
              ["The data is approved for use with Gemini in your organisation.",
               "You can describe the result you want and check it afterwards."],
              ["You would act on an answer without checking it.",
               "The file is an .xlsx you have not saved as Google Sheets."],
              [("Access", "Eligible plan, right account, Ask Gemini visible."),
               ("Scope", "The right tabs selected as sources."),
               ("Evidence", "Every answer checked with a formula.")],
              [S_SHEETS, S_PLANS, S_BLOG],
              B("Google's AI built into Sheets: tables, formulas, analysis, charts and actions from plain-English prompts.",
                "It speeds up routine spreadsheet work - but its output is a proposal until you check it.",
                "Can you name three things Gemini can do and one it should not decide for you?",
                ["Open a sheet > Ask Gemini (spark, top right).",
                 "Summarize this spreadsheet.",
                 "Which Position has the most applications?",
                 "Shortcut: Cmd + Ctrl + N (Mac) / Ctrl + Alt + N (Windows)."],
                ["Rows and dates match the About tab.",
                 "A COUNTIF agrees with Gemini's count."],
                shots=[dict(kind="shot", title="Gemini in Google Sheets: the Side Panel", file="gemini-side-panel.png",
                            caption="Summary of the sheet, suggestions, Gems and the prompt box with its sources.")])),
            S("Prompting Gemini and the Side Panel", 1,
              "A prompt is the instruction you type in the side panel. Good spreadsheet prompts name the tab and columns, "
              "state the task and the output you want, and add any rules. The panel also lets you choose sources - the "
              "dropdown in the prompt box picks which tabs Gemini looks at - and offers Insert, Copy, Retry, Undo, "
              "feedback (thumbs) and More options > Clear history. Your conversation is lost when you reload, close the "
              "file or go offline.",
              "Vague prompts give vague or wrong answers. Naming the tab and column removes guesswork, and selecting "
              "sources stops Gemini mixing up similar tables. Knowing that history disappears teaches you to insert or "
              "copy results you want to keep.",
              ["Write: task + tab/column names + output format + rules (e.g. 'don't change anything').",
               "Use the sources dropdown to focus Gemini on the tabs you mean.",
               "Refine with a follow-up before inserting; Retry for a different version."],
              ["Weak: 'analyse this'. Strong: 'Using Applications and Jobs, make a table of applications and openings per Position.'",
               "A follow-up adds Applications_per_Opening and sorts it before Insert.",
               "The result is inserted on its own tab so it survives a reload."],
              ["The task has a clear output - a number, a table, a formula or a chart.",
               "You can tell Gemini which tab and columns to use."],
              ["The question needs judgement Gemini cannot see (e.g. a client's preference).",
               "You rely on the panel history as your record - insert instead."],
              [("Clarity", "Tab, columns, task and output in every prompt."),
               ("Focus", "Sources set to the right tabs."),
               ("Record", "Results inserted; Prompt_Log updated.")],
              [S_SHEETS, S_PROMPTS],
              B("A prompt names the tab, columns, task and output. The panel adds sources, Insert, Retry, Undo and history.",
                "Precise prompts give precise answers; history is lost on reload, so insert what matters.",
                "Does your prompt say which tab, which columns and what the output should look like?",
                ["Using the Applications and Jobs tabs, make a table of applications and Openings per Position.",
                 "Follow-up: add Applications_per_Opening and sort high to low.",
                 "Then click Insert."],
                ["The table has 8 positions.",
                 "It survives a page reload."],
                shots=[dict(kind="shot", title="Gemini Panel Controls at a Glance", file="gemini-controls.png",
                            caption="The controls from Google's Explore Gemini in Sheets table.")]),
              compare=dict(title="Five Ways to Work with Gemini in Sheets",
                           headers=["Way in", "Side panel answer", "Insert", "Action", "=AI function", "Gem"],
                           rows=[("What you do", "Ask a question", "Ask, then click Insert", "Ask, then click Apply",
                                  "Type =AI(...) in a cell", "Pick your Gem in the panel"),
                                 ("Changes the sheet?", "No", "Yes, when you insert", "Yes - Undo available",
                                  "Yes, when you generate", "Only if you insert"),
                                 ("Best for", "Questions, insights", "Tables, formulas, charts",
                                  "Formatting, pivots, sort/filter", "Row-by-row text", "Repeatable expert tasks"),
                                 ("Lab", "1, 7", "1, 5, 8", "2, 3, 5", "6", "11")])),
            S("Why Data Quality Matters", 2,
              "Data quality is whether data is complete, consistent, unique, valid and accurate enough for the decision it "
              "supports. In recruitment exports the usual problems are duplicate application IDs, the same source spelt "
              "several ways ('LinkedIn', 'Linked In', 'JobStreet ' with a trailing space), missing or invalid emails, "
              "numbers stored as text ('S$4,800') and impossible values such as negative experience.",
              "Every count, chart and AI answer inherits the errors in its source. Duplicates inflate applications, spelling "
              "variants split a source into several, and a salary typed as text is silently ignored by AVERAGE. Gemini "
              "analyses the data you give it - it does not make bad data good.",
              ["Profile first: rows vs unique IDs, distinct values per category column, blanks and data types.",
               "Flag problems with conditional formatting before changing anything.",
               "Prove each count with a formula (COUNTUNIQUE, COUNTBLANK, COUNTIF)."],
              ["243 rows but 240 unique Candidate_IDs: 3 duplicates.",
               "'Linked In', 'linkedin' and 'JobStreet ' would split two sources.",
               "5 salaries typed as text and one negative Years_Experience."],
              ["Before any analysis, dashboard or AI insight on new data.",
               "Data comes from an export or several systems."],
              ["Fixing a value would mean guessing - flag it and ask the owner.",
               "Deleting rows you cannot explain."],
              [("Unique", "Rows = unique IDs, or duplicates explained."),
               ("Consistent", "One spelling per category."),
               ("Valid", "Numbers are numbers, dates are dates, values in range.")],
              [S_SHEETS, S_CF],
              B("Complete, consistent, unique, valid data. Typical issues: duplicates, spelling variants, text numbers.",
                "Every count and chart inherits the errors - 'Linked In' and 'LinkedIn' become two sources.",
                "Profile before you analyse: rows vs unique IDs, distinct values, data types.",
                ["Check the Applications tab for data-quality problems. Don't change anything.",
                 "Highlight duplicate values in the Candidate_ID column in orange.",
                 "List every distinct Source value exactly as spelt."],
                ["243 rows vs 240 unique IDs.",
                 "=COUNTUNIQUE(...) confirms it."])),
            S("Gemini Actions: Preview, Apply, Undo", 3,
              "An action is a change Gemini makes to your sheet from a prompt: apply conditional formatting, create a pivot "
              "table, add a dropdown or checkbox, sort, filter or clear a filter, find and replace, set a number format, "
              "insert, delete or freeze rows and columns, fill a range or format a table. Gemini first shows an Action "
              "preview card; nothing changes until you click Apply. Afterwards Settings (when available) lets you adjust "
              "the action and Undo reverses it. One prompt can combine several actions - a multi-step task.",
              "Actions turn menus you would hunt for into one sentence, while the preview keeps you in control. Because "
              "Undo is available only until you make further changes, you check each action straight away.",
              ["Describe the change, naming the tab and column ('In the Source column only ...').",
               "Read the Action preview card, then click Apply.",
               "Check the sheet immediately; use Settings to adjust or Undo to reverse."],
              ["'Replace Linked In and linkedin with LinkedIn in the Source column' - Apply - 7 sources remain.",
               "'Delete the Internal_Notes column' removes notes screening does not need.",
               "A multi-step prompt formats dates, adds a Stage dropdown and highlights Hired rows."],
              ["The change is clear and you can see the result on the sheet.",
               "You want several routine edits in one go."],
              ["The change cannot be checked or undone easily (e.g. deleting rows on the only copy).",
               "The instruction is ambiguous about which column or range."],
              [("Preview", "Action card read before Apply."),
               ("Control", "Checked straight away; Undo or Settings used."),
               ("Count", "Row count recorded before and after.")],
              [S_SHEETS, S_TABLES],
              B("A change Gemini makes from a prompt: shown on an Action preview card, applied when you click Apply.",
                "Menus become sentences - and the preview, Settings and Undo keep you in control.",
                "Did you check the result before your next change? Undo only lasts until then.",
                ["In the Source column, replace 'Linked In' and 'linkedin' with 'LinkedIn'.",
                 "Delete the Internal_Notes column.",
                 "Freeze the top row and the first column.",
                 "Sort the table by Applied_Date in descending order."],
                ["Filter on Source shows 7 values.",
                 "Still 240 rows after each change."],
                try_title="Try It with Gemini Actions", try_head="ASK GEMINI, THEN APPLY")),
            S("Data Prep: From Export to Clean Table", 3,
              "Data preparation turns a raw export into a table you can analyse: one header row, one record per row, one "
              "kind of value per column, consistent categories, real numbers and dates, and no notes or blank rows inside "
              "the data. In Google Sheets you combine Gemini actions with built-in tools such as Data > Data cleanup > "
              "Remove duplicates and Trim whitespace, then format the range as a table.",
              "Clean data makes every later formula, pivot table, chart and AI answer trustworthy. Fixing in helper columns "
              "and keeping counts before and after lets you prove nothing was lost.",
              ["Remove exact duplicates and trim whitespace with Data cleanup.",
               "Standardise categories and convert text numbers with Gemini actions.",
               "Tidy structure: helper columns, drop unneeded columns, freeze headers, apply a table style."],
              ["243 rows become 240 after Remove duplicates.",
               "Name_Clean uses =PROPER(TRIM(B2)); the original names stay.",
               "A Stage dropdown stops new spelling variants creeping in."],
              ["Before analysis, dashboards or sharing.",
               "The same export arrives every week - write the steps down once."],
              ["The original export is your only copy - work on a copy.",
               "A fix needs information you don't have."],
              [("Shape", "One header row, one record per row."),
               ("Types", "COUNT over a number column equals the row count."),
               ("Audit", "Originals kept; counts before and after.")],
              [S_SHEETS, S_TABLES, S_DROPDOWN],
              B("Turn an export into an analysis-ready table: no duplicates, one spelling per category, real numbers.",
                "Clean data is what makes every later formula, chart and AI answer trustworthy.",
                "Can you prove the row count before and after each change?",
                ["How can I remove duplicate rows on the Applications tab?",
                 "Set Expected_Salary to currency S$ with no decimal places.",
                 "Insert Name_Clean with =PROPER(TRIM(B2)) filled down.",
                 "Apply a table style to the data."],
                ["240 rows, 7 sources.",
                 "=COUNT on salaries = 240."])),
            S("Formulas: VLOOKUP, COUNTIF and Nested IF", 4,
              "A formula starts with = and calculates a value. VLOOKUP(search key, range, column number, FALSE) finds a key "
              "in the first column of a range and returns a value from another column. IF(test, if true, if false) returns "
              "one of two results, and IFs can be nested, with AND/OR, for three or more outcomes. COUNTIF counts cells "
              "that meet one condition; COUNTIFS counts rows that meet several.",
              "Formulas make screening rules repeatable and auditable: anyone can click a cell and see the rule, and the "
              "result recalculates when data or thresholds change. Keeping thresholds in a Settings tab means one edit "
              "re-screens everyone.",
              ["Write the business rule in words, including edge cases.",
               "Lock lookup ranges and setting cells with $ before filling down.",
               "Check one row by hand and reconcile totals with COUNTIF."],
              ["=VLOOKUP(E2,Jobs!$A$2:$H$9,5,FALSE) returns the role's Min_Years.",
               "=IF(K2<=Q2,\"Within budget\",\"Above budget\") checks salary fit.",
               "Strong + Possible + Not suitable = 240."],
              ["A value follows a fixed rule from other values.",
               "The result must update when data or thresholds change."],
              ["Typing a number that could be calculated.",
               "Hard-coding a threshold inside the formula."],
              [("Readable", "Rule in words matches the formula."),
               ("Robust", "Ranges locked; errors handled."),
               ("Reconciled", "One row by hand; totals add up.")],
              [S_VLOOKUP, S_IF, S_COUNTIFS],
              B("VLOOKUP fetches from a table, IF decides, nested IF/AND handles several outcomes, COUNTIF(S) counts.",
                "Rules become repeatable and auditable - change a threshold once and everyone is re-screened.",
                "Can you work row 2 out by hand and get the same answer?",
                ["Look up the Job_ID in E2 on Jobs and return Min_Years.",
                 "Return Within budget if K2 <= Q2, otherwise Above budget.",
                 "Strong if M2 >= pass mark AND H2 >= R2; Possible if M2 >= 60; else Not suitable."],
                ["Row 2 checked by hand.",
                 "Totals add up to 240."],
                try_head="DESCRIBE THE RULE")),
            S("Generate, Explain and Fix Formulas with Gemini", 4,
              "Gemini creates formulas from a description: ask in the side panel, or type = in a cell and press Cmd + Ctrl "
              "+ G (Mac) or Ctrl + Alt + G (Windows), then click Insert into the selected cell. It can explain any formula "
              "step by step. When a cell shows an error, hover over it and click Fix: Gemini reviews the formula, explains "
              "the problem and suggests a correction.",
              "You no longer need to remember syntax - but you still need to read the formula. Explanations teach as you "
              "go and help you audit inherited sheets; Fix turns cryptic errors such as #REF! into plain English.",
              ["Click the target cell, describe the formula with cell references, then Insert and fill down.",
               "Ask Gemini to explain the formula and work through one row.",
               "Hover over an error and click Fix; read why before accepting."],
              ["#REF! in Budget_Max: VLOOKUP asked for column 9 of an 8-column range - Fix changes it to 8.",
               "Gemini writes the nested IF for Screen_Result from one sentence.",
               "Its explanation of row 2 matches M2, H2 and R2."],
              ["You know the rule but not the syntax.",
               "You inherit a sheet full of formulas you didn't write."],
              ["You can't read the formula Gemini wrote - ask for an explanation first.",
               "The fix changes the meaning of the rule, not just the syntax."],
              [("Placement", "Target cell selected before Insert."),
               ("Understanding", "Explanation matched to real values."),
               ("Fixes", "Reason for the error understood.")],
              [S_SHEETS, S_VLOOKUP],
              B("Describe it and Gemini writes it; ask and Gemini explains it; hover an error and Fix repairs it.",
                "No syntax to memorise - but you still read, explain and check every formula.",
                "Could you explain this formula to a colleague in one sentence?",
                ["Type = in a cell, then Cmd + Ctrl + G (Mac) / Ctrl + Alt + G.",
                 "Explain the formula in T2 step by step.",
                 "Hover over #REF! > Fix."],
                ["Q2 shows S$6,500 after Fix.",
                 "Explanation matches row 2."],
                try_head="ASK GEMINI FOR THE FORMULA")),
        ],
    ),
    # ================================================================== TOPIC 2
    dict(
        num=2,
        code="02",
        title="Data Analytics and Visualization",
        subtitle=(
            "tables, trackers and dropdowns · conditional formatting · the AI function and Fill with Gemini · data "
            "analysis, insights and pivot tables · charts and graphs"
        ),
        weighting="Labs 5-8",
        concepts=[
            ("Structure from text", "Gemini turns notes into a table you refine before you insert it."),
            ("Rules that colour", "Conditional formatting flags what matters; Settings lets you edit the rule."),
            ("AI in a cell", "=AI(prompt, range) extracts, categorises and summarises text row by row."),
            ("Insights with evidence", "Analysis steps show how Gemini calculated; you confirm with a formula."),
            ("Pivot tables on request", "Gemini builds a pivot table; you adjust it and check its totals."),
            ("Inserted charts are copies", "A chart Gemini inserts doesn't follow later changes - build linked ones too."),
        ],
        sections=[
            S("Tables, Trackers and Dropdowns", 5,
              "Gemini can create a table from scratch ('create an onboarding checklist') or from unstructured text such as "
              "meeting or interview notes, show it in the panel, let you refine it with follow-ups ('add an Outcome "
              "column') and insert it into the sheet. Dropdowns limit a column to valid values and checkboxes record "
              "yes/no states; Gemini adds both as actions.",
              "Trackers only work if everyone records things the same way. A table with dropdowns and checkboxes keeps "
              "data consistent from the start, so the analysis later is easy and trustworthy.",
              ["Ask for the table with exact column names and allowed values.",
               "Refine with follow-ups, then Insert on a new tab.",
               "Add dropdowns and checkboxes with actions; test them."],
              ["12 lines of interview notes become a 12-row Interview_Tracker.",
               "Status allows only Scheduled, Completed, No-show and Rescheduled.",
               "Reference_Checked is a checkbox column."],
              ["Information arrives as free text but must be tracked.",
               "Several people update the same sheet."],
              ["The notes contain sensitive details the tracker doesn't need.",
               "You insert before checking the draft against the notes."],
              [("Columns", "Named and ordered as requested."),
               ("Values", "Dropdowns restrict to valid options."),
               ("Fidelity", "Every note appears exactly once.")],
              [S_SHEETS, S_DROPDOWN, S_TABLES],
              B("Gemini builds tables from scratch or from notes; dropdowns and checkboxes keep trackers consistent.",
                "Consistent input today means reliable analysis tomorrow.",
                "Does every note appear once, with a valid Status?",
                ["Using the notes on Interview_Notes, create a table with Date, Time, Candidate ... and Status.",
                 "Follow-up: add Outcome and Reference_Checked columns.",
                 "Make Status a dropdown with Scheduled, Completed, No-show and Rescheduled."],
                ["12 rows; statuses 5/3/2/2.",
                 "Dropdowns and checkboxes work."],
                try_head="ASK GEMINI, THEN INSERT")),
            S("Conditional Formatting with Gemini", 5,
              "Conditional formatting changes a cell's look when a rule is true: highlight rows over a threshold, values "
              "that exceed another column, duplicates or past dates, or shade values with a colour scale. Gemini creates "
              "the rule from a sentence ('Highlight rows where Screening_Score is 85 or more in light green'). The rules "
              "are visible and editable in Format > Conditional formatting or via Settings on the action card.",
              "Formatting makes exceptions jump out - the candidates above budget, the long notice periods - without "
              "changing the data. Because the rules are live, the colours update when the data changes.",
              ["Say what to format, the condition and the colour; say 'whole row' if you mean it.",
               "Apply, then count the coloured cells with COUNTIF to confirm.",
               "Edit thresholds in the rule rather than adding a second rule."],
              ["Score 85+ rows green: 11 rows; edited to 80: 21 rows.",
               "Expected_Salary bold red when it is above Budget_Max: 12 cells.",
               "A red-to-green colour scale on Interview_Score."],
              ["You need exceptions to stand out for a reviewer.",
               "The rule is simple enough to state in one sentence."],
              ["Colour is the only signal - add a column for accessibility and filtering.",
               "Too many colours compete and nothing stands out."],
              [("Rule", "Visible in Format > Conditional formatting."),
               ("Count", "COUNTIF agrees with the coloured rows."),
               ("Restraint", "Few colours, each with a meaning.")],
              [S_CF, S_SHEETS],
              B("Formatting that follows a rule: highlight rows, compare columns, colour scales, duplicates.",
                "Exceptions jump out without changing the data - and update as the data changes.",
                "Does a COUNTIF give the same number as the coloured rows?",
                ["Highlight rows where Screening_Score is 85 or more in light green.",
                 "Make Expected_Salary bold red when it is greater than Budget_Max.",
                 "Add a colour scale to Interview_Score from red to green."],
                ["11 green rows (21 at 80).",
                 "12 red salaries."],
                try_head="ASK GEMINI, THEN APPLY")),
            S("The AI Function (=AI)", 6,
              "The AI function puts Gemini in a cell: =AI(\"prompt\", [range]) (or =Gemini(...)). It can generate text, "
              "summarise, categorise (including sentiment) and get real-time information from Google Search. You type the "
              "formula, select the cells and click Generate and insert; Refresh and insert regenerates. The range is the "
              "only data it sees - it doesn't read the whole sheet or Drive. Results are text, cannot be undone, are "
              "limited to 350 selected cells at a time and do not refresh automatically when inputs change.",
              "It turns free text - candidate summaries, interview notes - into structured columns you can filter, count "
              "and chart. Because results are AI-generated, you measure their accuracy before you rely on them.",
              ["Write a specific prompt with the output format ('Output only the number').",
               "Point the range at the cells it needs; fill down and Generate and insert.",
               "Compare a sample with known values; refresh after editing the prompt."],
              ["=AI(\"Extract the notice period in weeks ...\", D2) turns 'one month's notice' into 4.",
               "=AI(\"Classify this interview feedback as Positive, Mixed or Negative ...\", E2).",
               "A Checks tab counts how many AI values match the answer key."],
              ["Each row needs the same judgement on free text.",
               "You can check a sample against known answers."],
              ["The output feeds a decision about a person without review.",
               "You need numbers to calculate - convert and check first."],
              [("Prompt", "Specific, with the output format."),
               ("Accuracy", "Measured on a sample or answer key."),
               ("Fairness", "No personal characteristics in prompts or outputs.")],
              [S_AI],
              B("=AI(\"prompt\", range) in a cell: generate, summarise, categorise, or search - row by row.",
                "Free text becomes columns you can filter and count - once you have measured the accuracy.",
                "How many AI answers match the recorded values?",
                ["=AI(\"Extract the notice period in weeks. Output only the number.\", D2)",
                 "=AI(\"Classify this feedback as Positive, Mixed or Negative.\", E2)",
                 "Select the cells > Generate and insert."],
                ["Notice matches near 30/30.",
                 "Sentiment split vs Answer_Key."],
                try_head="TYPE IN A CELL",
                shots=[dict(kind="pair", title="The AI Function in Google Sheets",
                            images=[("ai-function-formula.png", "Type the =AI formula",
                                     "A prompt plus the cells it should use."),
                                    ("ai-function-results.png", "Generate and insert",
                                     "Gemini fills every selected AI cell.")])])),
            S("Fill with Gemini and AI Columns", 6,
              "Fill with Gemini completes a column from the context of the table: type one or two examples and drag the "
              "fill handle, or select an empty range and choose Fill, optionally with a custom prompt. In a table, Insert "
              "AI column adds a column whose first row shows the AI function, ready to autofill. The side panel can also "
              "categorise a whole column at once and return a summary table.",
              "Examples are often easier than instructions: show Gemini one correct answer and it follows the pattern. "
              "Side-panel categorisation gives the big picture - themes and counts - that row-by-row formulas cannot.",
              ["Type a correct example in the first cell.",
               "Select the range and use Fill with Gemini (or an AI column).",
               "Spot-check rows and ask the side panel for themes and counts."],
              ["Top_Skills: one example in I2, Gemini fills I3:I31.",
               "The side panel groups 30 feedback notes into themes.",
               "A bias check on the generated summaries."],
              ["The pattern is easy to show but hard to describe.",
               "You need both per-row values and an overview."],
              ["The example is wrong - errors spread down the column.",
               "The column will be used without spot-checks."],
              [("Example", "First value correct and typical."),
               ("Coverage", "Every row filled, none invented."),
               ("Overview", "Theme counts add up to the rows.")],
              [S_AI, S_BLOG],
              B("Show one example and Gemini fills the column; or let the side panel categorise the whole column.",
                "Examples beat long instructions - and themes give the big picture.",
                "Spot-check five rows: did Gemini follow your example?",
                ["Type an example in I2, select I2:I31 > Fill.",
                 "Group the Interview_Feedback into themes and count each.",
                 "Do any summaries mention personal characteristics?"],
                ["I2:I31 filled.",
                 "Theme counts add up to 30."],
                single=True)),
            S("Data Analysis and Insights with Gemini", 7,
              "Gemini answers questions about the data in your sheet: identify trends, compare groups, calculate rates and "
              "averages, suggest analyses ('What analysis can you help me perform with this sheet?') and even discuss "
              "regression and prediction. Analysis steps shows how it calculated (and Show code, where offered), and "
              "Export to Docs sends the response to a new Google Doc. With 'Use Google Search' in the prompt it can bring "
              "in web information.",
              "Managers want answers, not tables. Gemini gets you to a first answer in seconds; Analysis steps and a "
              "formula check make it defensible. Web answers are external evidence and need their sources checked.",
              ["Ask a specific question with the measure, group and period.",
               "Open Analysis steps; confirm the key number with COUNTIFS or AVERAGEIFS.",
               "Ask for insights with numbers and actions, then Export to Docs."],
              ["Applications peaked in June 2026 (98).",
               "Referral has the best hire rate (12.8%); LinkedIn brings the most hires (11).",
               "HR Executive takes longest to fill (39.3 days)."],
              ["You need a quick, explainable answer from a dataset.",
               "You will check the key numbers before sharing."],
              ["A small group drives the result (e.g. 78 referrals) and nobody checks it.",
               "Web results without sources."],
              [("Definition", "Measures defined (what is a hire?)."),
               ("Traceability", "Analysis steps read; formula check done."),
               ("Context", "Group sizes stated with every rate.")],
              [S_SHEETS],
              B("Ask questions of the data: trends, comparisons, rates. Analysis steps shows the working.",
                "A first answer in seconds - made defensible with a formula check.",
                "Which number in Gemini's insight did you confirm with COUNTIFS?",
                ["What analysis can you help me perform with this sheet?",
                 "Identify trends in applications by Month.",
                 "Which Source has the best hire rate?",
                 "Export to Docs."],
                ["Peak June 98.",
                 "Referral 12.8%."],
                shots=[dict(kind="shot", title="A Gemini Analysis Response", file="gemini-chart-response.png",
                            caption="Analysis steps, Insert, Preview, Copy, Sources, Export to Docs and feedback.")])),
            S("Pivot Tables with Gemini", 7,
              "A pivot table summarises a large table by grouping rows and aggregating values - counts, sums, averages - "
              "with fields in rows, columns and filters. Gemini creates one from a sentence ('Create a pivot table that "
              "shows the count of Candidate_ID with Source in rows and Stage in columns'), usually on a new sheet, and "
              "Settings opens the pivot table editor to adjust it.",
              "Pivot tables answer 'how many / how much by group' questions and stay linked to the data, so they refresh "
              "when it changes. Combined with Gemini you get the structure without hunting through the editor.",
              ["Name the value, the aggregation and the row/column fields.",
               "Apply, then adjust in Settings (filters, sorting, totals).",
               "Check one cell and the grand total with COUNTIFS."],
              ["Source x Stage: LinkedIn Hired 11, Rejected 147; grand total 720.",
               "Average Days_To_Hire by Position, sorted high to low.",
               "Both checked with COUNTIFS / AVERAGEIFS."],
              ["You need a grouped summary that updates with the data.",
               "The same breakdown is needed regularly."],
              ["The source data still has duplicates or spelling variants.",
               "A single number would do - use COUNTIFS."],
              [("Fields", "Rows, columns and values as intended."),
               ("Total", "Grand total equals the row count."),
               ("Check", "One cell confirmed by formula.")],
              [S_PIVOT, S_SHEETS],
              B("Group and aggregate a table - counts, sums, averages - by rows, columns and filters.",
                "Grouped answers that refresh with the data, created from one sentence.",
                "Does the grand total equal the number of rows?",
                ["Create a pivot table: count of Candidate_ID, Source in rows, Stage in columns.",
                 "Click Settings to add a filter.",
                 "=COUNTIFS(... \"LinkedIn\" ... \"Hired\")"],
                ["Grand total 720.",
                 "LinkedIn Hired 11."],
                try_head="ASK GEMINI, THEN APPLY", single=True)),
            S("Charts and Graphs with Gemini", 8,
              "Gemini generates charts from a description - 'Create a chart with Month on the x-axis and applications on "
              "the y-axis', 'Make a bar chart of hires by Source'. You can Preview the chart, Copy it, check Analysis steps, "
              "Export to Docs, and Insert it. Inserting adds a new tab with the chart and its underlying data; the chart is "
              "linked to that new tab's data and fully editable.",
              "The right chart makes a finding obvious in seconds. Asking for the chart type, axes and sorting gets a "
              "usable first draft; you then make the title state the finding and add alt text for accessibility.",
              ["Describe the chart type, axes, measure and sort order.",
               "Preview, then Insert; read the new-tab message.",
               "Rewrite the title as the finding; add alt text."],
              ["Line: applications by month - 'Applications peaked in June'.",
               "Sorted bar: hires by source - LinkedIn first.",
               "Column: the hiring funnel 720 / 61 / 47 / 41."],
              ["You need a quick, editable chart of a clear question.",
               "The chart is a one-off snapshot for a report."],
              ["The chart must follow new data - see Inserted vs Linked Charts.",
               "The chart type hides the story (e.g. a pie with many slices)."],
              [("Fit", "Chart type matches the question."),
               ("Title", "States the finding."),
               ("Access", "Alt text added.")],
              [S_SHEETS, S_CHART],
              B("Describe the chart; Preview, then Insert. Gemini adds a new tab with the chart and its data.",
                "A good chart makes the finding obvious - and its title should say it.",
                "Does the title state the finding, not just the measure?",
                ["Create a line chart with Month on the x-axis and applications on the y-axis.",
                 "Make a bar chart of hires by Source, sorted from most to fewest.",
                 "Suggest a title for each chart that states the main finding."],
                ["Peak June 98.",
                 "Funnel 720/61/47/41."],
                try_head="ASK GEMINI, THEN INSERT")),
            S("Inserted vs Linked Charts", 8,
              "A chart inserted from the Gemini panel is built on a copy of the data placed on its own new tab. Google's "
              "guidance is explicit: the generated chart doesn't link or respond to changes in the original data set used "
              "to generate it. A chart you build with Insert > Chart on a live range - or on a pivot table or formula "
              "table - updates whenever that range changes.",
              "Reports and dashboards must stay true when the data changes. Knowing which charts are snapshots and which "
              "are live prevents a dashboard from quietly showing last week's numbers.",
              ["Use Gemini-inserted charts for snapshots and drafts.",
               "For live charts, build a pivot table or formula table, then Insert > Chart on it.",
               "Test: change one source value and see which charts move."],
              ["Changing one Stage to Hired: the inserted chart stays the same.",
               "The chart on the Month pivot table updates.",
               "Dashboards in Topic 3 use only linked charts."],
              ["Snapshot: a one-off chart in a report or email.",
               "Live: dashboards and recurring reports."],
              ["Using an inserted chart on a dashboard that must refresh.",
               "Forgetting to undo test edits to the source data."],
              [("Purpose", "Snapshot or live - decided on purpose."),
               ("Test", "One value changed and checked."),
               ("Reset", "Test edits undone.")],
              [S_SHEETS, S_CHART],
              B("Gemini-inserted charts use a copy of the data; Insert > Chart on a live range updates.",
                "Dashboards must stay true when data changes - snapshots don't.",
                "Change one value: which of your charts moved?",
                ["Will the chart you inserted update if I change the Applications tab?",
                 "Create a pivot table that counts Candidate_ID by Month.",
                 "Then Insert > Chart on the pivot table."],
                ["Inserted chart unchanged.",
                 "Pivot chart updated."],
                single=True)),
        ],
    ),
    # ================================================================== TOPIC 3
    dict(
        num=3,
        code="03",
        title="Interactive Dashboard",
        subtitle=(
            "dropdown selectors and KPI formulas · linked charts, alerts and protection · Gems for repeatable screening "
            "· optimisation, reporting and responsible sharing"
        ),
        weighting="Labs 9-12",
        concepts=[
            ("Selectors drive everything", "Dropdowns feed COUNTIFS; 'All' becomes the wildcard *."),
            ("KPIs are formulas", "Never type a number Gemini told you - the dashboard must recalculate."),
            ("Charts on live ranges", "Insert > Chart on the dashboard tables, so charts follow the dropdowns."),
            ("Gems for repeat work", "Saved instructions + knowledge files = the same screening every time."),
            ("Optimise, then decide", "Gemini's solver finds the best combination; a person makes the call."),
            ("Share the minimum", "Only the fields a viewer needs, view-only, after the external-sharing warning."),
        ],
        sections=[
            S("What Makes a Dashboard Interactive", 9,
              "An interactive dashboard is one page of KPIs, tables and charts that viewers can re-cut themselves. In "
              "Google Sheets the interactivity comes from selector cells - dropdowns - whose values feed the formulas "
              "behind every KPI and table, so changing a dropdown recalculates the whole page.",
              "One dashboard answers many questions ('how are we doing for Software Engineers from LinkedIn?') without "
              "building a new report each time. Because everything is formula-driven, it stays correct when data is added.",
              ["Plan the questions, the KPIs and the selectors (e.g. Position, Source).",
               "Build a selector with a dropdown whose list includes 'All'.",
               "Make every KPI and table read the selectors."],
              ["C3 Position and C4 Source drive seven KPIs.",
               "Funnel, monthly and source tables use the same filters.",
               "Software Engineer: 104 applications, 6 hires."],
              ["The same questions are asked for different groups.",
               "Data is refreshed regularly."],
              ["A one-off answer - a pivot table or Gemini question is faster.",
               "Groups are so small that individuals could be identified."],
              [("Questions", "Each KPI answers a stated question."),
               ("Drivers", "Every number reads the selectors."),
               ("Tests", "At least three views checked.")],
              [S_DROPDOWN, S_COUNTIFS],
              B("One page whose KPIs, tables and charts all follow dropdown selectors.",
                "One dashboard answers many questions - and stays right as data grows.",
                "Which three views will you test to prove it works?",
                ["Create a dropdown in C3 with the values from Lists!A2:A10.",
                 "Create a dropdown in C4 with the values from Lists!B2:B9.",
                 "Set both to All."],
                ["C3 lists All + 8 positions.",
                 "C4 lists All + 7 sources."],
                try_head="ASK GEMINI, THEN APPLY", single=True)),
            S("KPI Formulas Driven by Dropdowns", 9,
              "Each KPI is a formula that filters by the selectors. COUNTIFS counts rows that meet every condition; "
              "AVERAGEIFS averages a column for matching rows. The pattern IF($C$3=\"All\",\"*\",$C$3) turns 'All' into "
              "the wildcard *, which matches any value. IFERROR shows 0 or '-' instead of #DIV/0! when nothing matches.",
              "Formula KPIs recalculate instantly and can be audited cell by cell. Gemini writes them from a description, "
              "but you must test edge cases - 'All', a single group, and a combination with no hires.",
              ["Describe the count, the filters and what 'All' means.",
               "Insert and lock references with $ before filling down.",
               "Test All/All, one group, and an empty combination."],
              ["B7 =COUNTIFS(...F...,IF($C$3=\"All\",\"*\",$C$3),...G...,IF($C$4=\"All\",\"*\",$C$4)) = 720.",
               "Hire rate =IFERROR(E7/B7,0) = 5.7%.",
               "Data Analyst + LinkedIn: 30 applications, 0 hires, '-' days."],
              ["Counts, rates and averages filtered by selectors.",
               "The same formula must work for every group."],
              ["A KPI needs logic you can't express or check in a formula.",
               "Typed numbers instead of formulas."],
              [("Wildcard", "'All' handled with *."),
               ("Errors", "IFERROR on every ratio."),
               ("Edges", "Empty combinations tested.")],
              [S_COUNTIFS, S_IF],
              B("COUNTIFS/AVERAGEIFS with IF($C$3=\"All\",\"*\",$C$3): every KPI follows the dropdowns.",
                "Formula KPIs recalculate instantly - test 'All', one group and an empty mix.",
                "What does your formula return when a combination has no rows?",
                ["Count rows where Position = C3 and Source = C4; All means any value.",
                 "Hires: the same count where Stage is Hired.",
                 "Hire rate: E7/B7, 0 if B7 is 0."],
                ["All/All: 720 and 41.",
                 "No #DIV/0! anywhere."],
                try_head="DESCRIBE THE KPI")),
            S("Dashboard Design: Charts, Alerts and Protection", 10,
              "A finished dashboard puts selectors at the top, KPIs in a row, and three or four charts below, each linked "
              "to a dashboard table so it follows the dropdowns. A metric switch (a dropdown plus an IF) lets one chart show "
              "different measures. Conditional formatting turns KPI cells into alerts. Hiding gridlines and helper tabs and "
              "protecting everything except the selectors makes it safe to share.",
              "A dashboard is used by people who didn't build it. Clear layout, alerts that draw the eye and protection "
              "against accidental edits make it trustworthy in other hands.",
              ["Build charts with Insert > Chart on the dashboard tables.",
               "Add a metric switch and KPI alerts with Gemini actions.",
               "Hide gridlines and helper tabs; protect all but the selectors; test three views."],
              ["Customer Success Executive: 103 applications, 7 hires - all charts redraw.",
               "Hire rate below 5% turns red; days to hire above 35 turns amber.",
               "Viewers can change C3:C5 but cannot edit formulas."],
              ["Others will use the dashboard regularly.",
               "A few KPIs need attention when they cross a threshold."],
              ["Gemini-inserted (static) charts on a live dashboard.",
               "Alerts on every cell - nothing stands out."],
              [("Layout", "Selectors > KPIs > charts."),
               ("Live", "Every chart follows the dropdowns."),
               ("Safe", "Formulas protected; helpers hidden.")],
              [S_CHART, S_CF, S_PROTECT],
              B("Selectors on top, KPIs in a row, linked charts below, alerts on the KPIs, everything else protected.",
                "Other people will use it - clarity, alerts and protection make it trustworthy.",
                "Change a dropdown: does every chart redraw?",
                ["How do I insert a chart from a range so that it updates?",
                 "Create a dropdown in C5 with Applications and Hires.",
                 "Highlight F7 in light red when it is below 5%."],
                ["Charts redraw for each Position.",
                 "Alerts fire for HR Executive."],
                try_title="Build It with Gemini", try_head="ASK GEMINI",
                flow=dict(title="From KPI Formulas to Dashboard",
                          steps=["Selectors and KPI formulas (Lab 9)", "Linked charts on dashboard tables",
                                 "Metric switch", "KPI alerts", "Protect, summarise, share"]))),
            S("Gems: Reusable Expert Assistants", 11,
              "A Gem is a custom version of Gemini with saved instructions and, optionally, knowledge files. You create "
              "it at gemini.google.com > Gems > New Gem, test it in the preview, save it, and then use it in the Gemini app "
              "or from the Gems list in the Sheets side panel. Premade Gems are also available; Gems are not supported in "
              "every language.",
              "Repeat tasks done by different people drift. A Gem applies the same instructions, rubric and output "
              "format every time, so screening is faster and more consistent - while the decision stays with a person.",
              ["Write instructions with Persona, Task, Context and Format.",
               "Add knowledge files from Drive (job descriptions, rubric).",
               "Test on a known example, save, then use it from the Sheets side panel."],
              ["'Orchid Bay Candidate Screener' scores finalists 0-4 on five criteria.",
               "Knowledge: OrchidBay_Job_Descriptions and OrchidBay_Screening_Rubric.",
               "Tested on one candidate: 12/20, Hold."],
              ["The same expert task is repeated by several people.",
               "The rules can be written down and checked."],
              ["Instructions or files contain confidential data you are not allowed to share with AI.",
               "The Gem's recommendation would be used as the decision."],
              [("Instructions", "Persona, Task, Context, Format."),
               ("Knowledge", "Current, approved files only."),
               ("Testing", "Known example checked before use.")],
              [S_GEMS, S_SHEETS],
              B("A custom Gemini with saved instructions and knowledge files - reused from the Sheets side panel.",
                "The same rubric and format every time: faster, more consistent screening.",
                "Did you test the Gem on a candidate whose answer you already know?",
                ["gemini.google.com > Gems > New Gem.",
                 "Paste Persona / Task / Context / Format instructions.",
                 "Add the job descriptions and rubric from Drive.",
                 "In Sheets: Ask Gemini > Gems > your Gem."],
                ["Test candidate scores 12/20, Hold.",
                 "Gaps match the data."],
                try_title="Build Your Gem", try_head="IN THE GEMINI APP")),
            S("Writing Gem Instructions That Are Fair", 11,
              "Google's prompt guidance recommends four parts: Persona (who Gemini should be), Task (what to do), Context "
              "(the facts, rules and limits) and Format (how to present the answer). For HR use, Context also carries the "
              "fairness rules: which evidence to use, which characteristics never to use or guess, what to do when "
              "information is missing, and that a person makes the decision.",
              "Instructions are the Gem's policy. Explicit evidence and fairness rules reduce bias and make the output "
              "explainable; a fixed format makes it easy to insert and check in Sheets.",
              ["State the evidence allowed and the scoring rules.",
               "List the characteristics never to use or infer.",
               "Fix the output table and ask for an 'unsure' list."],
              ["Evidence: skills, experience, interview score, salary, notice period.",
               "Never: age, gender, race, religion, nationality, marital status, health.",
               "Ask the Gem which information it used for each recommendation."],
              ["Any Gem that touches decisions about people.",
               "Output will be inserted into a sheet and checked."],
              ["Vague instructions such as 'pick the best candidate'.",
               "Using a Gem to process data your policy doesn't allow."],
              [("Evidence", "Allowed inputs listed."),
               ("Fairness", "Prohibited inputs listed."),
               ("Transparency", "Reasons and 'unsure' cases shown.")],
              [S_PROMPTS, S_GEMS],
              B("Persona, Task, Context, Format - with the evidence allowed and the characteristics never used.",
                "Instructions are the Gem's policy: explicit rules make it fairer and explainable.",
                "Could a candidate understand why the Gem recommended Hold?",
                ["PERSONA: careful, fair recruitment analyst.",
                 "CONTEXT: use only the row and the job description.",
                 "Never use age, gender, race, religion, nationality ...",
                 "FORMAT: one table, with a one-line reason."],
                ["Reasons cite evidence only.",
                 "Unsure cases listed."],
                try_title="Write the Instructions", try_head="GEM INSTRUCTIONS", single=True)),
            S("The Optimization Problem Solver", 12,
              "Gemini in Sheets can solve optimisation tasks - choosing the best combination under limits, such as "
              "allocating budgets, scheduling staff or selecting projects. You describe the objective (maximise or "
              "minimise something), the decisions (what can change) and the constraints (the limits that must hold).",
              "Hiring under a budget is a combination problem: the 'top two per role' may not fit. A solver finds the best "
              "feasible choice and shows the trade-off - and formulas prove the constraints hold.",
              ["State the objective, the decisions and every constraint.",
               "Compare with the obvious choice to see the trade-off.",
               "Record the choice with checkboxes and prove it with SUMIFS and COUNTIFS."],
              ["Maximise total Weighted_Score; 2 hires per role; salary within S$41,900.",
               "Top two per role costs S$43,100 - over budget.",
               "The optimum swaps one Software Engineer and loses 1 point."],
              ["Many combinations and hard limits.",
               "You can verify the result with formulas."],
              ["The objective leaves out what matters (e.g. team fit).",
               "You accept the answer without checking the constraints."],
              [("Model", "Objective, decisions, constraints written out."),
               ("Proof", "Constraints checked with formulas."),
               ("Judgement", "A person reviews what the score misses.")],
              [S_SHEETS],
              B("Describe an objective, decisions and constraints; Gemini finds the best feasible combination.",
                "The obvious picks may break the budget - the solver shows the best trade-off.",
                "Do your SUMIFS prove every constraint holds?",
                ["Maximise the total Weighted_Score.",
                 "Hire exactly the Openings per Position.",
                 "Keep total Expected_Salary within Constraints!B8."],
                ["Within budget = TRUE.",
                 "Two per role, 8 in total."],
                single=True)),
            S("Sharing and Responsible Use", 12,
              "Gemini can use your Drive files ('What are the main points of ...') and Gmail as context, and lists the "
              "Sources it used. When a file is shared outside your domain, the side panel warns that content added by "
              "Gemini may be visible to external users. Conversations in Sheets are not saved to Gemini Activity, and "
              "Clear history removes output you have not inserted. Gemini can be inaccurate and is not professional advice.",
              "HR data is personal data. Responsible use means minimising what goes into prompts and shared files, "
              "checking sources, keeping a human decision, and giving feedback when output is wrong or unsafe.",
              ["Use only approved, minimal data; check the Sources of any answer.",
               "Share a minimal view, view-only, and heed the external-sharing warning.",
               "Keep the decision with a person; give feedback; clear history."],
              ["Share_View holds only Candidate_ID, Position, Weighted_Score and Selected.",
               "The recommendation is exported to Docs and checked against the formulas.",
               "Fictional data in class; real data only where your policy allows."],
              ["Before sharing any sheet that holds personal data.",
               "Whenever Gemini uses Drive, Gmail or the web."],
              ["Pasting confidential or personal data into a tool your organisation hasn't approved.",
               "Letting AI output stand as the decision about a person."],
              [("Minimise", "Only the fields the viewer needs."),
               ("Source", "Files and web sources checked."),
               ("Accountable", "A person decides and signs off.")],
              [S_SHEETS, S_PROTECT],
              B("Use Drive and Gmail as context, check Sources, share minimal views, and keep a human decision.",
                "HR data is personal: minimise it, check it, and stay accountable.",
                "What is the least data this viewer needs to see?",
                ["What are the main points of OrchidBay_Screening_Rubric?",
                 "Which columns contain personal data the client doesn't need?",
                 "Create a Share_View tab with only four columns."],
                ["Sources expanded and checked.",
                 "Shared as Viewer only."],
                shots=[dict(kind="shot", title="Choosing Gemini's Sources", file="gemini-sources.png",
                            caption="Gemini lists the sources it used - and you can limit it to the tabs you choose.")])),
        ],
    ),
]

# ---------------------------------------------------------------- the Gemini side-panel tour
INTERFACE_TOUR = dict(
    title="The Gemini Side Panel — What Each Part Does",
    after="Prompting Gemini and the Side Panel",
    screenshot="gemini-side-panel.png",
    items=[
        ("Ask Gemini (spark)", "Top right of Sheets. Opens the panel with a summary of the sheet."),
        ("Suggestions and Gems", "Suggested prompts (More suggestions for others) and premade or custom Gems."),
        ("Prompt box and sources", "Type a prompt; the sources dropdown picks which tabs Gemini uses."),
        ("Response controls", "Insert, Copy, Retry, Preview, Analysis steps, Export to Docs, thumbs."),
        ("More options, Expand, Close", "Clear history; make the panel larger; close it."),
    ],
    models_title="Shortcuts and Key Controls",
    models=[
        ("Insert / Copy", "Keep a result: insert it into the sheet or copy it."),
        ("Retry", "A different version; Retry with Google Search adds the web."),
        ("Analysis steps / Show code", "See how Gemini calculated an answer."),
        ("Settings / Undo", "Adjust or reverse the last action."),
        ("Shortcuts", "Summarise: Cmd+Ctrl+N / Ctrl+Alt+N. Formula: = then Cmd+Ctrl+G / Ctrl+Alt+G."),
    ],
)

DAY_THEMES = {
    1: "Fundamentals of Google Sheet, data analytics and visualization, and an interactive hiring dashboard with Gemini on HR data",
}


def SCHEDULE(lab_titles):
    # Concepts are taught just before the lab that uses them: concepts for Lab n, then Lab n.
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:45", 15, "admin",
                 "Welcome, course introduction, learning outcomes, Gemini access check and the Orchid Bay scenario"),
                ("9:45", "9:55", 10, "topic",
                 "Topic 1 - Fundamentals of Google Sheet. Concepts for Lab 1: what Gemini in Google Sheets can do, "
                 "prompting and the side panel"),
                ("9:55", "10:20", 25, "lab", "Hands-on: " + lab_titles([1])),
                ("10:20", "10:25", 5, "topic", "Topic 1 - Concepts for Lab 2: why data quality matters"),
                ("10:25", "10:50", 25, "lab", "Hands-on: " + lab_titles([2])),
                ("10:50", "11:05", 15, "break", "Tea break"),
                ("11:05", "11:10", 5, "topic",
                 "Topic 1 - Concepts for Lab 3: Gemini actions (preview, apply, undo) and data prep"),
                ("11:10", "11:40", 30, "lab", "Hands-on: " + lab_titles([3])),
                ("11:40", "11:45", 5, "topic",
                 "Topic 1 - Concepts for Lab 4: VLOOKUP, COUNTIF and nested IF; generating, explaining and fixing formulas"),
                ("11:45", "12:15", 30, "lab", "Hands-on: " + lab_titles([4])),
                ("12:15", "12:25", 10, "topic",
                 "Topic 2 - Data Analytics and Visualization. Concepts for Lab 5: tables, trackers and dropdowns; "
                 "conditional formatting"),
                ("12:25", "12:55", 30, "lab", "Hands-on: " + lab_titles([5])),
                ("12:55", "13:55", 60, "lunch", "Lunch break"),
                ("13:55", "14:00", 5, "topic",
                 "Topic 2 - Concepts for Lab 6: the AI function (=AI), Fill with Gemini and AI columns"),
                ("14:00", "14:30", 30, "lab", "Hands-on: " + lab_titles([6])),
                ("14:30", "14:35", 5, "topic",
                 "Topic 2 - Concepts for Lab 7: data analysis and insights with Gemini; pivot tables"),
                ("14:35", "15:05", 30, "lab", "Hands-on: " + lab_titles([7])),
                ("15:05", "15:10", 5, "topic",
                 "Topic 2 - Concepts for Lab 8: charts and graphs with Gemini; inserted vs linked charts"),
                ("15:10", "15:40", 30, "lab", "Hands-on: " + lab_titles([8])),
                ("15:40", "15:55", 15, "break", "Tea break"),
                ("15:55", "16:05", 10, "topic",
                 "Topic 3 - Interactive Dashboard. Concepts for Lab 9: what makes a dashboard interactive; KPI formulas "
                 "driven by dropdowns"),
                ("16:05", "16:35", 30, "lab", "Hands-on: " + lab_titles([9])),
                ("16:35", "16:40", 5, "topic",
                 "Topic 3 - Concepts for Lab 10: dashboard design - linked charts, alerts and protection"),
                ("16:40", "17:10", 30, "lab", "Hands-on: " + lab_titles([10])),
                ("17:10", "17:15", 5, "topic",
                 "Topic 3 - Concepts for Lab 11: Gems and writing fair Gem instructions"),
                ("17:15", "17:45", 30, "lab", "Hands-on: " + lab_titles([11])),
                ("17:45", "17:50", 5, "topic",
                 "Topic 3 - Concepts for Lab 12: the optimisation problem solver; sharing and responsible use"),
                ("17:50", "18:20", 30, "lab", "Hands-on: " + lab_titles([12])),
                ("18:20", "18:30", 10, "recap", "Topic recaps mapped to LO1-LO3, your next steps and questions"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="Gemini in Google Sheets for HR and Recruitment",
    move_to_first_topic=["statement", "deep_dives"],
    after_schedule=["pillars"],
    concepts_title="The Orchid Bay Scenario",
    concepts=[
        ("Orchid Bay Talent Partners", "A fictional Singapore recruitment and HR services firm."),
        ("The Q3 2026 hiring drive", "8 client roles, 12 openings, 240 applications - plus 2026 year-to-date data."),
        ("One storyline", "Raw export > clean data > screening formulas > tracker > insights > dashboard > Gem > decision."),
        ("Your role", "Talent analyst using Gemini to screen candidates and report - and checking every number."),
    ],
    statement=dict(
        headline="Gemini drafts. Formulas prove. People decide.",
        body="Describe the task precisely, check every result against the data, and keep decisions about candidates with accountable people.",
        kicker="C817 OPERATING PRINCIPLE",
    ),
    pillars_title="Twelve Labs in Three Topics",
    pillars=[
        ("Fundamentals of Google Sheet", ["Lab 1: Gemini Side Panel & Summaries", "Lab 2: Data Quality Check",
                                          "Lab 3: Data Prep", "Lab 4: Formulas: VLOOKUP, COUNTIF & Nested IF"]),
        ("Data Analytics & Visualization", ["Lab 5: Tables, Trackers & Conditional Formatting",
                                            "Lab 6: AI Function & Fill with Gemini", "Lab 7: Data Analysis & Insights",
                                            "Lab 8: Charts & Visualisation"]),
        ("Interactive Dashboard", ["Lab 9: Dashboard KPIs & Selectors", "Lab 10: Interactive Dashboard", "Lab 11: Gems",
                                   "Lab 12: Optimisation, Reporting & Safe Sharing"]),
    ],
    deep_dives=[
        dict(
            title="What Gemini in Google Sheets Does - and Where You Practise It",
            kicker="FROM GOOGLE'S OFFICIAL GUIDE",
            items=[
                ("Summarise and ask", "Summaries and questions about your data - Labs 1, 2."),
                ("Perform actions", "Formatting, find and replace, sort, filter, freeze, insert, delete - Labs 2, 3, 5."),
                ("Create formulas", "Generate, explain and fix - Labs 4, 9."),
                ("Create tables", "From scratch or from notes - Lab 5."),
                ("AI function", "=AI and Fill with Gemini in cells - Lab 6."),
                ("Analysis and insights", "Trends, pivot tables, Export to Docs - Lab 7."),
                ("Charts and graphs", "Preview, Insert, Copy - Lab 8."),
                ("Gems", "Custom assistants in the side panel - Lab 11."),
                ("Optimisation solver", "Best combination under constraints - Lab 12."),
                ("Drive, Gmail and the web", "Files, emails and search as context - Labs 7, 12."),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Gemini for Google Sheet (C817). It follows the same three topics - Fundamentals of "
    "Google Sheet, Data Analytics and Visualization, and Interactive Dashboard - and the same twelve connected labs as "
    "the slide deck, Lesson Plan and lab folders. Every lab uses fictional data from Orchid Bay Talent Partners, a "
    "made-up Singapore recruitment and HR firm running its Q3 2026 hiring drive."
)

LG_INTRO2 = (
    "The course follows Google's official guide, Collaborate with Gemini in Google Sheets, and the AI function guide, "
    "as current in October 2026. Each concept explains what the feature is, why it matters, how it works, a worked "
    "example and when to use or avoid it. Each lab folder contains an instruction PDF with sample prompts, "
    "sample-prompts.txt and the mock-data workbook; every prompt is also on the Lab Prompts web page with a Copy button. "
    "Gemini's output remains a proposal until you have checked it in the lab's Test It step."
)

LG_SETUP = dict(
    needs=[
        "A laptop with a current Chrome, Edge, Firefox or Safari browser.",
        "A Google account with Gemini in Google Sheets: a Google Workspace plan with Gemini, or a Google AI Pro or "
        "Ultra plan. The Ask Gemini (spark) button must appear at the top right of Google Sheets.",
        "The AI function (=AI) and Gems available on that account (Labs 6 and 11). Gemini features need a supported "
        "language - English is used throughout the course.",
        "Google Drive space for the twelve lab workbooks and two Google Docs.",
        "The course labs folder: one sub-folder per lab with its instruction PDF, sample-prompts.txt and data/ workbook "
        "(and, for Lab 11, gem-instructions.txt and two knowledge documents).",
    ],
    verify_text=(
        "Upload labs/lab-01-*/data/OrchidBay_Q3_Applications_Export.xlsx to Google Drive, open it and choose File > Save "
        "as Google Sheets. In the new file click Ask Gemini at the top right and confirm that the side panel shows a "
        "summary of the spreadsheet. Type =AI( in an empty cell to check the AI function is recognised, and open "
        "gemini.google.com to check you can see Gems. Labels can change as Google updates the product."
    ),
    verify_code=(
        "labs/\n"
        "  lab-01-<theme>/\n"
        "    Lab-01-Instructions.pdf     instructions + sample prompts\n"
        "    sample-prompts.txt          copy-ready prompts\n"
        "    data/OrchidBay_<dataset>.xlsx\n"
        "  lab-11-gems/\n"
        "    gem-instructions.txt        Gem instructions to paste\n"
        "    data/gem-knowledge/*.docx   job descriptions + screening rubric\n"
        "Google Drive/                   your Google Sheets copies"
    ),
    conventions=[
        "All Orchid Bay companies, people, IDs and values are fictional training data; emails use example.com.",
        "Prompts are shown in shaded boxes; copy them from the prompts web page or sample-prompts.txt and adapt them.",
        "Labels tell you where to send each prompt: ASK GEMINI (answer in the panel), INSERT (then Insert), ACTION "
        "(then Apply), FORMULA (then Insert into a cell), AI FUNCTION (type in a cell), GEM and GEMINI APP.",
        "S$ is used for currency, dates are yyyy-mm-dd and the reporting date is 2026-09-30.",
        "Record each prompt, what Gemini did, how you verified it and your decision on the Prompt_Log tab.",
        "Gemini's output can vary between runs; the Test It values come from the data, so check against them.",
    ],
)

LAB_NOTE = (
    "Use only the supplied fictional Orchid Bay data or information you are authorised to process. Do not paste "
    "credentials, confidential business material or real candidates' or employees' personal data into Gemini, the AI "
    "function or a Gem unless your organisation has approved it."
)

LG_WRAPUP = dict(
    title="Wrap-Up - The Complete C817 Workflow",
    intro=(
        "Across twelve labs you took one hiring drive from a raw export to a decision: cleaned, screened, tracked, "
        "analysed, visualised, put on an interactive dashboard, screened with a Gem and optimised within budget - with a "
        "formula check between every Gemini output and every people decision."
    ),
    sections=[
        dict(title="Fundamentals of Google Sheet", bullets=[
            "Open Gemini on a native Sheets file; name tabs and columns; insert what you want to keep.",
            "Profile and flag data-quality problems, then prepare the data with actions you preview and undo.",
            "Describe formulas in plain English; read the explanation; fix errors with Fix.",
        ]),
        dict(title="Data Analytics and Visualization", bullets=[
            "Turn notes into trackers with dropdowns, checkboxes and conditional formatting.",
            "Use =AI and Fill with Gemini for text - and measure the accuracy.",
            "Ask for insights and pivot tables, read Analysis steps, and chart with titles that state the finding.",
        ]),
        dict(title="Interactive Dashboard", bullets=[
            "Drive every KPI and table from dropdowns with COUNTIFS and AVERAGEIFS.",
            "Use linked charts, alerts and protection; summarise and export to Docs.",
            "Automate repeat screening with a fair Gem; optimise within constraints; share the minimum.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Re-run all twelve labs from the original workbooks without looking at your finished files.",
    "Pick one weekly spreadsheet task at work and write the Gemini prompt for it - then check the result with a formula.",
    "Build one interactive dashboard for a report you produce every month.",
    "Create one Gem for a repeat task, with fair, evidence-only instructions.",
    "Check Google's Collaborate with Gemini in Google Sheets page regularly - features and labels change often.",
]

LG_GLOSSARY = [
    ("Action", "A change Gemini makes to the sheet from a prompt, shown on an Action preview card and applied with Apply."),
    ("Action preview card", "The card that describes a proposed Gemini action before you apply it."),
    ("AI function", "=AI(\"prompt\", [range]) - a Sheets function that sends a prompt to Gemini and returns text into a cell."),
    ("Analysis steps", "A control under a Gemini answer that shows how it analysed the data."),
    ("AVERAGEIFS", "Averages a range for rows that meet one or more conditions."),
    ("Conditional formatting", "Formatting that applies when a rule is true, e.g. highlight rows where score >= 85."),
    ("COUNTIF / COUNTIFS", "Count cells that meet one condition / rows that meet several conditions."),
    ("Dropdown", "An in-cell list of allowed values."),
    ("Export to Docs", "Sends a Gemini response to a new Google Doc."),
    ("Fill with Gemini", "Completes a column from examples or a prompt, using the context of the table."),
    ("Fix", "Gemini's button on a formula error that explains and corrects the formula."),
    ("Gem", "A custom Gemini with saved instructions and knowledge files, reusable in the Gemini app and side panel."),
    ("Hire rate", "Hires divided by applications for the same group."),
    ("Insert", "Puts a Gemini table, text, formula or chart into the sheet."),
    ("KPI", "Key performance indicator: one headline measure calculated by formula."),
    ("Linked chart", "A chart built with Insert > Chart on a live range, so it updates when the range changes."),
    ("Optimization problem solver", "Gemini's solver for choosing the best combination under constraints."),
    ("Pivot table", "A summary that groups rows and aggregates values by fields in rows, columns and filters."),
    ("Prompt", "The instruction you give Gemini; best with task, tab and column names, output format and rules."),
    ("Sources", "The tabs, files or web pages Gemini used; choose tabs in the prompt box and expand Sources under answers."),
    ("VLOOKUP", "Finds a key in the first column of a range and returns a value from another column."),
    ("Wildcard *", "In COUNTIFS criteria, matches any text - used so 'All' counts every value."),
]

NEXT_STEPS = dict(
    title="Keep the Verified Workflow",
    items=[
        "Use Gemini on one real spreadsheet task this week - and check it with a formula.",
        "Turn one monthly report into an interactive dashboard driven by dropdowns.",
        "Create one Gem for a task you repeat, with fair, evidence-only instructions.",
        "Keep people decisions with accountable people: Gemini drafts, formulas prove, people decide.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now use Gemini in Google Sheets to clean, analyse and visualise data, build interactive dashboards and "
        "reusable Gems - while keeping evidence, privacy and human judgement in control."
    ),
    kicker="GEMINI FOR GOOGLE SHEET · C817",
)

VERSION_HISTORY = [
    ("1.0", "27 July 2026", "Initial release - C817 AI Application for Google Sheet courseware.", TRAINER),
    ("1.1", "4 October 2026", "Course retitled to Gemini for Google Sheet.", TRAINER),
    ("2.0", VERSION_DATE,
     "Revamped to follow Google's official 'Collaborate with Gemini in Google Sheets' guide and the AI function guide: "
     "three topics (Fundamentals of Google Sheet; Data Analytics and Visualization; Interactive Dashboard); twelve "
     "connected labs on a fictional HR firm's hiring drive, each in its own folder with mock data and an instruction PDF; "
     "copy-ready Lab Prompts web page; official screenshots; new content on actions, Fix, the AI function, Fill with "
     "Gemini, pivot tables, linked charts, interactive dashboards, Gems and the optimisation solver.", TRAINER),
]
