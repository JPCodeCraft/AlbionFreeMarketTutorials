<!--
title: "Albion Online Black Market Flipper Tutorial"
summary: Learn how to profit in Albion Online by flipping items from the regular markets to the black market.
author: "Albion Free Market"
date: "2024-07-19"
category: "tutorial"
tags: ["black market", "flipper"]
-->

# ALBION FREE MARKET FLIPPER TUTORIAL

- This collection of tutorials is for the [Black Market Flipper](https://albionfreemarket.com/flipper) in Albion Free Market.

## BASICS

### What exactly is a flip?

- The Black Market Flipper tool is used to find **single-use**, **instant** flips.
- By single-use, we mean that the flip can be utilized only once. This is not the place to look for daily transport trade routes.
- By instant, we mean that you buy an item from a sell order in a normal market and instantly sell the item to a buy order on the Black Market.

### Where's the price data coming from?

- The price data is provided by [The Albion Online Data Project](https://www.albion-online-data.com/).
- To get your data uploaded, make sure to use the client that can be downloaded at their webpage.
- Alternatively, you can also use the [Albion Free Market Data Client](https://github.com/JPCodeCraft/AlbionDataAvalonia/releases). This project is an alternative to the official AODP client and provides essentially the same functionality, but has a graphical interface that might make it easier to use.
- Both clients work by _sniffing_ network traffic and collecting market data. If you feel insecure about this, you can check the source code and realize that no private data is uploaded anywhere.

### How are flips found?

- Flips are found by comparing every single market order that goes to AODP's database.
- Albion Free Market holds sell orders for 60 minutes and buy orders for 30 minutes. This is done to reduce the number of _false positives_, where the system might think an order is available but in fact it's already been consumed ingame.

### What does it mean to consume a flip?

- Consuming a flip has the following effects:
  - The orders used in that flip are market as consumed, so every flip that uses any of those orders are also considered consumed
  - The flip is sent to your _Consumed Flips (this session)_ table, so you can easily track them
- Notice that even thought a flip has already been consumed, it's still visible for all users. That's done to avoid _trolling_, where an ill intended user might consumed multiple flips to make them disapear. So, it is possible that a consumed flip is still available.
- If after 10 minutes of consuming an order, that same order is seen by the system again, it's then marked as unconsumed, which reflects on the status of the flips that use it.

#### Is this allowed?

> _Our position is quite simple. As long as you just look and analyze we are ok with it. The moment you modify or manipulate something or somehow interfere with our services we will react (e.g. perma-ban, take legal action, whatever)_.

> ~MadDave, Technical Lead at Sandbox Interactive for Albion Online, [source](https://forum.albiononline.com/index.php/Thread/51604-Is-it-allowed-to-scan-your-internet-trafic-and-pick-up-logs/?postID=512670#post512670)

### Where should I flip from?

- Albion Free Market's system finds flips from anywhere prices are uploaded.
- The most obvious flip consists of buying an item in **Caerleon** and selling it to the **Black Market**. This is the safest form of flipping, as it does not involve transporting through red zones. It's also the most disputed form of flipping, so expect lower profits. From Caerleon, 100k profit flips are common, 500k profit flips are uncommon, 1M+ profit flips are rare.
- You can also buy the items in the **royal cities** and transport them to the **Black Market**. This adds an extra layer of risk, as you can get ganked while crossing the red zones. You can expect higher profits and a bigger pool of flips to choose from when flipping like this. **Brecillien** is the most profitable city, but also the most dangerous one to flip from.

## FLIPPER STATISTICS

- The flipper page shows a chart with the total value of consumed flips per hour per server. The highlighted area of the chart represents weekends.
- You can use the chart to see if someone recently flipped on your server, which might bring the availability of flips down. On the other hand, if no one has fliped for some hours, it's likely that you'll find good flips.
  <img src="https://github.com/JPCodeCraft/AlbionFreeMarketTutorials/assets/11092613/becd311d-9835-4e91-afaf-8dcf1eba24c5" style="max-width: 1200px; width: 100%;">
- There's also information about the top flips for the server you're at and the current flips status for each server.
  <img src="https://github.com/JPCodeCraft/AlbionFreeMarketTutorials/assets/11092613/bdda6d3c-6dc9-4947-9033-37b8e27d2466" style="max-width: 1200px; width: 100%;">

## UPGRADE FLIPS

### Basics

- An upgrade flip is when you buy a lower enchantment item (for example, a 7.0 item) and upgrade it using runes, souls and relics until it matches a buy order in the Black Market (for example, a 7.3 item).
- This means that you must buy the base item, buy (or have in stock) the upgrade items (runes, souls or relics), upgrade the item in the city and then sell it to the Black Market.
- Upgrade flips add a new layer of complexity because you have to manage rune stocks, but they also increase the number of available flips and their potential profit, especially if you manage to buy your runes at good prices.

### Upgrade Items Prices

- Albion Free Market's system uses upgrade items prices to calculate the flip profit. In short, the total cost of the flip is the base item + upgrade items + taxes and fess.
- All taxes and fess are calculated automatically.
- You can load prices from The Albion Online Data Project, chossing one or more Buy Locations, as well as none to average them all out.
- There are 3 types of prices that can be loadded:
  - Buy Order: this loads up the highest buy order price from AODP. It'll automatically add setup fee when calculating profits. Use this if you're setting up buy orders for your upgrade items.
  - Sell Order: this loads up the lowest sell order price from AODP. There's no setup fee, since this is an insta buy from the market.
  - Average Price: this loads up the average trade value for the giben number of days. By design, we add setup fee to this, since it's hard to insta buy for the average price.
- You can save your prices to the database and reload them anytime. Attention: saving is never automatic, you must click the save button.

### Upgrade Items Available Amount

- Albion Free Market can keep track of the amount of upgrade items you have, so you don't flip more items than you can.
- To make the most of this, set the "Hide Missing Upgrade Mats" checkbox, so you can't see the flips you don't have items to upgrade.
- If you leave the "Available Amount" field empty, the system won't check amounts for that item.
- Once you click "Consume Flip", the system automatically deduces the used number of items from you available items count.
- Attention: to save the amounts to the database, you should manually click the save button. Saves are not automatic.

<video src="https://github.com/user-attachments/assets/dcf29b21-e55c-4c7c-803d-3469f9d0ae28" style="max-width: 1200px; width: 100%;" controls autoplay muted></video>
