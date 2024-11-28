import pandas as pd
from tsat import (
    fill_missing_values,
    plot_trends,
    smooth_data,
    detect_outliers,
    resample_data,
    detrend_data,
)

def test_smooth_data():
    series = pd.Series([1, 2, 3, 4, 5, 6, 7], index=pd.date_range("2023-01-01", periods=7))
    smoothed = smooth_data(series, window=3)
    assert smoothed.isna().sum() == 2, "Smoothing window not applied correctly."
    print("smooth_data passed.")

def test_detect_outliers():
    series = pd.Series([1, 2, 3, 100, 5], index=pd.date_range("2023-01-01", periods=5))
    outliers = detect_outliers(series)
    assert outliers == [3], "Outliers not detected correctly."
    print("detect_outliers passed.")

def test_resample_data():
    series = pd.Series([1, 2, 3], index=pd.date_range("2023-01-01", periods=3, freq="D"))
    resampled = resample_data(series, "W")
    assert len(resampled) == 1, "Resampling did not aggregate correctly."
    print("resample_data passed.")

def test_detrend_data():
    series = pd.Series(range(1, 13), index=pd.date_range("2023-01-01", periods=12))
    detrended = detrend_data(series)
    assert detrended.mean() < 1e-10, "Data not detrended correctly."
    print("detrend_data passed.")

if __name__ == "__main__":
    test_smooth_data()
    test_detect_outliers()
    test_resample_data()
    test_detrend_data()
