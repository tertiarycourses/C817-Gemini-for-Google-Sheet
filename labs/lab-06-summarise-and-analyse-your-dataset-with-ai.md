# Lab 6 — Summarise and Analyse Your Dataset with AI

**Topic 02:** Analysing and Automating Data with AI in Sheets  |  **Day 1**  |  **Approx. 45 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Use AI to summarise the dataset and answer analytical questions, verifying every figure against a formula.

## What you'll build

A short, written analysis of the quarter in which every figure has been verified.

**Tools and techniques:** Gemini side panel, summarisation, AVERAGE, SUMIFS, segment analysis

## Prerequisites

- Lab 5 complete — the dataset is clean, dates standardised and sorted.
- Your grand total from Lab 2 (cell K1) still in place for cross-checking.

## Steps

### Step 1

Ask AI for a summary of the quarter.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Summarise the Orders tab: total sales value, number of orders, average order value, and the best-selling product. Show the figure for each.
```

### Step 2

Verify the total sales against your grand total from Lab 2 (cell K1) — they should match.

### Step 3

Verify the average order value yourself.

Formula (paste into the cell):

```text
=AVERAGE(I2:I200)
```

### Step 4

Ask a segment question.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Which Region had the highest total sales, and by how much more than the second-highest?
```

### Step 5

Cross-check the winning region with a SUMIF like the one you built in Lab 3.

### Step 6

Ask an analytical trend question.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Did sales grow or fall across the three months in this quarter? Give the monthly total for each month and describe the trend in one sentence.
```

### Step 7

Verify the monthly totals with a quick pivot or a SUMIFS by month; if any figure does not match, investigate before trusting it.

### Step 8

Write a 3-bullet summary of the quarter in a notes area, using only figures you have verified.

## Test it

You have a written 3-bullet summary in which every figure — total sales, average order value and the top region — matches a formula or count you computed yourself.

## Troubleshooting

- **Gemini's total sales differ from K1.** One of them is wrong. Re-check that K1 sums the full I2:I200 and that Gemini used the same range; the clean data from Lab 5 should make them agree.
- **The monthly split looks off.** Confirm every Order Date is a real date (right-aligned), not text (left-aligned); text dates won't group by month. Fix in Lab 5's date step.
- **Gemini gives an average that seems too high or low.** Averages are easily skewed. Compute =AVERAGE(I2:I200) yourself and, if they differ, ask Gemini which rows it included.

## Challenge

Ask Gemini for the single biggest driver of the quarter's result (a product, region or month) and verify its claim with your own SUMIF.

## Reflection

LO5 — Use AI to summarise the dataset and answer analytical questions, verifying every figure against a formula. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
