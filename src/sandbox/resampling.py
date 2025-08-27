import pandas as pd
from pathlib import Path
from scipy.interpolate import interp1d

# Sample dictionary
original_dict = {
    "Freq": [0.2, 2, 3, 4, 5, 100],
    "Data": [11.2, 21, 32.5, 45, 60, 61]
}

directory = Path(__file__).cwd() / "mock_data"

# Read CSV file into a DataFrame
df = pd.read_csv(directory / "transferimpedance.csv")

# Interpolate the data based on the frequencies in original_dict
interpolator = interp1d(df["Freq"], df["Data"], kind='linear',
                        fill_value='extrapolate')
resampled_data = interpolator(original_dict["Freq"])

# Perform element-wise operation of the "Data" columns
new_data = [x - y for x, y in zip(original_dict["Data"], resampled_data)]

# Print updated dictionary
print(original_dict["Freq"])
print(original_dict["Data"])
print(resampled_data)
print(new_data)