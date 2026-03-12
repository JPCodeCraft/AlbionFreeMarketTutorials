<!--
title: "Albion Online Bandit Assault Times for Every Server"
summary: "Bandit Assault start times and trigger chances for the Americas, Asia, and Europe servers, plus a side-by-side comparison table."
author: "Albion Free Market"
createdAt: "2026-03-12"
updatedAt: "2026-03-12"
category: "article"
tags: ["Faction Warfare", "Bandit Assault", "Guides"]
-->

# Albion Online Bandit Assault Times for Every Server

Bandit Assault is one of Albion Online's biggest Faction Warfare events in the red zones, and the trigger windows are different on the Americas, Asia, and Europe servers. This guide gives you the raw UTC schedule from Albion's game data, along with the configured chance for a Bandit Assault to start at each window.

## What Bandit Assault Is

Bandit Assault starts with Caerleon taking control of the Outposts in all five lethal Provinces. From there, every faction races to generate Bandit Assault Supplies by capturing Outposts, clearing Faction Camps, and opening Faction Chests.

In the second phase, the event narrows to two non-adjacent red-zone Provinces. Those zones become the main objective, with fortress chest fights deciding a large part of the final standings and rewards.

Bandit Assault is a great opportunity to transport goods from the royal cities to the Black Market or Caerleon, since most PvP players in the red zones will be instantly targeted by faction-flagged blobs.

## How Bandit Assault Triggers

The game files define fixed daily windows when a Bandit Assault roll can happen, and each window has its own trigger chance. The times below come from `times.xml`, `times_asia.xml`, and `times_europe.xml`, while the percentages come from the matching `factionwarfareredzoneevent` XML files.

All times below are shown in **UTC**. These tables intentionally use the raw XML times and **ignore** the `offsetseconds="-900"` values.

## Bandit Assault Times Comparison

This table makes it easier to compare the trigger chance on each server at the same UTC hour.

| UTC Time | Americas | Asia | Europe |
| --- | --- | --- | --- |
| 01:00 UTC | 60% | - | 30% |
| 02:00 UTC | - | 30% | - |
| 03:00 UTC | 60% | - | 20% |
| 05:00 UTC | 40% | 30% | 20% |
| 07:00 UTC | 20% | 50% | 20% |
| 09:00 UTC | - | 60% | 0% |
| 11:00 UTC | 20% | 40% | 40% |
| 13:00 UTC | 30% | 60% | 50% |
| 15:00 UTC | 30% | 60% | 50% |
| 17:00 UTC | 40% | 60% | 60% |
| 19:00 UTC | 50% | 30% | 60% |
| 21:00 UTC | 50% | 20% | 60% |
| 23:00 UTC | 60% | - | 50% |

## Americas Server Bandit Assault Times

| UTC Time | Chance to Trigger |
| --- | --- |
| 01:00 UTC | 60% |
| 03:00 UTC | 60% |
| 05:00 UTC | 40% |
| 07:00 UTC | 20% |
| 11:00 UTC | 20% |
| 13:00 UTC | 30% |
| 15:00 UTC | 30% |
| 17:00 UTC | 40% |
| 19:00 UTC | 50% |
| 21:00 UTC | 50% |
| 23:00 UTC | 60% |

## Asia Server Bandit Assault Times

| UTC Time | Chance to Trigger |
| --- | --- |
| 02:00 UTC | 30% |
| 05:00 UTC | 30% |
| 07:00 UTC | 50% |
| 09:00 UTC | 60% |
| 11:00 UTC | 40% |
| 13:00 UTC | 60% |
| 15:00 UTC | 60% |
| 17:00 UTC | 60% |
| 19:00 UTC | 30% |
| 21:00 UTC | 20% |

## Europe Server Bandit Assault Times

| UTC Time | Chance to Trigger |
| --- | --- |
| 01:00 UTC | 30% |
| 03:00 UTC | 20% |
| 05:00 UTC | 20% |
| 07:00 UTC | 20% |
| 09:00 UTC | 0% |
| 11:00 UTC | 40% |
| 13:00 UTC | 50% |
| 15:00 UTC | 50% |
| 17:00 UTC | 60% |
| 19:00 UTC | 60% |
| 21:00 UTC | 60% |
| 23:00 UTC | 50% |

The Europe server currently includes a 09:00 UTC slot in the XML with a 0% trigger chance, so it is effectively disabled unless Albion changes the configuration.

## Sources

- Official overview: https://albiononline.com/news/feature-focus-bandit-assault
- Americas data: https://github.com/ao-data/ao-bin-dumps/blob/master/factionwarfareredzoneevent.xml and https://github.com/ao-data/ao-bin-dumps/blob/master/times.xml
- Asia data: https://github.com/ao-data/ao-bin-dumps/blob/master/factionwarfareredzoneevent_asia.xml and https://github.com/ao-data/ao-bin-dumps/blob/master/times_asia.xml
- Europe data: https://github.com/ao-data/ao-bin-dumps/blob/master/factionwarfareredzoneevent_europe.xml and https://github.com/ao-data/ao-bin-dumps/blob/master/times_europe.xml
