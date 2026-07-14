<!--
title: "How Albion Online Repair Costs Are Calculated"
summary: "Learn the current Albion Online repair formula, including Item Value, missing durability, the repair modifier, server multiplier, and rounding."
author: "Albion Free Market"
createdAt: "2026-07-14"
updatedAt: "2026-07-14"
category: "tutorial"
tags: ["Game Mechanics", "Repair Costs", "Item Value", "Economy"]
-->

# How Albion Online Repair Costs Are Calculated

Repair cost in Albion Online is not based on an item's market price. An inexpensive artifact can be costly to repair, while an expensive high-quality item can have the same repair bill as its Normal-quality version. The reason is that Albion uses a hidden number called **Item Value**.

If you only need an estimate, add your damaged items to the [Albion Free Market Repair Cost Calculator](https://albionfreemarket.com/repaircost). If you want to calculate the cost yourself, this guide explains the current formula, how Item Value is determined, and where rounding changes the result.

## The Current Repair Formula

For each physical item:

```text
Repair cost =
ceil(Item Value × missing durability fraction × 16.5 × server multiplier)
```

If you enter damage as a percentage number, such as `5` rather than `0.05`, the same formula can be written as:

```text
Repair cost = ceil(Item Value × damage percentage × 0.165 × server multiplier)
```

The total for several items is:

```text
Total repair cost = sum of each separately rounded item cost
```

| Variable | Meaning |
| --- | --- |
| `Item Value` | Hidden game-defined economic value of the item |
| `Missing durability fraction` | Percentage to restore divided by 100 |
| `16.5` | Current repair Silver modifier from Albion game data |
| `Server multiplier` | Current global multiplier for Americas, Asia, or Europe |
| `ceil` | Always round upward to the next whole Silver |

The complete current data rule clamps the damage fraction between 0 and 1. In practice, that simply means damage cannot be below 0% or above 100%.

## Damage Percentage Means the Amount Missing

The calculator expects the durability that must be restored, not the durability that remains.

```text
Damage percentage = 100% - current condition
```

Examples:

| Current condition | Damage to enter |
| ---: | ---: |
| 100% | 0% |
| 95% | 5% |
| 92.5% | 7.5% |
| 40% | 60% |
| 0% | 100% |

AFM accepts damage from 0% to 100% with up to two decimal places. Its default of 5% is only a convenient starting value; replace it with the actual missing durability of the item.

Maximum durability points are not part of the Silver formula. A value such as `13,500 durability` determines how the item wears down, but the repair calculation uses the percentage missing.

## Current Game-Data Modifiers

Albion's current repair data provides these values:

| Game-data value | Current number | Purpose |
| --- | ---: | --- |
| Lower cost factor | 0 | Minimum damage fraction |
| Upper cost factor | 1 | Maximum damage fraction |
| Silver modifier | 16.5 | Converts Item Value and damage into Silver |

These are game-data values and can change in a future patch. The AFM calculator reads the current data rather than relying on an old formula.

You may still find older Albion repair calculations based on `Item Value / 7`. That is not the formula used by the current game-data implementation and should not be used for present estimates.

## The Server Global Multiplier

The last part of the formula is a global multiplier for the selected Albion server. Americas, Asia, and Europe can have slightly different values, and those values can change over time.

The examples in this guide use `1.156` as an illustrative snapshot. Do not treat it as a permanent constant. The [Repair Cost Calculator](https://albionfreemarket.com/repaircost) applies the latest available multiplier for the server selected in your AFM settings.

Market activity and an item's own market price do not determine this multiplier. It is a separate server-wide value obtained from Albion.

## What Is Item Value?

Item Value is a hidden economic value stored in Albion's item data. It is used by several game systems, but it is not the same as any of these:

- Current sell order price.
- Current buy order price.
- Average market price or EMV.
- Item Power.
- Durability points.
- The Silver and focus spent when crafting.

Some items have a direct Item Value in the game data. For other items, AFM resolves the value from their crafting ingredients:

```text
Item Value =
sum(ingredient Item Value × ingredient quantity) / amount crafted
```

If an ingredient also lacks a direct value, the same process is repeated through its own recipe. No intermediate rounding is required; only the final Silver repair cost is rounded upward.

Crafting fees, focus, Resource Return Rate, nutrition, laborer journals, and market taxes do not enter this calculation.

## Refined Material Item Values

Normal refined resources currently follow a particularly useful pattern:

```text
Refined material Item Value = 2^(tier + enchantment)
```

| Tier | `.0` | `.1` | `.2` | `.3` | `.4` |
| --- | ---: | ---: | ---: | ---: | ---: |
| T2 | 4 | — | — | — | — |
| T3 | 8 | — | — | — | — |
| T4 | 16 | 32 | 64 | 128 | 256 |
| T5 | 32 | 64 | 128 | 256 | 512 |
| T6 | 64 | 128 | 256 | 512 | 1,024 |
| T7 | 128 | 256 | 512 | 1,024 | 2,048 |
| T8 | 256 | 512 | 1,024 | 2,048 | 4,096 |

For standard equipment, multiply the value in this table by the quantities of refined materials in the recipe and add the results.

This pattern is a shortcut for normal refined materials in current data, not a replacement for checking the actual Item Value of artifacts, tokens, mounts, special items, or unusual recipes.

## Standard Equipment Example: T4 Broadsword

A T4 Broadsword uses:

- 16 T4 Metal Bars.
- 8 T4 Leather.
- Each T4.0 refined material has Item Value 16.

Its Item Value is therefore:

```text
Item Value = (16 bars × 16) + (8 leather × 16)
           = 256 + 128
           = 384
```

Now suppose the Broadsword has 5% missing durability and the example server multiplier is `1.156`:

```text
Repair cost = ceil(384 × 0.05 × 16.5 × 1.156)
            = ceil(366.2208)
            = 367 Silver
```

The item's market price could be 5,000 Silver or 500,000 Silver and the result would still be 367 Silver under those same repair conditions.

## How Enchantment Changes Repair Cost

There is no separate “enchantment repair multiplier.” Enchantment changes the crafting recipe to use enchanted materials, and those materials have higher Item Values.

For example, a T4.1 Broadsword still uses 24 total refined materials, but each T4.1 material has Item Value 32:

```text
T4.1 Broadsword Item Value = 24 × 32 = 768
```

That is twice the T4.0 Item Value, so its repair cost is approximately twice as high before final rounding.

Tier works in the same indirect way. Higher-tier materials have higher Item Values; there is no additional tier coefficient in the repair formula.

## How Artifacts Change Repair Cost

Artifact equipment adds the Item Value of its artifact or special component to the normal material value. The artifact is simply another recipe ingredient; there is no separate artifact percentage.

For example, a T4 Clarent Blade has:

- Base refined-material value: `384`.
- Artifact component value: `96`.
- Total Item Value: `480`.

At 5% damage with the same example server multiplier:

```text
Repair cost = ceil(480 × 0.05 × 16.5 × 1.156)
            = ceil(457.776)
            = 458 Silver
```

This is why two weapons with the same tier and similar market prices can have different repair costs. Artifact, Avalonian, Crystal, Fey, Royal, and other special components can contribute different Item Values.

For these items, using the AFM calculator is more reliable than trying to maintain a large artifact-value list by hand.

## Quality Does Not Affect Repair Cost

Normal, Good, Outstanding, Excellent, and Masterpiece versions of the same item share the same Item Value.

Quality can strongly affect market price and Item Power, but it does not add anything to the repair formula. A Masterpiece T4 Broadsword and a Normal T4 Broadsword with the same missing durability have the same repair cost.

EMV is also not an input. AFM displays `Repair / EMV` only to help you judge whether repairing an item makes economic sense.

## Why Every Physical Item Must Be Rounded Separately

Repair cost is rounded upward for each physical item before the costs are added.

Using the T4 Broadsword example, one sword costs `367 Silver` to repair. Two separate swords cost:

```text
ceil(384 × 0.05 × 16.5 × 1.156)
+ ceil(384 × 0.05 × 16.5 × 1.156)

= 367 + 367
= 734 Silver
```

Combining the two Item Values first gives the wrong answer:

```text
ceil(768 × 0.05 × 16.5 × 1.156)
= ceil(732.4416)
= 733 Silver
```

The one-Silver difference comes entirely from rounding. When repairing several physical items, calculate each one independently, even when they are identical and have the same damage percentage.

## What Affects Repair Cost?

| Factor | Effect |
| --- | --- |
| Missing durability percentage | Directly multiplies the cost |
| Item Value | Directly multiplies the cost |
| Server global multiplier | Directly multiplies the cost |
| Tier | Indirect effect through material Item Values |
| Enchantment | Indirect effect through enchanted material Item Values |
| Artifact or special component | Its Item Value is added through the recipe |
| Quantity | Each physical item is calculated and rounded separately |

## What Does Not Affect Repair Cost?

- **Quality:** It changes Item Power and market price, not Item Value.
- **Maximum durability points:** Only the percentage missing is used.
- **Market price and EMV:** They are useful for deciding whether to repair, but not for calculating the fee.
- **Premium status:** There is no Premium term in the formula.
- **City or location:** There is no city-specific term.
- **Crafting station fee, focus, or Resource Return Rate:** These do not change Item Value.
- **Overcharge:** There is no separate overcharge coefficient; only the resulting missing durability matters.
- **Awakened traits, strain, and attunement:** They do not add an instance-specific repair modifier. The underlying item's tier, enchantment, recipe, and damage still apply.

## Common Calculation Mistakes

- Entering remaining condition instead of missing durability.
- Using market price in place of Item Value.
- Applying an extra quality, tier, or artifact percentage that does not exist.
- Treating maximum durability points as part of the formula.
- Combining several items before rounding.
- Using the old `Item Value / 7` estimate.
- Hardcoding a server multiplier copied from an old example.

## Calculate a Complete Repair Bill Automatically

Manual calculation is practical for a normal item when you know its recipe. Artifact equipment, special items, mixed enchantments, and multiple damaged pieces are easier to handle with the [Albion Free Market Repair Cost Calculator](https://albionfreemarket.com/repaircost).

The calculator loads current Item Values and repair modifiers, applies the selected server multiplier, rounds every physical item correctly, compares the result with EMV, and creates a shareable URL for the complete repair list.

The essential rule is simple: repair cost comes from **Item Value and missing durability**, not from what the item is currently worth on the market.
