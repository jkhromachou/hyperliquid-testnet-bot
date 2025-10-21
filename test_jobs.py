from jobs import PositionJob
from indicators import macd_cross_below_minus40, rsi_above_70
import pandas as pd

# Mock price data for testing
data = pd.Series([50000, 50500, 50200, 49900, 49700, 49500, 49300, 49000])

def test_position_job_macd():
    job = PositionJob("BTC", "long", 50000, macd_cross_below_minus40)
    triggered = job.rule(data)
    print(f"MACD Rule triggered? {triggered}")

def test_position_job_rsi():
    job = PositionJob("ETH", "short", 3000, rsi_above_70)
    triggered = job.rule(data)
    print(f"RSI Rule triggered? {triggered}")

if __name__ == "__main__":
    test_position_job_macd()
    test_position_job_rsi()
