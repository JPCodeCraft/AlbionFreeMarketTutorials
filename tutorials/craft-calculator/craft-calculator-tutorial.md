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

- This tutorial is for the [Crafting & Refining Calculator](https://albionfreemarket.com/crafting) in Albion Free Market.

## WHY USE THIS CALCULATOR?

- Plan crafting or refining batches before you ever touch a station. Know the costs, profit, and focus you are about to spend.
- Keep every moving piece in sync: input prices, output markets, focus, fame, hauling weight, journals, and city bonuses.
- Track entire craft groups so you can repeat profitable runs or iterate on price changes quickly.

## BEFORE YOU START

- **Price data** comes from the Albion Online Data Project (AODP). Keep your data client running so refreshes stay accurate.
- **Masterpiece supporter perks** unlock saving craft groups, loading history, and storing spec profiles. Without it you can still experiment, but nothing persists between sessions.
- **Terminology reminders:** "Runs" equals how many times you craft a recipe, RRR stands for Resource Return Rate, and "Leftovers" are resources recovered by RRR that will be in your inventory after the crafting session is done.

## TAB-BY-TAB GUIDE

### INTRO TAB

- **What you see:** A friendly overview of the calculator, highlight cards for the biggest features, and links back to the legacy calculator and craft history.
- **Why start here:** It outlines the recommended flow: Load & Save → Setup → Inputs/Outputs → Specs → Results → Shopping/Selling, so you always know which tab fixes which problem.
- **Quick takeaway:** Give it a once-over the first time you use the tool, then jump straight into Load & Save for your day-to-day runs.

### LOAD & SAVE TAB

- **Save controls:**
  - `Save current craft group as new` stores your very first configuration; once saved, the same button swaps to `Update current craft group`, which is used to save changes to an existing craft group.
  
<img width="269" height="170" alt="image" src="https://github.com/user-attachments/assets/34df1828-1efe-442f-b3c1-735ca5fc79b3" />

  - `Save As New Copy` lets you branch a duplicate without touching the original.

<img width="423" height="180" alt="image" src="https://github.com/user-attachments/assets/d31dcd17-86e5-4f06-9bd4-ceb0191631a7" />

  - The `Craft Group Name` field labels your setup (think "Brecilien T5 Bags" or "Caerleon Steel Bars").
  - All save buttons require **Masterpiece** support.
- **Load controls:**
  - `Load User Craft Groups` pulls every setup tied to your account (supporter-only).
  - Craft groups appear as cards showing their key products, number of crafts, and last updated time.
  - Each card offers `Load`, `Clone`, and `Delete` actions. Clone pulls a copy into the active session so you can test tweaks safely.
 
<img width="1288" height="606" alt="image" src="https://github.com/user-attachments/assets/063f33f0-59fd-4623-8579-45f33da86ed4" />

- **Craft history:**
  - `Load Done Crafts History` fills a sortable table with every "Done" batch you logged through Albion Free Market (supporter-only).
  - Columns cover the essentials: items crafted, server, total income vs. expenses, input/output weight, fame, focus, profit per focus, craft fees, overall profit %, and completion timestamp.
  - Clone any historic run straight back into the calculator or clear old records when you’re tidying up.

<img width="1690" height="921" alt="image" src="https://github.com/user-attachments/assets/6a76ae27-f85e-40fe-967b-2947208159d0" />

### SETUP TAB

- **General settings:**
  - Select your `Server`, choose how many `Average Days` of price history to reference (3–30), and toggle `Has Premium` so taxes are correct.
  - `Reset` wipes the current craft group; the floating save button mirrors the Load & Save tab for easy access.

<img width="892" height="169" alt="image" src="https://github.com/user-attachments/assets/72a8100e-9c73-4593-b26a-72148d7178d4" />

- **Adding crafts:**
  - `Add a Craft Group` opens a searchable list of every craftable item. Pick one or many; each adds a full craft entry to the table. We always show the highest tier item, and once you click it all tiers will be added to the `Crafts Table`.

 <img width="469" height="260" alt="image" src="https://github.com/user-attachments/assets/eb1bd11d-3254-4a09-83dd-e54dfd557bf5" />

  - Filters narrow the `Crafts Table` by `Tiers`, `Enchantments`, minimum daily sales, or quick toggles like Hide Missing Prices, Only Main Recipes, Hide Unselected Crafts, Hide Focus Info, Hide Fame Info, and Hide Consumables Picker.
  - A text filter helps when you already know the exact item name.

<img width="1356" height="193" alt="image" src="https://github.com/user-attachments/assets/cf9571a0-0d37-47ea-a30e-221d54a92d4e" />

- **RRR management:**
  - Enable `Automatically calculate RRR` to let the calculator pull the correct resource return rate based on specs and city bonus. This should work correctly for every crafting condition excep `Hideouts Crafting`.

 <img width="443" height="125" alt="image" src="https://github.com/user-attachments/assets/9c0a5b2c-bee2-4c2d-ae22-fbe7e84fbdad" />

  - Leave it off to manually enter RRR's. You can use `Use Calculated RRR (All)` as a one-time push wherever you still want suggested values.

<img width="472" height="143" alt="image" src="https://github.com/user-attachments/assets/7a2683ac-2919-4c15-983d-da51baae197e" />

- **Group summary & cleanup:**
  - At a glance you’ll see total crafts, how many are visible, how many are selected, and how many still need prices.
  - Category chips let you filter one product family; you can also delete a whole category or remove every unused craft with one click.
  - The red cleaning button removes all the crafts that are not marked as `Craft` from the table. You should only use this if you prefer a cleaner table. But it's best to leave all crafts in the table, so you can easily compare profits.
 
<img width="408" height="145" alt="image" src="https://github.com/user-attachments/assets/aae5f376-7fc3-4661-87de-c0918f758b83" />

  - Set your `Available Focus` budget, then auto-fill runs with `Runs = Daily Sell Avg` (uses market history) or `Runs = Max Available Focus` (sets the runs of crafts marked as `Use Focus` to the maximum amount to use all your focus).

<img width="635" height="69" alt="image" src="https://github.com/user-attachments/assets/395b259e-f5f5-4aa8-8e8f-44c7e63e643c" />

- **Crafts table highlights:**
  - **Product:** Shows the item, daily sales velocity in your sell location, copy and price-check shortcuts, plus warnings if prices are missing.
  - **Craft Location:** Choose where you’ll craft or refine; propagate that choice to all crafts or just matching categories.
  - **Consumables:** Attach food/potions that affect production, set their quantities, and push the same setup to other rows.
  - **Runs:** Set how many batches you’ll craft. Propagation shortcuts cover all crafts, same category, or even crafts that share the same journal. One run means one crafting action ingame, which usually results in 1 item output, but can be more, like `Potions` that output 5 per run.
  - **Extra Expenses:** Add extra silver costs (transport, plot rent, guild cut) and reuse the number elsewhere, if you want.
  - **Weight:** Get input vs. output weight so you can plan hauling trips.
  - **Ignore Journals / Use Focus / No Sales Tax:** Toggle journal handling, focus usage, and taxes per craft. Every toggle has share-to-all and share-to-category buttons. You should use `No Sales Taxes` if you're not selling via the market.
  - **RRR:** Override the resource return rate when auto mode is off. Propagation runs globally, per category, or to crafts using the same journal.
  - **Daily Bonus:** Pick the rotating city bonus, if available. There’s even a shortcut that only copies to crafts sharing both category and location.
  - **Craft Fee Per Nutrition:** Input the station fee you recorded in-game and spread it across similar crafts instantly.
  - **Results columns:** Live totals for expenses, craft fame, fame per silver/focus, focus usage, craft fees, profit, and profit percentage.
  - **Craft checkbox:** Only checked rows feed the Results, Shopping List, and Selling List tabs. You should check the `Craft` box if you plan to actually craft that item.

<img width="2421" height="701" alt="image" src="https://github.com/user-attachments/assets/e3144059-7d64-41b0-b8f1-1735bc340e22" />

### INPUTS TAB

- **Global actions:**
  - Refresh prices from AODP: this loads the prices from AODP. If an item has no price set, it will use the loaded price. If there's already a price, it won't overwrite. This loads up both buy, sell and average prices.
  - Set all prices to AODP: forces overwrite of every buy price with the latest data.
  - Set all leftover prices to user prices: Force sync leftover sell prices with what you pay.
  - Checkboxes to hide unused inputs (inputs that are not used in any of the crafts that you marked as `Craft`, show only missing prices, and toggle miniature price charts.
 
<img width="483" height="123" alt="image" src="https://github.com/user-attachments/assets/6d84d03b-8ead-4ba9-b033-0151c87bedb7" />

- **Filtering:** Category chips and a text filter make it easy to zoom in on one resource family or item.

<img width="1681" height="584" alt="image" src="https://github.com/user-attachments/assets/8421b9f9-1f83-4dd4-9736-65a1c7c108ed" />

- **Table essentials:**
  - **Item:** The material you need, with copy and market-check shortcuts.
  - **Amount (Leftovers):** Total amount required for all selected runs and how much you expect to have left in your inventory after you craft.
  - **Buy Location:** Pick the city where you plan to purchase the material. Propagation buttons push that city to every input or just matching categories.
  - **Buy From:** Choose whether you’ll fill a sell order, place a buy order, or use average price. That choice drives AODP lookups and setup fee assumptions. If you buy from sell order, there's no setup fee. If you buy from a buy order or average price, there is setup fee.
  - **AODP Price:** Live market price with age stamp and daily average. One click copies it into your user price.
  - **User Price:** Your custom buy price. You should fill this with the price you actually paid for the items.
  - **Chart:** Optional sparkline using the calculator’s cached history so you can sanity-check price trends. Very important to check if your prices makes sense.
  - **Sell Leftovers To & Leftovers:** Decide how to liquidate recovered materials, pull fresh AODP values, and set your own sell price.
  - **Add to Crafts:** If the input itself is craftable, drop it straight into your craft group with the correct run count based on demand. You can use this to do `cascade crafting`, like if you want to refine from T4 to T6, using the outputs of a craft as inputs in another craft.

<img width="2035" height="803" alt="image" src="https://github.com/user-attachments/assets/afc59995-df9e-487a-a75c-114202871fd0" />

### OUTPUTS TAB

- **Global actions & filters:** Same layout as Inputs: refresh prices, push AODP data, hide unused entries, show charts, and filter by category or text.

<img width="501" height="287" alt="image" src="https://github.com/user-attachments/assets/e907a730-bac1-4975-88bb-ee3db2639a17" />


- **Table essentials:**
  - **Item:** Finished product listing with copy/price buttons.
  - **Amount:** Total quantity you expect to craft from all selected runs.
  - **Sell Location:** Set where you plan to sell. Propagate the choice to every output or just the matching category.
  - **Sell To:** Pick sell order, buy order, or average price to define your exit strategy and fees.
  - **AODP Price:** Live price readout with age and volume data. Click once to copy it into your sell price.
  - **User Price:** Manual sell price. You should set the price you actually sold it for in here.
  - **Chart:** Snapshot of recent market movement in the chosen location so you can confirm the trend.

<img width="2186" height="653" alt="image" src="https://github.com/user-attachments/assets/7a78887a-e254-4ed1-af28-63161aeb6536" />

### SPECS TAB

- **Save & load:** Supporters can store spec profiles (`Save Specs`) and reload them later (`Load Specs`).
- **Tree view:** The calculator pulls every destiny board node relevant to your active crafts. Each node shows its icon and localized name.
- **Adjusting levels:** Type your current specialization level into each field. Changing values triggers the calculator to recompute focus efficiency instantly.

<img width="1585" height="878" alt="image" src="https://github.com/user-attachments/assets/64b4618d-39e7-432e-86d4-2a55a0d772e8" />

### RESULTS TAB

- **Category filter:** Chips let you focus on one product family when reviewing profitability.
- **Totals card:** See total income, expenses, input/output weight, fame, focus (with profit per focus), craft fees, and final profit at a glance. Profit numbers turn green for gains and red for losses.

<img width="2266" height="424" alt="image" src="https://github.com/user-attachments/assets/f9afa5d0-63da-46ae-9968-ab10793169db" />

- **Per-craft cards:** Every craft you marked as `Craft` gets a deep dive:
  - Income vs. expenses and percent profit.
  - RRR, input/output weight, fame, focus, and profit per focus.
  - **Inputs section:** Quantity used, leftover returns, where you buy them, unit price, setup fees, taxes, and net cost after leftovers.
  - **Outputs section:** Gross income, chosen sell location, fees, taxes, and net income.
  - **Additional costs:** Crafting fees, fixed costs, and extra expenses broken out clearly.
  - Copy and price-check buttons for quick follow-up in-game.
 
<img width="2268" height="1069" alt="image" src="https://github.com/user-attachments/assets/40d3c4d6-e6f5-40f1-915d-90cf55c093b5" />

### SHOPPING LIST TAB

- **Category filter:** Focus on a material family if you’re staging the run in batches.
- **Grouped by buy location:** Each section represents a city or market, showing total weight so you can plan hauling capacity.
- **Per-item cards:**
  - Quantity, weight, buy order type, unit price, total cost before fees, leftover income, setup fees, sales taxes, and net spend.
  - Copy and price-check buttons for quick lookups while you’re at the market.

  <img width="2124" height="1001" alt="image" src="https://github.com/user-attachments/assets/ae539c95-5a02-47a8-80d7-0e90d1237bef" />

### SELLING LIST TAB

- **Category filter:** Same chips as the shopping view so you can isolate one product line.
- **Grouped by sell location:** Each block represents the city you’ll sell in, complete with total weight for transport planning.
- **Per-item cards:**
  - Quantity, weight, sell order type, unit price, gross income, setup fees, sales taxes, and net income.
- **Travel planning:** Use the weight totals to decide whether you need multiple trips, transport gear, or guild mamoths.

  <img width="2118" height="1006" alt="image" src="https://github.com/user-attachments/assets/7a3c277c-2936-4f6b-9892-6f5704ed0743" />

## GENERAL HINTS

- Refresh prices before every crafting session! The market moves fast and old data ruins margins.
- Use the propagate buttons liberally; they keep large craft groups consistent without manual copy/paste.
- Once you finish a batch in-game, record it through Albion Free Market (`Save Craft as Done`).
