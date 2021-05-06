import matplotlib.pyplot as plt

# Use a black background for the displayed graph
plt.style.use('dark_background')


def plot_bar(labels, data, y_axis_label):

    # Pick n random colors
    # Where n is the length of the provided data/labels list
    from matplotlib import colors
    color_names = list(colors.CSS4_COLORS.keys())

    from random import sample
    random_colors = sample(color_names, len(labels))

    # Plot a bar chart with the provided labels and data
    plt.bar(labels, data, color=random_colors)
    plt.ylabel(y_axis_label)

    # Required to display the plotted bar
    plt.show()
