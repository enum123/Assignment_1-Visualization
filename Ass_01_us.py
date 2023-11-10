import pandas as pd
import matplotlib.pyplot as plt


def plot_line_graph(x, y, title, x_label, y_label, legend_labels=None,
                    colors=None, markers=None, line_styles=None):
    """
    Creating a Line plot using Matplotlib's pyplot with x and y values.

    Parameters:
    - x: List of x-axis values.
    - y: List of corresponding y-axis values.
    - title: Title of the plot.
    - x_label: Label for the x-axis.
    - y_label: Label for the y-axis.
    - legend_labels: Legends for the graph.
    """
    plt.figure(figsize=(8, 8))
    # Plot the lines
    for i in range(len(y)):
        if colors is not None:
            color = colors[i]
        else:
            color = None
        if markers is not None:
            marker = markers[i]
        else:
            marker = None
        if line_styles is not None:
            line_style = line_styles[i]
        else:
            line_style = None

        plt.plot(x[i], y[i], label=legend_labels[i] if legend_labels else None,
                 color=color,
                 marker=marker, linestyle=line_style)

    # Set labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add a legend if legend_labels are provided
    if legend_labels:
        plt.legend()

    # Display the plot
    plt.grid(True)
    plt.savefig('Avocado_line_plot.jpg', dpi=500)
    plt.show()


def create_bar_plot(x_values, y_values, color, title="Bar Plot",
                    x_label="X-axis",
                    y_label="Y-axis", y_ticks=[], y_tick_label=[]):
    """
    Creating a bar plot using Matplotlib's pyplot.

    Parameters:
    - x_values: List of x-axis values.
    - y_values: List of corresponding y-axis values.
    - title: Title of the plot (default is "Bar Plot").
    - x_label: Label for the x-axis (default is "X-axis").
    - y_label: Label for the y-axis (default is "Y-axis").
    """
    # Create a bar plot
    fig, ax = plt.subplots(figsize=(8, 8))
    bars = ax.bar(x_values, y_values, color=color)
    for bars in ax.containers:
        ax.bar_label(bars)
    # Add title and labels
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_tick_label)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Show the plot
    plt.savefig('Avocado_bar_plot.jpg', dpi=500)
    plt.show()


def create_scatter_plot(x_values, y_values, labels, title="Scatter Plot",
                        x_label="X-axis", y_label="Y-axis"):
    """
    Creating a scatter plot using Matplotlib's pyplot.

    Parameters:
    - x_values: List of x-axis values.
    - y_values: List of corresponding y-axis values.
    - title: Title of the plot (default is "Scatter Plot").
    - x_label: Label for the x-axis (default is "X-axis").
    - y_label: Label for the y-axis (default is "Y-axis").
    """
    # Create a scatter plot
    plt.figure(figsize=(8, 8))
    for i in range(len(x_values)):
        plt.scatter(x_values[i], y_values, label=labels[i], alpha=0.6)

    # Add title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()

    # Show the plot
    plt.savefig('Avocado_scatter_plot.jpg', dpi=500)
    plt.show()


def get_data_and_plots(dataframe):
    """
    Refining Data for the plots from Avocado Dataset.

    Parameters:
    - dataframe: DateFrame of Avocado Data Set.
    """
    # Refining Data For line plot.
    # getting the mean of average Price grouped by type and year.
    org_data = dataframe.groupby(['type', 'year'])['AveragePrice'].mean()
    org_data = pd.DataFrame(org_data)
    org_data = org_data.reset_index()
    conv_data = org_data[org_data['type'] == "conventional"]
    org_data = org_data[org_data['type'] == "organic"]
    title = "Comparison between Organic and Conventional"\
            " Avocado’s average price from 2015 to 2018."
    x_label = "Years"
    y_label = "Avarage Price in $"
    legend_labels = ['organic', 'conventional']
    colors = ['red', 'green']
    # Giving Data to Line Plot Funtion for plotting.
    plot_line_graph([org_data['year'], conv_data['year']],
                    [org_data['AveragePrice'], conv_data['AveragePrice']],
                    title, x_label, y_label, legend_labels, colors)
    # Refining data for bar plot.
    # getting data of total volume sold over year in each region
    reg_vol_sol = dataframe.groupby(['region', 'year'])['Total Volume'].sum()
    reg_vol_sol = pd.DataFrame(reg_vol_sol)
    reg_vol_sol = reg_vol_sol.reset_index()
    reg_vol_sol = reg_vol_sol[reg_vol_sol['year'] == 2015]
    reg_vol_sol = reg_vol_sol.sort_values(by='Total Volume', ascending=True)
    title = "Ten Regions with least Avocado's sale"
    y_value = list(reg_vol_sol['Total Volume'] / 1000)
    labels = list(reg_vol_sol['region'])
    x_label = "Regions"
    y_label = 'Total Volume Sold'
    color = ['lightblue', 'blue', 'purple', 'red', 'green']
    y_tick = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    y_tick_label = ['1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
    # Giving the data to bar plot funtion for plotting.
    create_bar_plot(labels[:10], y_value[:10], color, title, x_label,
                    y_label, y_tick, y_tick_label)
    # Refining the data for Scatter plot.
    # Getting the data of bags and total volume for comparision.
    Small_Bags_data = dataframe['Small Bags']
    Large_Bags_data = dataframe['Large Bags']
    EX_Large_Bags_data = dataframe['XLarge Bags']
    total_vol = dataframe['Total Volume']
    labels = ['Small Bags', 'Large Bags', 'XLarge Bags']
    title = 'Comparison Between Different Categories of  Avocado Bag sold'
    x_label = 'Number of Bages Sold'
    y_label = 'Total Volume Sold'
    # Giving data to Scatter plot Funtion for plotting.
    create_scatter_plot([Small_Bags_data, Large_Bags_data, EX_Large_Bags_data],
                        total_vol, labels, title, x_label, y_label)
# Defining dataframe equal to avocado data set.
dataframe = pd.read_csv('avocado.csv')
get_data_and_plots(dataframe)
