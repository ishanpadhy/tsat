import pandas as pd
import numpy as np
from tsat import TimeSeriesAnalyzer  # Assuming your class is in a file named tsat.py

def test_smooth_data():
    # Test data
    data = pd.Series([10, 15, 200, 20, 25])
    analyzer = TimeSeriesAnalyzer(data)
    
    # Smooth the data
    smoothed = analyzer.smooth_data()
    
    # Assert statements (update with expected values)
    assert smoothed.max() <= 60  # Example: Adjust based on known upper bound
    assert smoothed.min() >= 5   # Example: Adjust based on known lower bound

def test_detect_outliers():
    # Test data
    data = pd.Series([10, 15, 200, 20, 25])
    analyzer = TimeSeriesAnalyzer(data)
    
    # Detect outliers
    outliers = analyzer.detect_outliers()
    
    # Assert statements
    assert 200 in outliers.values
    assert 10 not in outliers.values  # Example: Adjust based on known non-outliers

def test_resample_data():
    # Test data
    date_rng = pd.date_range(start='2023-01-01', end='2023-01-31', freq='D')
    data = pd.Series(range(len(date_rng)), index=date_rng)
    analyzer = TimeSeriesAnalyzer(data)
    
    # Resample the data
    resampled = analyzer.resample_data(freq='W-SUN')
    
    # Assert statements
    assert len(resampled) > 0
    assert resampled.index.freq == 'W-SUN'

def test_rolling_window_stats():
    # Test data
    data = pd.Series([1, 2, 3, 4, 5, 6])
    analyzer = TimeSeriesAnalyzer(data)
    
    # Compute rolling statistics
    rolling_stats = analyzer.rolling_window_stats(window=3, stats=["mean", "std"])
    
    # Assert statements
    assert "mean" in rolling_stats
    assert len(rolling_stats["mean"]) == len(data)
    assert rolling_stats["mean"].isnull().sum() == 2  # First two should be NaN for window=3

def test_plot_time_series():
    # Test data
    date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
    data = pd.Series(np.random.randint(0, 10, size=len(date_rng)), index=date_rng)
    analyzer = TimeSeriesAnalyzer(data)
    analyzer.plot_time_series()

if __name__ == "__main__":
    test_smooth_data()
    test_detect_outliers()
    test_resample_data()
    test_rolling_window_stats()
    test_plot_time_series()
    print("All tests passed!")
