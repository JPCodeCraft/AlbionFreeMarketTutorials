<!--
title: "The Albion Online Data Project Client Tutorial"
summary: "Learn how to install and use The Albion Online Data Project client to gather Albion Online market prices."
author: "Albion Free Market"
createdAt: "2024-07-19"
updatedAt: "2024-12-19"
category: "tutorial"
tags: ["AODP", "Data Client"]
-->

# ALBION ONLINE DATA PROJECT

- This is a getting started tutorial for the [Albion Online Data Project](https://www.albion-online-data.com/).

## What is the Albion Online Data Project?

- The goal of the project is to collect Albion Online market data and provide it to anyone via a public API.
- The project stores buy and sell orders data, average prices and amounts, and gold price history.
- You can go to the project's [Discord Server](https://discord.gg/TWz64zPFtC) to get in touch with the project's admins or support the project.
- [Albion Free Market](https://albionfreemarket.com) and multiple other websites and sheets make use of the project's data to provide its information as well as the backend analysis.

## What's the client used for?

- The data client is used to collect the market information you see in the game.
- It works by _sniffing_ the network packets sent to the game, parsing the market information and, finally, uploading it to the centralized servers. So it's only capable of uploading information you actually look for in the game (pages of market orders, history charts and gold history).
- The [source code](https://github.com/ao-data/albiondata-client) is open, so you can make sure the data that's being uploaded is limited to the market data. No private information is uploaded.

## Installation and Usage

- You can download the client from the project's [repository releases page](https://github.com/ao-data/albiondata-client/releases)
- Download the latest version that matches your operational system (if you're on Windows, get _albiondata-client-amd64-installer.exe_).

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_bfd4949aa437.png" alt="AODP Installation" width="1156" height="749">

- Ignore Windows safety warnings by clicking on _Run Anyway_. They show up because AODP is not a certified publisher. Once again, the code is open source, and you can check how safe the application is yourself.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_07f479b8d502.png" alt="AODP Installation" width="1426" height="560">

- You need administrator rights to install the client.
- Follow the on-screen instructions to complete the installation.
- [WinPcap 4.1.3](https://www.winpcap.org/) will also be installed. This is the driver that allows the _packet sniffing_. Follow instruction to complete its installation.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_a3a915a3363e.png" alt="AODP Installation" width="1349" height="518">

- Make sure to keep the option _Automatically start the WinPcap driver at boot time_ checked, since it's required for the Albion Online Data Project to work.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_58ae2f02f926.png" alt="AODP Installation" width="1501" height="705">

- Once the installation is complete, you can run the client from the start menu or the desktop icon. This is what the client looks like.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_bdef248c0f71.png" alt="AODP Installation" width="1340" height="652">

- The client starts automatically on Windows boot in a minimized state. So, if you need to open the client, you can find it in the system tray, near the watch.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_bd8cfc7e9368.png" alt="AODP Installation" width="622" height="195">

- When idle (not uploading), the client is very low weight and won't harm your everyday usage of your computer. So there's no reason to worry about it running when you're not playing the game.
- Once you get in-game, the client will start uploading market data.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_b3ebb1203a49.png" alt="AODP Installation" width="1346" height="664">

- You can close the client by right clicking the system tray button and choosing _Quit_.

## Uninstallation

- You can uninstall the client and WinPcap just like any other software.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_ab39da8d070d.png" alt="AODP Installation" width="770" height="93">

## Encrypted Data

- If your prices are not updating with the client, it's probable that you have encrypted data, especially if your character is new or if you haven't played much on that character.
- Both the official AODP data client and the alternative AFM Data Client will tell you that you have encrypted data.
- When you're encrypted, gold and historical prices are uploaded, but market orders are not.
- No one knows exactly how to stop getting data encrypted, but it's been noted that older accounts, where players actually play the game, don't have encrypted data. So the best known way to get your data unencrypted is to just play the game.

## Alternative AFM Data Client

- Alternatively, you can use the [AFM Data Client](https://github.com/JPCodeCraft/AlbionDataAvalonia/).
- It essentially performs the same functions as the official AODP client but offers a more user-friendly interface and additional features, as detailed in the link above.
- To download and install, simply follow the instructions on the [GitHub Page](https://github.com/JPCodeCraft/AlbionDataAvalonia/).
- If you use this client, uninstall the official AODP one to avoid uploading everything twice.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/aodp/image_fdc1687d1ba6.png" alt="AFM Data Client" width="1414" height="705">
