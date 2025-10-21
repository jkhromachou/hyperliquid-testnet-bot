import pandas as pd
from indicators import compute_macd, compute_rsi, macd_cross_below_minus40, rsi_above_70

# Load mock BTC data
df = pd.read_csv("mock_data/BTC_4h.csv")
prices = df["close"]

def test_macd():
    macd, signal = compute_macd(prices)
    assert len(macd) == len(prices)
    print("✅ MACD computed successfully")

def test_rsi():
    rsi = compute_rsi(prices)
    assert rsi.iloc[-1] > 0
    print("✅ RSI computed successfully")

def test_macd_rule():
    triggered = macd_cross_below_minus40(prices)
    print(f"MACD Cross Triggered? {triggered}")

def test_rsi_rule():
    triggered = rsi_above_70(prices)
    print(f"RSI > 70 Triggered? {triggered}")

if __name__ == "__main__":
    test_macd()
    test_rsi()
    test_macd_rule()
    test_rsi_rule()
