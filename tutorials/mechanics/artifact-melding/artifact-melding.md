<!--
title: "Artifact Melding Costs and Chances in Albion Online"
summary: "Artifact Foundry material costs, category probabilities, and a T4 Warrior rune-melding example with market prices."
author: "Albion Free Market"
createdAt: "2026-09-17"
updatedAt: "2026-09-19"
category: "tutorial"
tags: ["Game Mechanics", "Crafting", "Artifact Melding", "Economy"]
-->

# Artifact Melding Costs and Chances in Albion Online

Artifact melding turns runes, souls, relics, or Avalonian shards into a random artifact at the Artifact Foundry. Each meld produces one artifact from the selected pool.

You choose the material tier, material type, and category. Choosing a category narrows the possible results and uses more materials per attempt.

## Materials per meld

| Material | Any category | Warrior, Hunter, or Mage |
| --- | ---: | ---: |
| Runes | 36 | 50 |
| Souls | 36 | 50 |
| Relics | 36 | 50 |
| Avalonian shards | 36 | 50 |

Use materials of the tier you want to meld. The material type determines the artifact family available. Melding has no separate silver fee and does not receive crafting resource returns or Focus bonuses.

## Category choice and probabilities

For **T4 rune melding**, the pools are:

| Category | Possible artifacts | Chance of each artifact |
| --- | ---: | ---: |
| Any | 28 | 1/28 = 3.5714% |
| Warrior | 10 | 1/10 = 10% |
| Hunter | 9 | 1/9 = 11.1111% |
| Mage | 9 | 1/9 = 11.1111% |

The artifacts within each of these pools have equal weights. The Any pool gives each artifact the same chance; it does not first give each category a one-third chance.

For a particular Warrior artifact, selecting Warrior raises the chance from **3.5714% to 10%**. The average number of attempts until that artifact appears falls from **28 to 10**. In material terms, that is **1,008 runes on average with Any**, compared with **500 runes with Warrior**.

Those averages are not guarantees. Ten Warrior melds give a **65.1322%** chance of getting a particular Warrior artifact at least once:

```text
Chance in 10 attempts = 1 − (1 − 0.10)^10 = 65.1322%
```

## Example: T4 Warrior rune melding

This example uses **Bridgewatch on the Americas server**. The market snapshot was retrieved on **September 19, 2026**, with individual listings last observed on September 18–19. These are observed minimum sell prices; they can change and do not guarantee a sale or sufficient quantity.

A T4 Rune was listed at **10 silver**, so buying the materials outright costs:

```text
Cost per meld = 50 runes × 10 silver = 500 silver
```

All ten possible artifacts are Adept's artifacts. Each has a **10% chance**:

| Artifact | Observed sell price |
| --- | ---: |
| Morgana Halberd Head | 190 |
| Ancient Hammer Head | 213 |
| Ursine Guardian Remains | 145 |
| Lost Crossbow Mechanism | 135 |
| Ancient Chain Rings | 1,288 |
| Ancient Padding | 515 |
| Runed Rock | 125 |
| Bloodforged Blade | 86 |
| Ancient Shield Core | 42 |
| Ancient Bindings | 444 |

Because the chances are equal, add all ten prices and divide by ten:

```text
Average artifact value = 3,183 / 10 = 318.30 silver
Expected result before selling fees = 318.30 − 500 = −181.70 silver
```

### Selling fees

For a Premium character selling through sell orders, the setup fee is **2.5%** and the sales tax is **4%**. Assume each artifact is listed and sold individually at the observed price, with no relisting.

Round each fee up to whole silver. For a Bloodforged Blade sold at 86 silver, the setup fee is **3 silver** and the sales tax is **4 silver**, leaving **79 silver**.

Applying the same calculation to all ten outcomes gives:

| Result per meld | Expected silver |
| --- | ---: |
| Artifact value before fees | 318.30 |
| Setup fee and sales tax | 21.70 |
| Sale proceeds after fees | 296.60 |
| Rune purchase cost | 500.00 |
| Profit or loss | −203.40 |

At these prices, **100 melds consume 5,000 runes**, cost **50,000 silver**, and produce an expected loss of **20,340 silver** after the stated selling fees. Actual results depend on which artifacts appear and the prices achieved.

## Comparing choices

For any other pool, calculate each artifact's price multiplied by its probability, then add the results. Subtract material costs and applicable market fees.

A narrower pool helps when targeting a particular artifact, but its higher material cost can make it worse for selling random outputs. Compare the entire pool, including the low-value results.

[Artifact Melding Calculator](https://albionfreemarket.com/artifact-melding-calculator)
