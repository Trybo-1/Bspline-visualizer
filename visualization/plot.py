import matplotlib.pyplot as plt

print("Plotting points...")
points = [
    (0, 0),  # P0
    (1, 3),  # P1
    (3, 3),  # P2
    (4, 0)   # P3
]

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x, y, "o")
plt.title("Plot of Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()