<!--
title: "The Albion Online Data Project Client Tutorial"
summary: "Learn how to install and use The Albion Online Data Project client to gather Albion Online market prices."
author: "Albion Free Market"
date: "2024-07-19"
category: "tutorial"
tags: ["aodp", "client"]
-->

# ALBION ONLINE DATA PROJECT

- This is a getting started tutorial for the [Albion Online Data Project](https://www.albion-online-data.com/).

## What is the Albion Online Data Project?

- The goal of the project is to collect Albion Online market data and provide it to anyone via a public API.
- The project stores buy and sell orders data, as well as average prices and amounts.
- You can go to the project's [Discord Server](https://discord.gg/TWz64zPFtC) to get in touch with the project's admins or support the project.
- [Albion Free Market](https://albionfreemarket.com) and multiple other websites and sheets make use of the project's data to provide its information as well as the backend analysis.

## What's the client used for?

- The data client is used to collect the market information you see in the game.
- It works by _sniffing_ the network packets sent to the game, parsing the market information and, finally, uploading it to the centralized servers. So it's only capable of uploading information you actually look for in the game (pages of market orders, history charts and gold history).
- The [source code](https://github.com/ao-data/albiondata-client) is open, so you can make sure the data that's being uploaded is limited to the market data. No private information is uploaded.

## Installation and Usage

- You can download the client from the project's [repository release's page](https://github.com/ao-data/albiondata-client/releases)
- Download the latest version that matches your operational system (if you're on Windows, get _albiondata-client-amd64-installer.exe_).

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image.png" style="max-width: 1200px; width: 100%;">

- Ignore Windows safety warnings by clicking on _Run Anyway_. They show up because AODP is not a certified publisher. Once again, the code is open source, and you can check how safe the application is yourself.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-1.png" style="max-width: 1200px; width: 100%;">

- You need administrator rights to install the client.
- Follow the on-screen instructions to complete the installation.
- [WinPcap 4.1.3](https://www.winpcap.org/) will also be installed. This is the driver that allows the _packet sniffing_. Follow instruction to complete its installation.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-2.png" style="max-width: 1200px; width: 100%;">

- Make sure to keep the option _Automatically start the WinPcap driver at boot time_ checked, since it's required for the Albion Online Data Project to work.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-3.png" style="max-width: 1200px; width: 100%;">

- Once the installation is complete, you can run the client from the start menu or the desktop icon. This is what the client looks like.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-4.png" style="max-width: 1200px; width: 100%;">

- The client starts automatically on Windows boot in a minimized state. So, if you need to open the client, you can find it in the system tray, near the watch.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-5.png" style="max-width: 1200px; width: 100%;">

- When idle (not uploading), the client is very low weight and won't harm your everyday usage of your computer. So there's no reason to worry about it running when you're not playing the game.
- Once you get in-game, the client will start uploading market data.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-6.png" style="max-width: 1200px; width: 100%;">

- You can close the client by right clicking the system tray button and choosing _Quit_.

## Uninstallation

- You can uninstall the client and WinPcap just like any other software.

<img src="https://raw.githubusercontent.com/JPCodeCraft/AlbionFreeMarketTutorials/main/tutorials/aodp/image-7.png" style="max-width: 1200px; width: 100%;">