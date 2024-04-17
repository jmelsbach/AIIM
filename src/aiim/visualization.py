import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import ipywidgets as widgets

import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
import torch


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



def plot_tensor_as_bar():
    """
    Plots a NumPy array or PyTorch tensor as a bar plot.

    Parameters:
    - data (numpy.ndarray or torch.Tensor): The data to plot.

    Returns:
    - None
    """
    
    a = widgets.FloatSlider(description='Input Value', min=min, max=max)
    b = widgets.FloatSlider(description='Input Value', min=min, max=max)
    c = widgets.FloatSlider(description='Input Value', min=min, max=max)
    d = widgets.FloatSlider(description='Input Value', min=min, max=max)
    e = widgets.FloatSlider(description='Input Value', min=min, max=max)

    data = np.array([a,b,c,d,e]) 

    # Ensure the data is a 1D array
    if data.ndim != 1:
        raise ValueError("Data must be a 1D array or tensor.")

    # Create the bar plot
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(data)), data)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Bar Plot of Data')
    plt.show()


# Update the softmax function to handle empty or zero-size arrays
def softmax(x):
    if x.size == 0:
        return np.array([])
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

# Function to plot the bar chart
def plot_softmax2(val1, val2, val3, val4, val5):
    values = np.array([val1, val2, val3, val4, val5])
    softmax_values = softmax(values)
    
    plt.bar(range(len(values)), softmax_values)
    plt.xlabel('Index')
    plt.ylabel('Softmax Probability')
    plt.title('Softmax Function Interactive Plot')
    plt.ylim(0, 1)
    plt.show()


def plot_softmax(val1, val2, val3, val4, val5):
    values = np.array([val1, val2, val3, val4, val5])
    softmax_values = softmax(values)
    
    # Clear the previous plot to prevent overlap
    plt.clf()
    
    # Create the bar chart
    bars = plt.bar(range(len(values)), softmax_values)
    
    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    
    plt.xlabel('Index')
    plt.ylabel('Softmax Probability')
    plt.title('Softmax Function Interactive Plot')
    plt.ylim(0, 1)
    plt.show()

# Create a function that sets up the sliders and the interactive plot
def softmax_with_sliders():
    # Create 5 sliders for input values
    sliders = {
        'val1': FloatSlider(min=-10, max=10, step=0.1, value=0, description='Value 1'),
        'val2': FloatSlider(min=-10, max=10, step=0.1, value=0, description='Value 2'),
        'val3': FloatSlider(min=-10, max=10, step=0.1, value=0, description='Value 3'),
        'val4': FloatSlider(min=-10, max=10, step=0.1, value=0, description='Value 4'),
        'val5': FloatSlider(min=-10, max=10, step=0.1, value=0, description='Value 5')
    }
    
    # Use the interact function to create the interactive plot
    interact(plot_softmax, **sliders)

# Call the function to display the sliders and the initial plot
softmax_with_sliders()