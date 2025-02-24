<!--
title: "Albion Online Black Market Flipper Tutorial"
summary: "Learn how to profit in Albion Online by flipping items from the regular markets to the black market."
author: "Albion Free Market"
createdAt: "2024-07-19"
updatedAt: "2025-02-24"
category: "tutorial"
tags: ["black market", "flipper"]
-->

# ALBION FREE MARKET FLIPPER TUTORIAL

- This tutorial is for the [Black Market Flipper](https://albionfreemarket.com/flipper) in Albion Free Market.

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
- Albion Free Market holds sell orders for 60 minutes and buy orders for 30 minutes. This is done to reduce the number of _false positives_, where the system might think an order is available but in fact it's already been consumed in game.

### What does it mean to consume a flip?

- Consuming a flip has the following effects:
  - The orders used in that flip are market as consumed, so every flip that uses any of those orders are also considered consumed
  - The flip is sent to your _Consumed Flips (this session)_ table, so you can easily track them
- Notice that even thought a flip has already been consumed, it's still visible for all users. That's done to avoid _trolling_, where an ill intended user might consume multiple flips to make them disappear. So, it is possible that a consumed flip is still available.
- If after 10 minutes of consuming an order, that same order is seen by the system again, it's then marked as unconsumed, which reflects on the status of the flips that use it.

#### Is this allowed?

> _Our position is quite simple. As long as you just look and analyze we are ok with it. The moment you modify or manipulate something or somehow interfere with our services we will react (e.g. perma-ban, take legal action, whatever)_.

> MadDave, Technical Lead at Sandbox Interactive for Albion Online, [source](https://forum.albiononline.com/index.php/Thread/51604-Is-it-allowed-to-scan-your-internet-trafic-and-pick-up-logs/?postID=512670#post512670)

### Where should I flip from?

- Albion Free Market's system finds flips from anywhere prices are uploaded.
- The most obvious flip consists of buying an item in **Caerleon** and selling it to the **Black Market**. This is the safest form of flipping, as it does not involve transporting through red zones. It's also the most disputed form of flipping, so expect lower profits. From Caerleon, 100k profit flips are common, 500k profit flips are uncommon, 1M+ profit flips are rare.
- You can also buy the items in the **royal cities** and transport them to the **Black Market**. This adds an extra layer of risk, as you can get ganked while crossing the red zones. You can expect higher profits and a bigger pool of flips to choose from when flipping like this. **Brecilien** is the most profitable city, but also the most dangerous one to flip from.

## FLIPPER STATISTICS

- The flipper page shows a chart with the total value of consumed flips per hour per server. The highlighted area of the chart represents weekends.
- You can use the chart to see if someone recently flipped items on your server, which might bring the availability of flips down. On the other hand, if no one has flipped for some hours, it's likely that you'll find good flips.

![Albion Online Flipper Chart](https://github.com/JPCodeCraft/AlbionFreeMarketTutorials/assets/11092613/becd311d-9835-4e91-afaf-8dcf1eba24c5)

- There's also information about the top flips for the server you're at and the current flips' status for each server.

![Albion Online Flipper Stats](https://github.com/JPCodeCraft/AlbionFreeMarketTutorials/assets/11092613/bdda6d3c-6dc9-4947-9033-37b8e27d2466)

## FILTERING FLIPS

- First, make sure you have the right server set, choosing it on the top right settings button.

![Albion Online Flipper Server Selection](https://github.com/user-attachments/assets/a42d61f8-fc19-4b45-be6a-b1e2be538463)

- These are the filters available:
  - Buy Location: select one or more places where you are buying the items to flip.
  - Sell Location: select one or more places where you are selling the items. Usually, you set this to Black Market.
  - Tiers: filter the flips by the item's tier. Can select multiple.
  - Minimum Profit (premium): the system will only show flips above the minimum value set here.
  - Max Buy Age (minutes): the system will only show flips where the sell order price (the item you buy) is no older than the value set here. Mas is 60 minutes, after that the systems ignores the flip.
  - Max Sell Age (minutes): the system will only show flips where the buy order price (where you sell the item) is no older than the value set here. Max is 30 minutes, after that the system ignores the flip.
  - Upgrade From's: if the flip is an upgrade, only show flips where it upgrades from one of the selected enchantments.
  - Upgrade To's: if the flip is an upgrade, only show flips where it upgrades to one of the selected enchantments.
  - Max Rune Count: if the flip is an upgrade, only show flips where all the upgrade requirements (runes) amounts are bellow the max limit set. Useful if you have a limited amount of runes and want to focus on maximizing their usage.
  - Hide Upgrades: select this if you're not willing to do upgrade flips, so they don't show in the list. The upgrade UI will also be hidden.
  - Hide Consumed: if you select this, the table won't show flips that have had any one of it's buy/sell orders consumed.
  - Hide Duped: if you select this, no flips where the buy or the sell order is used more than once will be shown. By default, the system shows the highest profit one.
  - Hide Missing Upgrade Mats: if you select this, the system will not show flips where the needed amount of upgrade mats is higher than the Available Amount you set. If you leave the Available Amount field empty, that item will not be checked for missing materials.

![Albion Online Flipper Filters](https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/flipper/image.png)

## UPGRADE FLIPS

### Basics

- An upgrade flip is when you buy a lower enchantment item (for example, a 7.0 item) and upgrade it using runes, souls and relics until it matches a buy order in the Black Market (for example, a 7.3 item).
- This means that you must buy the base item, buy (or have in stock) the upgrade items (runes, souls or relics), upgrade the item in the city and then sell it to the Black Market.
- Upgrade flips add a new layer of complexity because you have to manage rune stocks, but they also increase the number of available flips and their potential profit, especially if you manage to buy your runes at good prices.

### Upgrade Items Prices

- Albion Free Market's system uses upgrade items prices to calculate the flip profit. In short, the total cost of the flip is the base item + upgrade items + taxes and fess.
- All taxes and fess are calculated automatically.
- You can load prices from The Albion Online Data Project, choosing one or more Buy Locations, as well as none to average them all out.
- There are 3 types of prices that can be loaded:
  - Buy Order: this loads up the highest buy order price from AODP. It'll automatically add a setup fee when calculating profits. Use this if you're setting up buy orders for your upgrade items.
  - Sell Order: this loads up the lowest sell order price from AODP. There's no setup fee, since this is an insta-buy from the market.
  - Average Price: this loads up the average trade value for the given number of days. By design, we add setup fee to this, since it's hard to insta-buy for the average price.
- You can save your prices to the database and reload them anytime. Attention: saving is never automatic, you must click the save button.

### Upgrade Items Available Amount

- Albion Free Market can keep track of the amount of upgrade items you have, so you don't flip more items than you can.
- To make the most of this, set the “Hide Missing Upgrade Mats” checkbox, so you can't see the flips you don't have items to upgrade.
- If you leave the “Available Amount” field empty, the system won't check amounts for that item.
- Once you click “Consume Flip”, the system automatically deduces the used number of items from you available items count.
- Attention: to save the amounts to the database, you should manually click the save button. Saves are not automatic.

<video src="https://github.com/user-attachments/assets/dcf29b21-e55c-4c7c-803d-3469f9d0ae28" controls autoplay muted></video>

## FINDING FLIPS

- It's very unusual to simply load the Flipper page and find good flips. You usually need to actively search the market. So, the best way to find flips, is to look at the highest amount and variety of market orders you can. Albion Free Market's flipper tool will analyze each order to find the best flips possible.
- Here's an example of how you can load up multiple prices to find flips:
  - Start in Caerleon. Sort Prices by duration descending (highest to lowest). That way, you'll see the newest offers available.
  - Choose a category that sell in the BM, like accessories.
  - Choose a tier, like 8
  - Choose an enchantment, like 4
  - Go through all pages available or the maximum of 20
  - Go to enchantment 3
  - See all pages
  - Repeat all enchantments, then all tiers, then all categories.
- This would be a full market scan and would take some 20 minutes or more. If you want something faster, you can use fewer filters. You can even not choose a category, only go through the latest orders for each tier/enchantment.
- Then, go to the Black Market.
  - Keep the default sort order (the highest price)
  - Choose a category
  - Choose a tier
  - Choose an enchantment
  - Stop the page scrolling when the values are too low. For example, there is no point in seeing prices of .4 items at 300k. They are worth a lot more.
  - Repeat for all options

<video src="https://github.com/user-attachments/assets/d4d210a5-f3b4-41bf-abb0-72f9e98c09b2" controls autoplay muted></video>

## FLIPPING MISTAKES TO AVOID

- If you don't have much silver, don't spend all of it flipping. Sometimes flips might fail, and you end up with a long wait for the item to sell.
- If you are flipping to BM from Royals, make sure you know how to transport safely. In case you get ganked you lose it all.
- Expensive high enchantment items tend to sell VERY SLOWLY on the Black Market, so if you miss the flip you will have to wait a long time (weeks sometimes) to sell the item, and you'll probably lose some silver doing it.
- Make sure you're buying the right items. It's common to buy wrong qualities/tiers and waste silver.
- It can happen that when you get to the Black Market, the buy order is gone. This can happen because someone flipped the item or because the BM price went up, and the order got fulfilled by an existing sell order. In this case, you can create a sell order or, depending on the item, try to sell it on the normal market.
- The above mistake is much more common on lower-tier/enchant items, for which the prices tend to increase more rapidly and reach a sell order price faster. However, it can also happen on high-tier, expensive items, so be careful.

## DEALING WITH FAILED FLIPS

- It's inevitable that flips will fail eventually. When that happens, you should mark the flip as failed on the "Your Flips" page.

<video src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/flipper/video.mp4" controls autoplay muted></video>

- There are two viable paths to follow:
  - Set up a sell order in the Black Market and wait for it to sell.
  - Keep all failed flips in a bank tab and periodically scan the Black Market. Check the "Your Flips" page while filtering to show only failed flips. This will allow you to see if there are any buy orders that will be profitable to sell to.

![Albion Online Failed Flips](https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/flipper/image1.png)

## Flipper Impact Report (as of February 2025)

The Albion Free Market Black Flipper plays a significant role in Albion Online's economy by influencing multiple areas, from market liquidity to player engagement. Here is a detailed breakdown of its impact:

| Impact Area             | Description                                                                           | Supporting Data                                 |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Market Liquidity        | Increases demand for player market items, aiding sellers in converting loot to silver | 195,000+ items flipped, 152B+ silver bought     |
| Black Market Item Stock | Keeps the Black Market stock full, allowing better loot drops for players             | 195,000+ items flipped                          |
| Price Stabilization     | Absorbs excess supply when player market prices are low, preventing price drops       | 195,000+ items flipped                          |
| Upgrade Material Market | Boosts demand for runes, souls, and relics, benefiting sellers                        | 15B+ silver worth of materials purchased        |
| Inflation Control       | Generates sales tax as a silver sink, removing currency to combat inflation           | 6B+ silver in taxes from the 4% sales tax       |
| Player Engagement       | Drives active market participation through continuous trading and city-to-city travel | 195,000+ items flipped                          |
| Influence on PvP Action | Transporters who buy in Royal Cities and sell in the Black Market create PvP hotspots | Promotes PvP encounters and risk-reward balance |

These figures reflect the state of the flipper as of **February 2025**, highlighting the extensive impact of the Black Market Flipper on the Albion Online economy.

## VIDEO TUTORIALS

### Raw Caerleon to Black Market Flipping Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/huP-mvR3EN0?si=JMpPyXj6jaM_-YsK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/aQ4pNCKHZ5Y?si=pxU8J_p1VM7yQsc3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/ttqGJGkiQ8c?si=W0OIdjFPKLHio4tT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Raw Brecilen to Black Market Flipping Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/jw4Gz5MDVs0?si=1fTBB-L2nCN1QpP8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Bandit Hour Safe Transport Tutorial by iFlow

<iframe width="560" height="315" src="https://www.youtube.com/embed/qPJfQVqnaMQ?si=w6iubnhLndrgNyDH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Turkish videos by Yoian Albion

<iframe width="560" height="315" src="https://www.youtube.com/embed/wc4GrRVsWcs?si=Ws_dkQXcWW1sXlRN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/6XFE8d4C7pg?si=gTU2GK9-cU36Gcy4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Quick tutorial by LilDolphinAlbion

<iframe width="560" height="315" src="https://www.youtube.com/embed/2RcZQ1C_9HM?si=s3T1DHE0ZFyuO7cj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Begginer Video by Jack Voids

<iframe width="560" height="315" src="https://www.youtube.com/embed/CdYctYfpP-o?si=MZMt8B_ynC2ou6G-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
