import matplotlib.pyplot as plt
import numpy as np


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
