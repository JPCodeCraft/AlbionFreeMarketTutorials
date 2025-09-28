<!--
title: "Albion Online Crafting & Refining Calculator Tutorial"
summary: "Learn how to plan profitable crafting runs with Albion Free Market's Crafting & Refining Calculator."
author: "Albion Free Market"
createdAt: "2025-09-28"
updatedAt: "2025-09-28"
category: "tutorial"
tags: ["Craft Calculator", "Crafting", "Refining", "Economy"]
-->

# ALBION FREE MARKET CRAFTING & REFINING CALCULATOR TUTORIAL

- This tutorial is for the [Crafting & Refining Calculator](https://albionfreemarket.com/craft-calculator) in Albion Free Market.

## WHY USE THIS CALCULATOR?

- Plan crafting or refining batches before you ever touch a station. Know the costs, time, and focus you are about to spend.
- Keep every moving piece in sync: input prices, output markets, focus, fame, hauling weight, journals, and city bonuses.
- Track entire craft groups so you can repeat profitable runs, share setups with guildmates, or iterate on price changes quickly.

## BEFORE YOU START

- **Price data** comes from the Albion Online Data Project (AODP). Keep your data client running so refreshes stay accurate.
- **Masterpiece supporter perks** unlock saving craft groups, loading history, and storing spec profiles. Without it you can still experiment, but nothing persists between sessions.
- **Terminology reminders:** "Runs" equals how many times you craft a recipe, RRR stands for Resource Return Rate, and "Leftovers" are resources recovered by RRR.

## TAB-BY-TAB GUIDE

### INTRO TAB

- **What you see:** A friendly overview of the calculator, highlight cards for the biggest features, and links back to the legacy calculator and craft history.
- **Why start here:** It outlines the recommended flow—Load & Save → Setup → Inputs/Outputs → Specs → Results → Shopping/Selling—so you always know which tab fixes which problem.
- **Quick takeaway:** Give it a once-over the first time you use the tool, then jump straight into Load & Save for your day-to-day runs.

### LOAD & SAVE TAB

- **Save controls:**
  - `Save current craft group as new` stores your very first configuration; once saved, the same button swaps to `Update current craft group`.
  - `Save As New Copy` lets you branch a duplicate without touching the original.
  - The `Craft Group Name` field labels your setup (think "Brecilien T5 Bags" or "Caerleon Steel Bars").
  - All save buttons respect the slow-API guardrail and require **Masterpiece** support.
- **Load controls:**
  - `Load User Craft Groups` pulls every setup tied to your account (supporter-only).
  - Craft groups appear as cards showing their key products, number of crafts, and last updated time.
  - Each card offers `Load`, `Clone`, and `Delete` actions. Clone pulls a copy into the active session so you can test tweaks safely.
- **Craft history:**
  - `Load Done Crafts History` fills a sortable table with every "Done" batch you logged through Albion Free Market (supporter-only).
  - Columns cover the essentials: items crafted, server, total income vs. expenses, input/output weight, fame, focus, profit per focus, craft fees, overall profit %, and completion timestamp.
  - Clone any historic run straight back into the calculator or clear old records when you’re tidying up.

### SETUP TAB

- **General settings:**
  - Select your `Server`, choose how many `Average Days` of price history to reference (3–30), and toggle `Has Premium` so taxes and focus are correct.
  - `Reset` wipes the current craft group; the floating save button mirrors the Load & Save tab and still needs supporter access.
- **Adding crafts:**
  - `Add a Craft Group` opens a searchable list of every craftable item. Pick one or many; each adds a full craft entry to the table.
  - Filters narrow the table by `Tiers`, `Enchantments`, minimum daily sales, or quick toggles like Hide Missing Prices, Only Main Recipes, Hide Unselected Crafts, Hide Focus Info, Hide Fame Info, and Hide Consumables Picker.
  - A text filter helps when you already know the exact item name.
- **RRR management:**
  - Enable `Automatically calculate RRR` to let the calculator pull the correct resource return rate based on specs and city bonus.
  - Prefer manual? Leave it off and use `Use Calculated RRR (All)` as a one-time push wherever you still want suggested values.
- **Group summary & cleanup:**
  - At a glance you’ll see total crafts, how many are visible, how many are selected, and how many still need prices.
  - Category chips let you focus on one product family; you can also delete a whole category or remove every unused craft with one click.
  - Set your `Available Focus` budget, then auto-fill runs with `Runs = Daily Sell Avg` (uses market history) or `Runs = Max Available Focus` (splits your focus pool across active crafts).
- **Crafts table highlights:**
  - **Product:** Shows the item, daily sales velocity in your sell location, copy and price-check shortcuts, plus warnings if prices are missing.
  - **Craft Location:** Choose where you’ll craft or refine; propagate that choice to all crafts or just matching categories.
  - **Consumables:** Attach food/potions that affect production, set their quantities, and push the same setup to other rows.
  - **Runs:** Set how many batches you’ll craft. Propagation shortcuts cover all crafts, same category, or even crafts that share the same journal.
  - **Extra Expenses:** Add extra silver costs (transport, plot rent, guild cut) and reuse the number elsewhere.
  - **Weight:** Get input vs. output weight so you can plan hauling trips.
  - **Ignore Journals / Use Focus / No Sales Tax:** Toggle journal handling, focus usage, and taxes per craft. Every toggle has share-to-all and share-to-category buttons.
  - **RRR:** Override the resource return rate when auto mode is off. Propagation runs globally, per category, or to crafts using the same journal.
  - **Daily Bonus:** Pick the rotating city bonus that applies (e.g., "Martlock Smithing"). There’s even a shortcut that only copies to crafts sharing both category and location.
  - **Craft Fee Per Nutrition:** Input the station fee you recorded in-game and spread it across similar crafts instantly.
  - **Results columns:** Live totals for expenses, craft fame, fame per silver/focus, focus usage, craft fees, profit, and profit percentage.
  - **Craft checkbox:** Only checked rows feed the Results, Shopping List, and Selling List tabs—use it to park experimental crafts without deleting them.

### INPUTS TAB

- **Global actions:** Refresh prices from AODP, overwrite every buy price with the latest data, or sync leftover sell prices with what you pay. You can also hide unused inputs, show only missing prices, and toggle miniature price charts.
- **Filtering:** Category chips and a text filter make it easy to zoom in on one resource family or item.
- **Table essentials:**
  - **Item:** The material you need, with copy and market-check shortcuts.
  - **Amount (Leftovers):** Total amount required for all selected runs and how much you expect to get back through RRR.
  - **Buy Location:** Pick the city where you plan to purchase the material. Propagation buttons push that city to every input or just matching categories.
  - **Buy From:** Choose whether you’ll fill a sell order, place a buy order, or use average price. That choice drives AODP lookups and setup fee assumptions.
  - **AODP Price:** Live market price with age stamp and daily average. One click copies it into your user price.
  - **User Price:** Your custom buy price—perfect when you already have stockpiles or insider deals.
  - **Chart:** Optional sparkline using the calculator’s cached history so you can sanity-check price trends.
  - **Sell Leftovers To & Leftovers:** Decide how to liquidate recovered materials, pull fresh AODP values, and set your own sell price.
  - **Add to Crafts:** If the input itself is craftable, drop it straight into your craft group with the correct run count based on demand.

### OUTPUTS TAB

- **Global actions & filters:** Same layout as Inputs—refresh prices, push AODP data, hide unused entries, show charts, and filter by category or text.
- **Table essentials:**
  - **Item:** Finished product listing with copy/price buttons.
  - **Amount:** Total quantity you expect to craft from all selected runs.
  - **Sell Location:** Set where you plan to sell. Propagate the choice to every output or just the matching category.
  - **Sell To:** Pick sell order, buy order, or average price to define your exit strategy and fees.
  - **AODP Price:** Live price readout with age and volume data. Click once to copy it into your sell price.
  - **User Price:** Manual sell price for when you’re undercutting, overpricing, or logging private deals.
  - **Chart:** Snapshot of recent market movement in the chosen location so you can confirm the trend.

### SPECS TAB

- **Save & load:** Supporters can store spec profiles (`Save Specs`) and reload them later (`Load Specs`). Handy when you juggle multiple characters.
- **Tree view:** The calculator pulls every destiny board node relevant to your active crafts. Each node shows its icon and localized name.
- **Adjusting levels:** Type your current specialization level (0–120) into each field. Changing values triggers the calculator to recompute focus efficiency and RRR suggestions instantly.
- **Multiple crafts:** Specs are grouped by root tree (e.g., "Warrior Weapons"). Expand each and set the branches you actually own.

### RESULTS TAB

- **Category filter:** Chips let you focus on one product family when reviewing profitability.
- **Totals card:** See total income, expenses, input/output weight, fame, focus (with profit per focus), craft fees, and final profit at a glance. Profit numbers turn green for gains and red for losses.
- **Per-craft cards:** Every craft you marked as `Craft` gets a deep dive:
  - Income vs. expenses and percent profit.
  - RRR, input/output weight, fame, focus, and profit per focus.
  - **Inputs section:** Quantity used, leftover returns, where you buy them, unit price, setup fees, taxes, and net cost after leftovers.
  - **Outputs section:** Gross income, chosen sell location, fees, taxes, and net income.
  - **Additional costs:** Crafting fees, fixed costs, and extra expenses broken out clearly.
  - Copy and price-check buttons for quick follow-up in-game.
- **Missing crafts warning:** If nothing is selected in Setup, the tab nudges you to head back and tick the crafts you actually plan to run.

### SHOPPING LIST TAB

- **Category filter:** Focus on a material family if you’re staging the run in batches.
- **Grouped by buy location:** Each section represents a city or market, showing total weight so you can plan hauling capacity.
- **Per-item cards:**
  - Step counter (1, 2, 3…) to keep your itinerary organised.
  - Quantity, weight, buy order type, unit price, total cost before fees, leftover income, setup fees, sales taxes, and net spend.
  - Copy and price-check buttons for quick lookups while you’re at the market.
- **No data warning:** If nothing shows, double-check that your crafts are selected and resources aren’t filtered out.

### SELLING LIST TAB

- **Category filter:** Same chips as the shopping view so you can isolate one product line.
- **Grouped by sell location:** Each block represents the city you’ll sell in, complete with total weight for transport planning.
- **Per-item cards:**
  - Quantity, weight, sell order type, unit price, gross income, setup fees, sales taxes, and net income.
  - Copy and price-check shortcuts for quick posting and undercut checks.
- **Travel planning:** Use the weight totals to decide whether you need multiple trips, transport gear, or guild mamoths.

## NEXT STEPS

- Refresh prices before every crafting session—the market moves fast and old data ruins margins.
- Use the propagate buttons liberally; they keep large craft groups consistent without manual copy/paste.
- Once you finish a batch in-game, record it through Albion Free Market so the history table stays useful.
