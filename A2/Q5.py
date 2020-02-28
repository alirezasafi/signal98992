import numpy as np
from A2.DrawPlot import get_x_coordinates, show, set_plot_coordinates, set_plot, pi
# input signal
x_coordinates = get_x_coordinates(s_point=-5, e_point=6)
y_coordinates = (3 * np.sin(np.radians(pi * x_coordinates))) + (3 * np.absolute(np.cos(np.radians(7 * x_coordinates))))
set_plot_coordinates(x_coordinates=x_coordinates, y_coordinates=y_coordinates)
set_plot(x_label="n", y_label="x[n]", title="Q5_in")
show()


def system(y_coordinates):
    for i in range(len(y_coordinates)):
        if y_coordinates[i] < 0:
            y_coordinates[i] = 0
        elif y_coordinates[i] > 5:
            y_coordinates[i] = 5
    return y_coordinates


# output signal
sys_x_coordinates = get_x_coordinates(s_point=-5, e_point=6)
sys_y_coordinates = system(y_coordinates)
set_plot_coordinates(x_coordinates=sys_x_coordinates, y_coordinates=sys_y_coordinates)
set_plot(x_label="n", y_label="y[n]", title="Q5_out")
show()
