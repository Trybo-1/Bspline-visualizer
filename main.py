import numpy as np

from bspline.basis import *
from bspline.spline import evaluate_spline
from visualization.plot import plot

control_points = np.array([
    [0, 0],
    [1, 3],
    [3, 3],
    [4, 0],
    [6, 2],
    [7, 5],
    [9, 1]
])


degree = 3

knots = create_knot_vector(
    len(control_points),
    degree
)

curve_points = []


# The valid parameter range
t_values = np.linspace(
    knots[degree],
    knots[-degree - 1],
    500
)

for t in t_values:

    point = evaluate_spline(
        t,
        control_points,
        degree,
        knots
    )

    curve_points.append(point)


curve_points = np.array(curve_points)

plot(control_points, curve_points)