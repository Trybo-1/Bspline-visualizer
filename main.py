import numpy as np

from bspline.spline import BSpline
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

spline = BSpline(control_points)

curve_points = spline.create_curve()

plot(spline.control_points, curve_points)