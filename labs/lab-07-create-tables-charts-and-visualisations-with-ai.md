# Lab 7 — Create Tables, Charts and Visualisations with AI

**Topic 02:** Analysing and Automating Data with AI in Sheets  |  **Day 1**  |  **Approx. 55 min**  |  **Course:** Gemini for Google Sheet (C817)

## Scenario

Riverside Supplies is a small home-and-garden retailer. You have just been handed last quarter's orders as a single Google Sheet — hundreds of rows exported from the till system, with inconsistent text, mixed date formats and a few blank cells. Your manager wants the quarter's numbers and a chart by the end of the day. Across this course you use Gemini AI in Google Sheets to turn that messy export into clean, analysed, charted data you can trust. Use this scenario only if you cannot use a real spreadsheet from your own workplace; your own non-confidential data is always preferred.

## Goal

Use AI to build a summary/pivot table and the right, clearly labelled chart to tell the data's story.

## What you'll build

A verified pivot table plus a labelled column chart and a monthly-trend line chart.

**Tools and techniques:** Gemini side panel, pivot tables, Insert > Chart, chart types, chart formatting

## Prerequisites

- Lab 6 complete — you have verified figures to check your charts against.

## Steps

### Step 1

Ask AI which summary table best shows sales performance and how to build it.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
I want to see total sales by Region and by month. What pivot table should I build, and what are the steps in Google Sheets?
```

### Step 2

Build the pivot (Insert > Pivot table): Rows = Region, Columns = month of Order Date, Values = SUM of Total.

### Step 3

Verify one cell of the pivot against a SUMIFS you write for that same region and month.

### Step 4

Ask AI to recommend the best chart to compare sales across regions.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
What is the best chart type to compare total sales across Regions, and why?
```

### Step 5

Insert the chart: select the region totals, then Insert > Chart, and set the recommended type (for example a column chart).

### Step 6

Ask AI to improve it, then apply the suggestions — a clear title, axis labels, and bars sorted highest to lowest.

Prompt to give Gemini (paste into the Ask Gemini panel):

```text
Suggest a clear title and axis labels for a column chart of total sales by Region, sorted highest to lowest.
```

### Step 7

Add a second chart for the monthly trend: a line chart of total sales by month.

### Step 8

Check the trend chart matches the direction you found in your Lab 6 analysis.

## Test it

You have a pivot table whose figures you verified against a formula, a labelled column chart of sales by region sorted high-to-low, and a line chart of the monthly trend consistent with your Lab 6 analysis.

## Troubleshooting

- **The pivot totals don't match your Lab 6 figures.** Check the Values field is SUM of Total (not COUNT), and that the pivot's source range covers all rows including any added in cleaning.
- **The chart plots the wrong series.** Select only the summary cells (labels + one value column) before Insert > Chart, or edit the chart's data range in the Chart editor > Setup.
- **The column chart isn't sorted high-to-low.** Sort the summary table the chart is built on; charts follow their source order. Or ask Gemini for the exact sort steps.

## Challenge

Ask Gemini which single chart would best tell your manager the quarter's story in one glance, build it, and give it a headline title that states the finding.

## Reflection

LO6 — Use AI to build a summary/pivot table and the right, clearly labelled chart to tell the data's story. In your own words, how will you use this in your own spreadsheets, and how will you check the AI got it right?

## Deliverable

Save your work — it becomes part of your cleaned, analysed **Riverside Supplies** sheet, the single dataset you complete and validate in Lab 8.

---

*Gemini for Google Sheet (C817) · C817 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
