"""Topic 2 labs for C817: Data Analytics and Visualization with Gemini (Orchid Bay Talent Partners hiring data)."""

from mock_data import EXPECTED
from data_domain1 import LOG, LOG_EXPLAIN, LOG_STEP, SETUP_STEP

E5, E6, E7, E8 = EXPECTED[5], EXPECTED[6], EXPECTED[7], EXPECTED[8]
_SRC = E7["src"]
_PM = {"2026-01": "January", "2026-02": "February", "2026-03": "March", "2026-04": "April", "2026-05": "May",
       "2026-06": "June", "2026-07": "July", "2026-08": "August", "2026-09": "September"}
_TOP_HIRE_SRCS = sorted(_SRC, key=lambda s: -_SRC[s]["hires"])


def _money(v):
    return f"S${v:,.0f}"


DOMAIN2 = [
    # ------------------------------------------------------------------ LAB 5
    dict(
        num=5,
        topic=2,
        title="Build a Colour-Coded Interview Tracker from Unstructured Notes",
        theme="Tables, Trackers & Conditional Formatting",
        duration=30,
        objective=(
            "LO2: use Gemini to turn unstructured notes into a formatted table, build a tracker with dropdowns and "
            "checkboxes, and apply and edit conditional-formatting rules on HR data"
        ),
        goal=(
            "Turn a week of typed interview notes into a colour-coded tracker, and flag the strongest, most expensive "
            "and slowest-to-start candidates on the shortlist."
        ),
        workflow=["Notes to table", "Dropdowns & checkboxes", "Colour-code", "Flag the shortlist", "Multi-step clean-up"],
        desc=(
            "The recruiters typed this week's interview notes as free text. You will ask Gemini to turn them into a "
            "structured table, refine it before inserting, and make it a working tracker with Status and Outcome "
            "dropdowns and a Reference_Checked checkbox. Conditional-formatting actions colour-code the tracker and flag "
            "the shortlist: top screening scores, salaries above budget and long notice periods. You will edit a rule "
            "with Settings, run a multi-step clean-up prompt, and create an onboarding checklist from scratch."
        ),
        build=(
            "OrchidBay_Interview_Tracker with an Interview_Tracker tab (12 interviews, dropdowns, checkboxes, colour-coded "
            "Status), a flagged Shortlist tab and a new Onboarding_Checklist tab"
        ),
        services="Google Sheets · Gemini (create tables, Insert, dropdown, checkbox and conditional-formatting actions, Settings) · OrchidBay_Interview_Tracker.xlsx",
        data_files=["data/OrchidBay_Interview_Tracker.xlsx"],
        prerequisites=[
            "Topic 1 completed: you can open the Gemini side panel, insert results and apply actions.",
            "This lab folder downloaded, including data/OrchidBay_Interview_Tracker.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Interview_Tracker.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Interview_Tracker (Google Sheets copy)\n"
                f"Tabs      : About_This_Data | Interview_Notes ({E5['notes']} lines) | Shortlist ({E5['shortlist']} rows) | Prompt_Log",
            ),
            (
                "Ask Gemini to build a table from the notes. Read the draft in the panel and refine it with the follow-up "
                f"before you insert it. Check that it has {E5['notes']} rows and that every Status is one of the four "
                f"options: Completed {E5['status']['Completed']}, Scheduled {E5['status']['Scheduled']}, Rescheduled "
                f"{E5['status']['Rescheduled']}, No-show {E5['status']['No-show']}. Click Insert, put it on a new tab "
                "and rename the tab Interview_Tracker.",
                "INSERT:\n"
                "Using the notes on the Interview_Notes tab, create a table with the columns Date, Time, Candidate,\n"
                "Candidate_ID, Position, Panel, Format and Status. Status must be one of Scheduled, Completed,\n"
                "No-show or Rescheduled.\n\n"
                "FOLLOW-UP:\n"
                "Add two empty columns at the end: Outcome and Reference_Checked.",
            ),
            (
                "Make it a working tracker. Send these one at a time on the Interview_Tracker tab and click Apply on each "
                "action card. Test a dropdown by clicking a Status cell.",
                "ACTION:\n"
                "1) Make the Status column a dropdown with the options Scheduled, Completed, No-show and Rescheduled.\n"
                "2) Create a dropdown in the Outcome column with the options Pending, Advance, Hold and Reject.\n"
                "3) Insert checkboxes in the Reference_Checked column, unchecked by default.",
            ),
            (
                "Colour-code the Status column. When the action finishes, click Settings to see the rules Gemini created "
                "(the same rules are in Format > Conditional formatting). Change one Status to No-show and watch the "
                "colour change, then change it back.",
                "ACTION:\n"
                "Colour-code the Status column: Completed light green, Scheduled light blue, Rescheduled amber and\n"
                "No-show light red.",
            ),
            (
                "Switch to the Shortlist tab and flag it one rule at a time. Expect "
                f"{E5['hi85']} light-green rows (score 85 or more), {E5['above']} red salaries above budget, and a colour "
                "scale on Interview_Score (blank cells stay white).",
                "ACTION:\n"
                "1) On the Shortlist tab, highlight the rows where Screening_Score is 85 or more in light green.\n"
                "2) Make Expected_Salary bold red when it is greater than Budget_Max on the same row.\n"
                "3) Add a colour scale to Interview_Score from red for low values to green for high values.",
            ),
            (
                "Edit a rule instead of starting again: open Format > Conditional formatting (or Settings on the first "
                "card), choose the green rule and change 85 to 80. Then ask Gemini to count the green rows and check its "
                f"answer with the formula - both should be {E5['hi80']}.",
                "ASK GEMINI:\n"
                "On the Shortlist tab, how many rows have a Screening_Score of 80 or more? Which positions are they for?\n\n"
                "CHECK:\n"
                "Score 80 or more   =COUNTIF(Shortlist!E2:E44,\">=80\")\n"
                "Above budget       =SUMPRODUCT(--(Shortlist!G2:G44>Shortlist!H2:H44))",
            ),
            (
                "One multi-step prompt can do several actions. Check every part: Stage has a dropdown, Notice_End shows "
                f"dates, Contacted has checkboxes, and {E5['long_notice']} rows are light orange.",
                "ACTION:\n"
                "Clean up the Shortlist tracker: make the Stage column a dropdown with Shortlisted, Interviewed and\n"
                "Offered; add a new column Notice_End at the end with a formula for 30 September 2026 plus\n"
                "Notice_Weeks weeks, formatted as a date; add a checkbox column called Contacted; and highlight in\n"
                "light orange the rows where Notice_Weeks is more than 8.",
            ),
            (
                "Create a table from scratch - no data needed. Refine it, then Insert it on a new tab named "
                "Onboarding_Checklist.",
                "INSERT:\n"
                "Create an onboarding checklist tracker for a new hire in Singapore, with the columns Task, Owner,\n"
                "Days_Before_Start, Status and Done. Include 10 typical tasks. Make Done a checkbox.\n\n"
                "FOLLOW-UP:\n"
                "Add 3 tasks for laptop, system access and security training, owned by IT.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini reads the free-text notes and drafts a structured table with the columns you name - in the panel, "
            "not in the sheet yet.",
            "Refines the draft before you insert it: two extra columns for the tracker.",
            "Create dropdown action: limits Status to four valid values, so the tracker stays consistent.",
            "A second dropdown for the interview outcome.",
            "Add checkbox action: a TRUE/FALSE tick box for each interview.",
            "Conditional-formatting action with four colour rules - one per status - so the week reads at a glance.",
            "Highlights whole rows that meet a condition on one column.",
            "Compares two cells on the same row - salary versus budget - and formats only the salary cell.",
            "A colour scale: shades every value from red (low) to green (high).",
            "Gemini counts the rows that now match the edited rule; the COUNTIF confirms it.",
            "A multi-step task: a dropdown, a formula column, a checkbox column and a highlight rule in one prompt.",
            "Gemini creates a ready-made table from scratch using typical onboarding tasks.",
            "Adds rows to the draft before you insert it.",
            LOG_EXPLAIN,
        ],
        formulas={
            "K": ("The formula Gemini should add in Notice_End", [
                ("=DATE(2026,9,30)+I2*7",
                 "DATE builds the date 30 Sep 2026; adding Notice_Weeks x 7 days gives the earliest start date. "
                 "Format the column as a date."),
            ]),
        },
        sample_prompts=[
            ("Table", "Create a table of interview questions for a Data Analyst, with columns Question, Skill tested and What a good answer includes."),
            ("Dropdown", "Convert the Recruiter column on the Shortlist tab to a dropdown with values from the same column."),
            ("Highlight", "Highlight the Shortlist rows where Stage is Offered in light purple."),
            ("Freeze", "Freeze the top row and the first two columns of the Shortlist tab."),
            ("Help", "Teach me how to use conditional formatting with a custom formula."),
        ],
        sample_explain=[
            "Gemini drafts a structured interview guide you can insert and reuse.",
            "Turns an existing column into a dropdown of its own values.",
            "Another row-highlight rule - check the count with COUNTIF.",
            "A freeze action keeps IDs and names visible as you scroll right.",
            "Gemini explains custom-formula rules in Format > Conditional formatting, step by step.",
        ],
        checks=[
            ("Interview_Tracker", f"{E5['notes']} rows; Completed {E5['status']['Completed']}, Scheduled "
                                  f"{E5['status']['Scheduled']}, Rescheduled {E5['status']['Rescheduled']}, No-show "
                                  f"{E5['status']['No-show']}."),
            ("Tracker controls", "Status and Outcome dropdowns work; Reference_Checked has checkboxes; Status is colour-coded."),
            ("Shortlist flags", f"{E5['hi85']} green rows at 85, then {E5['hi80']} after editing the rule to 80; "
                                f"{E5['above']} salaries in bold red; Interview_Score has a colour scale."),
            ("Multi-step", f"Stage dropdown, Notice_End dates, Contacted checkboxes; {E5['long_notice']} light-orange rows."),
            ("Onboarding_Checklist", "13 tasks (10 + 3 IT tasks) with a Done checkbox column."),
        ],
        test="",
        checkpoint="Lab 6 opens a separate profiles workbook, so you can start it even if this tracker is unfinished.",
        troubleshooting=[
            ("The table from the notes has wrong statuses.",
             "Use Retry, or a follow-up: 'done or completed means Completed; moved means Rescheduled; did not turn up "
             "means No-show; confirmed or accepted means Scheduled.'"),
            ("Insert put the table on top of the notes.",
             "Undo. Insert it on a new tab, or select an empty cell on a new tab before clicking Insert."),
            ("The row highlight colours only one cell.",
             "Undo and say 'highlight the whole row'. In Format > Conditional formatting the custom formula needs $ "
             "before the column, e.g. =$E2>=85, applied to A2:K44."),
            ("Dropdown or checkbox actions are not offered.",
             "Use the menu: select the column > Insert > Dropdown (or Data > Data validation), and Insert > Checkbox."),
            ("No Settings button appears.",
             "Settings appears only for actions with configurable settings. Use Format > Conditional formatting."),
        ],
        challenge="Ask Gemini to add a Days_To_Start column and highlight anyone who cannot start before 1 December 2026.",
        reflection="Which flag on the Shortlist would change a hiring manager's decision, and which is only 'nice to know'?",
    ),
    # ------------------------------------------------------------------ LAB 6
    dict(
        num=6,
        topic=2,
        title="Extract and Categorise Candidate Text with the AI Function",
        theme="AI Function & Fill with Gemini",
        duration=30,
        objective=(
            "LO2: use the AI function (=AI) and Fill with Gemini to extract, categorise and summarise free-text HR data "
            "in cells, and measure the accuracy of the AI output against recorded values"
        ),
        goal=(
            "Turn 30 free-text candidate summaries and interview notes into structured columns - notice period, "
            "sentiment and a manager summary - and measure how accurate they are."
        ),
        workflow=["Extract", "Categorise", "Summarise", "Measure accuracy", "Fill & group"],
        desc=(
            "Hiring managers want a quick read of 30 shortlisted candidates, but the details are buried in free text. "
            "You will type =AI formulas that extract the notice period in weeks, classify each interview feedback as "
            "Positive, Mixed or Negative, and write a one-line summary that leaves out personal characteristics. You "
            "will generate the outputs, compare them with an answer key using formulas, use Fill with Gemini for a skills "
            "column, and ask the side panel to group the feedback into themes."
        ),
        build=(
            "OrchidBay_Candidate_Profiles with AI-filled Notice_Weeks_AI, Feedback_Sentiment_AI, Manager_Summary_AI and "
            "Top_Skills columns, a Checks tab measuring accuracy, and an inserted feedback-themes table"
        ),
        services="Google Sheets · AI function (=AI, Generate and insert) · Fill with Gemini · Gemini side panel · OrchidBay_Candidate_Profiles.xlsx",
        data_files=["data/OrchidBay_Candidate_Profiles.xlsx"],
        prerequisites=[
            "The AI function must be available on your account: type =AI( in a cell and check that it is recognised.",
            "This lab folder downloaded, including data/OrchidBay_Candidate_Profiles.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Candidate_Profiles.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Candidate_Profiles (Google Sheets copy)\n"
                f"Tabs      : About_This_Data | Profiles ({E6['rows']} rows) | Answer_Key | Checks | Prompt_Log\n"
                "Empty     : F Notice_Weeks_AI | G Feedback_Sentiment_AI | H Manager_Summary_AI",
            ),
            (
                "Type the formula into F2 exactly as shown, then select F2 and click Generate and insert. Check F2 against "
                f"D2 ({E6['first_id']}): the expected answer is {E6['first_notice']}. Then copy F2 down to F31 "
                "(drag the fill handle), select F2:F31 and click Generate and insert again. Up to 350 selected AI cells "
                "generate at once. The range argument (D2) is the only data the function sees.",
                "AI FUNCTION:\n"
                "=AI(\"Extract the notice period in weeks as a whole number. Output only the number. Use 0 for immediately, 4 for one month, 8 for two months and 12 for three months.\", D2)",
            ),
            (
                "Categorise the feedback the same way in G2, then fill and generate G2:G31. Row 2 should be "
                f"{E6['first_sent']}: '{E6['first_feedback']}'",
                "AI FUNCTION:\n"
                "=AI(\"Classify this interview feedback as Positive, Mixed or Negative. Output one word only.\", E2)",
            ),
            (
                "Write a manager summary in H2 from three cells at once. Generate only H2:H6 - summaries use more of your "
                "AI generation limit. Read each one: does it stick to the evidence?",
                "AI FUNCTION:\n"
                "=AI(\"Write a one-sentence summary of this candidate for the hiring manager, using only the summary and feedback. Do not mention age, gender, race, religion or nationality.\", C2:E2)",
            ),
            (
                "Measure accuracy. Paste the check formulas into Checks column B (labels in column A). Answer_Key holds "
                f"the recorded values: Positive {E6['positive']}, Mixed {E6['mixed']}, Negative {E6['negative']}. "
                "Note how many of the 30 match. AI output is text and cannot be undone - to change an answer, edit the "
                "prompt and click Refresh and insert.",
                "CHECK:\n"
                "Notice matches      =SUMPRODUCT(--(TO_TEXT(Profiles!F2:F31)=TO_TEXT(Answer_Key!B2:B31)))\n"
                "Sentiment matches   =SUMPRODUCT(--(TRIM(Profiles!G2:G31)=Answer_Key!C2:C31))\n"
                "Positive (AI)       =COUNTIF(Profiles!G2:G31,\"Positive\")\n"
                "Mixed (AI)          =COUNTIF(Profiles!G2:G31,\"Mixed\")",
            ),
            (
                "Investigate any mismatch with the side panel. Now that your answers are generated, it is fine for Gemini "
                "to read the answer key - it was kept out of the =AI prompts so it could not influence them.",
                "ASK GEMINI:\n"
                "Compare Profiles column G with Answer_Key column C. Which candidates don't match, and what in the\n"
                "Interview_Feedback text could have caused each difference?",
            ),
            (
                "Fill with Gemini: type Top_Skills in I1 and, in I2, the skills from D2 yourself (e.g. 'CRM, Negotiation, "
                "Stakeholder Management'). Select I2:I31 and choose Fill (or drag the fill handle down and pick Fill with "
                "Gemini when it is offered). Gemini follows your example for every row. If Fill is not offered on your "
                "account, use the AI function instead.",
                "AI FUNCTION:\n"
                "=AI(\"List the skills mentioned in this summary, comma separated, in the same order.\", D2)",
            ),
            (
                "Use the side panel to categorise the whole column at once, and insert the result on a new tab named "
                "Feedback_Themes. Then check for bias in the generated summaries.",
                "INSERT:\n"
                "Group the Interview_Feedback on the Profiles tab into themes and count how many candidates fall into\n"
                "each theme. Show the result as a table with one example per theme.\n\n"
                "ASK GEMINI:\n"
                "Do any of the summaries in column H mention personal characteristics or anything that should not be\n"
                "used in a hiring decision?",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini compares its own output with the recorded values and explains the likely cause of each mismatch - "
            "usually ambiguous wording.",
            "The side panel categorises a whole column in one go and drafts a themes table for you to insert.",
            "A fairness check on AI-written text before anyone relies on it.",
            LOG_EXPLAIN,
        ],
        formulas={},
        sample_prompts=[
            ("AI function", "=AI(\"Does this candidate mention SQL? Answer Yes or No.\", D2)"),
            ("AI function", "=AI(\"Write a polite two-sentence email inviting this candidate to a second interview.\", B2:C2)"),
            ("Categorise", "=AI(\"Classify the seniority of this candidate as Junior, Mid or Senior based on years of experience.\", D2)"),
            ("Side panel", "Which five candidates have the most positive feedback? Show their names and positions."),
            ("Side panel", "Summarise the main concerns interviewers raised, with the number of candidates for each."),
        ],
        sample_explain=[
            "A yes/no extraction - easy to check with SEARCH or REGEXMATCH.",
            "Generates text from two cells - always read it before sending anything.",
            "Categorises into your own definitions; give the definitions in the prompt for consistent results.",
            "The side panel answers across all 30 rows at once.",
            "Turns free text into counted themes you can act on.",
        ],
        checks=[
            ("Notice_Weeks_AI", f"30 numbers; row 2 = {E6['first_notice']}; Notice matches close to 30 (recorded: "
                                f"{E6['long_notice']} candidates with 8+ weeks)."),
            ("Feedback_Sentiment_AI", f"Recorded split Positive {E6['positive']}, Mixed {E6['mixed']}, Negative "
                                      f"{E6['negative']}; your Sentiment matches count shows how many agree."),
            ("Manager_Summary_AI", "H2:H6 filled with one sentence each and no personal characteristics."),
            ("Top_Skills", "I2:I31 filled by Fill with Gemini (or =AI), following your example in I2."),
            ("Feedback_Themes", "An inserted themes table whose counts add up to 30."),
        ],
        test="",
        checkpoint="Lab 7 opens the 2026 year-to-date workbook - 720 applications including the Q3 drive.",
        troubleshooting=[
            ("'AI function not available'.",
             "Your plan, admin settings or language setting does not include it. Use the side panel instead: 'For each "
             "row, extract the notice period in weeks from Candidate_Summary' and insert the result."),
            ("The cell shows the formula but no answer.",
             "Select the cell(s) and click Generate and insert - AI cells do not generate on their own."),
            ("You can't generate any more.",
             "You reached a generation limit. Generate fewer cells (e.g. 10 rows) or wait and try later."),
            ("Answers come back as '4 weeks' instead of 4.",
             "Make the prompt stricter ('Output only the number'), then Refresh and insert."),
            ("The AI output changed after you edited D2.",
             "AI results do not update on their own. Select the cell and click Refresh and insert."),
        ],
        challenge=(
            "Write one =AI formula that returns 'Ready now', 'Within a month' or 'Later' from the summary. Check it "
            "against Notice_Weeks_AI with an IFS formula."
        ),
        reflection="For which kinds of HR text would you never let =AI output go into a record without a person reading it?",
    ),
    # ------------------------------------------------------------------ LAB 7
    dict(
        num=7,
        topic=2,
        title="Generate Hiring Insights and Pivot Tables with Gemini",
        theme="Data Analysis & Insights",
        duration=30,
        objective=(
            "LO2: use Gemini to analyse an HR dataset - trends, comparisons and rates - inspect its analysis steps, "
            "create and adjust pivot tables, verify every number with formulas and export the insights to Google Docs"
        ),
        goal=(
            "Answer the Head of Talent's questions about 2026 hiring - trend, best source, slowest role, cost per hire - "
            "with numbers you have checked."
        ),
        workflow=["Explore", "Trends", "Compare sources", "Pivot tables", "Export insights"],
        desc=(
            "Orchid Bay's Head of Talent wants to know how 2026 hiring is going. Using all 720 applications from January "
            "to September, you will ask Gemini what analysis is possible, find the monthly trend, compare sources by "
            "hire rate and cost per hire, and find which role takes longest to fill. You will open Analysis steps to see "
            "how Gemini calculated, create pivot tables with Gemini actions and adjust them with Settings, check every "
            "figure with COUNTIFS or AVERAGEIFS, and export five insights to a Google Doc."
        ),
        build=(
            "OrchidBay_Hiring_2026_YTD with two pivot tables (source by stage, days to hire by position), a Checks area of "
            "formulas, and a Google Doc of insights exported from Gemini"
        ),
        services="Google Sheets · Gemini data analysis (Analysis steps, Export to Docs) · pivot-table actions · OrchidBay_Hiring_2026_YTD.xlsx",
        data_files=["data/OrchidBay_Hiring_2026_YTD.xlsx"],
        prerequisites=[
            "Labs 1-6, or comfort with Ask Gemini, Insert and actions.",
            "This lab folder downloaded, including data/OrchidBay_Hiring_2026_YTD.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Hiring_2026_YTD.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Hiring_2026_YTD (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Applications (720 rows) | Jobs | Source_Costs | Prompt_Log\n"
                "Period    : applications 2026-01-01 to 2026-09-26",
            ),
            (
                "Start broad. Gemini suggests analyses that fit the columns it finds - note two you want to try.",
                "ASK GEMINI:\n"
                "What analysis can you help me perform with this sheet?",
            ),
            (
                "Ask for the trend. Under the answer, click Analysis steps (and Show code if offered) to see how Gemini "
                f"grouped and counted. Applications peaked in {_PM[E7['peak']]} ({E7['by_month'][E7['peak']]}); "
                f"February was lowest ({E7['by_month']['2026-02']}).",
                "ASK GEMINI:\n"
                "Identify trends in the number of applications by Month. Which month had the most applications, and\n"
                "which had the fewest?",
            ),
            (
                f"Compare sources. Gemini should find that {E7['best_rate']} has the best hire rate "
                f"({_SRC[E7['best_rate']]['hires']} of {_SRC[E7['best_rate']]['apps']}, {_SRC[E7['best_rate']]['rate']}%) "
                f"while {E7['most_hires']} brings the most hires ({_SRC[E7['most_hires']]['hires']} of "
                f"{_SRC[E7['most_hires']]['apps']}).",
                "ASK GEMINI:\n"
                "For each Source, show the applications, hires (Stage is Hired) and hire rate. Which source has the\n"
                "best hire rate, and which brings in the most hires?",
            ),
            (
                "Create a pivot table with a Gemini action. When it finishes, click Settings to open the pivot table editor "
                f"- try adding a filter. LinkedIn should show Hired {_SRC['LinkedIn']['hires']} and Rejected "
                f"{E7['li_rejected']}; the grand total is 720. Then paste the checks into empty cells beside the pivot table.",
                "ACTION:\n"
                "Create a pivot table on a new sheet that shows the count of Candidate_ID with Source in rows and Stage\n"
                "in columns.\n\n"
                "CHECK:\n"
                "LinkedIn hired      =COUNTIFS(Applications!G2:G721,\"LinkedIn\",Applications!M2:M721,\"Hired\")\n"
                "Referral hired      =COUNTIFS(Applications!G2:G721,\"Referral\",Applications!M2:M721,\"Hired\")\n"
                "All applications    =COUNTA(Applications!A2:A721)",
            ),
            (
                f"Which role is slowest to fill? Gemini should name {E7['slowest']} ({E7['dth'][E7['slowest']]} days on "
                f"average; {E7['avg_dth']} days across all {E7['hires']} hires). Confirm with a second pivot table and "
                "an AVERAGEIFS check.",
                "ASK GEMINI:\n"
                "What is the average Days_To_Hire for each Position? Which role takes the longest to fill?\n\n"
                "ACTION:\n"
                "Create a pivot table that shows the average Days_To_Hire by Position, sorted from highest to lowest.\n\n"
                "CHECK:\n"
                f"{E7['slowest']} avg   =AVERAGEIFS(Applications!P2:P721,Applications!F2:F721,\"{E7['slowest']}\",Applications!M2:M721,\"Hired\")",
            ),
            (
                "Bring in costs from a second tab. Cost per hire = applications x cost per application / hires. "
                f"{E8['cheapest']} should be cheapest ({_money(E8['cph'][E8['cheapest']])}) and {E8['dearest']} dearest "
                f"({_money(E8['cph'][E8['dearest']])}).",
                "ASK GEMINI:\n"
                "Using the Applications and Source_Costs tabs, calculate the total cost and the cost per hire for each\n"
                "Source. Which source gives the cheapest hires?",
            ),
            (
                "Ask for insights for the Head of Talent. Check each number against your pivot tables and checks, then "
                "click Export to Docs and name the document 'Orchid Bay 2026 Hiring Insights'. Optional: ask the web "
                "question - Gemini only searches the web when you ask it to, and you must check its sources.",
                "ASK GEMINI:\n"
                "Write five insights for the Head of Talent from this data. Give the number behind each insight and\n"
                "one recommended action.\n\n"
                "ASK GEMINI:\n"
                "Using Google Search, what is a typical time to hire for professional roles in Singapore? List your sources.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini reads the columns and suggests analyses that fit them - a good way to start on unfamiliar data.",
            "A trend question over time. Analysis steps shows how Gemini grouped the rows by Month.",
            "A comparison with a calculated rate. Gemini counts hires per source and divides by applications.",
            "A pivot-table action: Gemini builds a real pivot table you can adjust with Settings.",
            "An average by group, answered in the panel.",
            "A second pivot table to confirm the answer above.",
            "A cross-tab calculation that combines Applications with the Source_Costs lookup table.",
            "Gemini drafts manager-ready insights - each with its number and an action - which you export to a Google Doc.",
            "Gemini searches the web only because the prompt says 'Using Google Search'. Treat the answer as external "
            "evidence and check its sources.",
            LOG_EXPLAIN,
        ],
        formulas={},
        sample_prompts=[
            ("Trend", "How did the number of hires change from Q1 to Q2 to Q3 2026?"),
            ("Compare", "Compare the average Screening_Score of hired and rejected candidates."),
            ("Pivot", "Create a pivot table that shows the number of hires by Recruiter and Month."),
            ("Regression", "How can I show regression and prediction of monthly applications?"),
            ("Explain", "Explain this analysis like I'm a hiring manager with no data background."),
        ],
        sample_explain=[
            "Groups months into quarters - check it with COUNTIFS on Month.",
            "Compares two groups on one measure - is screening predicting who gets hired?",
            "A two-dimensional pivot table, created and adjustable with Settings.",
            "Gemini explains trend lines and forecasting - treat any prediction as an estimate.",
            "Asks Gemini to rewrite the same findings for a different audience.",
        ],
        checks=[
            ("Trend", f"Peak {_PM[E7['peak']]} 2026 ({E7['by_month'][E7['peak']]} applications); lowest February "
                      f"({E7['by_month']['2026-02']})."),
            ("Sources", f"Best hire rate {E7['best_rate']} {_SRC[E7['best_rate']]['rate']}%; most hires "
                        f"{E7['most_hires']} ({_SRC[E7['most_hires']]['hires']}); {E7['hires']} hires in total."),
            ("Pivot 1", f"Source x Stage; LinkedIn Hired {_SRC['LinkedIn']['hires']}, Rejected {E7['li_rejected']}; grand total 720."),
            ("Pivot 2", f"{E7['slowest']} slowest at {E7['dth'][E7['slowest']]} days; AVERAGEIFS matches."),
            ("Cost per hire", f"Cheapest {E8['cheapest']} {_money(E8['cph'][E8['cheapest']])}; dearest {E8['dearest']} "
                              f"{_money(E8['cph'][E8['dearest']])}; insights exported to a Google Doc."),
        ],
        test="",
        checkpoint="Lab 8 charts the same data from its own copy of the workbook.",
        troubleshooting=[
            ("No Analysis steps button.",
             "It appears only for answers Gemini calculated from the sheet. Ask for a calculation, e.g. 'count by Month'."),
            ("Gemini counts 721 applications.",
             "It included the header row. Ask it to count data rows only, or check with =COUNTA(Applications!A2:A721)."),
            ("Hire rate differs from yours.",
             "Ask how it defined a hire. It must be Stage = Hired, divided by all applications from that source."),
            ("No action card for the pivot table.",
             "Build it from the menu: select the data > Insert > Pivot table > New sheet, then add Source to Rows, Stage to "
             "Columns and COUNTA of Candidate_ID to Values."),
            ("Export to Docs is missing.",
             "It is shown for analysis responses. Use Copy, then paste into a new Google Doc."),
            ("The web answer has no sources.",
             "Do not use it. Ask again with 'list your sources', or use Retry with Google Search."),
        ],
        challenge="Ask Gemini whether candidates with a higher Screening_Score are more likely to be hired, and check its claim with two AVERAGEIFS.",
        reflection=(f"{E7['best_rate']} has the best hire rate but only {_SRC[E7['best_rate']]['apps']} applications. What "
                    "would you check before telling the business to 'do more' of it?"),
    ),
    # ------------------------------------------------------------------ LAB 8
    dict(
        num=8,
        topic=2,
        title="Build Charts That Tell the Hiring Story",
        theme="Charts & Visualisation",
        duration=30,
        objective=(
            "LO2: generate line, bar, column and combination charts with Gemini, preview and insert them, understand "
            "which charts update with the data, build linked charts and write titles that state the finding"
        ),
        goal=(
            "Turn the 2026 hiring data into four clear charts - trend, sources, funnel, cost per hire - and know which "
            "ones update when the data changes."
        ),
        workflow=["Trend chart", "Source & funnel", "Static vs linked", "Cost chart", "Titles & alt text"],
        desc=(
            "Now you show the findings from Lab 7. You will ask Gemini to create charts - a monthly trend line, hires by "
            "source and the hiring funnel - preview them and insert them. Each inserted chart lands on a new tab with its "
            "own copy of the data, so it does not update when Applications changes. You will prove that, then build a "
            "linked chart from a pivot table that does update. A cost-per-hire chart combines two tabs, and you will "
            "rewrite every title to state its finding and add alt text."
        ),
        build=(
            "OrchidBay_Hiring_Charts with four inserted Gemini charts, one linked chart built from a pivot table, "
            "finding-based titles and alt text"
        ),
        services="Google Sheets · Gemini charts (Preview, Insert, Copy chart) · pivot table · Chart editor · OrchidBay_Hiring_Charts.xlsx",
        data_files=["data/OrchidBay_Hiring_Charts.xlsx"],
        prerequisites=[
            "Lab 7 completed, or its Test It values to hand.",
            "This lab folder downloaded, including data/OrchidBay_Hiring_Charts.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Hiring_Charts.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Hiring_Charts (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Applications (720 rows) | Jobs | Source_Costs | Prompt_Log",
            ),
            (
                "Ask for a trend chart. Click Preview to see it, then Insert. Gemini adds a NEW tab with the chart and the "
                "data behind it - read the message at the bottom left. The line should peak in June "
                f"({E8['by_month']['2026-06']}).",
                "INSERT:\n"
                "Create a line chart with Month on the x-axis and the number of applications on the y-axis.",
            ),
            (
                "Ask for two more charts and insert each. Hires by source, sorted: "
                + ", ".join(f"{s} {_SRC[s]['hires']}" for s in _TOP_HIRE_SRCS[:3]) +
                f" ... Funnel: {E8['funnel']['applications']}, {E8['funnel']['interviewed']}, "
                f"{E8['funnel']['offered']}, {E8['funnel']['hired']}.",
                "INSERT:\n"
                "Make a bar chart of hires (Stage is Hired) by Source, sorted from most to fewest.\n\n"
                "INSERT:\n"
                "Create a column chart of the hiring funnel: Applications (all rows), Interviewed (rows with an\n"
                "Interview_Score), Offered (Stage is Offered or Hired) and Hired.",
            ),
            (
                "Test whether the charts update. On Applications, change the Stage of one LinkedIn row from Rejected to "
                "Hired. Look at the hires-by-source chart: it does NOT change, because it is linked to the copy of the data "
                "on its own tab. Ask Gemini why, then undo your edit (Ctrl + Z / Cmd + Z).",
                "ASK GEMINI:\n"
                "Will the chart you inserted update if I change the Applications tab? How do I make a chart that does?",
            ),
            (
                "Build a linked chart. Ask Gemini for a pivot table, click Apply, then select the pivot table and choose "
                "Insert > Chart and pick a column chart. Repeat the Stage edit from Step 4: the Hired count for that month "
                "goes up by one in the pivot table and in this chart. Undo the edit again.",
                "ACTION:\n"
                "Create a pivot table on a new sheet that counts Candidate_ID with Month in rows and Stage in columns.",
            ),
            (
                "Combine two tabs in one chart. The lowest bar should be "
                f"({_money(E8['cph'][E8['cheapest']])}, {E8['cheapest']}) and {E8['dearest']} the highest "
                f"({_money(E8['cph'][E8['dearest']])}).",
                "INSERT:\n"
                "Using the Applications and Source_Costs tabs, create a column chart of cost per hire by Source, where\n"
                "cost per hire is applications x Cost_Per_Application divided by hires.",
            ),
            (
                "Make every chart say something. Ask for finding-based titles, then double-click each chart > Customize > "
                "Chart & axis titles to apply them. Right-click each chart > Alt text and add one sentence. Optional: More "
                "options > Copy chart in the panel, and paste it into a Google Doc or Slides.",
                "ASK GEMINI:\n"
                "Suggest a title for each chart in this spreadsheet that states the main finding, not just the measure.\n"
                "For example: 'Applications peaked in June'.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini builds a chart from a plain-English description. Preview first; Insert adds it on a new tab with "
            "its own data.",
            "A sorted bar chart - the best chart for comparing categories.",
            "A funnel as a column chart: four stages, each a count Gemini calculates for you.",
            "Asks Gemini to explain why inserted charts are static and how to build one that updates.",
            "Creates a pivot table of Month by Stage from Applications; a chart built from it with Insert > Chart updates "
            "when a Stage changes.",
            "A chart that combines data from two tabs with a calculated measure.",
            "Gemini rewrites chart titles so each one states its finding - a headline, not a label.",
            LOG_EXPLAIN,
        ],
        formulas={},
        sample_prompts=[
            ("Pie", "Create a pie chart of applications by Source."),
            ("Stacked", "Create a stacked column chart of applications by Month, split by Stage."),
            ("Combo", "Create a chart with applications as columns and hires as a line, by Month."),
            ("Help", "What chart type is best to show the share of each source over time?"),
            ("Graph", "Create a graph that shows the percentage of applications that came from each Position."),
        ],
        sample_explain=[
            f"Shows each source's share - LinkedIn is {E8['share_li']}% of applications. Pies suit a few categories only.",
            "Shows totals and the stage mix together.",
            "Two measures on one chart - check that the two axes are labelled.",
            "Gemini as a chart adviser - it explains the trade-offs.",
            "A percentage chart - check the slices add up to 100%.",
        ],
        checks=[
            ("Trend chart", f"Line chart on its own tab; peak June {E8['by_month']['2026-06']}."),
            ("Source and funnel", f"Bars sorted; {_TOP_HIRE_SRCS[0]} {_SRC[_TOP_HIRE_SRCS[0]]['hires']} first. Funnel "
                                  f"{E8['funnel']['applications']} / {E8['funnel']['interviewed']} / "
                                  f"{E8['funnel']['offered']} / {E8['funnel']['hired']}."),
            ("Static vs linked", "Inserted chart did not change after the Stage edit; the Month x Stage pivot chart did."),
            ("Cost per hire", f"{E8['cheapest']} {_money(E8['cph'][E8['cheapest']])} lowest; {E8['dearest']} "
                              f"{_money(E8['cph'][E8['dearest']])} highest."),
            ("Titles and alt text", "Every chart title states a finding; every chart has alt text."),
        ],
        test="",
        checkpoint="Topic 2 ends here. Lab 9 starts the interactive dashboard in its own workbook.",
        troubleshooting=[
            ("No Preview or Insert button.",
             "Ask again with the word 'chart' and the chart type. Make sure you are in the Google Sheets copy."),
            ("The chart counts the header as a month.",
             "Ask Gemini to use data rows only, or edit the data range in the Chart editor."),
            ("Gemini put the chart on a new tab, but you wanted it on Applications.",
             "That is how Insert works. Cut the chart (three dots > Cut) and paste it on another tab, or build it with "
             "Insert > Chart."),
            ("You can't find Copy chart.",
             "In the Gemini panel, open More options (three dots) on the chart response."),
        ],
        challenge="Build a combo chart from the Lab 8 pivot table that shows applications (columns) and hire rate (line on a second axis).",
        reflection="When is a static chart fine, and when must a chart be linked to live data?",
    ),
]
