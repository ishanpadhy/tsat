import pandas as pd
from tsat import smooth_data, detect_outliers, resample_data, plot_time_series_analysis, rolling_window_stats

# Test the smooth_data function
def test_smooth_data():
    # Create a sample time series
    series = pd.Series([1, 2, 3, 100], index=pd.date_range("2023-01-01", periods=4, freq="D"))
    
    # Apply smoothing
    smoothed = smooth_data(series)
    
    # Assert the smoothed values are within the expected range
    assert smoothed.iloc[3] == 65.5, "Smoothing did not clip outliers to the correct upper bound."
    
    print("smooth_data passed.")

# Test the detect_outliers function
def test_detect_outliers():
    # Create a sample time series with an outlier
    series = pd.Series([1, 2, 3, 100], index=pd.date_range("2023-01-01", periods=4, freq="D"))
    
    # Detect outliers
    outliers = detect_outliers(series)
    
    # Expected outlier is at index 2023-01-04 with value 100
    expected_outliers = [pd.Timestamp('2023-01-04 00:00:00')]
    
    # Adjust the outliers to match the expected output
    outlier_indexes = outliers.index.tolist()
    
    # Assert the outliers are correctly detected
    assert outlier_indexes == expected_outliers, f"Outliers not detected correctly. Detected: {outliers}, Expected: {expected_outliers}"
    
    print("detect_outliers passed.")

# Test the resample_data function
def test_resample_data():
    # Create a sample time series
    series = pd.Series([1, 2, 3], index=pd.date_range("2023-01-01", periods=3, freq="D"))
    
    # Resample the data with weekly frequency starting on Sunday
    resampled = resample_data(series, "W-SUN")
    
    # Debug print the resampled result
    print(resampled)
    
    # Assert that the resampled data has 2 values
    assert len(resampled) == 2, f"Expected 2 resampled values, but got {len(resampled)}."
    
    # Assert the aggregated values for the respective weeks
    assert resampled.iloc[0] == 1.0, f"Expected 1.0 for the first week, but got {resampled.iloc[0]}"
    assert resampled.iloc[1] == 2.5, f"Expected 2.5 for the second week, but got {resampled.iloc[1]}"
    
    print("resample_data passed.")

# Test the plot_time_series_analysis function
def test_plot_time_series_analysis():
    # Create a sample time series
    series = pd.Series(
        [1, 2, 3, 100, 50, 60, 5, 10, 15],
        index=pd.date_range("2023-01-01", periods=9, freq="D"),
    )
    
    # Generate the plots
    plot_time_series_analysis(series)
    
    print("plot_time_series_analysis executed successfully.")


# Test the rolling_window_stats function
def test_rolling_window_stats():
    # Create a sample time series
    series = pd.Series(
        [10, 20, 30, 40, 50, 60, 70],
        index=pd.date_range("2023-01-01", periods=7, freq="D"),
    )
    
    # Calculate rolling statistics
    results = rolling_window_stats(series, window=3)
    
    # Assert the statistics are calculated correctly (using sample checks)
    assert results["mean"].iloc[2] == 20, f"Expected mean: 20, but got {results['mean'].iloc[2]}"
    assert results["std"].iloc[3] == 10.0, f"Expected std: 10.0, but got {results['std'].iloc[3]}"  # Updated to 10.0
    assert results["median"].iloc[4] == 40, f"Expected median: 40, but got {results['median'].iloc[4]}"
    
    print("rolling_window_stats passed.")



# Run all tests
def run_tests():
    test_smooth_data()
    test_detect_outliers()
    test_resample_data()
    test_plot_time_series_analysis()
    test_rolling_window_stats()


# Execute the tests
run_tests()

