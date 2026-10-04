# Lab 3 — Combine and Troubleshoot Formulas with AI

**Topic 01:** Getting Started with AI in Google Sheets  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Use AI to build a multi-step formula, then diagnose and fix a broken one against a value you can confirm.

## What you'll build

A verified region-total formula (SUMIF) and an AI-assisted fix for a deliberately broken formula.

**Tools and techniques:** Gemini side panel, SUMIF, COUNTIF, troubleshooting, refinement

## Prerequisites

- Lab 2 complete — the Total column filled and verified.

## Steps

### Step 1

In cell K3, ask AI for a formula that adds up Total for every order where Region is 'North'.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Write a formula for K3 that sums column I where column D equals "North", for rows 2 to 200.
```

### Step 2

Paste it into K3 and note the figure.

Formula (paste into the cell):

```text
=SUMIF(D2:D200,"North",I2:I200)
```

### Step 3

Verify: filter the sheet to Region = North and read the status-bar Sum of the visible Total cells — it should match K3.

### Step 4

Spot the problem: the Region column is messy ('north', 'North ', 'NORTH'), so SUMIF may miss rows and under-count. Tell AI and ask for a fix.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
My Region column has inconsistent capitalisation and extra spaces, so SUMIF misses rows. Give me a formula that totals Total for North regardless of case or spaces.
```

### Step 5

Paste the improved formula Gemini gives and compare the new North total with the old one.

Formula (paste into the cell):

```text
=SUMIF(D2:D200,"*north*",I2:I200)
```

### Step 6

Ask AI to explain, in one or two sentences, why the first formula missed rows.

### Step 7

Break something on purpose: change K3 to reference the wrong column, then paste the wrong result to Gemini and ask what is wrong.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
This formula gives the wrong total: =SUMIF(C2:C200,"North",I2:I200). What is wrong and how do I fix it?
```

### Step 8

Apply Gemini's fix and confirm the corrected total matches your filtered check from step 3.

## Test it

K3 gives a North total that matches your filtered status-bar Sum, and you have used AI to diagnose and correct a deliberately broken formula.

## Troubleshooting

- **SUMIF returns 0.** The text in column D probably doesn't exactly match 'North'. Try the case/space-tolerant formula Gemini suggested, or check for hidden spaces with TRIM.
- **The wildcard version totals too much.** '*north*' also matches values that merely contain 'north'. If a region like 'Northgate' exists, ask Gemini for a TRIM/LOWER exact-match version instead.
- **Gemini's fix uses a function you don't know.** Ask it to explain the new formula step by step before you trust it — that is exactly the Lab 2 explain technique.

## Challenge

Ask Gemini for a single formula that returns the total for whichever region is currently the highest, so it updates automatically if the data changes.

## Reflection

LO2 — Use AI to build a multi-step formula, then diagnose and fix a broken one against a value you can confirm. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
