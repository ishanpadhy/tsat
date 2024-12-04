import pandas as pd
import matplotlib.pyplot as plt

# Function to smooth the data
def smooth_data(series):
    # Calculate the Q1, Q3, and IQR
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Clip the data to within bounds to remove outliers
    smoothed = series.clip(lower=lower_bound, upper=upper_bound)
    
    # Print for debugging
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f"Smoothed Data: {smoothed}")
    
    return smoothed

# Function to detect outliers
def detect_outliers(series):
    # Calculate the Q1, Q3, and IQR
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Find the outliers based on the bounds
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    
    # Print for debugging
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    print(f"Detected Outliers: {outliers}")
    
    return outliers

# Function to resample data with a given frequency
def resample_data(series, freq='W-SUN'):
    # Resample and aggregate the data, here using mean for aggregation
    resampled = series.resample(freq).mean()  # Can also use .sum() depending on your requirement
    
    # Print for debugging
    print(f"Resampled Data: {resampled}")
    
    return resampled

# Function to visualize data
def plot_time_series_analysis(series):
    # Plot the original time series data
    plt.figure(figsize=(14, 6))
    plt.plot(series, label="Original Data", color="blue")
    plt.title("Time Series Data")
    plt.legend()
    plt.grid(True)
    plt.show()


# Function to compute rolling statistics
def rolling_window_stats(series, window=3, stats=["mean", "std", "median"]):
    """
    Computes rolling statistics (mean, std, median) over a specified window.

    Args:
        series (pd.Series): The input time series.
        window (int): The window size for rolling statistics.
        stats (list): List of statistics to calculate ("mean", "std", "median").

    Returns:
        dict: A dictionary containing rolling statistics as Series.
    """
    results = {}
    
    if "mean" in stats:
        results["mean"] = series.rolling(window=window).mean()
    
    if "std" in stats:
        results["std"] = series.rolling(window=window).std()
    
    if "median" in stats:
        results["median"] = series.rolling(window=window).median()
    
    # Print results for debugging
    for stat, result in results.items():
        print(f"{stat.capitalize()}:\n{result}\n")
    
    return results
