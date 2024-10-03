import pandas as pd

df = pd.read_csv('lucas.csv')

has_nan = df.isnull().values.any()
non_numeric = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).isnull().values.any()

print("Has NaN:", has_nan)
print("Has non-numeric values:", non_numeric)