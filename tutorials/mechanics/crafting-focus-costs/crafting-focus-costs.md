<!--
title: "How Crafting Specialization Reduces Focus Costs in Albion Online"
summary: "Focus Cost Efficiency, shared specialization bonuses, and the Focus needed to craft a T4.0 Broadsword."
author: "Albion Free Market"
createdAt: "2026-07-21"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Crafting", "Focus", "Specialization"]
-->

# How Crafting Specialization Reduces Focus Costs in Albion Online

Using Focus improves resource returns when crafting. The recipe has a base Focus cost, and your crafting levels reduce the amount you spend through Focus Cost Efficiency.

Focus Cost Efficiency is a rating. Adding 1,000 efficiency does not subtract 1,000 Focus from a recipe.

## The Focus cost formula

Every **10,000 Focus Cost Efficiency halves the base cost**:

```text
Focus cost = Base Focus cost × 0.5^(Efficiency / 10,000)
```

The exponent allows the same formula to work between the 10,000-point steps.

| Focus Cost Efficiency | Share of base cost paid |
| --- | ---: |
| 0 | 100% |
| 10,000 | 50% |
| 20,000 | 25% |
| 30,000 | 12.5% |
| 40,000 | 6.25% |

An additional 10,000 efficiency always halves the remaining cost. The absolute saving becomes smaller as your cost falls.

## Where efficiency comes from

An item can receive bonuses from its general crafting node, its own specialization, and the shared bonuses of other applicable specializations.

For a Broadsword, these contributions include:

| Node | Efficiency added per level when crafting a Broadsword |
| --- | ---: |
| Sword Crafter | 30 |
| Broadsword Crafting Specialist: shared sword bonus | 30 |
| Broadsword Crafting Specialist: Broadsword-specific bonus | 250 |
| Claymore Crafting Specialist: shared sword bonus | 30 |
| Dual Swords Crafting Specialist: shared sword bonus | 30 |

One level of Broadsword specialization therefore contributes **280 efficiency** to Broadsword crafting. One level of Claymore specialization contributes **30** to Broadswords through its shared bonus; its Claymore-specific bonus applies only to Claymores.

Other applicable nodes can also contribute. Their shared values can differ, so use each node's actual bonus rather than treating every specialization as another 30 points.

## Example: T4.0 Broadsword

An **Adept's Broadsword, T4.0**, has a base Focus cost of **1,286**. The following examples keep every contributing node at zero except those named in the table.

| Sword Crafter | Broadsword specialist | Claymore specialist | Total efficiency | Focus per Broadsword |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 0 | 0 | 300 | 1,259.53 |
| 50 | 50 | 0 | 15,500 | 439.18 |
| 100 | 100 | 0 | 31,000 | 149.99 |
| 100 | 100 | 100 | 34,000 | 121.83 |

For the third row:

```text
Efficiency = (100 × 30) + (100 × 280) = 31,000
Focus cost = 1,286 × 0.5^3.1 = 149.9851
```

The displayed values are formula results rounded to two decimal places. Use the whole-number Focus requirement shown in the crafting window when planning an exact batch.

### A fixed Focus budget

A budget of **9,000 Focus** supports approximately:

| Example above | Complete Broadswords within the budget |
| --- | ---: |
| Sword Crafter 10, no listed specializations | 7 |
| Sword Crafter 50 and Broadsword specialist 50 | 20 |
| Sword Crafter 100 and Broadsword specialist 100 | 60 |
| Both at 100, plus Claymore specialist 100 | 73 |

These counts assume enough materials for every craft and no other Focus use. The 34,000-efficiency example is a specific combination of nodes, not the maximum possible efficiency.

## Lower Focus cost and resource returns

At the same location and with the same production bonuses, both a low-specialization and a high-specialization crafter receive the same return rate when using Focus. The higher-specialization crafter spends less Focus to obtain that return on each item.

For example, ordinary Broadsword crafting in Lymhurst with Focus and no daily bonus has a **47.9167% resource return rate**. Raising Broadsword specialization makes that rate cheaper to use; it does not raise the percentage itself.

The silver value of saved Focus depends on the extra materials recovered and the crafts you can perform with it. A low Focus cost alone does not establish whether a recipe is profitable.

[Simple Craft Calculator](https://albionfreemarket.com/craft-calculator-simple) · [Full Craft Calculator](https://albionfreemarket.com/crafting) · [Your Specs](https://albionfreemarket.com/yourspecs)
