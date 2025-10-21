# 🧭 Beginner Setup Guide — Hyperliquid Testnet Bot

Welcome! 🎉  
This guide walks you step-by-step through installing, configuring, and running your **Hyperliquid Testnet Bot**, even if you’ve never coded or used a trading bot before.

---

## 📂 Folder Overview

After setup, your folder structure should look like this:

D:\Jibreel\Downloads\hyperliquid-testnet-bot
│
├── main.py
├── config_testnet.yaml
├── api_client.py
├── indicators.py
├── jobs.py
├── utils.py
├── requirements.txt
├── mock_data
│ ├── BTC_4h.csv
│ └── ETH_4h.csv
└── tests
|  ├── test_indicators.py
|  └── test_jobs.py


| File / Folder | Purpose |
|----------------|----------|
| `main.py` | 🚀 Starts and runs the bot loop. |
| `config_testnet.yaml` | ⚙️ Main configuration — add API keys, webhook, and trading rules here. |
| `api_client.py` | Connects to the Hyperliquid Testnet API. |
| `indicators.py` | 🧮 Contains trading indicators (MACD, RSI). You can add new strategies here. |
| `jobs.py` | Defines and manages each position’s behavior. |
| `utils.py` | 🧰 Handles logging and sending messages to Discord. |
| `mock_data/` | Contains fake BTC/ETH data for safe offline testing. |
| `tests/` | Simple test scripts to check logic and indicators. |
| `requirements.txt` | Lists Python packages the bot depends on. |

---

## 🪄 Installation — First Time Setup

1. **Open PowerShell**  
   Press **Windows + S**, type **PowerShell**, and open it.  

2. **Navigate to the bot folder**
Create a virtual environment

powershell
python -m venv venv
Activate the environment
powershell
venv\Scripts\activate
You’ll know it worked if (venv) appears before your prompt.

Install all dependencies

powershell
pip install -r requirements.txt
⚙️ Configuration — Editing config_testnet.yaml
This file controls how your bot behaves. Open it in Notepad or VS Code.

🔑 API Keys
Replace the placeholders with your Hyperliquid Testnet keys (not real ones):

yaml
Copy code
account_address: "YOUR_ACCOUNT_ADDRESS_HERE"
secret_key: "YOUR_SECRET_KEY_HERE"
📢 Discord Webhook
Paste your Discord webhook URL so the bot can send updates:

yaml
Copy code
discord: "https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL_HERE"
You can create one in Discord by going to:
Server Settings → Integrations → Webhooks → New Webhook → Copy URL

💹 Positions (Strategies)
Each block under positions defines one trading strategy:

yaml
Copy code
positions:
  - asset: "BTC"
    side: "long"
    entry_price: 50000
    rule: "macd_cross_below_minus40"
  - asset: "ETH"
    side: "short"
    entry_price: 3000
    rule: "rsi_above_70"
Field	Description
asset	The coin symbol (e.g., BTC, ETH).
side	"long" = buy expecting price to rise. "short" = sell expecting price to fall.
entry_price	The approximate price where you entered the trade.
rule	The condition that will trigger a close (e.g., macd_cross_below_minus40).

You can add as many as you want — just copy one block and edit the details.

🧮 Understanding Built-in Strategies
All indicators live in indicators.py.

MACD Rule
python
Copy code
def macd_cross_below_minus40(data):
    macd, _ = compute_macd(data)
    return macd.iloc[-2] > -40 and macd.iloc[-1] <= -40
Closes a long when MACD crosses below –40.

RSI Rule
python
Copy code
def rsi_above_70(data):
    rsi = compute_rsi(data)
    return rsi.iloc[-1] > 70
Closes a short when RSI rises above 70.

🧠 Adding a New Strategy
You can create your own rules easily.

Open indicators.py

Add your new function:

python
def price_drop_5_percent(data, entry_price):
    current_price = data.iloc[-1]
    return current_price <= entry_price * 0.95
Open main.py and register it inside rule_map:

python
Copy code
rule_map = {
    "macd_cross_below_minus40": macd_cross_below_minus40,
    "rsi_above_70": rsi_above_70,
    "price_drop_5_percent": price_drop_5_percent
}
Now you can use "price_drop_5_percent" inside config_testnet.yaml.

🧪 Testing Before Running the Bot
Run the following from PowerShell to ensure everything works.

Test Indicators
powershell
python tests\test_indicators.py
Test Position Jobs
powershell
python tests\test_jobs.py
If successful, you’ll see messages like:

✅ MACD computed successfully
✅ RSI computed successfully
MACD Cross Triggered? False
RSI > 70 Triggered? False
🚀 Running the Bot
Start the bot manually:

powershell
python main.py
Example output:

🧪 Testnet bot started successfully.
✅ [TESTNET] Triggered close for BTC (macd_cross_below_minus40)
The bot will monitor each strategy independently and close positions automatically when conditions are met.

📜 Log File
All bot activity (price checks, triggers, errors) is logged in:

\hyperliquid-testnet-bot\bot.log
Check this file if something doesn’t look right.

🧱 Quick Reference
File	Edit?	Purpose
config_testnet.yaml	✅ Yes	Add your API keys, webhook, and trading rules
main.py	⚙️ Optional	Add new rule names to the rule map
indicators.py	⚙️ Optional	Add or modify indicator formulas
mock_data/	⚙️ Optional	Use for testing offline
api_client.py	❌ No	Handles API communication
tests/	⚙️ Optional	Verify indicators and rules work

🔁 Restarting the Bot
Whenever you restart your PC or terminal:

powershell
cd \hyperliquid-testnet-bot
venv\Scripts\activate
python main.py
🚫 Common Issues & Fixes
Problem	Fix
Bot won’t start	Ensure (venv) is active and you’re in the correct folder.
“Module not found”	Run pip install -r requirements.txt again.
No Discord alerts	Verify your webhook URL starts with https://discord.com/api/webhooks/.
Bot silent / no actions	The rules may not be triggered yet. Check bot.log.
File not found	Confirm you’re inside D:\Jibreel\Downloads\hyperliquid-testnet-bot.

⚠️ Important Notes
This bot uses Hyperliquid Testnet — no real money is involved.

Each position in your config runs as its own independent strategy.

You can safely test new indicators here before moving to mainnet.

Always test carefully; a wrong condition might close positions unexpectedly.

Use the logs and Discord messages to monitor behavior.
