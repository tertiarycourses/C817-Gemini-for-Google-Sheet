"""Topic 3 labs for C817: Interactive Dashboard - KPIs, interactivity, Gems and safe sharing (Orchid Bay data)."""

from mock_data import EXPECTED, FINALISTS, POS_JOB, _must_have
from data_domain1 import LOG, LOG_EXPLAIN, LOG_STEP, SETUP_STEP

E9, E10, E11, E12 = EXPECTED[9], EXPECTED[10], EXPECTED[11], EXPECTED[12]
_A, _SE, _DL, _CS, _OPS, _HR = E9["all"], E9["se"], E9["da_li"], E10["cs"], E10["ops"], E10["hr"]


def _money(v):
    return f"S${v:,.0f}"


# ---- the screening rubric (mirrors OrchidBay_Screening_Rubric.docx) applied to the finalists
def rubric(r):
    gaps = len(_must_have(r))
    skills = 4 if gaps == 0 else (2 if gaps == 1 else 0)
    diff = r["Years_Experience"] - POS_JOB[r["Position"]][4]
    exp = 0 if diff < 0 else (2 if diff == 0 else (3 if diff <= 2 else 4))
    fi = r["Final_Interview"]
    intv = 4 if fi >= 4.5 else (3 if fi >= 4.0 else (2 if fi >= 3.5 else (1 if fi >= 3.0 else 0)))
    mx = POS_JOB[r["Position"]][7]
    sal = 4 if r["Expected_Salary"] <= mx else (2 if r["Expected_Salary"] <= mx * 1.1 else 0)
    n = r["Notice_Weeks"]
    avail = 4 if n <= 4 else (2 if n <= 8 else 0)
    total = skills + exp + intv + sal + avail
    rec = ("Advance" if total >= 16 and gaps == 0 else "Hold" if total >= 11 else "Decline")
    return dict(skills=skills, exp=exp, intv=intv, sal=sal, avail=avail, total=total, rec=rec, gaps=gaps)


RUB = {r["Candidate_ID"]: rubric(r) for r in FINALISTS}
_DA = [r for r in FINALISTS if r["Position"] == "Data Analyst"]
_T = next(r for r in _DA if _must_have(r))           # the Data Analyst finalist with a must-have gap
_TR = RUB[_T["Candidate_ID"]]
_REC = {k: sum(1 for v in RUB.values() if v["rec"] == k) for k in ("Advance", "Hold", "Decline")}

GEM_INSTRUCTIONS = """PERSONA
You are the Orchid Bay Candidate Screener, a careful and fair recruitment analyst at Orchid Bay Talent Partners, a Singapore recruitment and HR firm.

TASK
Screen candidates for a role against the job description and the screening rubric in your knowledge files, and recommend Advance, Hold or Decline for each one.

CONTEXT
- Use only two sources: the candidate's row (Years_Experience, Key_Skills, Expected_Salary, Budget_Max, Notice_Weeks, Final_Interview_Score, Candidate_Summary) and the job description for the candidate's Position.
- Score each rubric criterion from 0 to 4 exactly as the rubric defines it, then add them up to a total out of 20.
- A must-have skill counts only if it appears in Key_Skills or Candidate_Summary.
- Never use or guess age, gender, race, religion, nationality, marital status or health. Do not treat a name or a school as evidence of ability.
- If information is missing, say "not enough information". Do not guess.
- Your recommendation supports the hiring manager. A person makes the hiring decision.

FORMAT
Return one table with these columns: Candidate_ID, Position, Must-have gaps, Skills, Experience, Interview, Salary fit, Availability, Total /20, Recommendation, Reason (one line, evidence only).
After the table, list any candidate where you were unsure and why.
"""

_TEST_ROW = (f"{_T['Candidate_ID']} | Data Analyst | {_T['Years_Experience']} years | Key_Skills: {_T['Key_Skills']} | "
             f"Expected_Salary {_money(_T['Expected_Salary'])} | Budget_Max {_money(POS_JOB['Data Analyst'][7])} | "
             f"Notice_Weeks {_T['Notice_Weeks']} | Final_Interview_Score {_T['Final_Interview']}")

DOMAIN3 = [
    # ------------------------------------------------------------------ LAB 9
    dict(
        num=9,
        topic=3,
        title="Build the Dashboard's Selectors and KPI Formulas",
        theme="Dashboard KPIs & Selectors",
        duration=30,
        objective=(
            "LO3: use Gemini to add dropdown selectors and generate the COUNTIFS and AVERAGEIFS formulas that drive a "
            "dashboard's KPIs and summary tables, and test that every KPI responds correctly to the selectors"
        ),
        goal=(
            "Build the formula layer of an interactive hiring dashboard: two dropdowns (Position, Source) that drive seven KPIs "
            "and three summary tables."
        ),
        workflow=["Selectors", "Count KPIs", "Rate & average KPIs", "Summary tables", "Test the filters"],
        desc=(
            "The Head of Talent wants one page that answers 'how is hiring going?' for any role and any source. You will "
            "turn two cells into dropdown selectors, then ask Gemini for the formulas: COUNTIFS that treat 'All' as "
            "'every value', a hire rate, AVERAGEIFS for screening score and days to hire, and the funnel, monthly and "
            "source tables that the charts in Lab 10 will use. Every KPI is a formula, never a typed number, so it "
            "changes when the selectors change - and you test that it does."
        ),
        build=(
            "OrchidBay_Dashboard_Build with Position and Source dropdowns in C3:C4, a KPI row (B7:H7) and funnel, monthly "
            "and source tables that all respond to the dropdowns"
        ),
        services="Google Sheets · Gemini dropdown actions and formula generation (COUNTIFS, AVERAGEIFS, IFERROR) · OrchidBay_Dashboard_Build.xlsx",
        data_files=["data/OrchidBay_Dashboard_Build.xlsx"],
        prerequisites=[
            "Lab 4 (formulas) and Lab 7 (analysis) completed, or comfort with COUNTIFS.",
            "This lab folder downloaded, including data/OrchidBay_Dashboard_Build.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Dashboard_Build.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Dashboard_Build (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Dashboard | Applications (720 rows) | Jobs | Lists | Prompt_Log\n"
                "Dashboard : C3 Position, C4 Source, KPI labels B6:H6, tables at B10, E10 and I10",
            ),
            (
                "Turn the two yellow cells into selectors, one action at a time. Then set both to All.",
                "ACTION:\n"
                "1) On the Dashboard tab, create a dropdown in C3 with the values from Lists!A2:A10.\n"
                "2) On the Dashboard tab, create a dropdown in C4 with the values from Lists!B2:B9.",
            ),
            (
                "Click B7 and ask for the core formula. The trick is that 'All' must mean 'any value' - Gemini usually "
                f"replaces it with the wildcard \"*\". Insert it: with All / All, B7 must show {_A['apps']}.",
                "FORMULA:\n"
                "Create a formula for Dashboard!B7 that counts the rows on Applications (rows 2-721) where Position in\n"
                "column F equals C3 and Source in column G equals C4. If C3 or C4 is \"All\", count every value for\n"
                "that column.",
            ),
            (
                "Ask for the next three KPIs one at a time, clicking the target cell before each Insert. Expect "
                f"Interviews {_A['interviews']}, Offers {_A['offers']} and Hires {_A['hires']}.",
                "FORMULA:\n"
                "1) Create a formula for C7: the same count as B7, but only rows where Interview_Score (column L) is not blank.\n"
                "2) Create a formula for D7: the same count as B7, but only rows where Stage (column M) is Offered or Hired.\n"
                "3) Create a formula for E7: the same count as B7, but only rows where Stage (column M) is Hired.",
            ),
            (
                "Now the rate and averages. Format F7 as a percentage and G7:H7 with one decimal place. With All / All: "
                f"hire rate {_A['rate']}%, average screening score {_A['score']}, average days to hire {_A['dth']}.",
                "FORMULA:\n"
                "1) Create a formula for F7 that divides Hires in E7 by Applications in B7, showing 0 if B7 is 0.\n"
                "2) Create a formula for G7: the average Screening_Score (column K) for the rows that match C3 and C4.\n"
                "3) Create a formula for H7: the average Days_To_Hire (column P) for Hired rows that match C3 and C4, showing \"-\" if there are none.",
            ),
            (
                "Fill the tables the charts will use. The funnel just points at the KPIs. For the monthly table, insert "
                "the formulas in F11 and G11, then fill down to row 19. For the source table, insert J11 and fill down to "
                f"J17. With All / All, June (F16) = {_A['by_month']['2026-06'][0]} and LinkedIn hires (J11) = "
                f"{_A['by_source']['LinkedIn']}.",
                "ACTION:\n"
                "Fill Dashboard!C11:C14 with the formulas =B7, =C7, =D7 and =E7.\n\n"
                "FORMULA:\n"
                "1) Create a formula for F11 that counts applications where Month (Applications column D) equals E11, using the same Position and Source filters as B7.\n"
                "2) Create a formula for G11: the same as F11 but only Hired rows.\n"
                "3) Create a formula for J11 that counts Hired rows where Source equals I11 and Position matches C3 (All means any).",
            ),
            (
                "Test the selectors. Set C3 to Software Engineer (C4 All): Applications "
                f"{_SE['apps']}, Hires {_SE['hires']}, hire rate {_SE['rate']}%. Set C3 to Data Analyst and C4 to "
                f"LinkedIn: {_DL['apps']} applications and {_DL['hires']} hires, and H7 shows '-' instead of an error. Ask "
                "Gemini to check one view, and confirm with the formula.",
                "ASK GEMINI:\n"
                "On the Dashboard tab, Position is set in C3. Check the KPI row B7:H7 against the Applications tab - are\n"
                "the counts and averages correct for that position?\n\n"
                "CHECK:\n"
                "SE hires   =COUNTIFS(Applications!F2:F721,\"Software Engineer\",Applications!M2:M721,\"Hired\")",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "A dropdown action whose options come from a range - the Position list, starting with All.",
            "A second selector for Source.",
            "Gemini writes a COUNTIFS that uses IF($C$3=\"All\",\"*\",$C$3): when the selector says All, the wildcard * "
            "matches every value.",
            "The same COUNTIFS with an extra condition: Interview_Score is not blank (\"<>\").",
            "Offers = Offered + Hired: two COUNTIFS added together, because COUNTIFS has no OR.",
            "Hires = the same COUNTIFS with Stage = Hired.",
            "A rate with IFERROR, so an empty selection shows 0 instead of #DIV/0!.",
            "AVERAGEIFS takes the column to average, then (range, criterion) pairs - the same filters as the counts.",
            "The average days to hire for hired candidates only, with \"-\" when there are no hires.",
            "A fill-range action that links the funnel table to the KPI cells.",
            "A COUNTIFS that adds a third condition - Month equals the month in column E - so one formula fills nine rows.",
            "The same as the monthly count, but for hires only.",
            "Hires per source, filtered by Position only, so the source chart can compare all sources.",
            "Gemini checks the dashboard against the raw data; the COUNTIFS confirms it independently.",
            LOG_EXPLAIN,
        ],
        formulas={
            "C": ("The formula Gemini should write", [
                ('=COUNTIFS(Applications!$F$2:$F$721,IF($C$3="All","*",$C$3),Applications!$G$2:$G$721,IF($C$4="All","*",$C$4))',
                 "COUNTIFS counts rows that meet every (range, criterion) pair. IF swaps 'All' for \"*\", a wildcard "
                 "that matches any text. $ locks the ranges and the selector cells so the formula can be copied."),
            ]),
            "H": ("The formula Gemini should write", [
                ('=IFERROR(AVERAGEIFS(Applications!$K$2:$K$721,Applications!$F$2:$F$721,IF($C$3="All","*",$C$3),Applications!$G$2:$G$721,IF($C$4="All","*",$C$4)),0)',
                 "AVERAGEIFS(average range, criteria range 1, criterion 1, ...). IFERROR shows 0 if no rows match."),
            ]),
            "K": ("The formula Gemini should write", [
                ('=COUNTIFS(Applications!$F$2:$F$721,IF($C$3="All","*",$C$3),Applications!$G$2:$G$721,IF($C$4="All","*",$C$4),Applications!$D$2:$D$721,E11)',
                 "E11 has no $, so it becomes E12, E13 ... as you fill down - one formula for every month."),
            ]),
        },
        sample_prompts=[
            ("KPI", "Create a formula for the offer acceptance rate: Hired divided by Offered plus Hired, for the selected Position and Source."),
            ("KPI", "Create a formula that returns the most common Source for the selected Position."),
            ("Selector", "Create a dropdown in C5 with the values 2026-01 to 2026-09."),
            ("Explain", "Explain the formula in B7 to someone who has never used COUNTIFS."),
            ("Check", "Which formulas on the Dashboard tab would break if a new Position were added?"),
        ],
        sample_explain=[
            "A ratio KPI built from two COUNTIFS - check it on one position by hand.",
            "Gemini may use INDEX/MATCH or QUERY; verify with the Lab 7 source table.",
            "A third selector you could add to the COUNTIFS criteria.",
            "A plain-language explanation for a colleague who will maintain the dashboard.",
            "Gemini reviews the dashboard's robustness - the Lists ranges are fixed-size.",
        ],
        checks=[
            ("Selectors", "C3 lists All + 8 positions; C4 lists All + 7 sources."),
            ("All / All", f"B7:H7 = {_A['apps']}, {_A['interviews']}, {_A['offers']}, {_A['hires']}, {_A['rate']}%, "
                          f"{_A['score']}, {_A['dth']}."),
            ("Tables", f"Funnel {_A['apps']}/{_A['interviews']}/{_A['offers']}/{_A['hires']}; June applications "
                       f"{_A['by_month']['2026-06'][0]}; LinkedIn hires {_A['by_source']['LinkedIn']}."),
            ("Software Engineer", f"{_SE['apps']} applications, {_SE['hires']} hires, {_SE['rate']}%; the COUNTIFS check "
                                  f"shows {_SE['hires']}."),
            ("Data Analyst + LinkedIn", f"{_DL['apps']} applications, {_DL['hires']} hires; H7 shows '-' (no error)."),
        ],
        test="",
        checkpoint=(
            "Lab 10 provides these finished KPI formulas in its own workbook, so you can continue even if a formula "
            "here is not working."
        ),
        troubleshooting=[
            ("B7 shows 0 with All / All.",
             "The formula is comparing to the text 'All'. Ask Gemini: 'when C3 is All, use the wildcard \"*\"'."),
            ("Numbers are right for All but wrong for one position.",
             "Check the selector spelling matches Applications exactly - pick from the dropdown, do not type."),
            ("No dropdown action, or Gemini's formula doesn't insert.",
             "Dropdown: select C3 > Insert > Dropdown > 'Dropdown (from a range)' > Lists!A2:A10. Formulas: copy the "
             "formula shown under 'The formula Gemini should write' on the prompts page and adapt the condition."),
            ("#DIV/0! in F7 or H7.",
             "Wrap the formula in IFERROR - ask Gemini to 'show 0 (or -) instead of an error'."),
            ("Filling down F11 changes C3 to C4.",
             "The selector references need $ ($C$3, $C$4). Ask Gemini to make them absolute."),
        ],
        challenge="Add an Offer acceptance KPI (Hired / (Offered + Hired)) in I7 and test it for Customer Success Executive.",
        reflection="Why must every KPI on a dashboard be a formula rather than a number Gemini told you?",
    ),
    # ------------------------------------------------------------------ LAB 10
    dict(
        num=10,
        topic=3,
        title="Make the Hiring Dashboard Interactive and Visual",
        theme="Interactive Dashboard",
        duration=30,
        objective=(
            "LO3: turn the KPI formulas into an interactive, visual dashboard - linked charts, a metric switch, "
            "conditional-formatting alerts, protection and a Gemini summary exported to Google Docs"
        ),
        goal=(
            "Finish a one-page hiring dashboard whose charts, alerts and KPIs all respond to the dropdowns - and prove "
            "it with three test views."
        ),
        workflow=["Linked charts", "Test views", "Metric switch", "KPI alerts", "Polish & summarise"],
        desc=(
            "The KPI formulas from Lab 9 are ready: dropdowns in C3:C4 drive the KPIs and three tables. You will add charts that "
            "are linked to those tables (unlike Gemini-inserted charts, which are static copies), so they redraw when a "
            "dropdown changes. A third dropdown switches the monthly chart between Applications and Hires, and "
            "conditional-formatting alerts flag a low hire rate and a slow time to hire. You will hide the gridlines, "
            "protect the formulas, and ask Gemini to summarise the dashboard for the Head of Talent."
        ),
        build=(
            "OrchidBay_Dashboard_Interactive: a protected Dashboard tab with three linked charts, a metric switch, KPI "
            "alerts and a Gemini summary exported to Google Docs"
        ),
        services="Google Sheets · Insert > Chart (linked) · Gemini actions (dropdown, conditional formatting) and formulas · Export to Docs · OrchidBay_Dashboard_Interactive.xlsx",
        data_files=["data/OrchidBay_Dashboard_Interactive.xlsx"],
        prerequisites=[
            "Lab 9 completed, or its Test It values to hand.",
            "This lab folder downloaded, including data/OrchidBay_Dashboard_Interactive.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Dashboard_Interactive.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Dashboard_Interactive (Google Sheets copy)\n"
                "Dashboard : C3 Position and C4 Source dropdowns (All) | KPIs B7:H7 | tables B10, E10, I10\n"
                f"Check     : B7 = {_A['apps']} and E7 = {_A['hires']} with All / All",
            ),
            (
                "Ask Gemini how to make charts that update, then build three yourself: select E10:G19 > Insert > Chart > "
                "Line chart; select B10:C14 > Insert > Chart > Bar chart; select I10:J17 > Insert > Chart > Column chart. "
                "Drag them into a grid below the tables.",
                "ASK GEMINI:\n"
                "How do I insert a chart from a range on this tab so that it updates when the values in the range change?",
            ),
            (
                "Test interactivity. Set C3 to Customer Success Executive: the KPIs show "
                f"{_CS['apps']} applications and {_CS['hires']} hires, and all three charts redraw. Set C4 to Referral, "
                "then put both back to All.",
                "",
            ),
            (
                "Add a metric switch. Type Show in B5 and apply the dropdown action. Type =\"Monthly \"&C5 in H10, insert "
                "Gemini's formula in H11 and fill it down to H19. Then edit the line chart (double-click > Setup > Data "
                "range) to use E10:E19 and H10:H19. Switching C5 to Hires now redraws the line.",
                "ACTION:\n"
                "Create a dropdown in Dashboard!C5 with the options Applications and Hires.\n\n"
                "FORMULA:\n"
                "Create a formula for H11 that returns F11 when C5 is \"Applications\" and G11 when C5 is \"Hires\".",
            ),
            (
                "Add alerts, one action at a time. Test them: Operations Supervisor turns F7 red "
                f"({_OPS['rate']}%); HR Executive turns F7 red ({_HR['rate']}%) and H7 amber ({_HR['dth']} days).",
                "ACTION:\n"
                "1) Highlight Dashboard!F7 in light red when it is below 5%.\n"
                "2) Highlight Dashboard!H7 in amber when it is more than 35.\n"
                "3) Add a white-to-green colour scale to Dashboard!J11:J17.",
            ),
            (
                "Polish it yourself: View > Show > untick Gridlines; right-click the Lists tab > Hide sheet; Data > Protect "
                "sheets and ranges > protect the Dashboard tab except C3:C5, so viewers can use the dropdowns but cannot "
                "break the formulas. Then set C3 and C4 back to All and ask Gemini for a summary. Check its numbers against "
                "B7:H7, then click Export to Docs.",
                "ASK GEMINI:\n"
                "Summarise what the Dashboard tab shows in five bullet points for the Head of Talent, using the KPI row\n"
                "and the three tables. Mention the best month, the best source for hires and one risk.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Gemini explains the difference between its static inserted charts and Insert > Chart on a live range.",
            "A dropdown action for the metric switch.",
            "Gemini writes an IF that picks one of two columns, so a single chart can show either measure.",
            "A conditional-formatting alert on a KPI cell: below 5% hire rate turns red.",
            "A second alert: more than 35 days to hire turns amber.",
            "A colour scale on the source table - the darker the green, the more hires.",
            "Gemini reads the dashboard and drafts a manager summary; check each number before you export it to Docs.",
            LOG_EXPLAIN,
        ],
        formulas={
            "C": ("The formula Gemini should write", [
                ('=IF($C$5="Hires",G11,F11)',
                 "If the switch says Hires, show the hires count; otherwise show applications. $C$5 stays fixed as you "
                 "fill down; G11 and F11 move with each row."),
            ]),
        },
        sample_prompts=[
            ("Image", "Create an image of a simple header banner with an orchid and the words Hiring Dashboard."),
            ("Layout", "Suggest a clean layout for this dashboard: where should the KPIs, charts and selectors go?"),
            ("Alert", "Highlight the Hires cells in the monthly table that are 0 in light grey."),
            ("Number format", "Format F7 as a percentage with one decimal place and G7:H7 with one decimal place."),
            ("Review", "Review this dashboard for a colleague: what is unclear, and what would you add?"),
        ],
        sample_explain=[
            "Gemini generates an image; Insert image places it on the sheet. Keep branding simple and fictional.",
            "Gemini as a design adviser - you decide what to apply.",
            "Another conditional-formatting rule for empty months.",
            "A set-number-format action for the KPI row.",
            "A critique from Gemini - a quick usability check before you share.",
        ],
        checks=[
            ("Linked charts", "Three charts built with Insert > Chart from E10:G19 (or E10:E19 + H10:H19), B10:C14 and I10:J17."),
            ("Customer Success Executive", f"{_CS['apps']} applications, {_CS['hires']} hires, {_CS['rate']}%; all charts redraw."),
            ("Metric switch", "C5 = Hires changes the line chart and the H10 header to 'Monthly Hires'."),
            ("Alerts", f"Operations Supervisor: F7 red ({_OPS['rate']}%). HR Executive: F7 red ({_HR['rate']}%), H7 amber "
                       f"({_HR['dth']})."),
            ("Polish", "No gridlines, Lists hidden, Dashboard protected except C3:C5; summary exported to Docs."),
        ],
        test="",
        checkpoint="Lab 11 moves to the final decision: 16 finalists for four roles, screened with a Gem.",
        troubleshooting=[
            ("The chart doesn't change when you change C3.",
             "It was inserted from the Gemini panel (a static copy) or from the wrong range. Delete it and use Insert > "
             "Chart on the Dashboard table."),
            ("The line chart shows Applications and Hires together.",
             "Edit the data range to E10:E19 and H10:H19 only."),
            ("The F7 alert never turns red.",
             "F7 holds a fraction (0.043), not 4.3. The rule must be 'less than 0.05' - open Settings or Format > "
             "Conditional formatting to check."),
            ("Viewers can't use the dropdowns after protection.",
             "In Protect sheets and ranges, tick 'Except certain cells' and add C3:C5."),
        ],
        challenge="Add a 'Data as at' note in A2 that comes from a formula (e.g. =\"Data as at \"&TEXT(MAX(Applications!C2:C721),\"yyyy-mm-dd\")).",
        reflection="Which three people would use this dashboard, and what would each of them need protected or hidden?",
    ),
    # ------------------------------------------------------------------ LAB 11
    dict(
        num=11,
        topic=3,
        title="Create a Candidate Screener Gem and Use It in Sheets",
        theme="Gems",
        duration=30,
        objective=(
            "LO3: create a custom Gem with instructions and knowledge files, use it from the Gemini side panel in Sheets "
            "to screen candidates consistently, and check its output for accuracy and fairness"
        ),
        goal=(
            "Build a reusable Candidate Screener Gem that scores finalists against Orchid Bay's rubric the same way every "
            "time - and check it against the data."
        ),
        workflow=["Write instructions", "Add knowledge", "Test the Gem", "Screen in Sheets", "Check & decide"],
        desc=(
            "Screening 16 finalists by hand takes the recruiters a day, and every recruiter scores a little differently. "
            "You will create a Gem - a custom Gemini with saved instructions - in the Gemini app. Its instructions follow "
            "the Persona, Task, Context and Format pattern; its knowledge is the job descriptions and the screening "
            "rubric from Google Drive. You will test it on one candidate, open it from the Gems list in the Sheets side "
            "panel, screen all four roles, insert the results, check them against the data and record the human decision."
        ),
        build=(
            "An 'Orchid Bay Candidate Screener' Gem with instructions and two knowledge files, and OrchidBay_Finalists "
            "with a Gem_Screening tab, checks and a Hiring_Manager_Decision dropdown"
        ),
        services="Gemini app (gemini.google.com) · Gems · Google Drive · Google Sheets Gemini side panel (Gems) · OrchidBay_Finalists.xlsx",
        data_files=["data/OrchidBay_Finalists.xlsx", "data/gem-knowledge/OrchidBay_Job_Descriptions.docx",
                    "data/gem-knowledge/OrchidBay_Screening_Rubric.docx"],
        extra_files=[("gem-instructions.txt", GEM_INSTRUCTIONS, "the Gem instructions to paste")],
        prerequisites=[
            "Gems available on your account (gemini.google.com > Gems). Gems are not available in every language.",
            "This lab folder downloaded: data/OrchidBay_Finalists.xlsx, the two .docx files in data/gem-knowledge/ and "
            "gem-instructions.txt.",
        ],
        steps=[
            (
                "Upload OrchidBay_Finalists.xlsx and the two .docx files in data/gem-knowledge/ to Google Drive. Open the "
                "workbook and choose File > Save as Google Sheets. Open each .docx and choose File > Save as Google Docs, "
                "so the Gem can read them as Docs.",
                "Required state:\n"
                "Drive     : OrchidBay_Finalists (Sheets) | OrchidBay_Job_Descriptions (Docs) | OrchidBay_Screening_Rubric (Docs)\n"
                f"Finalists : {E11['n']} rows - four each for {', '.join(E11['roles'])}",
            ),
            (
                "In a new browser tab go to gemini.google.com > Gems (in the left menu, or Explore Gems) > New Gem. Name "
                "it Orchid Bay Candidate Screener. Paste the instructions below (also in gem-instructions.txt) into "
                "Instructions. Under Knowledge, click Add files and choose the two Google Docs from Drive.",
                "GEMINI APP:\n" + GEM_INSTRUCTIONS.strip(),
            ),
            (
                "Test the Gem in the preview panel on the right before saving. Paste this one candidate. A correct "
                f"answer finds the missing must-have skill ({', '.join(_must_have(_T))}) and scores "
                f"{_TR['total']}/20 - Skills {_TR['skills']}, Experience {_TR['exp']}, Interview {_TR['intv']}, Salary "
                f"{_TR['sal']}, Availability {_TR['avail']} - so it recommends {_TR['rec']}. If it is wrong, improve the "
                "instructions and test again. Then click Save.",
                "GEMINI APP:\n"
                "Screen this candidate for the Data Analyst role:\n" + _TEST_ROW,
            ),
            (
                "Go back to OrchidBay_Finalists in Sheets. Open the Gemini side panel, click Gems and choose Orchid Bay "
                "Candidate Screener (reload the sheet if it isn't listed yet). Screen the first role and click Insert, "
                "putting the table on a new tab named Gem_Screening.",
                "GEM:\n"
                "Screen the four Data Analyst finalists on the Finalists tab using the rubric. Identify candidates by\n"
                "Candidate_ID only and ignore Full_Name. Return the table in your standard format.",
            ),
            (
                "Screen the other three roles. Insert adds each table on a new tab - keep them, or use Copy and paste each "
                "one onto Gem_Screening below the Data Analyst table, leaving a blank row between tables.",
                "GEM:\n"
                "Now screen the Software Engineer, Customer Success Executive and Finance Associate finalists in the\n"
                "same format.",
            ),
            (
                "Check the Gem against the data. Must-have gaps should be exactly: "
                + "; ".join(f"{k} ({', '.join(v)})" for k, v in E11["gaps"].items()) +
                f". Above budget: {', '.join(E11['over_budget'])}. Applying the rubric exactly gives "
                f"{_REC['Advance']} Advance, {_REC['Hold']} Hold and {_REC['Decline']} Decline. Paste the check and "
                "list any row where the Gem differs - then ask the Gem about its evidence.",
                "CHECK:\n"
                "Above budget   =SUMPRODUCT(--(Finalists!F2:F17>Finalists!G2:G17))\n\n"
                "GEM:\n"
                "For each recommendation, which pieces of information did you use? Did you use anything other than\n"
                "skills, experience, interview score, salary and notice period?",
            ),
            (
                "Record the human decision - the Gem only recommends. Apply the action, then choose a decision for the "
                "Data Analyst rows yourself.",
                "ACTION:\n"
                "Add a column called Hiring_Manager_Decision at the end of the Data Analyst table on the Gem_Screening\n"
                "tab, with a dropdown of Advance, Hold and Decline.",
            ),
            (LOG_STEP, LOG),
        ],
        explain=[
            "Creates the Gem's saved instructions in the Gemini app: Persona, Task, Context (rules and fairness) and "
            "Format. Every chat with the Gem starts from them.",
            "Tests the Gem on one known candidate before you save it - compare its scores with the rubric by hand.",
            "Uses your Gem from the Sheets side panel: it reads the Finalists tab and applies the rubric from its "
            "knowledge files.",
            "Reuses the same instructions for three more roles - consistency without repeating the rubric.",
            "Asks the Gem to show its evidence - a transparency and fairness check.",
            "A dropdown action for the decision the hiring manager owns.",
            LOG_EXPLAIN,
        ],
        formulas={},
        sample_prompts=[
            ("Gem", "Write three interview questions for the weakest rubric area of each Advance candidate."),
            ("Gem", "Rank the Software Engineer finalists by Total and explain the ranking in one sentence each."),
            ("Gem", "Draft a polite email to a candidate you recommend we Decline, without giving scores."),
            ("Gemini app", "Improve my Gem instructions so the Reason column always quotes the evidence."),
            ("Side panel", "What are the main points of OrchidBay_Screening_Rubric?"),
        ],
        sample_explain=[
            "The Gem builds on its own screening to prepare the next interview.",
            "A ranked shortlist with reasons - check that the ranks follow the totals.",
            "The Gem drafts candidate communication; a person reviews it before sending.",
            "Gemini helps you improve the Gem itself.",
            "Gemini summarises a Drive file by name; expand Sources to see which file it used.",
        ],
        checks=[
            ("Gem", "Saved as 'Orchid Bay Candidate Screener' with instructions and both knowledge files."),
            ("Test candidate", f"{_T['Candidate_ID']}: gap {', '.join(_must_have(_T))}; {_TR['total']}/20; {_TR['rec']}."),
            ("Must-have gaps", "; ".join(f"{k} ({', '.join(v)})" for k, v in E11["gaps"].items()) + "."),
            ("Salary check", f"Above-budget formula = {len(E11['over_budget'])} ({', '.join(E11['over_budget'])})."),
            ("Decisions", f"Rubric applied exactly: {_REC['Advance']} Advance / {_REC['Hold']} Hold / {_REC['Decline']} "
                          "Decline; Hiring_Manager_Decision dropdown added and filled by you."),
        ],
        test="",
        checkpoint="Lab 12 uses the same 16 finalists to choose the hires within the client's budget.",
        troubleshooting=[
            ("The Gem isn't listed in the Sheets side panel.",
             "Reload the sheet. If Gems are not available in the side panel on your account, use the Gem at "
             "gemini.google.com and paste only the screening columns - Candidate_ID and C1:L17, never Full_Name - into "
             "the chat."),
            ("The Gem can't find the rubric.",
             "Check that both files were added under Knowledge and are Google Docs you can open."),
            ("The scores don't follow the rubric.",
             "Add to the instructions: 'Show the evidence for each criterion score before the total.' Test again."),
            ("The Gem mentions a candidate's background or school.",
             "That breaks the fair-screening rules. Strengthen the Context section and report it with the thumbs-down."),
        ],
        challenge="Create a second Gem, 'Orchid Bay Interview Planner', that turns a Gem_Screening row into a 30-minute structured interview plan.",
        reflection="What makes a Gem more consistent than typing the same long prompt each time - and what does it not fix?",
    ),
    # ------------------------------------------------------------------ LAB 12
    dict(
        num=12,
        topic=3,
        title="Optimise the Hiring Decision and Share Results Safely",
        theme="Optimisation, Reporting & Safe Sharing",
        duration=30,
        objective=(
            "LO3: use Gemini's optimisation problem solver to choose hires under constraints, verify the solution with "
            "formulas, export a recommendation to Google Docs, use Drive files as context and share HR results "
            "responsibly"
        ),
        goal=(
            "Choose the eight hires that give the highest total Weighted_Score within the client's salary budget, "
            "prove the answer, and share only what the client needs."
        ),
        workflow=["Optimise", "Compare", "Verify", "Recommend", "Share safely"],
        desc=(
            "The client wants eight hires - two for each of four roles - and one total monthly salary budget of "
            f"{_money(E12['budget'])}. Picking the top two in each role costs {_money(E12['unc_salary'])}, which is over "
            "budget. You will describe the problem to Gemini's optimisation solver, compare its answer with the "
            "no-budget choice, tick the selected candidates and prove the totals with formulas. Then you will export a "
            "recommendation to Google Docs, use a Drive file as context, build a minimal Share_View tab and share it "
            "safely."
        ),
        build=(
            "OrchidBay_Hiring_Decision with a Selected checkbox column, check formulas that prove the constraints, a "
            "recommendation in Google Docs and a separate Share_View file shared view-only"
        ),
        services="Google Sheets · Gemini optimisation problem solver · Export to Docs · Drive files as context · sharing · OrchidBay_Hiring_Decision.xlsx",
        data_files=["data/OrchidBay_Hiring_Decision.xlsx"],
        prerequisites=[
            "Lab 11 completed (the rubric Doc is in your Drive), or upload OrchidBay_Screening_Rubric.docx from the Lab 11 folder.",
            "This lab folder downloaded, including data/OrchidBay_Hiring_Decision.xlsx.",
        ],
        steps=[
            (
                SETUP_STEP.format(file="OrchidBay_Hiring_Decision.xlsx"),
                "Required state:\n"
                "File      : OrchidBay_Hiring_Decision (Google Sheets copy)\n"
                "Tabs      : About_This_Data | Finalists (16 rows) | Constraints | Prompt_Log\n"
                f"Budget    : Constraints!B8 = {_money(E12['budget'])} per month for {E12['total_openings']} hires",
            ),
            (
                "Describe the optimisation problem in plain English: the goal, what can change, and the limits. Gemini's "
                "optimisation solver works out the best combination. Note the candidates it picks, their total "
                "Weighted_Score and total salary - you prove them in Step 4 and compare them with Test It.",
                "ASK GEMINI:\n"
                "I need to choose hires from the Finalists tab. Maximise the total Weighted_Score. Hire exactly the\n"
                "number of Openings for each Position on the Constraints tab, and keep the total Expected_Salary of\n"
                "everyone hired at or below the budget in Constraints!B8. Which candidates should I hire?",
            ),
            (
                "Compare with the obvious choice. Without the budget, the top two per role cost "
                f"{_money(E12['unc_salary'])} - over the {_money(E12['budget'])} budget - so something has to give. "
                "Ask Gemini what it traded and how many points that cost. Note: the optimiser uses Weighted_Score only; "
                "remove anyone your Lab 11 review marked Decline before you rely on it.",
                "ASK GEMINI:\n"
                "If there were no budget limit, which candidates would you pick, what would they cost, and what is\n"
                "the trade-off compared with your answer?",
            ),
            (
                "Add the checkbox column with an action, then tick the eight recommended candidates yourself. Paste the "
                "checks into Constraints D2:D7 - they must show the budget is met and two hires per role.",
                "ACTION:\n"
                "Add a checkbox column called Selected at the end of the table on the Finalists tab, unchecked by default.\n\n"
                "CHECK:\n"
                "Total salary     =SUMIFS(Finalists!F2:F17,Finalists!M2:M17,TRUE)\n"
                "Total score      =SUMIFS(Finalists!K2:K17,Finalists!M2:M17,TRUE)\n"
                "Within budget    =SUMIFS(Finalists!F2:F17,Finalists!M2:M17,TRUE)<=Constraints!B8\n"
                "Data Analysts    =COUNTIFS(Finalists!C2:C17,\"Data Analyst\",Finalists!M2:M17,TRUE)\n"
                "All hires        =COUNTIF(Finalists!M2:M17,TRUE)",
            ),
            (
                "Draft the recommendation, check every number against your formulas, then click Export to Docs. Next, "
                "use a Drive file as context - expand Sources under the answer to confirm which file Gemini used.",
                "ASK GEMINI:\n"
                "Write a hiring recommendation for the client in under 200 words: the eight recommended hires by role,\n"
                "the total salary against the budget, the one trade-off made because of the budget, and the risks to\n"
                "check (notice periods and any must-have gaps).\n\n"
                "ASK GEMINI:\n"
                "What are the main points of OrchidBay_Screening_Rubric? Does my recommendation follow its fair\n"
                "screening rules?",
            ),
            (
                "Share only what the client needs. Ask Gemini which columns are personal data the client doesn't need, "
                "then create a minimal view. Do not share this workbook - it still holds names and summaries. Instead "
                "right-click the Share_View tab > Copy to > New spreadsheet, open the new file, and share only that file "
                "with your trainer as Viewer. Watch for the warning that content may be visible outside your domain.",
                "ASK GEMINI:\n"
                "Before I share this spreadsheet with the client, which columns contain personal data they don't need\n"
                "to see?\n\n"
                "ACTION:\n"
                "Create a new tab called Share_View with only Candidate_ID, Position, Weighted_Score and Selected for\n"
                "the rows where Selected is checked.",
            ),
            (LOG_STEP, LOG),
            (
                "Close the loop: give feedback on one helpful and one unhelpful answer with the thumbs up or down. Then, "
                "after Prompt_Log is complete, open More options > Clear history to remove the side-panel conversation.",
                "",
            ),
        ],
        explain=[
            "The optimisation problem solver: an objective (maximise score), decisions (who to hire) and constraints "
            "(openings per role, one budget).",
            "A what-if comparison that shows the cost of the budget constraint - the trade-off a manager needs to see.",
            "A checkbox action. You tick the selections, so the person - not Gemini - records the decision.",
            "Gemini drafts a client recommendation from the sheet; Export to Docs turns it into a Google Doc.",
            "Uses a Google Drive file as context by name, and checks the recommendation against its rules.",
            "Gemini reviews the sheet for data minimisation before sharing.",
            "Creates a minimal tab with only the fields the client needs.",
            LOG_EXPLAIN,
        ],
        formulas={},
        sample_prompts=[
            ("Optimise", "What is the highest total Weighted_Score possible if the budget is reduced by S$2,000?"),
            ("Optimise", "Schedule the eight final interviews across Monday and Tuesday so no interviewer has more than three in a row."),
            ("Docs", "Turn the recommendation into a one-page memo with a table of hires and start dates."),
            ("Gmail", "Catch me up on the latest emails about the Q3 hiring drive."),
            ("Share", "Which tabs in this spreadsheet would be risky to share outside Orchid Bay, and why?"),
        ],
        sample_explain=[
            "A sensitivity test: re-run the optimisation with a tighter budget.",
            "A scheduling problem - another kind of optimisation.",
            "Reformats the recommendation for a client audience.",
            "Gemini can reference your Gmail (if enabled) - check the Sources it lists.",
            "A data-sharing review before you click Share.",
        ],
        checks=[
            ("Optimum", f"{', '.join(E12['picks'])}."),
            ("Totals", f"Total score {E12['score']}; total salary {_money(E12['salary'])} (budget {_money(E12['budget'])}); "
                       "Within budget = TRUE."),
            ("Per role", "Two Selected per role; All hires = 8."),
            ("No-budget comparison", f"{E12['unc_score']} for {_money(E12['unc_salary'])}; swap "
                                     f"{', '.join(E12['swapped_out'])} -> {', '.join(E12['swapped_in'])}."),
            ("Share safely", "Recommendation exported to Docs; Share_View has 4 columns and 8 candidate rows (plus a "
                             "header); only the copied Share_View file is shared, as Viewer."),
        ],
        test="",
        checkpoint="This is the final lab. Your Drive now holds the full Orchid Bay workflow from raw export to decision.",
        troubleshooting=[
            ("Gemini answers without solving - it just picks the top scores.",
             "Restate the constraints as rules ('exactly 2 per Position', 'total salary at or below S$...'), or ask: "
             "'Use the optimisation solver.' The solver may not be available on every plan - then check the answer with "
             "the CHECK formulas."),
            ("Gemini's answer breaks the budget.",
             "Tick its picks and look at Within budget - it will show FALSE. Tell Gemini the total and ask again."),
            ("The SUMIFS show 0.",
             "The Selected column is not M, or the boxes are not ticked. Check the column letter in the formula."),
            ("No optimisation solver on your plan.",
             "Find it by hand: ask Gemini to 'list every pair of candidates for each Position with their combined "
             "Weighted_Score and Expected_Salary'. Start from the top pair in each role and swap the pair that loses the "
             "fewest points per S$ saved until the total salary fits the budget."),
            ("Gemini can't find the rubric file.",
             "Upload OrchidBay_Screening_Rubric.docx from the Lab 11 folder to Drive and save it as a Google Doc."),
        ],
        challenge="Ask Gemini for the best selection if the client adds a third Data Analyst opening and S$5,000 to the budget. Prove it with the checks.",
        reflection="The optimiser maximised a score. What does the score NOT capture that a hiring manager must still judge?",
    ),
]
