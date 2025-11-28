#program to create a bar graph 
import matplotlib.pyplot as plt 
x = ["English", "Hindi", "Maths", "Science", "Social Studies"]
y = [90, 75, 81, 65, 50]
plt.bar(x, y, color = ("Red", "Green", "Orange", "Blue", "Purple"))
plt.title("Student Report")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()