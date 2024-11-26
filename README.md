Time Series Analysis Toolkit (TSAT)

To Be Completed !

Example Useage

import pandas as pd
from tsat import fill_missing_values, plot_trends

# Example time series data
data = pd.Series([1, None, 3, None, 5], index=pd.date_range("2023-01-01", periods=5))

# Fill missing values
filled_data = fill_missing_values(data)

# Plot trends
plot_trends(filled_data)
