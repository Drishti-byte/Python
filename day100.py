#program to implement statistics on dataframe 
import pandas as pd 
c1 = [1300, 1500, 2000, 2200, 2500]
c2 = [3000, 3500, 2500, 2000, 1500]
c3 = [2000, 2500, 3000, 2500, 2000]
yrs = ["2020", "2021", "2022", "2023", "2024"]
df = pd.DataFrame({"Years" : yrs, "Company A" : c1, "Company B" : c2, "Company C" : c3})
print(df)
print(df.describe())