import numpy as np
from bspline.basis import basis_function


def evaluate_spline( u, control_points, degree, knots):

    curve_point = np.zeros(2)

    for i in range(len(control_points)):

        influence = basis_function(i,degree,u, knots)
        curve_point += (influence * control_points[i])

    return curve_point