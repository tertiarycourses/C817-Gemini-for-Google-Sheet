# Lab 5 — Clean, Transform and Organise Data with AI

**Topic 02:** Analysing and Automating Data with AI in Sheets  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Use AI to standardise messy text and dates, tidy fields, and organise the dataset into a clean table.

## What you'll build

A cleaned, consistently formatted Orders table ready for analysis.

**Tools and techniques:** Gemini side panel, TRIM, PROPER, CLEAN, date formatting, Data > Sort range

## Prerequisites

- Lab 4 complete — you have a prompt pattern to reuse here.
- A backup: File > Make a copy before you start, so you can compare before/after cleaning.

## Steps

### Step 1

Ask AI how to standardise the Region column so 'north', 'North ' and 'NORTH' all become 'North'.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Give me a formula for column J that returns column D with consistent capitalisation and no leading or trailing spaces.
```

### Step 2

Put the formula in J2 and fill it down; check that a few previously messy rows now read cleanly.

Formula (paste into the cell):

```text
=PROPER(TRIM(D2))
```

### Step 3

Lock the fix in: copy column J, then Edit > Paste special > Values only over column D, and delete the helper column J.

### Step 4

Ask AI to standardise the Order Date column to YYYY-MM-DD, and follow its steps (Format > Number > Date, or the formula it gives).

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Column B has dates in mixed formats. How do I make them all display as YYYY-MM-DD in Google Sheets?
```

### Step 5

Verify a couple of dates against what they clearly should be, and confirm none turned blank or wrong.

### Step 6

Tidy the Product column: ask AI for a formula to trim extra spaces and fix capitalisation, apply it, and paste values back as in step 3.

Formula (paste into the cell):

```text
=TRIM(E2)
```

### Step 7

Organise the data: select A1:I200 and use Data > Sort range (with 'Data has header row' ticked) to sort by Order Date, ascending.

### Step 8

Ask Gemini to check your work.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Look at the Orders tab. Are there any remaining blank cells, inconsistent categories or duplicate Order IDs I should fix?
```

## Test it

The Region and Product columns are consistent, all Order Dates display as YYYY-MM-DD, the data is sorted by date, and Gemini's check reports no remaining obvious issues (or you have fixed the ones it named).

## Troubleshooting

- **Paste special > Values only pasted formulas instead of values.** Use Edit > Paste special > Values only (not a plain Ctrl+V). The pasted cells should show text, not '=' formulas.
- **Some dates won't convert to YYYY-MM-DD.** Those cells are stored as text. Ask Gemini for a formula using DATEVALUE (or Split text to columns) to turn text dates into real dates first.
- **PROPER capitalises something it shouldn't (e.g., 'NW' region code).** Tell Gemini the exception and ask for a formula that leaves known codes uppercase, or fix those few cells by hand.

## Challenge

Ask Gemini to find and highlight duplicate Order IDs, then decide with a rule (keep the first, remove the rest) and apply it.

## Reflection

LO4 — Use AI to standardise messy text and dates, tidy fields, and organise the dataset into a clean table. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
