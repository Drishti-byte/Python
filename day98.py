#program to create multiple bar graphs using pandas 
import pandas as pd
import matplotlib.pyplot as plt 
c1 = [1800, 1500, 1000, 1500, 2000]
c2 = [2000, 2500, 1000, 1500, 2500]
yrs = ["2020", "2021", "2022", "2023", "2024"]
df = pd.DataFrame({"Years" : yrs, "Company A" : c1, "Company B" : c2})
df.index = df["Years"]
df.plot(kind = "bar", color = ["Red", "Green", "Yellow", "Orange", "Blue"])
plt.title("Sales Report from 2020-2024")
plt.xlabel("Years")
plt.ylabel("Sales(in Lakhs)")
plt.show()