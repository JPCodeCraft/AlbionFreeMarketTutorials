<!--
title: "How Crafting Quality Chances Work in Albion Online"
summary: "Base quality chances, additional quality rolls, and expected Broadsword quality with specialization and Focus."
author: "Albion Free Market"
createdAt: "2026-08-14"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Crafting", "Item Quality", "Focus"]
-->

# How Crafting Quality Chances Work in Albion Online

When you craft equipment, its quality is selected from Normal, Good, Outstanding, Excellent, and Masterpiece. Crafting quality bonuses give additional chances to roll, and the item keeps the best result.

These rolls happen when the item is created. Paid quality rerolls after crafting use a different set of probabilities.

## The base quality roll

One crafting quality roll has these chances:

| Quality | Chance |
| --- | ---: |
| Normal | 68.9% |
| Good | 25% |
| Outstanding | 5% |
| Excellent | 1% |
| Masterpiece | 0.1% |

A quality bonus changes how many rolls you receive. It does not directly add percentage points to the Masterpiece chance.

## Additional rolls

Start with one roll. Each complete **100 points of crafting quality bonus** adds another guaranteed roll. The remaining points give a chance of one further roll.

| Total quality bonus | Rolls per item |
| --- | --- |
| 0 | 1 |
| 50 | 1, with a 50% chance of a second |
| 100 | 2 |
| 150 | 2, with a 50% chance of a third |
| 750 | 8, with a 50% chance of a ninth |
| 800 | 9 |

An additional roll can leave the final quality unchanged or improve it. It cannot replace a better result with a worse one.

Using **Focus adds 50 quality bonus points** to ordinary equipment crafting. Applicable crafting nodes and crafting-quality food bonuses contribute to the same total.

## Calculating the chance of a quality goal

If one roll has chance `p` of reaching your desired quality or better, the chance of doing so in `n` rolls is:

```text
Chance of desired quality or better = 1 − (1 − p)^n
```

For Masterpiece, `p = 0.001`. Two rolls therefore give:

```text
Masterpiece chance = 1 − 0.999² = 0.1999%
```

For Excellent or better, include both Excellent and Masterpiece in the base chance: **1% + 0.1% = 1.1%**.

When an extra roll is only partly guaranteed, combine the two outcomes. A 50% chance of that extra roll means taking the average of the results with and without it.

## Example: crafting T4.0 Broadswords

Take an **Adept's Broadsword, T4.0**, with **Sword Crafter at 100** and **Broadsword Crafting Specialist at 100**. Set all other contributing crafting nodes to zero and use no quality food.

The quality bonus is:

| Contribution | Calculation | Quality bonus |
| --- | --- | ---: |
| Sword Crafter | 100 × 0.75 | 75 |
| Broadsword specialist: shared sword bonus | 100 × 0.75 | 75 |
| Broadsword specialist: Broadsword-specific bonus | 100 × 6 | 600 |
| Total without Focus | 75 + 75 + 600 | 750 |
| Total with Focus | 750 + 50 | 800 |

Without Focus, each item gets eight rolls and a 50% chance of a ninth. With Focus, every item gets nine rolls.

### Expected results from 100 crafts

The following quantities are averages. Because the batch contains 100 items, each number also represents that quality's percentage chance.

| Quality | Without Focus: 750 bonus | With Focus: 800 bonus |
| --- | ---: | ---: |
| Normal | 4.2890 | 3.4992 |
| Good | 54.3076 | 53.2540 |
| Outstanding | 32.4314 | 33.7714 |
| Excellent | 8.1252 | 8.5790 |
| Masterpiece | 0.8468 | 0.8964 |

The expected share of **Excellent or better** rises from **8.9720% to 9.4754%**. The Masterpiece chance rises from **0.8468% to 0.8964%**.

An expected 0.8964 Masterpieces per 100 crafts does not mean every batch produces one. At those settings, the chance of at least one Masterpiece in a 100-item batch is approximately **59.3613%**.

## Applying the numbers

Higher quality bonuses improve the distribution, but the result remains random. Price a crafting batch using the expected mix of qualities rather than treating every item as Excellent or Masterpiece.

Focus also changes resource returns. That material saving is a separate benefit from the quality improvement shown here. Extra rolls only apply where the crafted item supports those quality levels.

[Simple Craft Calculator](https://albionfreemarket.com/craft-calculator-simple) · [Full Craft Calculator](https://albionfreemarket.com/crafting)
