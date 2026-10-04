# Lab 4 — Write Effective Prompts for Spreadsheet Tasks

**Topic 01:** Getting Started with AI in Google Sheets  |  **Day 1**  |  **Approx. 35 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for spreadsheet work.

## What you'll build

A written four-part prompt pattern and one strong, tested prompt saved for reuse.

**Tools and techniques:** Prompt design, range/goal/output/conditions, refinement

## Prerequisites

- Labs 1-3 complete — you are comfortable running prompts in the Gemini panel.

## Steps

### Step 1

Run a deliberately vague prompt in the Gemini panel and note how generic the answer is.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Tell me about my sales.
```

### Step 2

Now run a specific prompt for the same intent and compare the result.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
From the Orders tab range A1:I200, list the top 5 products by total sales value. Show product name and total, sorted highest first, as a table.
```

### Step 3

Write down the four parts that made the second prompt work: the Range, the Goal, the Output format, and the Conditions.

### Step 4

Capture your reusable pattern in a notes cell or a document so every future prompt follows it.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
RANGE: <which cells/tab> | GOAL: <what to produce> | OUTPUT: <table/formula/number & where> | CONDITIONS: <filters, sort, limits>
```

### Step 5

Add conditions that keep results trustworthy: state the range explicitly and ask AI to show the formula it used so you can check it.

### Step 6

Rewrite one question of your own about the data using the pattern, and run it.

### Step 7

Refine once: change the Output or Conditions part (for example 'top 10', or 'North region only') and re-run to see the result change. Keep the better version.

### Step 8

Save your best prompt where you can find it again — you will reuse this pattern in every remaining lab.

## Test it

You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.

## Troubleshooting

- **The specific prompt still gives a vague answer.** Add the missing part of the pattern — most often the explicit Range (A1:I200) or the Output format ('as a table').
- **Gemini answers about the wrong columns.** Name the columns by their header ('by Product', 'by total sales value') rather than by letter, and restate the range.
- **Results differ each time you run the same prompt.** Pin the result by asking Gemini to show the formula it used, then paste that formula into the sheet so the answer is stable and checkable.

## Challenge

Turn your best prompt into a template with blanks (<RANGE>, <GOAL>, <OUTPUT>, <CONDITIONS>) and use it to answer a brand-new question about the data in one attempt.

## Reflection

LO3 — Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for spreadsheet work. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
