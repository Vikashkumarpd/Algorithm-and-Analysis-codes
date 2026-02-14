import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("quick_sort.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, marker='o')
plt.title("quick_sort")
plt.xlabel("n value")
plt.ylabel("Time (us)")
plt.grid(True)
plt.show()
