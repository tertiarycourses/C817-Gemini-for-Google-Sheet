"""Topic 1 labs for C817: Fundamentals of Google Sheet with Gemini (Orchid Bay Talent Partners hiring data)."""

from mock_data import EXPECTED

E1, E2, E3, E4 = EXPECTED[1], EXPECTED[2], EXPECTED[3], EXPECTED[4]


def _money(v):
    return f"S${v:,.0f}"


SETUP_STEP = (
    "Download {file} from this lab's data folder. In Google Drive choose New > File upload, open the uploaded file, "
    "then choose File > Save as Google Sheets - Gemini works best on a native Google Sheets file. Close the .xlsx tab "
    "and work only in the new Google Sheets copy. At the top right, click Ask Gemini (the spark icon) to open the "
    "Gemini side panel. Read the About_This_Data tab before you prompt."
)

LOG = (
    "LOG:\n"
    "List the prompts I sent you in this conversation. For each one, give a one-line summary of what\n"
    "you did, so I can copy it into the Prompt_Log tab."
)
LOG_STEP = (
    "Prompt_Log already lists every prompt in this lab with its step. Ask Gemini to recap the conversation, copy each "
    "line into What Gemini did, add How I verified in your own words, and choose Keep, Revise or Undo in the Decision "
    "dropdown. Google Sheets saves automatically. Tip: the side-panel history is lost when you reload the page, so "
    "insert or copy anything you want to keep."
)
LOG_EXPLAIN = ("Gemini recaps the conversation so you can fill in Prompt_Log: what each prompt did and how you checked "
               "it. This is your record of the lab.")

DOMAIN1 = [
    # ------------------------------------------------------------------ LAB 1
    dict(
        num=1,
        topic=1,
        title="Open Gemini and Explore the Q3 Candidate Export",
        theme="Gemini Side Panel & Summaries",
        duration=25,
        objective=(
            "LO1: open and use the Gemini side panel in Google Sheets to summarise a spreadsheet, ask questions about "
            "HR data across tabs and insert results, checking each answer against the data"
        ),
        goal=(
            "Get to know Gemini in Google Sheets on a real recruitment export: summarise it, question it across two tabs, "
            "insert a result and spot what looks wrong."
        ),
        workflow=["Open Gemini", "Summarise", "Ask across tabs", "Insert", "Spot issues"],
        desc=(
            "You are a talent analyst at Orchid Bay Talent Partners, a fictional Singapore recruitment and HR firm. The "
            "Q3 2026 hiring drive has just closed its first round: 243 rows exported from the applicant tracking system "
            "for eight client roles. You will open the Gemini side panel, read its automatic summary, ask questions in "
            "plain English, focus Gemini on the tabs you choose, insert a table into the sheet, and try the panel's "
            "controls - Retry, Undo, feedback and Clear history."
        ),
        build=(
            "OrchidBay_Q3_Applications_Export as a Google Sheets file with an inserted Applications_by_Position table, a "
            "check formula that confirms Gemini's stage count, and a filled Prompt_Log"
        ),
        services="Google Sheets · Gemini side panel (summary, prompts, sources, Insert) · OrchidBay_Q3_Applications_Export.xlsx",
        data_files=["data/OrchidBay_Q3_Applications_Export.xlsx"],
        prerequisites=[
            "A Google account with Gemini in Google Sheets: a Google Workspace plan with Gemini, or a Google AI Pro / "
            "Ultra plan. The Ask Gemini (spark) button must be visible at the top right of Sheets.",
            "Google Chrome or another current browser, signed in to that account.",
            "This lab folder downloaded, including data/OrchidBay_Q3_Applications_Export.xlsx.",
            "Data handling: all Orchid Bay data is fictional. With real candidate data, use only tools your organisation "
            "has approved, and only the columns the task needs.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Q3_Applications_Export.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Q3_Applications_Export (Google Sheets copy, not .xlsx)\n"
                "Tabs      : About_This_Data | Applications | Jobs | Prompt_Log\n"
                "Gemini    : side panel open on the right",
            ),
            (
                "When the side panel opens on a sheet that has data, Gemini shows a short summary of the spreadsheet and "
                "some suggested prompts. Click View more to read all of it. You can summarise at any time with the shortcut "
                "Cmd + Ctrl + N (Mac) or Ctrl + Alt + N (Windows). Now ask in your own words. Gemini should say that one row "
                f"is one candidate application, received between {E1['first']} and {E1['last']}.",
                "ASK GEMINI:\n"
                "Summarize this spreadsheet. What does one row on the Applications tab represent,\n"
                "and what time period does it cover?",
            ),
            (
                "Ask Gemini to describe the columns, and compare its answer with the data dictionary on About_This_Data. "
                f"It should report {E1['rows']} rows of data and {E1['cols']} columns. If a number is different, ask Gemini how "
                "it counted (for example, whether it included the header row).",
                "ASK GEMINI:\n"
                "Describe each column on the Applications tab in one line, and tell me how many rows of data there are.",
            ),
            (
                "Gemini can read every tab. To focus it, open the sources dropdown in the prompt box and tick only "
                "Applications and Jobs, then ask a question that needs both tabs. Before you insert the table, refine it "
                f"with a follow-up. Data Analyst should show {E1['pos']['Data Analyst']} applications for "
                f"{E1['openings']['Data Analyst']} openings. Click Insert, then rename the new tab Applications_by_Position. "
                "Insert keeps the result: the side-panel history is lost when you reload the page or go offline.",
                "INSERT:\n"
                "Using the Applications and Jobs tabs, make a table of each Position with the number of\n"
                "applications and the number of Openings.\n\n"
                "FOLLOW-UP:\n"
                "Add a column Applications_per_Opening and sort the table from highest to lowest.",
            ),
            (
                "Ask about the pipeline. Gemini should name Rejected as the largest stage "
                f"({E1['stage']['Rejected']} rows) and report {E1['stage']['Hired']} Hired. Then type the check formula "
                "into an empty cell on the Applications_by_Position tab - it must match Gemini's Rejected count. If it does "
                "not, the formula wins: ask Gemini how it counted.",
                "ASK GEMINI:\n"
                "How many candidates are at each Stage? Which stage has the most candidates?\n\n"
                "CHECK:\n"
                "Rejected count   =COUNTIF(Applications!O2:O244,\"Rejected\")\n"
                "Hired count      =COUNTIF(Applications!O2:O244,\"Hired\")",
            ),
            (
                "Explore the panel's controls. Send the first prompt, then click Retry for a different version. Use the "
                "thumbs up or down to give feedback. Open More options (three dots) to see More suggestions and Clear "
                "history, and Expand to make the panel larger. Then use Gemini for help with Sheets itself - you will use "
                "the answer about duplicates in Lab 3.",
                "ASK GEMINI:\n"
                "Explain this spreadsheet like I'm 5 years old.\n\n"
                "ASK GEMINI:\n"
                "How can I remove duplicates in Google Sheets?",
            ),
            (
                "Finish by asking Gemini what looks wrong - do not fix anything yet. A good answer mentions several of: "
                "repeated Candidate_IDs, Source spelt more than one way (e.g. 'Linked In'), blank emails, salaries "
                "typed as text such as 'S$4,800', and a negative Years_Experience. Lab 2 checks each one.",
                "ASK GEMINI:\n"
                "Is there anything in the Applications tab that looks wrong or inconsistent? List the issues with\n"
                "an example of each. Don't change anything.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini reads the whole spreadsheet and tells you what a row is and the date range - a quick first look "
            "before you analyse anything. Nothing in the sheet changes.",
            "Gemini describes every column and counts the rows, so you can compare its understanding with the data "
            "dictionary on About_This_Data.",
            "Combines two tabs - applications from Applications, openings from Jobs - into one table that Gemini "
            "drafts in the panel. It is not in your sheet until you click Insert.",
            "Refines the draft before you insert it: adds a ratio column and sorts it. Follow-ups change the draft, "
            "not your data.",
            "Counts candidates by Stage. The COUNTIF check formulas confirm Gemini's numbers independently.",
            "Asks Gemini to explain the sheet in very simple language - a good test of whether it understood the data. "
            "Try Retry to see a different version.",
            "Uses Gemini as a Google Sheets help desk: it explains Data > Data cleanup > Remove duplicates, which you "
            "use in Lab 3.",
            "Asks Gemini to look for problems without changing anything. Its list becomes your to-do list for Lab 2.",
            LOG_EXPLAIN,
        ],
        formulas={
            "E": ("The check formulas you type", [
                ('=COUNTIF(Applications!O2:O244,"Rejected")',
                 "COUNTIF(range, criterion) counts the cells in Stage (column O, rows 2-244) that equal \"Rejected\". "
                 "Applications! means the range is on the Applications tab."),
            ]),
        },
        sample_prompts=[
            ("Summary", "Give me a five-bullet summary of this candidate data for the Head of Talent."),
            ("Question", "Which Source brought in the most applications?"),
            ("Question", "Which recruiter owns the most applications, and for which positions?"),
            ("Help", "How do I freeze the header row in Google Sheets?"),
            ("Insight", "What's interesting about this data? Give three observations with the numbers behind them."),
        ],
        sample_explain=[
            "Gemini condenses the export into five points for a manager - check each number against the sheet.",
            "Counts applications per Source. Spelling variants such as 'Linked In' may split a source - you fix that in Lab 3.",
            "Counts applications per Recruiter and links each recruiter to their roles via Position.",
            "Gemini answers how-to questions about Google Sheets itself, step by step.",
            "Gemini looks for patterns and backs each one with a number you can check with COUNTIF.",
        ],
        checks=[
            ("Rows and columns", f"{E1['rows']} rows of data, {E1['cols']} columns; dates {E1['first']} to {E1['last']}."),
            ("Applications_by_Position tab", f"8 positions; Data Analyst {E1['pos']['Data Analyst']} applications for "
                                             f"{E1['openings']['Data Analyst']} openings; sorted by Applications_per_Opening."),
            ("Stage check", f"Rejected = {E1['stage']['Rejected']} and Hired = {E1['stage']['Hired']}, matching Gemini's answer."),
            ("Issues spotted", "Gemini lists repeated IDs, Source spelling variants, blank or invalid emails, text salaries "
                               "and a negative Years_Experience."),
            ("Prompt_Log", "Every prompt you ran has What Gemini did, How I verified and a Decision."),
        ],
        test="",
        checkpoint=(
            "Keep this file in Drive. Lab 2 opens its own copy of the same export, so you can start Lab 2 even if this "
            "lab is not finished."
        ),
        troubleshooting=[
            ("There is no Ask Gemini (spark) button.",
             "Gemini needs an eligible Google Workspace or Google AI plan. Check you are signed in to the right account "
             "(profile picture, top right) and that your admin has turned Gemini on. Pair with a neighbour meanwhile."),
            ("Gemini says it can't help with this file.",
             "You are probably in the .xlsx file. Choose File > Save as Google Sheets and work in the new copy."),
            ("Gemini's row count is off by one.",
             "It may have counted the header row. Ask: 'Count only data rows, excluding the header.'"),
            ("The side-panel conversation disappeared.",
             "History is lost when you reload, close the file or go offline. Insert results you want to keep."),
            ("Gemini answers about the wrong tab.",
             "Use the sources dropdown in the prompt box to select only the tabs you mean, and name the tab in the prompt."),
        ],
        challenge=(
            "Ask Gemini which recruiter has the highest share of Rejected applications. Confirm it with two COUNTIFS "
            "formulas for that recruiter."
        ),
        reflection="Which of Gemini's answers would you have trusted without the COUNTIF check, and why is that risky?",
    ),
    # ------------------------------------------------------------------ LAB 2
    dict(
        num=2,
        topic=1,
        title="Check the Quality of the Candidate Data with Gemini",
        theme="Data Quality Check",
        duration=25,
        objective=(
            "LO1: use Gemini to profile HR data for duplicates, inconsistent categories, missing or invalid values and "
            "wrong data types, highlight the problems and confirm each count with a formula"
        ),
        goal=(
            "Find, highlight and count every data-quality problem in the Q3 export before anyone analyses it - and "
            "prove each count with a formula."
        ),
        workflow=["Profile", "Find duplicates", "Highlight issues", "Count with formulas", "Report"],
        desc=(
            "Before the recruitment manager sees any numbers, you check the raw Q3 export. You will ask Gemini to "
            "profile the data, find the repeated Candidate_IDs and the Source spelling variants, and apply conditional "
            "formatting actions that highlight duplicates, bad emails, text salaries and impossible values. A Checks tab "
            "of formulas confirms every count, and Gemini drafts a short data-quality report. You do not fix anything "
            "yet - that is Lab 3."
        ),
        build=(
            "OrchidBay_Q3_Applications_QualityCheck with duplicates and problem cells highlighted, a Checks tab of "
            "formulas confirming each issue count, an inserted data-quality report and a filled Prompt_Log"
        ),
        services="Google Sheets · Gemini side panel (questions, conditional-formatting actions, formulas) · OrchidBay_Q3_Applications_QualityCheck.xlsx",
        data_files=["data/OrchidBay_Q3_Applications_QualityCheck.xlsx"],
        prerequisites=[
            "Lab 1 completed, or at least the Gemini side panel opened once.",
            "This lab folder downloaded, including data/OrchidBay_Q3_Applications_QualityCheck.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Q3_Applications_QualityCheck.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Q3_Applications_QualityCheck (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Applications | Jobs | Checks | Prompt_Log\n"
                "Rule      : find and flag only - do not fix anything in this lab",
            ),
            (
                "Ask Gemini to profile the data for the common problems. Read its list carefully: it is a starting point, "
                "not the final answer - the formulas in Step 6 decide.",
                "ASK GEMINI:\n"
                "Check the Applications tab for data-quality problems: duplicate Candidate_IDs, the same Source spelt\n"
                "different ways, missing or invalid emails, Expected_Salary values stored as text, and impossible values.\n"
                "Don't change anything. List each problem with how many rows it affects.",
            ),
            (
                "Ask about duplicates, then apply Gemini's conditional-formatting action. An Action preview card appears - "
                "read it and click Apply. When it finishes, Settings and Undo appear: Settings opens the rule, Undo "
                f"reverses it. There are {E2['rows']} rows but only {E2['unique']} unique IDs: "
                f"{', '.join(E2['dup_ids'])} each appear twice, so 6 cells turn orange (press Ctrl + Down arrow to reach "
                "the copies near the end).",
                "ASK GEMINI:\n"
                "Which Candidate_IDs appear more than once? Are those rows exact copies of each other?\n\n"
                "ACTION:\n"
                "Highlight duplicate values in the Candidate_ID column in orange.",
            ),
            (
                "Ask Gemini to list Source exactly as spelt. Besides the seven real sources you should see "
                f"'Linked In' ({E2['linked_in']}), 'linkedin' ({E2['linkedin_lower']}) and 'JobStreet ' with a trailing "
                f"space ({E2['jobstreet_space']}). Spelling variants split one source into several and corrupt every count "
                "by Source.",
                "ASK GEMINI:\n"
                "List every distinct value in the Source column exactly as it is spelt, including spaces and\n"
                "capital letters, with a count of each.",
            ),
            (
                "Send these one change at a time. After each Action preview card, click Apply, look at the sheet, and use "
                f"Undo if it is not what you wanted. Expect {E2['missing_email'] + E2['bad_email']} email cells "
                f"({E2['missing_email']} blank, {E2['bad_email']} without @), {E2['text_salary']} text salaries and "
                f"{E2['neg_years']} negative Years_Experience ({E2['neg_id']}).",
                "ACTION:\n"
                "1) Highlight cells in the Email column that are blank or do not contain @ in light red.\n"
                "2) Highlight Expected_Salary cells that contain text instead of a number in yellow.\n"
                "3) Highlight Years_Experience values below 0 in red.",
            ),
            (
                "Now prove each count. The Checks tab already has the labels in column A and the expected values in "
                "column C. First ask Gemini for the unique-ID formula and insert it into Checks!B3. Then paste the other "
                "check formulas into column B beside their labels. Every B must match its C; if Gemini's Step 2 numbers "
                "disagree, the formulas win.",
                "FORMULA:\n"
                "Create a formula that counts the unique Candidate_IDs in Applications column A, rows 2 to 244.\n\n"
                "CHECK:\n"
                "Total rows            =COUNTA(Applications!A2:A244)\n"
                "Unique IDs            =COUNTUNIQUE(Applications!A2:A244)\n"
                "Blank emails          =COUNTBLANK(Applications!C2:C244)\n"
                "Emails without @      =COUNTIFS(Applications!C2:C244,\"<>\",Applications!C2:C244,\"<>*@*\")\n"
                "Text salaries         =SUMPRODUCT(--ISTEXT(Applications!K2:K244))\n"
                "Negative experience   =COUNTIF(Applications!H2:H244,\"<0\")",
            ),
            (
                "Ask Gemini for a short report for the recruitment manager, then click Insert - Gemini adds the table to "
                "your spreadsheet (usually on a new tab); rename that tab DQ_Report. Or use Copy and paste it into an "
                "email draft.",
                "INSERT:\n"
                "Write a short data-quality report for the recruitment manager: each issue, how many rows it affects,\n"
                "why it matters for screening, and the fix you recommend. Use a table.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini profiles the whole tab for the five classic data-quality problems and lists them with row counts. "
            "Nothing changes in the sheet.",
            "Finds the repeated Candidate_IDs and checks whether the rows are full copies - which tells you they are "
            "export duplicates, not two different applications.",
            "A Gemini action: it proposes a conditional-formatting rule (Action preview card) and applies it when you "
            "click Apply. Settings shows the rule; Undo removes it.",
            "Lists Source values exactly as typed, so hidden variants such as a trailing space become visible.",
            "Highlights blank emails and emails without @ - candidates you cannot contact.",
            "Highlights salaries typed as text (e.g. 'S$4,800'); text is ignored by SUM and AVERAGE.",
            "Highlights an impossible negative experience value.",
            "Gemini writes a COUNTUNIQUE formula and inserts it into the cell you selected.",
            "Gemini turns the findings into a manager-friendly table: issue, rows, impact and recommended fix.",
            LOG_EXPLAIN,
        ],
        formulas={
            "H": ("The formula Gemini should write", [
                ("=COUNTUNIQUE(Applications!A2:A244)",
                 "COUNTUNIQUE counts each different value once. 243 rows but 240 unique IDs means 3 IDs are repeated."),
            ]),
        },
        sample_prompts=[
            ("Profile", "Which columns have blank cells, and how many blanks does each have?"),
            ("Validate", "Are there any Applied_Date values outside July to September 2026?"),
            ("Validate", "Do any rows have a Position that doesn't match the Position for their Job_ID on the Jobs tab?"),
            ("Highlight", "Highlight Full_Name cells that are all in capital letters in light purple."),
            ("Explain", "Why is a salary stored as text a problem when I calculate an average?"),
        ],
        sample_explain=[
            "Gemini counts blanks per column - a fast completeness profile.",
            "A range check on dates: anything outside the hiring drive is suspicious.",
            "A cross-tab consistency check between Applications and the Jobs reference table.",
            f"Shows the {E2['caps_names']} names typed in capitals, which Lab 3 tidies with PROPER.",
            "Gemini explains the impact of a data-type problem in plain English.",
        ],
        checks=[
            ("Duplicates", f"{E2['rows']} rows, {E2['unique']} unique IDs; {', '.join(E2['dup_ids'])} each appear twice; "
                           "6 orange cells."),
            ("Source variants", f"'Linked In' {E2['linked_in']}, 'linkedin' {E2['linkedin_lower']}, 'JobStreet ' "
                                f"(trailing space) {E2['jobstreet_space']}."),
            ("Emails", f"{E2['missing_email']} blank + {E2['bad_email']} without @ ({', '.join(E2['bad_email_ids'])}) = "
                       f"{E2['missing_email'] + E2['bad_email']} light-red cells."),
            ("Salaries and experience", f"{E2['text_salary']} text salaries in yellow; {E2['neg_years']} negative "
                                        f"Years_Experience ({E2['neg_id']}) in red."),
            ("Checks tab", "Six formulas in column B match the expected values already in column C "
                           f"({E2['rows']}, {E2['unique']}, {E2['missing_email']}, {E2['bad_email']}, {E2['text_salary']}, "
                           f"{E2['neg_years']})."),
        ],
        test="",
        checkpoint="Lab 3 opens a fresh copy of the same raw export and fixes every issue you found here.",
        troubleshooting=[
            ("There is no Apply button - Gemini only explains how.",
             "Rephrase as a direct instruction ('Highlight ... in orange'), and make sure the Applications tab is "
             "selected. If actions are not available on your plan, use Format > Conditional formatting with Gemini's "
             "steps."),
            ("Gemini highlights the whole row instead of the cell.",
             "Click Undo and say 'only the cells in the Candidate_ID column'."),
            ("COUNTUNIQUE returns 243.",
             "Check the range: it must be A2:A244 on Applications, not a range that includes the header twice."),
            ("Gemini's counts differ from the formulas.",
             "Ask Gemini how it counted. Trust the formula and refine the prompt."),
        ],
        challenge=(
            "Add a formula that counts the rows whose Position does not match the Position of their Job_ID on the Jobs "
            "tab (hint: ask Gemini for a SUMPRODUCT with VLOOKUP). The answer should be 0."
        ),
        reflection="Which issue would most distort a 'hires by source' report if nobody had caught it?",
    ),
    # ------------------------------------------------------------------ LAB 3
    dict(
        num=3,
        topic=1,
        title="Clean and Prepare the Candidate Data with Gemini Actions",
        theme="Data Prep",
        duration=30,
        objective=(
            "LO1: prepare raw HR data with Gemini actions and Sheets data-cleanup tools - remove duplicates, find and "
            "replace, set number formats, insert and delete columns, freeze, sort, filter and format as a table"
        ),
        goal=(
            "Turn the raw Q3 export into a clean, analysis-ready table of 240 applications, keeping a count before and "
            "after every change."
        ),
        workflow=["Remove duplicates", "Fix categories", "Fix types", "Restructure", "Sort & filter"],
        desc=(
            "You fix everything you found in Lab 2. Gemini explains how to remove duplicates, then performs actions for "
            "you: find and replace the Source variants, convert text salaries to numbers with a currency format, add a "
            "clean name column, delete the notes column, freeze the headers, apply a table style, and sort and filter "
            "the data. A multi-step prompt finishes the clean-up in one go. You check the row count after every change."
        ),
        build=(
            "OrchidBay_Q3_Applications_Prep as a clean table: 240 rows, seven Source values, numeric S$ salaries, a "
            "Name_Clean column, frozen headers, a Stage dropdown and Hired rows highlighted"
        ),
        services="Google Sheets · Gemini actions (find and replace, number format, insert/delete column, freeze, sort, filter, table style) · Data cleanup",
        data_files=["data/OrchidBay_Q3_Applications_Prep.xlsx"],
        prerequisites=[
            "Lab 2's list of issues (or its Test It values) to hand.",
            "This lab folder downloaded, including data/OrchidBay_Q3_Applications_Prep.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Q3_Applications_Prep.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Q3_Applications_Prep (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Applications | Jobs | Prompt_Log\n"
                f"Start     : {E2['rows']} rows, 17 columns (including Internal_Notes)",
            ),
            (
                "Ask Gemini how to remove duplicates, then follow its steps: select the whole Applications data range "
                "(click A1, then Ctrl + A), choose Data > Data cleanup > Remove duplicates, tick 'Data has header row' and "
                f"all columns. Sheets should report {E3['removed']} duplicate rows removed, {E3['rows_after']} rows remain.",
                "ASK GEMINI:\n"
                "How can I remove the duplicate rows on the Applications tab and keep one copy of each?",
            ),
            (
                "Fix the Source spellings with a Gemini action and click Apply on the preview card. Then remove the "
                "trailing space from 'JobStreet ' and the double spaces in names: select columns B and G and choose "
                "Data > Data cleanup > Trim whitespace. Open the filter on Source (Data > Create a filter) - you should "
                f"see exactly {E3['sources']} values.",
                "ACTION:\n"
                "In the Source column, find 'Linked In' and 'linkedin' and replace them with 'LinkedIn'.",
            ),
            (
                "Fix the data types and the impossible value one change at a time, clicking Apply after each preview. "
                f"Afterwards =COUNT(K2:K241) must return {E3['rows_after']} - every salary is a number. The recruiter "
                f"confirmed that {E3['neg_id']} has {E3['neg_true']} years of experience.",
                "ACTION:\n"
                "1) In the Expected_Salary column, find 'S$' and ',' and replace them with nothing.\n"
                "2) Set the number format of the Expected_Salary column to currency S$ with no decimal places.\n"
                f"3) For Candidate_ID {E3['neg_id']}, change Years_Experience from -{E3['neg_true']} to {E3['neg_true']}.",
            ),
            (
                "Tidy the structure. The new Name_Clean column fixes names typed in capitals or with extra spaces; check "
                "that it is filled all the way to the last row. Then remove the notes column - screening does not need "
                "free-text notes about candidates - and freeze the headers.",
                "ACTION:\n"
                "1) Insert a new column named Name_Clean to the right of Full_Name and fill it with =PROPER(TRIM(B2)) down to the last row.\n"
                "2) Delete the Internal_Notes column.\n"
                "3) Freeze the top row and the first column.",
            ),
            (
                "Apply a table style, then sort and filter. Gemini's sort and filter apply to the active table. Note the "
                f"filtered count - it should be {E3['se_referral']} rows - then clear the filter so all "
                f"{E3['rows_after']} rows show again. If the table style is not applied, select the data and choose "
                "Format > Convert to table.",
                "ACTION:\n"
                "1) Apply a table style to the data on the Applications tab to make it easier to read.\n"
                "2) Sort the table by Applied_Date in descending order.\n"
                "3) Filter for Software Engineer candidates whose Source is Referral.\n"
                "4) Clear the filter so all rows are visible.",
            ),
            (
                "Finish with one multi-step prompt - Gemini combines several actions in a single request. Check each "
                f"part: dates show as yyyy-mm-dd, Stage has a dropdown, and {E3['hired']} Hired rows are light green.",
                "ACTION:\n"
                "Finish cleaning this table: format Applied_Date as yyyy-mm-dd, make the Stage column a dropdown with\n"
                "Applied, Screened, Shortlisted, Interviewed, Offered, Hired, Rejected and Withdrawn, and highlight in\n"
                "light green the rows where Stage is Hired.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini acts as a help desk and walks you through Data > Data cleanup > Remove duplicates - a built-in tool "
            "you run yourself.",
            "A find-and-replace action: the two LinkedIn spelling variants become one standard value.",
            "Removes the currency symbol and thousands separator so each salary can be read as a number.",
            "Formats the cleaned numbers as S$ currency, so they read well and still calculate.",
            "Corrects the one impossible value with the figure the recruiter confirmed - a fix based on a fact, not a guess.",
            "Inserts a helper column whose formula tidies capitals and extra spaces; the original names stay unchanged.",
            "Deletes a column the analysis does not need - less personal data to share.",
            "Freezes the header row and the ID column so they stay visible as you scroll.",
            "Applies a table style - banded rows and a clear header - to the active data.",
            "Sorts the newest applications to the top.",
            "Filters the table to one role and one source, so you can count rows.",
            "Removes the filter so the whole table is visible again.",
            "One prompt, three actions: a date format, a dropdown for valid stages, and highlighting for hires.",
            LOG_EXPLAIN,
        ],
        formulas={
            "F": ("The formula in the new column", [
                ("=PROPER(TRIM(B2))",
                 "TRIM removes spaces at the start and end and squeezes double spaces to one; PROPER then capitalises "
                 "each word, so 'SITI  TAN ' becomes 'Siti Tan'. B2 is Full_Name on the same row."),
            ]),
        },
        sample_prompts=[
            ("Fill", "Fill the empty Email cells with the text 'missing - ask candidate'."),
            ("Insert", "Insert a new column called Source_Group after Source and leave it empty."),
            ("Number format", "Format Screening_Score as a whole number and Interview_Score with one decimal place."),
            ("Delete rows", "Delete the rows where Stage is Withdrawn."),
            ("Help", "How do I split the Key_Skills column into separate columns?"),
        ],
        sample_explain=[
            "Fill range: writes one value into every selected empty cell - flagging the gaps instead of hiding them.",
            "Insert dimension: adds an empty column exactly where you name it.",
            "Set number format: controls how numbers display without changing their values.",
            "Delete dimension: removes rows that match a condition. Try it on a copy - then Undo.",
            "Gemini explains Data > Split text to columns with ; as the separator.",
        ],
        checks=[
            ("Rows", f"{E3['rows_after']} rows after removing {E3['removed']} duplicates."),
            ("Source", f"Exactly {E3['sources']} values in the filter; LinkedIn {E3['linkedin']}, JobStreet {E3['jobstreet']}."),
            ("Salaries", f"=COUNT over the Expected_Salary column returns {E3['rows_after']}; values show as S$ with no "
                         "decimals."),
            ("Structure", f"Name_Clean filled to the last row; Internal_Notes gone; headers frozen; "
                          f"{E3['neg_id']} shows {E3['neg_true']} years."),
            ("Sort, filter, dropdown", f"Newest date ({E3['newest']}) at the top; the filter showed {E3['se_referral']} rows; "
                                       f"Stage dropdown added; {E3['hired']} Hired rows light green."),
        ],
        test="",
        checkpoint=(
            "This clean table is the starting point for Lab 4, which supplies the same 240 rows (plus a Budget_Max "
            "column) in its own workbook."
        ),
        troubleshooting=[
            ("Salaries still align left after the find and replace.",
             "They are still text. Select the column and choose Format > Number > Number, or ask Gemini: 'Convert the "
             "Expected_Salary values to numbers.'"),
            ("Gemini replaced 'LinkedIn' everywhere in the sheet.",
             "Click Undo and name the column: 'In the Source column only ...'."),
            ("Name_Clean stops part-way down.",
             "Ask Gemini to 'fill the formula down to row 241', or double-click the fill handle on C2."),
            ("No action card appears for sort, filter or table style.",
             "Do it from the menu: Data > Sort range, Data > Create a filter, Format > Convert to table."),
            ("Sort mixed up the rows.",
             "Undo, then make sure the whole table is selected (or converted to a table) before sorting."),
            ("Remove duplicates removed 0 rows.",
             "You selected only part of the data. Select from A1 to the last row and column, then run it again."),
        ],
        challenge=(
            "Ask Gemini to add a Source_Group column that labels LinkedIn, JobStreet, MyCareersFuture and Indeed as "
            "'Job board' and the rest as 'Direct'. Check the two groups add up to 240."
        ),
        reflection="Why should you fix data in a helper column, or keep the original, rather than overwrite it?",
    ),
    # ------------------------------------------------------------------ LAB 4
    dict(
        num=4,
        topic=1,
        title="Generate, Explain and Fix Screening Formulas",
        theme="Formulas: VLOOKUP, COUNTIF & Nested IF",
        duration=30,
        objective=(
            "LO1: use Gemini to generate VLOOKUP, IF, nested IF and COUNTIF/COUNTIFS formulas from plain-English rules, "
            "explain them step by step and fix formula errors, verifying the results on one row and in total"
        ),
        goal=(
            "Add four screening columns to the clean applications - Budget_Max, Min_Years, Salary_Fit and "
            "Screen_Result - and prove they are right."
        ),
        workflow=["Fix an error", "VLOOKUP", "IF", "Nested IF", "COUNTIF & check"],
        desc=(
            "The hiring managers want a first screen of all 240 applications. You will fix a broken lookup with Gemini's "
            "Fix button, then describe each rule in plain English and let Gemini write the formula: a VLOOKUP for the "
            "role's minimum experience, an IF for salary fit, and a nested IF with AND that labels each candidate "
            "Strong, Possible or Not suitable. Gemini explains the formula, COUNTIF and COUNTIFS summarise the results, "
            "and independent check formulas prove them."
        ),
        build=(
            "OrchidBay_Screening_Formulas with working Budget_Max, Min_Years, Salary_Fit and Screen_Result columns, a "
            "Checks tab of COUNTIF/COUNTIFS results that reconcile to 240, and a filled Prompt_Log"
        ),
        services="Google Sheets · Gemini formula help (side panel, = then Cmd/Ctrl + Ctrl/Alt + G, Fix) · OrchidBay_Screening_Formulas.xlsx",
        data_files=["data/OrchidBay_Screening_Formulas.xlsx"],
        prerequisites=[
            "Labs 1-3 completed, or familiarity with the Applications columns (see About_This_Data).",
            "This lab folder downloaded, including data/OrchidBay_Screening_Formulas.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Screening_Formulas.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Screening_Formulas (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Applications | Jobs | Settings | Checks | Prompt_Log\n"
                "Settings  : B1 report date 2026-09-30 | B2 pass mark 70 | B3 possible mark 60",
            ),
            (
                "Column Q (Budget_Max) shows an error. Hover over Q2 and click Fix: Gemini reviews the formula and explains "
                "the problem - VLOOKUP asks for column 9 of a range that has only 8 columns. Accept the fix, then copy Q2 "
                f"down to Q241 (or double-click the fill handle). Q2 should show {_money(E4['first_budget'])}. If you don't "
                "see Fix, ask Gemini instead.",
                "Before    : =VLOOKUP(E2,Jobs!$A$2:$H$9,9,FALSE)  ->  #REF!\n"
                "After     : =VLOOKUP(E2,Jobs!$A$2:$H$9,8,FALSE)  ->  " + _money(E4["first_budget"]) + "\n\n"
                "ASK GEMINI:\n"
                "Explain why the formula in Q2 shows #REF! and give me the corrected formula.",
            ),
            (
                "Type Min_Years in R1. Click R2, then ask Gemini for the formula - in the side panel, or type = in the cell "
                "and press Cmd + Ctrl + G (Mac) / Ctrl + Alt + G (Windows). Click Insert, then fill it down to row 241. "
                f"R2 should show {E4['first_min']} ({E4['first_pos']}).",
                "FORMULA:\n"
                "Create a formula for R2 that looks up the Job_ID in E2 on the Jobs tab (A2:H9) and returns Min_Years.",
            ),
            (
                f"Type Salary_Fit in S1, ask for the formula in S2, insert it and fill it down. S2 should say "
                + ("Within budget" if E4['first_salary'] <= E4['first_budget'] else "Above budget")
                + f" ({_money(E4['first_salary'])} against a Budget_Max of {_money(E4['first_budget'])}).",
                "FORMULA:\n"
                "Create a formula for S2 that returns \"Within budget\" if Expected_Salary in K2 is less than or equal to\n"
                "Budget_Max in Q2, otherwise \"Above budget\".",
            ),
            (
                "Type Screen_Result in T1. Describe the whole rule in one prompt - Gemini nests the IFs for you. Insert and "
                f"fill down. T2 ({E4['first_id']}, score {E4['first_score']}, {E4['first_years']} years) should say "
                f"{E4['first_result']}. Screen_Result only flags candidates for a recruiter to review - a person still "
                "reads every application before anyone is rejected.",
                "FORMULA:\n"
                "Create a formula for T2: if Screening_Score in M2 is at least the pass mark in Settings!B2 and\n"
                "Years_Experience in H2 is at least Min_Years in R2, return \"Strong\"; otherwise, if M2 is at least\n"
                "Settings!B3, return \"Possible\"; otherwise return \"Not suitable\".",
            ),
            (
                "Ask Gemini to explain the formula. Check its explanation against T2's actual values in M2, H2 and R2 - "
                "an explanation you can't match to the data is not an explanation.",
                "ASK GEMINI:\n"
                "Explain the formula in T2 step by step, and tell me what it returns for the candidate in row 2 and why.",
            ),
            (
                "On the Checks tab, put labels in column A and ask Gemini for these two formulas one at a time, inserting "
                f"each into column B. Expect {E4['strong']} Strong in total and {E4['da_strong']} Strong Data Analysts.",
                "FORMULA:\n"
                "1) Create a formula that counts how many cells in Applications!T2:T241 are \"Strong\".\n"
                "2) Create a formula that counts the rows on Applications where Position is \"Data Analyst\" and Screen_Result is \"Strong\".",
            ),
            (
                "Paste the independent checks below them. Strong + Possible + Not suitable must add up to 240, and the "
                "Above budget count must match a COUNTIF of Salary_Fit. Then ask Gemini a what-if question and test its "
                f"answer: change Settings!B2 to 75 - the Strong count should become {E4['strong75']} - then set it back to 70.",
                "CHECK:\n"
                "Possible          =COUNTIF(Applications!T2:T241,\"Possible\")\n"
                "Not suitable      =COUNTIF(Applications!T2:T241,\"Not suitable\")\n"
                "All results       =COUNTA(Applications!T2:T241)\n"
                "Above budget      =SUMPRODUCT(--(Applications!K2:K241>Applications!Q2:Q241))\n\n"
                "ASK GEMINI:\n"
                "If I change the pass mark in Settings!B2 from 70 to 75, how many candidates will be Strong?",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "If the Fix button does not appear, Gemini explains the #REF! error in the side panel and gives the corrected "
            "formula.",
            "Gemini writes a VLOOKUP that finds the row's Job_ID on the Jobs tab and returns the role's minimum years.",
            "Gemini writes an IF that compares two cells on the same row and returns one of two labels.",
            "A nested IF with AND: the business rule in one prompt, turned into a three-way label.",
            "Gemini explains each part of the formula and works it through for row 2, so you can check its logic by hand.",
            "COUNTIF counts the cells that equal \"Strong\".",
            "COUNTIFS counts rows that meet two conditions at once - Position and Screen_Result.",
            "A what-if question. Change the cell and compare Gemini's prediction with the recalculated COUNTIF.",
            LOG_EXPLAIN,
        ],
        formulas={
            "B": ("The formula Gemini should write", [
                ("=VLOOKUP(E2,Jobs!$A$2:$H$9,5,FALSE)",
                 "VLOOKUP(search key, range, column number, FALSE): finds E2 (Job_ID) in the first column of Jobs!A2:H9 "
                 "and returns the 5th column, Min_Years. FALSE means exact match. $ locks the range when you fill down."),
            ]),
            "C": ("The formula Gemini should write", [
                ('=IF(K2<=Q2,"Within budget","Above budget")',
                 "IF(test, value if true, value if false): if Expected_Salary is not above Budget_Max, say Within budget."),
            ]),
            "D": ("The formula Gemini should write", [
                ('=IF(AND(M2>=Settings!$B$2,H2>=R2),"Strong",IF(M2>=Settings!$B$3,"Possible","Not suitable"))',
                 "AND(...) is TRUE only when both tests pass: score at least the pass mark AND experience at least the "
                 "minimum. If not, the second IF checks the possible mark. The marks live in Settings, so changing a cell "
                 "re-screens everyone."),
            ]),
            "F": ("The formula Gemini should write", [
                ('=COUNTIF(Applications!T2:T241,"Strong")', "Counts the cells in Screen_Result that equal Strong."),
            ]),
            "G": ("The formula Gemini should write", [
                ('=COUNTIFS(Applications!F2:F241,"Data Analyst",Applications!T2:T241,"Strong")',
                 "COUNTIFS takes pairs of (range, criterion) and counts rows that meet ALL of them."),
            ]),
        },
        sample_prompts=[
            ("Lookup", "Create a formula that returns the Hiring_Manager for the Job_ID in E2 from the Jobs tab (A2:J9)."),
            ("Date", "Create a formula for the number of days between Applied_Date in D2 and the report date in Settings!B1."),
            ("Text", "Create a formula that returns TRUE if Key_Skills in J2 contains \"SQL\"."),
            ("Count", "Create a formula that counts Above budget candidates for each Position."),
            ("Explain", "Explain the difference between VLOOKUP and XLOOKUP, and when to use each."),
        ],
        sample_explain=[
            "VLOOKUP again, returning a different column (10, Hiring_Manager).",
            "Writes =Settings!$B$1-D2: subtracting dates gives the number of days.",
            "Writes =REGEXMATCH(J2,\"SQL\") or =ISNUMBER(SEARCH(\"SQL\",J2)) - a keyword screen.",
            "Gemini may build a small table of COUNTIFS - check one row by hand.",
            "Gemini explains both lookups; XLOOKUP needs no column number and can look left.",
        ],
        checks=[
            ("Fix", f"Q2 = {_money(E4['first_budget'])}; no #REF! left in column Q."),
            ("Row 2", f"{E4['first_id']}: Min_Years {E4['first_min']}, Salary_Fit Within budget, Screen_Result "
                      f"{E4['first_result']}."),
            ("Screen_Result totals", f"Strong {E4['strong']} + Possible {E4['possible']} + Not suitable "
                                     f"{E4['not_suitable']} = 240."),
            ("COUNTIFS", f"Strong Data Analysts = {E4['da_strong']}; Above budget = {E4['above']} "
                         f"(Within budget {E4['within']})."),
            ("What-if", f"Pass mark 75 gives {E4['strong75']} Strong; set back to 70 gives {E4['strong']}."),
        ],
        test="",
        checkpoint="Topic 1 ends here. Lab 5 starts Topic 2 with its own tracker workbook.",
        troubleshooting=[
            ("The Fix button does not appear.",
             "Click the cell and hover over the red triangle. If there is still no Fix, use the ASK GEMINI prompt in "
             "Step 2 and type the corrected formula yourself."),
            ("Gemini inserted the formula in the wrong cell.",
             "Undo, click the target cell first, then click Insert."),
            ("Gemini used XLOOKUP instead of VLOOKUP.",
             "Both are correct. Ask 'Use VLOOKUP instead' if you want to practise VLOOKUP."),
            ("The formula works in row 2 but not lower down.",
             "A range is not locked with $. Ask Gemini to 'make the Jobs range absolute' and fill down again."),
            ("Strong + Possible + Not suitable is not 240.",
             "Some rows have no formula or an error. Filter column T for blanks or #N/A."),
        ],
        challenge=(
            "Ask Gemini for one formula that returns the Strong count for every Position at once (hint: QUERY or a "
            "COUNTIFS against a list of positions). Check that it adds up to " + str(E4["strong"]) + "."
        ),
        reflection="Why is it better to keep the pass mark in Settings!B2 than to type 70 inside the formula?",
    ),
]
