import matplotlib.pyplot as plt

def plot(control_points, curve_points):

    plt.plot(
        control_points[:, 0],
        control_points[:, 1],
        "o--",
        label="Control polygon"
    )


    plt.plot(
        curve_points[:-1, 0],
        curve_points[:-1, 1],
        label="B-spline"
    )


    plt.title("B-Spline")

    plt.xlabel("X")

    plt.ylabel("Y")

    plt.grid()

    plt.legend()

    plt.show()