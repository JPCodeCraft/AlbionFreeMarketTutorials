<!--
title: "Quality Reroll Costs and Chances in Albion Online"
summary: "Quality reroll costs and probabilities, with a T4.0 Broadsword example from Normal to Excellent."
author: "Albion Free Market"
createdAt: "2026-09-19"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Item Quality", "Crafting"]
-->

# Quality Reroll Costs and Chances in Albion Online

A quality reroll is a paid attempt to improve an item's quality. The five qualities are Normal, Good, Outstanding, Excellent, and Masterpiece.

A reroll can keep the current quality or improve it, including skipping quality levels. It cannot lower quality. A Normal item always improves on its first reroll. Masterpiece is the highest quality and cannot be rerolled further.

Every attempt costs silver, including attempts that leave quality unchanged.

## Cost per attempt

The cost depends on the item's Item Value, the server's Global Multiplier, and its quality before the attempt:

```text
Reroll cost = Item Value × Global Multiplier × quality modifier
```

Item Value is a fixed game value, separate from the item's market price. The Global Multiplier is a server-specific value that can change over time.

| Current quality | Cost modifier |
| --- | ---: |
| Normal | 4.4 |
| Good | 5.5 |
| Outstanding | 6.6 |
| Excellent | 27.5 |

The price increases when the item reaches a higher quality. Repeated attempts at the same quality have the same cost while the Global Multiplier remains unchanged.

## Chances per attempt

Each row shows the possible results of one reroll from the listed quality. All values are percentages.

| Current quality | Good | Outstanding | Excellent | Masterpiece |
| --- | ---: | ---: | ---: | ---: |
| Normal | 80% | 15% | 4.95% | 0.05% |
| Good | 30% | 60% | 9.925% | 0.075% |
| Outstanding | 0% | 50% | 49.9% | 0.1% |
| Excellent | 0% | 0% | 99.5% | 0.5% |

For example, an Outstanding item has a 50% chance to remain Outstanding, a 49.9% chance to become Excellent, and a 0.1% chance to become Masterpiece. Its chance of reaching Excellent or better in that attempt is therefore 50%.

If an attempt leaves the quality unchanged, the next attempt has the same odds. Previous failures do not improve those odds.

## Example: T4.0 Broadsword, Normal to Excellent

This example uses an **Adept's Broadsword, T4.0**, on the **Americas** server. Start at Normal and stop as soon as it reaches Excellent or Masterpiece.

The Broadsword has an **Item Value of 384**. Its recipe uses 16 Steel Bars and 8 Worked Leather, each with an Item Value of 16:

```text
Item Value = (16 × 16) + (8 × 16) = 384
```

The Americas Global Multiplier was **1.156 on September 19, 2026**. Using that value gives these costs per attempt. Silver amounts are calculated at full precision and displayed to two decimal places.

| Current quality | Calculation | Silver per attempt |
| --- | --- | ---: |
| Normal | 384 × 1.156 × 4.4 | 1,953.18 |
| Good | 384 × 1.156 × 5.5 | 2,441.47 |
| Outstanding | 384 × 1.156 × 6.6 | 2,929.77 |
| Excellent | 384 × 1.156 × 27.5 | 12,207.36 |

The Excellent fee applies only if you continue toward Masterpiece. This example stops at Excellent or better, so that fee is never paid.

One possible sequence is:

1. Normal → Good: **1,953.18 silver**.
2. Good → Outstanding: **2,441.47 silver**.
3. Outstanding → Excellent: **2,929.77 silver**.

That sequence costs **7,324.42 silver**. Other sequences cost different amounts: the first attempt might reach Excellent immediately, or several attempts might leave the item at Good or Outstanding.

### Average cost and chance of success

Continuing until Excellent or better takes an average of **3.8143 attempts** and costs approximately **9,640.33 silver per item**. This includes the different possible paths and their changing attempt costs. The Broadsword's purchase or crafting cost is additional.

Stopping immediately on success gives these chances of reaching Excellent or better within a given number of attempts:

| Attempts allowed | Chance of Excellent or better |
| --- | ---: |
| 3 | 50.65% |
| 5 | 85.3585% |
| 10 | 99.5051% |
| 16 | 99.9922% |

An item that succeeds early needs no further attempts. The average cost is not a spending limit: an individual item can cost more or less. No finite number of attempts guarantees success.

## Quality and enchantment upgrades

Enchantment upgrades preserve an item's quality. Reroll costs use the Item Value of the item at the time of the attempt. If an enchantment upgrade increases that value, doing the same quality rerolls afterward costs more.

For an item you intend to enchant, compare rerolling before the upgrade with buying the desired quality directly. The reroll expense is only one part of the total cost.

[Simple Craft Calculator](https://albionfreemarket.com/craft-calculator-simple) · [Full Craft Calculator](https://albionfreemarket.com/crafting)
