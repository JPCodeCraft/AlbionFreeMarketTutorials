<!--
title: "How Crafting Station Fees Are Calculated in Albion Online"
summary: "Silver per 100 nutrition, Item Value, and the usage fee for one Broadsword or a batch of 100."
author: "Albion Free Market"
createdAt: "2026-09-10"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Crafting", "Station Fees", "Item Value"]
-->

# How Crafting Station Fees Are Calculated in Albion Online

A crafting station's usage fee is quoted in **silver per 100 nutrition**. The number on the station is a rate; the charge for your craft depends on how much nutrition that recipe consumes.

For ordinary equipment crafting, nutrition consumption is calculated from Item Value. Market prices do not enter this calculation.

## Nutrition consumption

The nutrition factor is **0.1125 per point of Item Value**:

```text
Nutrition consumed = Item Value × 0.1125 × Items crafted
```

Item Value is a fixed game value. For equipment whose value is derived from its recipe, add the ingredients' Item Values multiplied by their quantities, then account for the number of items the recipe produces.

The fee calculation is:

```text
Usage fee = Nutrition consumed × Station rate / 100
```

Calculate with full precision before rounding the final silver charge. The examples below round the result to the nearest whole silver.

## Example: T4.0 Broadsword

An **Adept's Broadsword, T4.0**, requires **16 Steel Bars and 8 Worked Leather**. Each of those materials has an Item Value of **16**.

```text
Broadsword Item Value = (16 × 16) + (8 × 16) = 384
Nutrition per Broadsword = 384 × 0.1125 = 43.2
```

At a station charging **500 silver per 100 nutrition**, one Broadsword costs:

```text
Usage fee = 43.2 × 500 / 100 = 216 silver
```

The quoted rate is 500, but this recipe uses only 43.2 nutrition, so its fee is 216 silver.

### Comparing station rates

These are example station rates applied to the real Broadsword recipe, not current offers from particular stations.

| Station rate per 100 nutrition | Calculated fee for one Broadsword | Rounded fee for one Broadsword | Fee for 100 Broadswords |
| ---: | ---: | ---: | ---: |
| 100 silver | 43.2 | 43 | 4,320 |
| 500 silver | 216 | 216 | 21,600 |
| 1,000 silver | 432 | 432 | 43,200 |

For 100 Broadswords at the 500 rate:

```text
Nutrition = 384 × 0.1125 × 100 = 4,320
Usage fee = 4,320 × 500 / 100 = 21,600 silver
```

The batch totals use the unrounded nutrition and fee. Multiplying an already rounded one-item fee can introduce a difference; at the 100 rate, 100 × 43 gives 4,300 instead of the calculated batch fee of 4,320. Separate crafting transactions may also round separately.

## What changes the fee?

**Item Value and quantity:** More nutrition means a larger fee. Higher tiers or enchantments can increase Item Value. Two items with very different market prices can still have the same fee if their Item Values match.

**The station rate:** Use the rate that applies to you at that station, including an associate rate if you qualify. Compare stations using the final fee for your recipe and quantity.

**The number of crafts:** Each additional craft consumes nutrition. If you use returned resources to make more items, those extra crafts have their own usage fees.

## What resource returns do not change

The fee is based on the craft's full nutrition requirement. Resource returns reduce net material consumption; they do not reduce the nutrition charged for the same number of items.

For example, crafting 100 T4.0 Broadswords at a station rate of 500 costs **21,600 silver** both with and without Focus. Focus changes the materials returned and your Focus consumption, while the station's usage fee remains the same.

This article covers the ordinary nutrition-based crafting usage fee. Any recipe-specific silver charge is additional. Tier 1 and Tier 2 items are exempt from the ordinary usage fee.

The total cost of producing and selling an item can also include materials, quality rerolls, market setup fees, and sales tax. Keep those expenses separate when comparing station charges.

[Simple Craft Calculator](https://albionfreemarket.com/craft-calculator-simple) · [Full Craft Calculator](https://albionfreemarket.com/crafting)
