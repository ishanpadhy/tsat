import pandas as pd
import matplotlib.pyplot as plt

# Existing functions remain here...

def smooth_data(series, window=3):
    """
    Smooths time series data using a simple moving average.

    Parameters:
        series (pd.Series): Time series data.
        window (int): The size of the moving average window.

    Returns:
        pd.Series: Smoothed time series data.
    """
    return series.rolling(window=window).mean()

def detect_outliers(series):
    """
    Identifies potential outliers using the IQR method.

    Parameters:
        series (pd.Series): Time series data.

    Returns:
        list: Indices of detected outliers.
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    return outliers.index.tolist()

def resample_data(series, frequency):
    """
    Resamples time series data to a specified frequency.

    Parameters:
        series (pd.Series): Time series data.
        frequency (str): Resampling frequency (e.g., 'D', 'W', 'M').

    Returns:
        pd.Series: Resampled time series data.
    """
    return series.resample(frequency).mean()

def detrend_data(series):
    """
    Detrends time series data by subtracting the rolling mean.

    Parameters:
        series (pd.Series): Time series data.

    Returns:
        pd.Series: Detrended time series data.
    """
    rolling_mean = series.rolling(window=12, min_periods=1).mean()
    return series - rolling_mean
