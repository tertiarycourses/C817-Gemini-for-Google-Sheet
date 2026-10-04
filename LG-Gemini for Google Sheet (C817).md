# Gemini for Google Sheet (C817) — Learner Guide

**Course Code:** C817  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.1 · 4 October 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with AI in Google Sheets  (50%)](#topic-01--getting-started-with-ai-in-google-sheets--50)
  - [Lab 1 — Set Up and Access Gemini AI in Google Sheets](#lab-1--set-up-and-access-gemini-ai-in-google-sheets)
  - [Lab 2 — Generate and Explain Formulas with AI](#lab-2--generate-and-explain-formulas-with-ai)
  - [Lab 3 — Combine and Troubleshoot Formulas with AI](#lab-3--combine-and-troubleshoot-formulas-with-ai)
  - [Lab 4 — Write Effective Prompts for Spreadsheet Tasks](#lab-4--write-effective-prompts-for-spreadsheet-tasks)
- [Topic 02 — Analysing and Automating Data with AI in Sheets  (50%)](#topic-02--analysing-and-automating-data-with-ai-in-sheets--50)
  - [Lab 5 — Clean, Transform and Organise Data with AI](#lab-5--clean-transform-and-organise-data-with-ai)
  - [Lab 6 — Summarise and Analyse Your Dataset with AI](#lab-6--summarise-and-analyse-your-dataset-with-ai)
  - [Lab 7 — Create Tables, Charts and Visualisations with AI](#lab-7--create-tables-charts-and-visualisations-with-ai)
  - [Lab 8 — Validate AI Output and Apply AI Safely to Work Data](#lab-8--validate-ai-output-and-apply-ai-safely-to-work-data)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Gemini for Google Sheet (C817) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 8 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build one connected result from a single dataset. You take a messy quarter of orders for a small retailer, 'Riverside Supplies', and use Gemini AI in Google Sheets to generate and explain formulas, clean and organise the data, analyse it, and turn it into charts you can trust. Wherever you can, use your own non-confidential data so you leave with skills applied to your own work; the supplied Riverside Supplies sample sheet is provided for everyone to follow along.


## Course Learning Outcomes

- LO1: Explain what generative AI and Gemini in Google Sheets are, and set up and access AI features inside a sheet.
- LO2: Generate spreadsheet formulas with AI and use AI to explain, step by step, what a formula does.
- LO3: Write clear, effective prompts that get accurate results for spreadsheet tasks.
- LO4: Use AI to clean, transform and organise messy spreadsheet data into a usable table.
- LO5: Summarise and analyse datasets with AI to surface useful, decision-ready insights.
- LO6: Create tables, charts and visualisations from your data using AI.
- LO7: Validate AI output for accuracy and apply AI safely and responsibly to real work data.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) with a current Chrome or Edge browser.
- A Google account with access to Google Sheets and Google Drive.
- Gemini in Google Sheets available and enabled on your account (the trainer confirms access at the start of the day).
- The sample 'Riverside Supplies — Q1 Orders' Google Sheet (the trainer shares a link; make your own copy with File > Make a copy) — or your own non-confidential dataset.

**Verify your setup**

Before Lab 1, confirm you can open Google Sheets, make your own copy of the sample sheet, and open the Gemini side panel ("Ask Gemini"). If Gemini is not visible on your account, tell the trainer.

```bash
Open sheets.google.com  ·  open the sample sheet  ·  File > Make a copy  ·  open the Gemini / Ask Gemini panel
```

**Conventions used in every lab**

- Placeholders such as <YOUR COPY> or <RANGE> are replaced with your own values.
- Prompts you give Gemini are shown in a shaded box — paste them into the side panel, or into an =AI() formula where a lab says so.
- Cell references (e.g., A2:I200) and menu paths (e.g., Insert > Chart) are written exactly as you will use them.
- Every lab ends with a 'Test it' step — verify the AI's result against a value you can confirm before you move on.


## Topic 01 — Getting Started with AI in Google Sheets  (50%)

Generative AI & Gemini in Sheets · Setting up and accessing AI · Generating and explaining formulas · Effective prompting

**Key concepts**

- Generative AI — AI that creates new content (text, formulas, summaries) from a plain-language request, rather than only looking things up.
- Gemini in Google Sheets — Google's built-in AI that helps you build formulas, clean data, analyse and summarise, directly inside a spreadsheet.
- Where to find it — the Gemini side panel ("Ask Gemini") and AI-assisted menus let you work in plain English without leaving your sheet.
- The =AI() function — a Sheets function that sends your prompt to Gemini and returns the result straight into a cell, so AI output becomes spreadsheet data.
- Generating formulas — describe the calculation you want in words and let AI write the correct formula (SUM, IF, VLOOKUP, and more) for you.
- Explaining formulas — paste any formula and ask AI to explain, step by step, what it does — a fast way to learn and to check an inherited sheet.
- Effective prompting — a good spreadsheet prompt names the range, the goal, the output format and any conditions, so the AI has no room to guess.
- Human in the loop — AI drafts; you check. Always verify a formula or result against a value you can confirm before you rely on it.


### Lab 1 — Set Up and Access Gemini AI in Google Sheets

Learning outcome: Open the sample sheet, make your own copy, open the Gemini side panel, and run a first AI prompt on the data..

Goal: This lab gets AI working in your spreadsheet. You make your own copy of the Riverside Supplies orders sheet, open the Gemini side panel, and ask a first read-only question so you can see the ask-check loop before you rely on it. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

Your own copy of the Riverside Supplies sheet in Drive, with Gemini open and a first answer verified.   (Tools: Google Sheets, Google Drive, Gemini side panel (Ask Gemini).)

**Step-by-step**

1. Open the sample 'Riverside Supplies — Q1 Orders' sheet from the link the trainer shares.
2. Make it yours: File > Make a copy, and save it to your Drive as 'Riverside Supplies — Q1 Orders (<YOUR NAME>)'.
3. Look at the Orders tab: note the columns Order ID, Order Date, Customer, Region, Product, Category, Quantity, Unit Price, Total — and that some cells are messy. You will fix those later.
4. Open the Gemini side panel — click 'Ask Gemini' (the sparkle, top-right). If you cannot see it, tell the trainer; access is confirmed at the start of the day.
5. Ask a first, read-only question to confirm Gemini can see your data.

   ```bash
   How many rows of orders are in the Orders tab, and what does each column mean?
   ```

6. Check the answer: compare the row count Gemini gives against the row count shown at the bottom-left of the sheet.
7. Ask one follow-up so you see Gemini use the data.

   ```bash
   Which 3 products appear most often in the Orders tab?
   ```

8. Confirm nothing changed — asking Gemini a question is read-only. You have now seen the ask-check loop safely.

**Test it**

You have your own copy of the sheet in Drive, the Gemini panel open, and a first answer whose row count matches the count shown at the bottom of the sheet.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 2 — Generate and Explain Formulas with AI

Learning outcome: Use AI to generate a spreadsheet formula from a plain-language description, and to explain an existing formula..

Goal: Now you let AI write formulas for you. You fill the blank Total column and add a grand total by asking Gemini for the formula, verify each against a value you can confirm, then paste an unfamiliar formula and have AI explain it step by step. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A working, AI-generated Total column and grand total, each verified, plus a plain-English explanation of a formula.   (Tools: Gemini side panel, formula generation, formula explanation, SUM, IF.)

**Step-by-step**

1. Click cell I2 (Total). Ask Gemini for a formula that multiplies Quantity by Unit Price.

   ```bash
   Write a Google Sheets formula for cell I2 that multiplies Quantity in G2 by Unit Price in H2.
   ```

2. Paste the formula into I2 and fill it down the column (double-click the small square at the cell's bottom-right).

   ```bash
   =G2*H2
   ```

3. Verify: pick any row and check by hand that Quantity x Unit Price equals the Total shown.
4. Ask AI for one formula that totals the whole Total column into cell K1.

   ```bash
   Write a formula for cell K1 that gives the grand total of the Total column I2:I200.
   ```

5. Paste it into K1 and read the result.

   ```bash
   =SUM(I2:I200)
   ```

6. Cross-check: select I2:I200 and read the Sum shown in the status bar at the bottom-right — it should match K1.
7. Learn from a formula: paste this into the Gemini panel and ask it to explain, step by step.

   ```bash
   Explain what this formula does, step by step: =IF(G2>=10,"Bulk","Standard")
   ```

8. Read the explanation and write one sentence in your notes on what =IF does.

**Test it**

The Total column is filled with a verified formula, K1 equals the status-bar Sum of I2:I200, and you can explain in one sentence what the =IF formula does.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 3 — Combine and Troubleshoot Formulas with AI

Learning outcome: Use AI to build a multi-step formula, then diagnose and fix a broken one against a value you can confirm..

Goal: Real formulas need combining and fixing. You ask AI for a conditional total (sales for one region), hit the messy-data edge case that makes it wrong, and use Gemini to diagnose and correct it — verifying every version against a filtered check. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A verified region-total formula (SUMIF) and an AI-assisted fix for a deliberately broken formula.   (Tools: Gemini side panel, SUMIF, COUNTIF, troubleshooting, refinement.)

**Step-by-step**

1. In cell K3, ask AI for a formula that adds up Total for every order where Region is 'North'.

   ```bash
   Write a formula for K3 that sums column I where column D equals "North", for rows 2 to 200.
   ```

2. Paste it into K3 and note the figure.

   ```bash
   =SUMIF(D2:D200,"North",I2:I200)
   ```

3. Verify: filter the sheet to Region = North and read the status-bar Sum of the visible Total cells — it should match K3.
4. Spot the problem: the Region column is messy ('north', 'North ', 'NORTH'), so SUMIF may miss rows and under-count. Tell AI and ask for a fix.

   ```bash
   My Region column has inconsistent capitalisation and extra spaces, so SUMIF misses rows. Give me a formula that totals Total for North regardless of case or spaces.
   ```

5. Paste the improved formula Gemini gives and compare the new North total with the old one.

   ```bash
   =SUMIF(D2:D200,"*north*",I2:I200)
   ```

6. Ask AI to explain, in one or two sentences, why the first formula missed rows.
7. Break something on purpose: change K3 to reference the wrong column, then paste the wrong result to Gemini and ask what is wrong.

   ```bash
   This formula gives the wrong total: =SUMIF(C2:C200,"North",I2:I200). What is wrong and how do I fix it?
   ```

8. Apply Gemini's fix and confirm the corrected total matches your filtered check from step 3.

**Test it**

K3 gives a North total that matches your filtered status-bar Sum, and you have used AI to diagnose and correct a deliberately broken formula.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 4 — Write Effective Prompts for Spreadsheet Tasks

Learning outcome: Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for spreadsheet work..

Goal: A result is only as good as the prompt. You run a vague prompt, then a specific one that names the range, goal, output and conditions, see the difference, and distil what worked into a reusable pattern you will use for the rest of the course. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A written four-part prompt pattern and one strong, tested prompt saved for reuse.   (Tools: Prompt design, range/goal/output/conditions, refinement.)

**Step-by-step**

1. Run a deliberately vague prompt in the Gemini panel and note how generic the answer is.

   ```bash
   Tell me about my sales.
   ```

2. Now run a specific prompt for the same intent and compare the result.

   ```bash
   From the Orders tab range A1:I200, list the top 5 products by total sales value. Show product name and total, sorted highest first, as a table.
   ```

3. Write down the four parts that made the second prompt work: the Range, the Goal, the Output format, and the Conditions.
4. Capture your reusable pattern in a notes cell or a document so every future prompt follows it.

   ```bash
   RANGE: <which cells/tab> | GOAL: <what to produce> | OUTPUT: <table/formula/number & where> | CONDITIONS: <filters, sort, limits>
   ```

5. Add conditions that keep results trustworthy: state the range explicitly and ask AI to show the formula it used so you can check it.
6. Rewrite one question of your own about the data using the pattern, and run it.
7. Refine once: change the Output or Conditions part (for example 'top 10', or 'North region only') and re-run to see the result change. Keep the better version.
8. Save your best prompt where you can find it again — you will reuse this pattern in every remaining lab.

**Test it**

You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


## Topic 02 — Analysing and Automating Data with AI in Sheets  (50%)

Cleaning, transforming & organising data · Summarising and analysing datasets · Tables, charts & visualisations · Validating and applying AI safely

**Key concepts**

- Cleaning data — AI can standardise text, fix inconsistent formats, split or merge columns and flag blanks, turning a messy sheet into a usable one.
- Transforming data — reshape data with AI: extract fields, categorise rows, convert units or reformat dates without writing complex formulas by hand.
- Organising data — sort, group and label records so a raw export becomes a structured table you can analyse.
- Summarising datasets — ask AI for totals, averages, top and bottom performers and a plain-language summary of what the numbers say.
- Analysing datasets — AI can spot trends, compare segments and answer "what" and "why" questions about your data in seconds.
- Tables and pivots — turn a flat list into a summary table or pivot with AI, grouping and aggregating the figures that matter.
- Charts and visualisations — describe the story you want to tell and let AI suggest and build the right chart to show it.
- Validating and applying safely — AI can be confidently wrong; check outputs against known values, keep confidential data out of prompts, and stay accountable for the result.


### Lab 5 — Clean, Transform and Organise Data with AI

Learning outcome: Use AI to standardise messy text and dates, tidy fields, and organise the dataset into a clean table..

Goal: Analysis is only as good as the data under it. You use Gemini to standardise the messy Region and Product text, fix the mixed date formats, and sort the records into a clean, consistent table — asking AI for the formula or steps each time and verifying the result. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A cleaned, consistently formatted Orders table ready for analysis.   (Tools: Gemini side panel, TRIM, PROPER, CLEAN, date formatting, Data > Sort range.)

**Step-by-step**

1. Ask AI how to standardise the Region column so 'north', 'North ' and 'NORTH' all become 'North'.

   ```bash
   Give me a formula for column J that returns column D with consistent capitalisation and no leading or trailing spaces.
   ```

2. Put the formula in J2 and fill it down; check that a few previously messy rows now read cleanly.

   ```bash
   =PROPER(TRIM(D2))
   ```

3. Lock the fix in: copy column J, then Edit > Paste special > Values only over column D, and delete the helper column J.
4. Ask AI to standardise the Order Date column to YYYY-MM-DD, and follow its steps (Format > Number > Date, or the formula it gives).

   ```bash
   Column B has dates in mixed formats. How do I make them all display as YYYY-MM-DD in Google Sheets?
   ```

5. Verify a couple of dates against what they clearly should be, and confirm none turned blank or wrong.
6. Tidy the Product column: ask AI for a formula to trim extra spaces and fix capitalisation, apply it, and paste values back as in step 3.

   ```bash
   =TRIM(E2)
   ```

7. Organise the data: select A1:I200 and use Data > Sort range (with 'Data has header row' ticked) to sort by Order Date, ascending.
8. Ask Gemini to check your work.

   ```bash
   Look at the Orders tab. Are there any remaining blank cells, inconsistent categories or duplicate Order IDs I should fix?
   ```


**Test it**

The Region and Product columns are consistent, all Order Dates display as YYYY-MM-DD, the data is sorted by date, and Gemini's check reports no remaining obvious issues (or you have fixed the ones it named).

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 6 — Summarise and Analyse Your Dataset with AI

Learning outcome: Use AI to summarise the dataset and answer analytical questions, verifying every figure against a formula..

Goal: With clean data you can ask real questions. You have Gemini summarise the quarter, compare segments and describe the trend across the three months — and you verify every figure it gives against a formula or count you compute yourself before you trust it. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A short, written analysis of the quarter in which every figure has been verified.   (Tools: Gemini side panel, summarisation, AVERAGE, SUMIFS, segment analysis.)

**Step-by-step**

1. Ask AI for a summary of the quarter.

   ```bash
   Summarise the Orders tab: total sales value, number of orders, average order value, and the best-selling product. Show the figure for each.
   ```

2. Verify the total sales against your grand total from Lab 2 (cell K1) — they should match.
3. Verify the average order value yourself.

   ```bash
   =AVERAGE(I2:I200)
   ```

4. Ask a segment question.

   ```bash
   Which Region had the highest total sales, and by how much more than the second-highest?
   ```

5. Cross-check the winning region with a SUMIF like the one you built in Lab 3.
6. Ask an analytical trend question.

   ```bash
   Did sales grow or fall across the three months in this quarter? Give the monthly total for each month and describe the trend in one sentence.
   ```

7. Verify the monthly totals with a quick pivot or a SUMIFS by month; if any figure does not match, investigate before trusting it.
8. Write a 3-bullet summary of the quarter in a notes area, using only figures you have verified.

**Test it**

You have a written 3-bullet summary in which every figure — total sales, average order value and the top region — matches a formula or count you computed yourself.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 7 — Create Tables, Charts and Visualisations with AI

Learning outcome: Use AI to build a summary/pivot table and the right, clearly labelled chart to tell the data's story..

Goal: Numbers persuade when they are shown well. You use Gemini to design a pivot of sales by region and month, then to recommend and build the right chart, and to refine its title, labels and sorting — checking each visual against the figures you verified in Lab 6. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A verified pivot table plus a labelled column chart and a monthly-trend line chart.   (Tools: Gemini side panel, pivot tables, Insert > Chart, chart types, chart formatting.)

**Step-by-step**

1. Ask AI which summary table best shows sales performance and how to build it.

   ```bash
   I want to see total sales by Region and by month. What pivot table should I build, and what are the steps in Google Sheets?
   ```

2. Build the pivot (Insert > Pivot table): Rows = Region, Columns = month of Order Date, Values = SUM of Total.
3. Verify one cell of the pivot against a SUMIFS you write for that same region and month.
4. Ask AI to recommend the best chart to compare sales across regions.

   ```bash
   What is the best chart type to compare total sales across Regions, and why?
   ```

5. Insert the chart: select the region totals, then Insert > Chart, and set the recommended type (for example a column chart).
6. Ask AI to improve it, then apply the suggestions — a clear title, axis labels, and bars sorted highest to lowest.

   ```bash
   Suggest a clear title and axis labels for a column chart of total sales by Region, sorted highest to lowest.
   ```

7. Add a second chart for the monthly trend: a line chart of total sales by month.
8. Check the trend chart matches the direction you found in your Lab 6 analysis.

**Test it**

You have a pivot table whose figures you verified against a formula, a labelled column chart of sales by region sorted high-to-low, and a line chart of the monthly trend consistent with your Lab 6 analysis.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


### Lab 8 — Validate AI Output and Apply AI Safely to Work Data

Learning outcome: Stress-test AI output for accuracy and write a personal checklist for applying AI safely to real work data..

Goal: The capstone. You deliberately test whether AI's answers hold up, learn to verify anything before you act on it, review what data is safe to put into a prompt, and write a safe-use checklist you apply to an earlier result — the habits that make AI in Sheets trustworthy at work. BUILDING BLOCK — what you do in this lab is applied to your copy of the Riverside Supplies sheet, the single dataset you clean, analyse and chart across all 8 labs.

**What you'll build**

A verification habit and a written safe-use checklist you have applied to an earlier lab's result.   (Tools: Validation, cross-checking, data privacy, safe-use checklist.)

**Step-by-step**

1. Ask AI a question with a knowable answer, then verify it with a formula.

   ```bash
   How many orders are from the North region?
   ```

2. Confirm the count yourself and compare.

   ```bash
   =COUNTIF(D2:D200,"North")
   ```

3. Try to catch a mistake: ask a trickier question and verify hard by recomputing it yourself.

   ```bash
   What percentage of total sales came from the top 3 customers? Show the range you used and the working.
   ```

4. If the AI figure is wrong or unclear, refine the prompt (state the range and ask it to show its working) and re-run.
5. Set the rule: never accept an AI number you cannot tie back to a formula or count in the sheet.
6. Review data safety: list which columns here would be sensitive if this were real company data (for example Customer names), and how you would protect them.
7. Ask AI for good practice, then sanity-check its advice against your own judgement.

   ```bash
   What should I avoid putting into an AI prompt when working with real company data, and why?
   ```

8. Draft your safe-use checklist — verify every figure; keep confidential data out of prompts; state the range; ask for the formula; record where AI was used — and apply it to one AI result from an earlier lab.

**Test it**

You have caught or ruled out at least one AI inaccuracy by verifying it against your own formula, and you have a written safe-use checklist that you applied to an earlier lab's result.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Riverside Supplies sample data if in doubt. Exact Gemini menu names and buttons may differ slightly between accounts and may change over time; the trainer will point out the current location on the day.

---


## Wrap-Up

In one day you have taken a messy spreadsheet from raw export to a clean, analysed and charted dataset — using Gemini AI at every step, and checking its work before trusting it.

**What you built**

- Gemini AI set up and accessible in your own copy of the Riverside Supplies sheet.
- Formulas generated and explained by AI, including a multi-step formula you refined and verified.
- A reusable prompt pattern (range, goal, output, conditions) for spreadsheet tasks.
- A cleaned, transformed and organised dataset from a messy export.
- An analysis — totals, averages, top performers and a summary table — plus the right chart to tell the story.
- A personal checklist for validating AI output and applying AI safely to real work data.

**What to do next**

- Point these techniques at one real, recurring spreadsheet task in your own week and measure the time saved.
- Keep verifying: check every AI formula or figure against a value you can confirm before you act on it.
- Save your best prompts so you and your team can reuse them.
- Keep confidential data out of prompts, and note where AI helped so your work stays accountable.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the clean-analyse-chart flow on the sample data from memory, writing your own prompts.
- Apply the techniques to a real, non-confidential spreadsheet from your own organisation.
- Review each lab's detailed steps in this guide and re-run the tasks on your own machine.


## Glossary

- **Generative AI** — AI that creates new content — text, formulas, summaries — from a plain-language request, rather than only retrieving existing answers.
- **Gemini** — Google's AI assistant; inside Google Sheets it helps you build formulas, clean data, analyse and summarise.
- **Gemini side panel** — The "Ask Gemini" panel in Sheets where you have a conversation about the data in your spreadsheet.
- **=AI() function** — A Google Sheets function that sends a prompt to Gemini and returns the result into a cell.
- **Prompt** — The plain-language instruction you give the AI; a good one states the range, goal, output format and conditions.
- **Formula** — A spreadsheet instruction (such as =SUM or =IF) that calculates a result from your data.
- **Range** — A block of cells, written like A2:I200, that a formula or prompt applies to.
- **Data cleaning** — Standardising and correcting data — fixing formats, trimming spaces, filling or flagging blanks — so it can be used.
- **Transforming data** — Reshaping data: splitting or merging columns, extracting fields, categorising rows or reformatting values.
- **Pivot table** — A summary table that groups and aggregates a flat list, such as total sales by region.
- **Chart** — A visual representation of data — bar, line, pie — used to show a pattern or comparison at a glance.
- **Validation** — Checking that an AI result is correct by comparing it against a value you can confirm yourself.
- **Hallucination** — A confident but wrong AI output; the reason every AI result must be verified before use.
- **Human in the loop** — The practice of a person reviewing and approving AI output before it is relied upon.
