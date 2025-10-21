# Hyperliquid Testnet Bot
Runs automated conditional closes for multiple positions on Hyperliquid Testnet.

## 📍Install Path
Whatever your drive is

## 🪄 Setup
1. Open PowerShell:
   cd "Your Path/hyperliquid-testnet-bot"
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

2. Edit config_testnet.yaml:
   - Paste your Hyperliquid Testnet API keys.
   - Paste your Discord webhook URL.

3. Create "mock_data" folder under your "hyperliquid-testnet-bot" main folder
   - Create as many text files for tickers you'd like to.
   - ex: BTC_4h.csv (Make sure to save these as .csv and not .txt)
   - Open each file in Notepad and paste in the sample data below for your specified ticker in this format:
timestamp,open,high,low,close,volume
2025-10-14 00:00,59750,60010,59380,59890,2100
2025-10-15 00:00,59890,60300,59600,60210,1950
2025-10-16 00:00,60210,60750,60110,60420,2300
2025-10-17 00:00,60420,60980,60220,60810,2400
2025-10-18 00:00,60810,61050,60450,60600,2000
2025-10-19 00:00,60600,60880,60170,60440,2200
2025-10-20 00:00,60440,60770,60200,60580,1800

4. Create a folder called "tests"
   - mkdir tests
   - add both "test_indicators.py" and "test_jobs.py" into this folder
   - Run them as follows: python tests\test_indicators.py OR python tests\test_jobs.py
   - Expected output example:
   ✅ MACD computed successfully
   ✅ RSI computed successfully
   MACD Cross Triggered? False
   RSI > 70 Triggered? False
   MACD Rule triggered? False
   RSI Rule triggered? False

5. Run the bot:
   python main.py
