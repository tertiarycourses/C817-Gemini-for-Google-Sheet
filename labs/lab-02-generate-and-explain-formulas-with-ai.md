# Lab 2 — Generate and Explain Formulas with AI

**Topic 01:** Getting Started with AI in Google Sheets  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Use AI to generate a spreadsheet formula from a plain-language description, and to explain an existing formula.

## What you'll build

A working, AI-generated Total column and grand total, each verified, plus a plain-English explanation of a formula.

**Tools and techniques:** Gemini side panel, formula generation, formula explanation, SUM, IF

## Prerequisites

- Lab 1 complete — your own copy of the sheet open with the Gemini panel available.

## Steps

### Step 1

Click cell I2 (Total). Ask Gemini for a formula that multiplies Quantity by Unit Price.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Write a Google Sheets formula for cell I2 that multiplies Quantity in G2 by Unit Price in H2.
```

### Step 2

Paste the formula into I2 and fill it down the column (double-click the small square at the cell's bottom-right).

Formula (paste into the cell):

```text
=G2*H2
```

### Step 3

Verify: pick any row and check by hand that Quantity x Unit Price equals the Total shown.

### Step 4

Ask AI for one formula that totals the whole Total column into cell K1.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Write a formula for cell K1 that gives the grand total of the Total column I2:I200.
```

### Step 5

Paste it into K1 and read the result.

Formula (paste into the cell):

```text
=SUM(I2:I200)
```

### Step 6

Cross-check: select I2:I200 and read the Sum shown in the status bar at the bottom-right — it should match K1.

### Step 7

Learn from a formula: paste this into the Gemini panel and ask it to explain, step by step.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Explain what this formula does, step by step: =IF(G2>=10,"Bulk","Standard")
```

### Step 8

Read the explanation and write one sentence in your notes on what =IF does.

## Test it

The Total column is filled with a verified formula, K1 equals the status-bar Sum of I2:I200, and you can explain in one sentence what the =IF formula does.

## Troubleshooting

- **Your pasted formula shows as text, not a result.** Make sure the cell is empty and the entry starts with '='. Remove any surrounding quotes or spaces Gemini may have added.
- **The fill-down stops early or fills the wrong range.** Select I2, then double-click the fill handle; if it stops, select I2:I200 and use Ctrl+D to fill down.
- **K1 doesn't match the status-bar Sum.** Check your SUM range covers every data row (I2:I200) and no more; a stray value below the data will throw it off.

## Challenge

Ask Gemini for a formula that flags any row where Total is blank, then use it to find the rows you will fill in Lab 5.

## Reflection

LO2 — Use AI to generate a spreadsheet formula from a plain-language description, and to explain an existing formula. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
