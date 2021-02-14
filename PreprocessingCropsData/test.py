from numpy import nan as NA
import pandas as pd

df = pd.DataFrame(([1, 4], [2, 5], [3, 6]), columns=["1", "2"])


# print(df.iloc[:, :])
# print()
# print(df.iloc[:, :].sum(axis=1))

# print(df)

print(df.iloc[:,0] + df.iloc[:, 1])
