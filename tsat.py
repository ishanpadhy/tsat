import pandas as pd
import matplotlib.pyplot as plt

def fill_missing_values(series):
    """
    Fills missing values in a time series using linear interpolation.

    Parameters:
        series (pd.Series): Time series data with potential missing values.

    Returns:
        pd.Series: Time series with missing values filled.
    """
    return series.interpolate(method="linear")

def plot_trends(series, window=3):
    """
    Plots the time series data along with a rolling mean for trend analysis.

    Parameters:
        series (pd.Series): Time series data to plot.
        window (int): Window size for calculating the rolling mean.
    """
    rolling_mean = series.rolling(window=window).mean()
    plt.figure(figsize=(10, 6))
    plt.plot(series, label="Original Data", marker="o")
    plt.plot(rolling_mean, label=f"{window}-Point Rolling Mean", color="orange")
    plt.title("Time Series Trends")
    plt.legend()
    plt.show()
