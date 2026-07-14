<!--
title: "How Albion Online Teleport Costs Are Calculated"
summary: "Learn the Albion Online Travel Planner formula, including item weight, travel factors, city distance, server multipliers, and rounding."
author: "Albion Free Market"
createdAt: "2026-07-14"
updatedAt: "2026-07-14"
category: "tutorial"
tags: ["Game Mechanics", "Teleport Costs", "Travel Planner", "Economy"]
-->

# How Albion Online Teleport Costs Are Calculated

Teleporting between cities can save a lot of time, but the Travel Planner's price is not based only on the weight shown in your inventory. Every item also has a hidden travel cost factor, and the game applies a route distance and a server-wide multiplier before showing the final Silver cost.

If you only need the result, add your luggage to the [Albion Free Market Teleport Calculator](https://albionfreemarket.com/teleport-calculator). If you want to understand or reproduce the calculation yourself, this guide explains every part of the math.

## The Teleport Cost Formula

Albion calculates each distinct item stack separately:

```text
One-distance stack cost =
ceil(150 × unit weight × travel cost factor × quantity × server multiplier)

Stack route cost = one-distance stack cost × route distance

Total teleport cost = sum of all stack route costs
```

`ceil` means always round upward to the next whole Silver. Even a calculated value of `500.01` becomes `501` Silver.

In a shorter mathematical form:

```text
Total = Σ [ceil(150 × W × F × Q × G) × D]
```

| Symbol | Meaning |
| --- | --- |
| `W` | Weight of one item in kilograms |
| `F` | The item's hidden travel cost factor |
| `Q` | Quantity of that item |
| `G` | Current global multiplier for your Albion server |
| `D` | Route distance: 1 or 2 |
| `150` | Base Silver charged per effective kilogram and distance |

Market price, Item Value, Estimated Market Value (EMV), quality, and Item Power are not part of this formula.

## Route Distance Between Cities

The five Royal Cities form a ring:

```text
Thetford → Fort Sterling → Lymhurst → Bridgewatch → Martlock → Thetford
```

Neighboring cities on this ring have distance 1. Every other pair of Royal Cities has distance 2. Every supported route involving Brecilien also has distance 2.

| From / To | Thetford | Fort Sterling | Lymhurst | Bridgewatch | Martlock | Brecilien |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Thetford** | — | 1 | 2 | 2 | 1 | 2 |
| **Fort Sterling** | 1 | — | 1 | 2 | 2 | 2 |
| **Lymhurst** | 2 | 1 | — | 1 | 2 | 2 |
| **Bridgewatch** | 2 | 2 | 1 | — | 1 | 2 |
| **Martlock** | 1 | 2 | 2 | 1 | — | 2 |
| **Brecilien** | 2 | 2 | 2 | 2 | 2 | — |

There are no directional differences: Thetford to Fort Sterling costs the same as Fort Sterling to Thetford for identical luggage.

This formula and the AFM calculator cover the supported luggage routes between these cities. Caerleon, starter towns, islands, hideouts, Outlands rests, and Smuggler Network destinations are outside the calculator's scope.

## Weight and Effective Weight

The Travel Planner does not use your character's percentage load. It uses the weight of the actual items you are moving.

That means:

- A better bag does not make teleporting cheaper.
- A mount's carrying capacity does not make teleporting cheaper.
- Pork Pie and carry-weight passives do not make teleporting cheaper.
- Your mount, bag, equipped gear, consumables, and inventory items must all be included if you are taking them with you.

For most equipment and ordinary items, the travel factor is 1, so effective weight equals normal weight. Special economic items can have much higher factors.

```text
Effective weight = unit weight × travel factor × quantity
```

Two inventories with the same displayed weight can therefore have very different teleport prices.

## Resource Weights and Travel Factors

Raw and refined resources follow a consistent pattern in current game data. Enchantment does not change their unit weight, but it increases their travel factor.

| Base tier | Unit weight | `.0` factor | `.1` | `.2` | `.3` | `.4` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| T1 | 0.15 kg | 1 | — | — | — | — |
| T2 | 0.23 kg | 1 | — | — | — | — |
| T3 | 0.34 kg | 1 | — | — | — | — |
| T4 | 0.51 kg | 2 | 4 | 8 | 16 | 32 |
| T5 | 0.76 kg | 4 | 8 | 16 | 32 | 64 |
| T6 | 1.14 kg | 8 | 16 | 32 | 64 | 128 |
| T7 | 1.71 kg | 16 | 32 | 64 | 128 | 256 |
| T8 | 2.56 kg | 32 | 64 | 128 | 256 | 256 |

For T4 and above, the current resource data follows this pattern:

```text
Resource travel factor = min(2^(tier + enchantment - 3), 256)
```

For example, a T6.2 resource has an effective tier of `6 + 2 = 8`, giving a factor of `2^(8 - 3) = 32`. The factor is capped at 256, which is why T8.4 remains at 256 rather than increasing to 512.

This is a pattern in the current item data, not a universal formula that should be applied to every Albion item.

## Other Important Travel Factors

Most weapons, armor, bags, capes, mounts, food, potions, and ordinary items use factor 1. The main exceptions are economic items that the game intentionally makes expensive to teleport.

### Laborer Journals

Crafting journals for Blacksmiths, Fletchers, Imbuers, and Tinkerers use these factors:

| Tier | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Travel factor** | 58 | 35 | 51 | 51 | 68 | 115 | 211 |

Gathering journals for Lumberjacks, Stonecutters, Prospectors, Croppers, and Gamekeepers use much larger factors at higher tiers:

| Tier | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Travel factor** | 58 | 89 | 154 | 204 | 410 | 985 | 1,966 |

Empty and full versions inherit the same weight and factor. Fishing, Mercenary, and trophy journals currently use the default factor of 1.

### Luxury Goods and Special Items

| Item group | Travel factor |
| --- | ---: |
| Luxury goods — rarity 1 | 3 |
| Luxury goods — rarity 2 | 7 |
| Luxury goods — rarity 3 | 27 |
| Avalonian Energy | 16 |
| Faction city hearts | 256 |

These grouped values are more practical than maintaining a list of thousands of individual items. For an unusual item, use its current game-data value through the AFM calculator.

## The Server Global Multiplier

The global multiplier is a server-wide Albion value. Americas, Asia, and Europe can have slightly different multipliers, and the numbers can change over time.

Do not permanently assume that the multiplier is 1. AFM reads the latest available multiplier for your selected server and applies it automatically. When calculating manually, use the current value rather than copying an old example from a guide.

The examples below use `1.156` only as an illustrative snapshot.

## Worked Example: T4 Ore

Suppose you want to teleport 10 T4 Ore from Thetford to Fort Sterling.

- Unit weight: `0.51 kg`
- Travel factor: `2`
- Quantity: `10`
- Server multiplier used in this example: `1.156`
- Route distance: `1`

First calculate effective weight:

```text
0.51 × 2 × 10 = 10.2 effective kg
```

Then calculate and round the one-distance cost:

```text
ceil(10.2 × 150 × 1.156)
= ceil(1,768.68)
= 1,769 Silver
```

Because the route distance is 1, the final cost is `1,769 Silver`.

If the same luggage traveled on a distance-2 route, the game would multiply after rounding:

```text
1,769 × 2 = 3,538 Silver
```

## Worked Example: Enchanted Resources

Now consider 20 T6.2 resources on a distance-2 route, using the same example multiplier.

- Unit weight: `1.14 kg`
- T6.2 resource factor: `32`
- Quantity: `20`
- Route distance: `2`

```text
Effective weight = 1.14 × 32 × 20 = 729.6 kg

One-distance cost = ceil(729.6 × 150 × 1.156)
                  = ceil(126,512.64)
                  = 126,513 Silver

Route cost = 126,513 × 2
           = 253,026 Silver
```

The physical stack weighs only `22.8 kg`, but its effective teleport weight is `729.6 kg` because of the hidden factor. This is why looking only at inventory weight produces the wrong answer for enchanted resources.

## Rounding Multiple Items Correctly

The Travel Planner rounds each distinct item entry before adding the total. If you carry Ore, Cloth, a mount, and a bag, calculate and round those four entries separately.

The correct order is:

1. Group identical items and apply their quantity.
2. Multiply by weight, factor, 150, and the server multiplier.
3. Round that item entry upward.
4. Multiply by route distance.
5. Repeat for the other items and add the results.

Do not round a one-unit cost and then multiply by quantity. Do not combine all effective weights and round only once. Do not multiply by distance before rounding.

## What Does Not Affect Teleport Cost?

- **Market price and EMV:** Used by AFM only to compare the teleport fee with the item's economic value.
- **Quality:** Normal and Masterpiece versions of the same item have the same teleport cost.
- **Equipment enchantment:** Ordinary `.0` through `.4` equipment inherits the same weight and factor. Enchanted resources are different because their own game-data factors increase.
- **Durability and repair state:** Damaged gear does not become cheaper to teleport.
- **Item Power, mastery, and awakened traits:** None of these enter the formula.
- **Carry capacity:** Bags, mounts, food, and passives change what you can carry, not what the Travel Planner charges.

## Common Calculation Mistakes

- Using total inventory weight without applying each item's travel factor.
- Treating the travel factor as an increase to market value instead of effective weight.
- Forgetting that T8.4 resource factors are capped at 256.
- Using the wrong side of the Royal City ring when deciding whether distance is 1 or 2.
- Hardcoding an old server multiplier.
- Rounding once at the end instead of once per distinct item.
- Forgetting to include equipped items and the mount being transported.

## Calculate a Complete Inventory Automatically

Manual calculations are useful for understanding the system or checking a specific trade. For a real transport with mixed items, use the [Albion Free Market Teleport Calculator](https://albionfreemarket.com/teleport-calculator). It loads current item weights and travel factors, applies the selected server's multiplier, handles route distance and rounding, and creates a shareable URL for the complete setup.

The most important rule to remember is that teleport cost is based on **effective weight**, not market price and not simply the kilograms shown in your inventory.
