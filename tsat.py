import pandas as pd

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
