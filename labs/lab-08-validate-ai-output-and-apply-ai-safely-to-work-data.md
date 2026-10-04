# Lab 8 — Validate AI Output and Apply AI Safely to Work Data

**Topic 02:** Analysing and Automating Data with AI in Sheets  |  **Day 1**  |  **Approx. 50 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Stress-test AI output for accuracy and write a personal checklist for applying AI safely to real work data.

## What you'll build

A verification habit and a written safe-use checklist you have applied to an earlier lab's result.

**Tools and techniques:** Validation, cross-checking, data privacy, safe-use checklist

## Prerequisites

- Labs 1-7 complete — you have several AI results to stress-test.

## Steps

### Step 1

Ask AI a question with a knowable answer, then verify it with a formula.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
How many orders are from the North region?
```

### Step 2

Confirm the count yourself and compare.

Formula (paste into the cell):

```text
=COUNTIF(D2:D200,"North")
```

### Step 3

Try to catch a mistake: ask a trickier question and verify hard by recomputing it yourself.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
What percentage of total sales came from the top 3 customers? Show the range you used and the working.
```

### Step 4

If the AI figure is wrong or unclear, refine the prompt (state the range and ask it to show its working) and re-run.

### Step 5

Set the rule: never accept an AI number you cannot tie back to a formula or count in the sheet.

### Step 6

Review data safety: list which columns here would be sensitive if this were real company data (for example Customer names), and how you would protect them.

### Step 7

Ask AI for good practice, then sanity-check its advice against your own judgement.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
What should I avoid putting into an AI prompt when working with real company data, and why?
```

### Step 8

Draft your safe-use checklist — verify every figure; keep confidential data out of prompts; state the range; ask for the formula; record where AI was used — and apply it to one AI result from an earlier lab.

## Test it

You have caught or ruled out at least one AI inaccuracy by verifying it against your own formula, and you have a written safe-use checklist that you applied to an earlier lab's result.

## Troubleshooting

- **You can't reproduce Gemini's percentage.** Ask it to show the exact ranges and steps, then rebuild them cell by cell; a mismatch usually means it used a different range or counted differently.
- **Gemini's safety advice sounds generic.** That's expected — treat it as a starting point and adapt it to your organisation's real data and rules; you own the final checklist.
- **You're unsure whether a column is sensitive.** When in doubt, treat it as sensitive: keep it out of prompts, or replace it with the supplied sample data.

## Challenge

Write a one-line 'AI used here' note for each figure and chart you kept, so anyone reviewing your sheet can see where AI helped and how you verified it.

## Reflection

LO7 — Stress-test AI output for accuracy and write a personal checklist for applying AI safely to real work data. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
