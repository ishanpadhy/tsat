import pandas as pd
from tsat import fill_missing_values, plot_trends

def test_fill_missing_values():
    series = pd.Series([1, None, 3, None, 5], index=pd.date_range("2023-01-01", periods=5))
    filled = fill_missing_values(series)
    assert filled.isna().sum() == 0, "Missing values were not filled correctly."
    print("fill_missing_values passed.")

def test_plot_trends():
    series = pd.Series([1, 2, 3, 4, 5], index=pd.date_range("2023-01-01", periods=5))
    try:
        plot_trends(series)
        print("plot_trends executed without error.")
    except Exception as e:
        print(f"plot_trends failed: {e}")

if __name__ == "__main__":
    test_fill_missing_values()
    test_plot_trends()
