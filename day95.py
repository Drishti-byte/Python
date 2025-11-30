#program to create a line chart 
import matplotlib.pyplot as plt 
c1 = [1300, 1500, 2000, 2500, 3000]
c2 = [3000, 2000, 1000, 1500, 2500]
yrs = ["2020", "2021", "2022", "2023", "2024"]
plt.plot(yrs, c1, color = "Red", label = "Company A")
plt.plot(yrs, c2, color = "Blue", label = "Company B")
plt.title("Sales Report from 2020-2024")
plt.xlabel("Years")
plt.ylabel("Sales(in Lakhs)")
plt.show()