import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    result = linregress(x,y)
    xpred1 = pd.Series([i for i in range(1880,2051)])
    ypred1 = result.slope*xpred1 + result.intercept
    plt.plot(xpred1, ypred1, 'r')

    # Create second line of best fit
    newdf = df.loc[df["Year"]>=2000]
    xnew = newdf["Year"]
    ynew = newdf["CSIRO Adjusted Sea Level"]
    res = linregress(xnew,ynew)
    xpred2 = pd.Series([i for i in range(2000,2051)])
    ypred2 = res.slope*xpred2 + res.intercept
    plt.plot(xpred2, ypred2, 'b')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()