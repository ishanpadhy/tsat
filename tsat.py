import pandas as pd
import matplotlib.pyplot as plt

class TimeSeriesAnalyzer:
    def __init__(self, data):
        """
        Initialize the TimeSeriesAnalyzer with the given data.

        Args:
            data (pd.Series): Time series data to analyze.
        """
        self.data = data

    def smooth_data(self):
        """
        Smooth the data by clipping outliers based on the IQR method.
        Returns:
            pd.Series: Smoothed time series data.
        """
        Q1 = self.data.quantile(0.25)               # First Quartile
        Q3 = self.data.quantile(0.75)               # Third Quartile
        IQR = Q3 - Q1                               # Inter Quartile Range = It is the range between 1st quartile and 3rd quartile

        lower_bound = Q1 - 1.5 * IQR                # defining lower bound
        upper_bound = Q3 + 1.5 * IQR                # defining upper bound

        smoothed = self.data.clip(lower=lower_bound, upper=upper_bound)         # Clip the data to within the upper and lower bounds to remove outliers

        print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
        print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
        print(f"Smoothed Data:\n{smoothed}")

        return smoothed

    def detect_outliers(self):
        """
        Detect outliers in the time series based on the IQR method.
        Returns:
            pd.Series: Series containing outliers.
        """
        Q1 = self.data.quantile(0.25)               # First Quartile
        Q3 = self.data.quantile(0.75)               # Third Quartile
        IQR = Q3 - Q1                               # Inter Quartile Range = It is the range between 1st quartile and 3rd quartile

        lower_bound = Q1 - 1.5 * IQR                # defining lower bounds for outliers detection
        upper_bound = Q3 + 1.5 * IQR                # defining upper bounds for outliers detection

        # Find the outliers based on the bounds. If anything is below the lower bound or above the upper bound, then such elements are considered as outliers 
        outliers = self.data[(self.data < lower_bound) | (self.data > upper_bound)]         

        print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
        print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
        print(f"Detected Outliers:\n{outliers}")

        return outliers

    def resample_data(self, freq='W-SUN'):
        """
        Resample the time series data with the given frequency.

        Args:
            freq (str): Frequency string (e.g., 'W-SUN' for weekly resampling).

        Returns:
            pd.Series: Resampled time series data.
        """
        resampled = self.data.resample(freq).mean()                 # Resample and aggregate the data, here using mean for aggregation

        print(f"Resampled Data:\n{resampled}")
        return resampled

    def plot_time_series(self):
        """
        Visualize the time series data
        """
        plt.figure(figsize=(14, 6))
        plt.plot(self.data, label="Original Data", color="blue")
        plt.title("Time Series Data")
        plt.legend()
        plt.grid(True)
        plt.show()

    def rolling_window_stats(self, window=3, stats=["mean", "std", "median"]):
        """
        Compute rolling statistics (mean, std, median) over a specified window.

        Args:
            window (int): The window size for rolling statistics.
            stats (list): List of statistics to calculate ("mean", "std", "median").

        Returns:
            dict: A dictionary containing rolling statistics as Series.
        """
        results = {}

        if "mean" in stats:
            results["mean"] = self.data.rolling(window=window).mean()           # calculating the rolling mean from the series for a specified window

        if "std" in stats:
            results["std"] = self.data.rolling(window=window).std()             # calculating the rolling standard deviation from the series for a specified window

        if "median" in stats:
            results["median"] = self.data.rolling(window=window).median()       # calculating the rolling median from the series for a specified window

        for stat, result in results.items():
            print(f"{stat.capitalize()}:\n{result}\n")

        return results
