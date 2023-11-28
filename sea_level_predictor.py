import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot(start_year=1880, end_year=2050, title='Rise in Sea Level', show_best_fit=True):
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Filter data based on the selected year range
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

    # Create scatter plot
    plt.scatter(filtered_df['Year'], filtered_df['CSIRO Adjusted Sea Level'])

    if show_best_fit:
        # Create first line of best fit for the entire range
        slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
        x = pd.Series([i for i in range(start_year, end_year + 1)])
        y = intercept + slope * x
        plt.plot(x, y, 'r', label='Best Fit Line 1880-2050')

        # Create second line of best fit for years from 2000
        new_df = df[(df['Year'] >= 2000) & (df['Year'] <= end_year)]
        new_slope, new_intercept, _, _, _ = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
        new_x = pd.Series([i for i in range(max(2000, start_year), end_year + 1)])
        new_y = new_intercept + new_slope * new_x
        plt.plot(new_x, new_y, 'g', label='Best Fit Line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title(title)

    # Display the legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gcf()  # Return the figure object

