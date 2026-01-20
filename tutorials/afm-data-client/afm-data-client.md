<!--
title: "Albion Free Market Data Client Tutorial"
summary: "Install and master the Albion Free Market Data Client to upload market data, track trades, and stay on top of your Albion prices."
author: "Albion Free Market"
createdAt: "2025-10-09"
updatedAt: "2025-10-09"
category: "tutorial"
tags: ["Data Client"]
-->

# ALBION FREE MARKET DATA CLIENT

- Learn how to install, configure, and use the Albion Free Market (AFM) Data Client, the alternative uploader for the Albion Online Data Project (AODP).

## What is the Albion Free Market Data Client?

- A free, open-source desktop app that captures in-game market data and forwards it to AODP so every Albion player can benefit from fresh prices.
- Ships with a friendly interface so you can see what is being uploaded, check your historical trades, and tweak performance without digging into config files.
- Can optionally keep uploads private for your own market flips or share everything back with the AFM community.
- Runs quietly in the system tray, auto-starts with your PC, and updates itself, so market coverage keeps flowing even if you forget it is there.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image1.png" alt="image" width="1063" height="686">

## Key Features

- 🧰 Collects buy orders, sell offers, price histories, gold prices, loadout quick-buy scans, and more.
- 🚀 Starts with Windows, minimizes to the tray, and auto-updates (Windows).
- 🧾 Logs every upload and exposes trade/mail history captured while you play.
- ⚙️ Lets you tune upload parallelism, duplicate detection, log verbosity, and Pow solve performance in real time.
- 🔐 Supports AFM sign-in to unlock private flips mode or share uploads with other AFM users.
- 🆓 Free, open source.

## Installation

### Windows

1. Download the latest `AFMDataClientSetup_v_x.x.x.x.exe` from the [GitHub releases page](https://github.com/JPCodeCraft/AlbionDataAvalonia/releases).
2. Run the installer and follow the prompts. Administrator rights are required for the optional driver installation.
3. The client launches minimized in the system tray after setup. Click the AFM icon to open the interface.
4. Automatic updates are enabled, so future releases install silently.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image2.png" alt="image" width="1170" height="815">

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image3.png" alt="image" width="400" height="158">

**Uninstalling on Windows**

- Use _Add or Remove Programs_ (or _Programs and Features_) to remove **AFM Data Client**.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image4.png" alt="image" width="905" height="184">

### Linux

**Option 1 — One-line installer**

```bash
curl -s https://api.github.com/repos/JPCodeCraft/AlbionDataAvalonia/releases/latest \
  | jq -r '.assets[] | select(.name == "AFMDataClient_Linux64_Installer.sh") | .browser_download_url' \
  | xargs curl -L -o installer.sh && sed -i 's/\r$//' installer.sh \
  && chmod +x installer.sh && ./installer.sh && rm installer.sh
```

**Option 2 — Manual**

1. Download `AFMDataClient_Linux64_Installer.sh` from the [releases page](https://github.com/JPCodeCraft/AlbionDataAvalonia/releases).
2. Normalize line endings: `sed -i 's/\r$//' AFMDataClient_Linux64_Installer.sh`
3. Make it executable: `chmod +x AFMDataClient_Linux64_Installer.sh`
4. Run it: `./AFMDataClient_Linux64_Installer.sh`

**Uninstalling on Linux**

```bash
curl -s https://api.github.com/repos/JPCodeCraft/AlbionDataAvalonia/releases/latest \
  | jq -r '.assets[] | select(.name == "AFMDataClient_Linux64_Uninstaller.sh") | .browser_download_url' \
  | xargs curl -L -o uninstaller.sh && sed -i 's/\r$//' uninstaller.sh \
  && chmod +x uninstaller.sh && ./uninstaller.sh && rm uninstaller.sh
```

> Linux builds do not auto-update. Simply re-run the installer to upgrade. Testing on Linux is limited, so expect rough edges.

### MacOS

- A Mac build is published, but mostly untested.

### Required Packet Capture Driver

- AFM depends on packet capture libraries to sniff Albion’s traffic.
- On Windows you must install **Npcap**. The client detects the driver and shows a dedicated screen if it is missing (see _PCap View_ below).
- On Linux the installer attempts to use `libpcap`. You may need administrator rights to add the dependency.

## First Launch & System Tray Behavior

- After installation the client auto-starts on boot and minimizes to the system tray. Right-click the tray icon to exit; left-click to restore the window.
- The app starts uploading as soon as you open market interfaces, price charts, quick-buy loadouts, or the gold exchange in game.
- Uploads target AODP by default. Sign in with your AFM account from the sidebar to access private flips or sharing toggles.

## Signing In and Upload Destinations

- Click **Sign In** in the left sidebar to authenticate with AFM.
- When signed in you can enable:
  - `Private Flips Mode` – send market orders only to your personal flips dashboard; nothing goes to AODP (except runes).
  - `Share with Other AFM Users` – re-enable community sharing while staying in private mode.
- Use **Sign Out** at any time. The app continues uploading to AODP when no AFM options are enabled.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image5.png" alt="image" width="188" height="161">

## Interface Walkthrough

### Main View Sidebar

- Navigation buttons switch between Dashboard, Trades, Mails, Settings, and Logs.
- The bottom card hosts the authentication controls described above. If Npcap is missing, the Dashboard button automatically routes you to the PCap view.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image6.png" alt="image" width="202" height="613">

### Dashboard

- **Upload Queue & Tasks** – shows current queue size, running upload workers, and success/skipped/failed totals. The red/green blocks flash when new uploads enter or complete.
- **Player Context** – displays the detected server shard, your character name, and current location once the client sees you in game.
- **Status Prompts** – surfaced when action is required:
  - _Change city_ – triggered if the game location cannot be tracked or is unsupported.
  - _Get in game_ – displayed until you log into Albion.
  - _Encrypted market orders_ – warns when uploads are blocked by market encryption (see troubleshooting).
- **Upload Counters** – cumulative totals for offers, requests, daily/weekly/monthly histories, and gold history pushes.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image7.png" alt="image" width="795" height="431">

### Trades

- Clicking **Load** fetches your recorded instant and order trades via `TradeService`.
- Use the search box to filter by item name (ignores spacing) and dropdowns to narrow by server, trade type, operation (bought vs sold), and city.
- The table shows timestamp, operation, quality, item, location, amount, unit silver, and total silver. The view auto-refreshes when new trades arrive.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image8.png" alt="image" width="1407" height="577">

### Mails

- Loads your market mails (fulfillments) collected in-game. Filters match those in Trades but replace trade type with auction type (Bought/Sold).
- The grid lists received time, operation, item, location, partial amount, full order size, unit silver, and total silver—ideal for cross-checking sales.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image9.png" alt="image" width="1270" height="577">

### Settings

- **Start Hidden** toggles whether the UI launches minimized.
- **Parallel uploads** slider controls the number of simultaneous uploads and surfaces live Pow solve statistics (latest, average, percentiles, min/max, standard deviation). Use **Clear** to reset the metrics window.
- Additional sliders let you define the duplicate hash cache size, logs kept in memory, mails per page, and trades per page.
- **Log verbosity** adjusts how much gets written to the in-app logs and tray notifications.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image10.png" alt="image" width="805" height="833">

### Logs

- Streams Serilog events captured by the client. Entries include timestamp, level, and formatted message (hyperlinks are styled as clickable when present).
- The list respects the “Maximum log entries” limit from Settings so the window stays responsive.

<img src="https://cdn.albionfreemarket.com/AlbionFreeMarketTutorials/tutorials/afm-data-client/image11.png" alt="image" width="1276" height="707">

### PCap View

- Appears if Npcap (or `libpcap` on Linux) is missing. Provides buttons to open the Npcap download page and re-check once installed.
- Use this view to quickly diagnose capture-driver issues before troubleshooting deeper network problems.

## Troubleshooting

### AFM Encryption Help

- If your prices are not updating, your market data is likely encrypted—common on new or inactive characters.
- Both the official AODP client and the AFM client flag encrypted uploads. When encryption is active, gold and historical prices upload but buy/sell orders do not.
- There is no guaranteed fix. The community’s best advice is to play actively; accounts tend to become unencrypted over time.
- Meeting the verification steps listed at <https://albiononline.com/gold-limits> may speed up the process.
- Until the data decrypts, powerful features such as the AFM Flipper cannot leverage your uploads efficiently.

### AFM Data Client Doesn't Work?

- Close the client (right-click the tray icon and choose **Quit**).
- Uninstall **WinPcap** via Windows Control Panel if it was previously installed.
- Install **Npcap** from <https://npcap.com/#download>.
- Restart the AFM client and test again.
- Using a VPN? Check its packet redirection settings and switch to an **NDIS/Legacy** mode instead of WFP if available.

## Uninstallation & Maintenance

- Remove the AFM client like any other application (see platform-specific instructions above).
- Whenever a new release drops, Windows will auto-update; Linux users should rerun the installer.
- Remember that running both the AFM client and the official AODP client simultaneously doubles uploads. Uninstall one to avoid duplicate data.

## Stay Involved

- Report issues or contribute enhancements on the [AlbionDataAvalonia GitHub repository](https://github.com/JPCodeCraft/AlbionDataAvalonia).
- Join the AFM community to compare flips, track market movements, and help keep Albion’s economy transparent for everyone.
