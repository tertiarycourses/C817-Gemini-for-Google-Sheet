# Lab 1 — Set Up and Access Gemini AI in Google Sheets

**Topic 01:** Getting Started with AI in Google Sheets  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Open the sample sheet, make your own copy, open the Gemini side panel, and run a first AI prompt on the data.

## What you'll build

Your own copy of the Riverside Supplies sheet in Drive, with Gemini open and a first answer verified.

**Tools and techniques:** Google Sheets, Google Drive, Gemini side panel (Ask Gemini)

## Prerequisites

- A Google account with access to Google Sheets and Google Drive.
- Gemini in Google Sheets enabled on your account — the trainer confirms this at the start of the day.
- Chrome or Edge, signed in to the correct Google account.

## Steps

### Step 1

Open the sample 'Riverside Supplies — Q1 Orders' sheet from the link the trainer shares.

### Step 2

Make it yours: File > Make a copy, and save it to your Drive as 'Riverside Supplies — Q1 Orders (<YOUR NAME>)'.

### Step 3

Look at the Orders tab: note the columns Order ID, Order Date, Customer, Region, Product, Category, Quantity, Unit Price, Total — and that some cells are messy. You will fix those later.

### Step 4

Open the Gemini side panel — click 'Ask Gemini' (the sparkle, top-right). If you cannot see it, tell the trainer; access is confirmed at the start of the day.

### Step 5

Ask a first, read-only question to confirm Gemini can see your data.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
How many rows of orders are in the Orders tab, and what does each column mean?
```

### Step 6

Check the answer: compare the row count Gemini gives against the row count shown at the bottom-left of the sheet.

### Step 7

Ask one follow-up so you see Gemini use the data.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Which 3 products appear most often in the Orders tab?
```

### Step 8

Confirm nothing changed — asking Gemini a question is read-only. You have now seen the ask-check loop safely.

## Test it

You have your own copy of the sheet in Drive, the Gemini panel open, and a first answer whose row count matches the count shown at the bottom of the sheet.

## Troubleshooting

- **You can't see 'Ask Gemini' in the toolbar.** Tell the trainer — Gemini access is provisioned per account. While you wait, follow the demo and pair with a neighbour who has access.
- **'Make a copy' is greyed out.** You must be signed in to your own Google account. Sign in, re-open the shared link, then File > Make a copy.
- **Gemini's row count doesn't match the sheet.** Ask again naming the tab and range explicitly ('in the Orders tab, range A2:I200'); Gemini may have counted a header row or an empty trailing row.

## Challenge

Ask Gemini to describe the range of Order Dates in the sheet (earliest and latest) — still read-only — and confirm it against what you can see when you sort the column.

## Reflection

LO1 — Open the sample sheet, make your own copy, open the Gemini side panel, and run a first AI prompt on the data. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
