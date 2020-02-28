import matplotlib.pyplot as plt
import numpy as np
pi = np.degrees(np.pi)


def get_x_coordinates(s_point, e_point):
    return np.arange(s_point, e_point, 1)


def set_plot_coordinates(x_coordinates, y_coordinates):
    plt.stem(x_coordinates, y_coordinates, '-', use_line_collection=True)
    plt.grid()


def set_plot(x_label=None, y_label=None, title=None):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if title:
        plt.savefig("{}.png".format(title))


def show():
    plt.show()



