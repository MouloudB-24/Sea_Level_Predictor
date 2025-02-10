import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7, label="Sea level")

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    intercept = result.intercept

    # Prepare values of the regression line
    years_extended =list(range(df['Year'].min(), 2051))
    predicted_levels = [slope * year + intercept for year in years_extended]

    plt.plot(years_extended, predicted_levels, color='green', label='Regression line from 1880')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = result_recent.slope
    intercept_recent = result_recent.intercept

    years_extended_recent = np.linspace(2000, 2050, 51)
    predicted_levels_recent = [slope_recent * year + intercept_recent for year in years_extended_recent]

    plt.plot(years_extended_recent, predicted_levels_recent, color='red', label='Regression line from 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == '__main__':
    draw_plot()