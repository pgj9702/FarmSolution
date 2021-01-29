import datetime
import pandas as pd

year = "2020"

Day_YMD = datetime.date(int(year), 1, 1)

Day_YMD = Day_YMD + datetime.timedelta(days=1)

print(type(Day_YMD.year))

# df1 = pd.DataFrame(columns=["a", "b", "c", "d"])
# df1.to_csv("test.csv", index=False, encoding="utf-8-sig")
#
#
# for n in range(10):
#     df2 = pd.DataFrame(columns=["1", "2", "3", "4"])
#
#     res = {"1": n, "2": n+1, "3": n+2, "4": n+3}
#
#     df2 = df2.append(res, ignore_index=True)
#
#     df2.to_csv("test.csv", mode="a", header=False, index=False, encoding="utf-8-sig")
