#program to create a pie chart 
import matplotlib.pyplot as plt 
streams = ["Medical", "Non-Medical", "Commerce with Maths", "Commerce with IP", "Arts"]
students = [10, 20, 30, 20, 20]
plt.pie(students, colors = ["Yellow", "Orange", "Blue", "Pink", "Purple"], labels = streams)
plt.title("Streams opted by students after 10th")
plt.show()