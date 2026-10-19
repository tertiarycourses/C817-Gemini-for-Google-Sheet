# Gemini for Google Sheet

Use Gemini in Google Sheets to check, prepare and analyse data, write formulas, build tracker tables, charts and an interactive dashboard, and automate repeat work with Gems. Every lab uses realistic HR and recruitment data.

| Course detail | Information |
|---|---|
| Course code | `C817` |
| Programme | Non-WSQ |
| Duration | 1 day · 7.5 hours |
| Format | Instructor-led, with 12 hands-on labs |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/gemini-for-google-sheet.html) |
| Lab prompts | [Copy-ready prompts page (step → prompt)](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/) |
| Courseware version | v2.0 · 19 October 2026 |

---

## About the course

Gemini in Google Sheets works from a side panel beside your data. You describe what you want in plain English, and Gemini can summarise the sheet and answer questions about it. It also creates tables and formulas, explains and fixes formulas, and performs actions such as conditional formatting, pivot tables, dropdowns, sorting, filtering and find and replace. It can build charts, analyse data and solve optimisation problems. The AI function (`=AI`) and Fill with Gemini work inside cells, and Gems let you save a reusable expert assistant.

The course follows Google's official guide, [Collaborate with Gemini in Google Sheets](https://support.google.com/docs/answer/14356410), and the [AI function guide](https://support.google.com/docs/answer/15877199).

All twelve labs follow one storyline. **Orchid Bay Talent Partners** is a fictional Singapore recruitment and HR firm running its Q3 2026 hiring drive: 240 applications for eight client roles. You take that drive from a raw applicant-tracking export to a hiring decision. Each lab ends with a **Test It** step that lists the exact values you should get, so you can check Gemini's output against the data.

## Learning outcomes

By the end of the course, you will be able to:

1. **Fundamentals of Google Sheet.** Use Gemini's side panel, actions and formula help to summarise, quality-check and prepare HR data. Generate, explain and fix formulas such as VLOOKUP, COUNTIF and nested IF.
2. **Data analytics and visualization.** Create colour-coded tables, trackers and dropdowns. Extract and categorise text with the AI function. Generate data analysis, insights, pivot tables and charts, verifying every result.
3. **Interactive dashboard.** Build an interactive hiring dashboard and automate repeat screening with a custom Gem. Use Gemini's optimisation solver, reporting and sharing features responsibly.

## Topics covered

| Topic | Content |
|---|---|
| **1. Fundamentals of Google Sheet** | What Gemini in Google Sheets can do · prompting and the side panel (sources, Insert, Retry, Undo, Clear history) · data quality checks · Gemini actions (preview, apply, undo) and data prep · VLOOKUP, COUNTIF and nested IF · generating, explaining and fixing formulas |
| **2. Data Analytics and Visualization** | Tables, trackers and dropdowns from unstructured notes · conditional formatting · the AI function (`=AI`), Fill with Gemini and AI columns · data analysis and insights (Analysis steps, Export to Docs) · pivot tables · charts and graphs · inserted vs linked charts |
| **3. Interactive Dashboard** | Dropdown selectors and KPI formulas (COUNTIFS, AVERAGEIFS) · linked charts, metric switch, KPI alerts and protection · Gems with fair, evidence-only instructions · the optimisation problem solver · Drive files as context and responsible sharing |

## Labs

Each lab has its own folder containing:

- an **instruction PDF** with every step and its prompt, sample prompts and the Test It values;
- `sample-prompts.txt`, with prompts ready to copy;
- the **mock-data workbook** in `data/`, with a Prompt_Log tab already listing the lab's prompts;
- for Lab 11, `gem-instructions.txt` and two knowledge documents (job descriptions and a screening rubric).

Every prompt is also on one web page that walks through each lab as **Step → Prompt → Step → Prompt**, with one-click Copy buttons: [Lab Prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/). See also the [labs index](labs/README.md).

| # | Lab | Theme | Instructions | Mock data |
|---:|---|---|---|---|
| 1 | [Open Gemini and Explore the Q3 Candidate Export](labs/lab-01-gemini-side-panel-and-summaries/Lab-01-Instructions.pdf) | Gemini Side Panel & Summaries | [PDF](labs/lab-01-gemini-side-panel-and-summaries/Lab-01-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-1) | [Q3 applications export](labs/lab-01-gemini-side-panel-and-summaries/data/OrchidBay_Q3_Applications_Export.xlsx) |
| 2 | [Check the Quality of the Candidate Data with Gemini](labs/lab-02-data-quality-check/Lab-02-Instructions.pdf) | Data Quality Check | [PDF](labs/lab-02-data-quality-check/Lab-02-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-2) | [Quality-check workbook](labs/lab-02-data-quality-check/data/OrchidBay_Q3_Applications_QualityCheck.xlsx) |
| 3 | [Clean and Prepare the Candidate Data with Gemini Actions](labs/lab-03-data-prep/Lab-03-Instructions.pdf) | Data Prep | [PDF](labs/lab-03-data-prep/Lab-03-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-3) | [Data-prep workbook](labs/lab-03-data-prep/data/OrchidBay_Q3_Applications_Prep.xlsx) |
| 4 | [Generate, Explain and Fix Screening Formulas](labs/lab-04-formulas-vlookup-countif-and-nested-if/Lab-04-Instructions.pdf) | Formulas: VLOOKUP, COUNTIF & Nested IF | [PDF](labs/lab-04-formulas-vlookup-countif-and-nested-if/Lab-04-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-4) | [Screening formulas](labs/lab-04-formulas-vlookup-countif-and-nested-if/data/OrchidBay_Screening_Formulas.xlsx) |
| 5 | [Build a Colour-Coded Interview Tracker from Unstructured Notes](labs/lab-05-tables-trackers-and-conditional-formatting/Lab-05-Instructions.pdf) | Tables, Trackers & Conditional Formatting | [PDF](labs/lab-05-tables-trackers-and-conditional-formatting/Lab-05-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-5) | [Interview tracker](labs/lab-05-tables-trackers-and-conditional-formatting/data/OrchidBay_Interview_Tracker.xlsx) |
| 6 | [Extract and Categorise Candidate Text with the AI Function](labs/lab-06-ai-function-and-fill-with-gemini/Lab-06-Instructions.pdf) | AI Function & Fill with Gemini | [PDF](labs/lab-06-ai-function-and-fill-with-gemini/Lab-06-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-6) | [Candidate profiles](labs/lab-06-ai-function-and-fill-with-gemini/data/OrchidBay_Candidate_Profiles.xlsx) |
| 7 | [Generate Hiring Insights and Pivot Tables with Gemini](labs/lab-07-data-analysis-and-insights/Lab-07-Instructions.pdf) | Data Analysis & Insights | [PDF](labs/lab-07-data-analysis-and-insights/Lab-07-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-7) | [2026 hiring year to date (720 rows)](labs/lab-07-data-analysis-and-insights/data/OrchidBay_Hiring_2026_YTD.xlsx) |
| 8 | [Build Charts That Tell the Hiring Story](labs/lab-08-charts-and-visualisation/Lab-08-Instructions.pdf) | Charts & Visualisation | [PDF](labs/lab-08-charts-and-visualisation/Lab-08-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-8) | [Hiring charts](labs/lab-08-charts-and-visualisation/data/OrchidBay_Hiring_Charts.xlsx) |
| 9 | [Build the Dashboard's Selectors and KPI Formulas](labs/lab-09-dashboard-kpis-and-selectors/Lab-09-Instructions.pdf) | Dashboard KPIs & Selectors | [PDF](labs/lab-09-dashboard-kpis-and-selectors/Lab-09-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-9) | [Dashboard build](labs/lab-09-dashboard-kpis-and-selectors/data/OrchidBay_Dashboard_Build.xlsx) |
| 10 | [Make the Hiring Dashboard Interactive and Visual](labs/lab-10-interactive-dashboard/Lab-10-Instructions.pdf) | Interactive Dashboard | [PDF](labs/lab-10-interactive-dashboard/Lab-10-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-10) | [Interactive dashboard](labs/lab-10-interactive-dashboard/data/OrchidBay_Dashboard_Interactive.xlsx) |
| 11 | [Create a Candidate Screener Gem and Use It in Sheets](labs/lab-11-gems/Lab-11-Instructions.pdf) | Gems | [PDF](labs/lab-11-gems/Lab-11-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-11) | [Finalists](labs/lab-11-gems/data/OrchidBay_Finalists.xlsx) · [Gem instructions](labs/lab-11-gems/gem-instructions.txt) · [job descriptions](labs/lab-11-gems/data/gem-knowledge/OrchidBay_Job_Descriptions.docx) · [rubric](labs/lab-11-gems/data/gem-knowledge/OrchidBay_Screening_Rubric.docx) |
| 12 | [Optimise the Hiring Decision and Share Results Safely](labs/lab-12-optimisation-reporting-and-safe-sharing/Lab-12-Instructions.pdf) | Optimisation, Reporting & Safe Sharing | [PDF](labs/lab-12-optimisation-reporting-and-safe-sharing/Lab-12-Instructions.pdf) · [prompts](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/#lab-12) | [Hiring decision](labs/lab-12-optimisation-reporting-and-safe-sharing/data/OrchidBay_Hiring_Decision.xlsx) |

### Before you start

- You need a Google account with Gemini in Google Sheets: a Google Workspace plan with Gemini, or a Google AI Pro or Ultra plan. The **Ask Gemini** (spark) button must appear at the top right of Sheets.
- Labs 6 and 11 also need the AI function (`=AI`) and Gems on your account.
- Upload each lab workbook to Google Drive and choose **File > Save as Google Sheets**. Gemini works best on native Google Sheets files.
- Gemini's features and labels are still rolling out, so some may differ on your screen. Each lab includes troubleshooting tips and fallbacks.

## Courseware package

| Item | Files |
|---|---|
| Slide deck | [PowerPoint](<courseware/Gemini for Google Sheet (C817)-v2.0.pptx>) · [PDF](<courseware/Gemini for Google Sheet (C817)-v2.0.pdf>) |
| Learner Guide | [Word](<courseware/LG-Gemini for Google Sheet (C817).docx>) · [PDF](<courseware/LG-Gemini for Google Sheet (C817).pdf>) |
| Lesson Plan | [Word](<courseware/LP-Gemini for Google Sheet (C817).docx>) · [PDF](<courseware/LP-Gemini for Google Sheet (C817).pdf>) |
| Labs | [labs/](labs/README.md): 12 lab folders with instruction PDFs, sample prompts and mock data |
| Lab prompts web page | [docs/prompts/](docs/prompts/index.html), published at [tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/](https://tertiarycourses.github.io/C817-Gemini-for-Google-Sheet/prompts/) |

The deck, Learner Guide, Lesson Plan, labs and prompts page are all generated from one content source in `.claude/skills/non-wsq-courseware-build/build/`, so they stay aligned. To rebuild them, run `build_courseware.sh` in that folder. The deck's screenshots come from Google Docs Editors Help and are credited on each slide.

## Distribution boundary

This repository publishes the current learner-facing courseware, labs and the prompts page. It does not publish superseded versions (`courseware/archive/`), source reference material or credentials. This is a non-WSQ commercial course, so it has no assessment.

## Data notice

All Orchid Bay organisations, people, IDs and values are **fictional training data**, generated for this course, and email addresses use the reserved `example.com` domain. Any resemblance to a real company or person is coincidental. Do not paste real candidates' or employees' personal data into Gemini unless your organisation has approved it.

## Provider

Developed and delivered by **Tertiary Infotech Academy Pte Ltd** (Tertiary Courses), Singapore · UEN 201200696W
Course page: <https://www.tertiarycourses.com.sg/gemini-for-google-sheet.html>
