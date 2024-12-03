import pandas as pd
from tsat import smooth_data, detect_outliers, resample_data

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

# Run all tests
def run_tests():
    test_smooth_data()
    test_detect_outliers()
    test_resample_data()

# Execute the tests
run_tests()
