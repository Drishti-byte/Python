#program to create a histogram 
import matplotlib.pyplot as plt 
items = ["electronics", "medicines", "stationary", "equipments"]
defects = [10, 20, 13, 14, 16, 18, 20]
plt.hist(defects, bins = 5, color = "blue")
plt.title("Defects found")
plt.xlabel("Items found with defects")
plt.ylabel("Numbers of defected peices")
plt.show()