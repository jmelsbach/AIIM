import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets


def plot_function(
    f,
    x: float = 0,
    min: float = -8,
    max: float = 8,
    num_points: int = 100,
):
    """
    Plots the function f in the range [min, max] with num_points.

    Args:
    f: function
    x: float
    min: float
    max: float
    num_points: int
    """

    _x = np.linspace(min, max, num_points)
    y = f(_x)
    plt.plot(_x, y)
    plt.plot(x, f(x), "ro")
    plt.legend([f"{f.__name__}({x:.2f})={f(x):.2f}"])
    plt.show()


def interactive_plot(fn, min=-8, max=8):
    a = widgets.FloatSlider(description='Input Value', min=min, max=max)
    out = widgets.interactive_output(plot_function, {'f': widgets.fixed(fn), 'x': a})
    return widgets.VBox([a, out])
