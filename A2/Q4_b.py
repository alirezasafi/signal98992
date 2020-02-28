import numpy as np
from A2.DrawPlot import get_x_coordinates, show, set_plot, set_plot_coordinates, pi

x_coordinates = get_x_coordinates(s_point=-50, e_point=51)
y_coordinates = 2 * np.exp(x_coordinates/10)
set_plot_coordinates(x_coordinates=x_coordinates, y_coordinates=y_coordinates)
set_plot(x_label="n", y_label="x[n] = 2e^(n/10)", title="Q4_b")
show()