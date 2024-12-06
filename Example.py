import pandas as pd
from tsat import TimeSeriesAnalyzer

# Example data
data = pd.Series([10, 20, 30, 40, 50])

# Initialize the analyzer
analyzer = TimeSeriesAnalyzer(data)

# Smooth the data
smoothed_data = analyzer.smooth_data()

print(smoothed_data)

# Plot the data
analyzer.plot_time_series()
