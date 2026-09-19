<!--
title: "How Resource Return Rate Is Calculated in Albion Online"
summary: "Production bonuses, Focus, and resource returns explained with a T4.0 Broadsword crafting example."
author: "Albion Free Market"
createdAt: "2026-07-17"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Crafting", "Refining", "Resource Return Rate"]
-->

# How Resource Return Rate Is Calculated in Albion Online

Resource Return Rate is the share of eligible materials returned when you craft or refine. A 25% return rate means that, over many crafts, you recover about one quarter of those materials.

The production bonus shown for a location is used to calculate that rate. A 25% production bonus does not mean a 25% resource return.

## From production bonus to return rate

Add the applicable production bonuses first, then calculate the return rate:

```text
Return rate = Production bonus / (100 + Production bonus)
```

Enter the production bonus as a percentage number. For a combined bonus of 33:

```text
Return rate = 33 / 133 = 24.8120%
```

The distinction comes from reusing returned resources. With a 33% production bonus, enough eligible materials for 100 crafts can support about 133 crafts if returns are repeatedly reused. This is an average over many crafts; individual returns and whole-item recipe requirements affect the final result.

## Which bonuses apply?

For ordinary equipment crafting in a Royal city, the main contributions are:

| Bonus | Production bonus added |
| --- | ---: |
| Royal city base | 18 percentage points |
| Matching city crafting specialization | 15 percentage points |
| Using Focus | 59 percentage points |
| Applicable daily production bonus | The announced bonus |

The specialized refining bonus is 40 percentage points in the matching Royal city. That gives 58% total production bonus before Focus or a daily bonus, equivalent to a 36.7089% return rate.

City specializations depend on the item being made. Islands and hideouts use their own location rules. An island does not receive the Royal city's 18-point base bonus, and hideout bonuses depend on the location and hideout power.

Specialization levels reduce the Focus needed for a craft. They do not increase its resource return rate when the location and Focus setting stay the same.

## Example: T4.0 Broadswords

An Adept's Broadsword requires **16 Steel Bars and 8 Worked Leather**. Lymhurst has a sword crafting bonus; Thetford does not.

These rates apply to the same recipe:

| Location and settings | Combined production bonus | Resource return rate |
| --- | ---: | ---: |
| Thetford, no Focus | 18% | 15.2542% |
| Lymhurst, no Focus | 18% + 15% = 33% | 24.8120% |
| Thetford, with Focus | 18% + 59% = 77% | 43.5028% |
| Lymhurst, with Focus | 18% + 15% + 59% = 92% | 47.9167% |
| Lymhurst, Focus and a +20% sword production day | 112% | 52.8302% |

The last row is an example of a matching bonus day, not a statement about today's bonus. A bonus for a different item category does not apply.

### Materials for 100 crafts

The gross recipe requirement for 100 Broadswords is **1,600 Steel Bars and 800 Worked Leather**. In Lymhurst, the expected returns and net consumption are:

| Material | Returned without Focus | Net consumed without Focus | Returned with Focus | Net consumed with Focus |
| --- | ---: | ---: | ---: | ---: |
| Steel Bars | 396.99 | 1,203.01 | 766.67 | 833.33 |
| Worked Leather | 198.50 | 601.50 | 383.33 | 416.67 |

For example, the focused Steel Bar calculation is:

```text
Returned bars = 1,600 × (92 / 192) = 766.67
Net consumed = 1,600 − 766.67 = 833.33 bars
```

These are expected averages. You receive whole resources, and each crafting action still requires its full recipe quantities to be available. Returned materials can fund later crafts in the batch.

## What the return rate does not cover

Use the rate only for ingredients that the recipe can return. Some recipes return additional finished products instead of ingredients, so their output must be handled differently.

Station fees, market fees, and the purchase cost of ingredients remain separate expenses. A better return rate reduces material consumption, but the cheapest overall location also depends on those expenses.

[Resource Return Rate Calculator](https://albionfreemarket.com/resource-return-rate-calculator) · [Simple Craft Calculator](https://albionfreemarket.com/craft-calculator-simple) · [Full Craft Calculator](https://albionfreemarket.com/crafting)
