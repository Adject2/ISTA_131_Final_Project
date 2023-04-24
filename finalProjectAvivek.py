#Author: Ashwin Vivek
#Class: ISTA 131
#Section leader: Kapua Loane
#Date: 4/20/2023
#Assignment: Final Project
# Description: This file contains code used to make three data plots/charts from the
#               Esport_Earnings.csv

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from matplotlib.ticker import MultipleLocator


def get_Esports_frame():
    df = pd.read_csv("ESport_Earnings.csv", index_col=0, encoding='latin-1')
    #df = pd.read_csv("ESport_Earnings.csv", index_col=0, skiprows=52, nrows=17, encoding='latin-1')
    return df

def make_fig_1(df):
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'gray', 'brown', 'pink', 'olive', 'cyan', 'yellow', 'black']
    labels = {}

    #Filtering the rows whose GameName contains "Call of Duty" but not "Call of Duty: Mobile"
    df_cod = df[df["GameName"].str.contains("Call of Duty") & ~df["GameName"].str.contains("Call of Duty: Mobile")]

    #Creating a scatter plot of the data and color code each point
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, (game, group) in enumerate(df_cod.groupby('GameName')):
        ax.scatter(group['Releaseyear'], group['TotalMoney'], c=colors[i % len(colors)], label=game)
        labels[game] = colors[i % len(colors)]

    #Adding axis labels and a title
    plt.xlabel('Game Release Year')
    plt.ylabel('Total Money Earned (Millions)')
    plt.title('Call of Duty: Total Money Earned vs Release Year')

    #Adding a line of regression to the data
    x = sm.add_constant(df_cod['Releaseyear'])
    model = sm.OLS(df_cod['TotalMoney'], x).fit()
    slope = model.params[1]
    intercept = model.params[0]
    plt.plot(df_cod['Releaseyear'], slope * df_cod['Releaseyear'] + intercept, color='black')

    #Set y-axis limits
    ax.set_ylim(50000, 7000000)

    #Setting y-axis tick locator at every half a million
    ax.yaxis.set_major_locator(MultipleLocator(500000))

    #Creating a legend and apply spacing
    handles = [plt.Line2D([], [], marker='o', linestyle='None', color=c, label=l) for l, c in labels.items()]
    plt.legend(handles=handles, loc='best')
    plt.subplots_adjust(wspace=0.3)

def make_fig_2(df):
    #Creating dataframe with top 10 earning Fighting Games
    df_fg = df[df["Genre"].str.contains("Fighting Game")]
    df_fg = df_fg.sort_values(by='TotalMoney')
    df_fg10 = df_fg.tail(10)

    #Creating horizontal bar chart with colors
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'gray', 'brown', 'pink', 'olive', 'cyan']
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.barh(df_fg10['GameName'], df_fg10['TournamentNo'],color=colors)

    #Adding y-value labels to the bars
    for i, bar in enumerate(bars):
        ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                str(df_fg10.iloc[i]['TournamentNo']), ha='left', va='center', fontsize=10)

    #Adding axis labels and a title
    plt.xlabel('Number of Tournaments', fontsize=12)
    plt.ylabel('Top 10 Earning Fighting Games', fontsize=12)
    plt.title('The Number of Tournaments for the Top Earning Fighting Games', fontsize=14)
    
    #Adjusting subplot parameters
    plt.subplots_adjust(left=0.15)

def make_fig_3(df):
    df_2015 = df.loc[(df["Top_Country"] == "United States") & (df["Releaseyear"] >= 2015), :]
    df_2015 = df_2015.sort_values(by='Top_Country_Earnings')
    df_10 = df_2015.tail(10)
    print(df_10)

    #calculating the percentage of Top_Country_Earnings over TotalMoney
    df_10.loc[:, 'Pct_Earnings'] = df_10['Top_Country_Earnings'] / df_10['TotalMoney'] * 100

    fig, ax = plt.subplots()
    ax.barh(df_10['GameName'], df_10['Pct_Earnings'], color='purple')

    #applying labels with percentage values by each bar
    for i, (name, value) in enumerate(zip(df_10['GameName'], df_10['Pct_Earnings'])):
        ax.text(value + 1, i, f'{value:.2f}%', ha='left', va='center')

    #setting the title and axis labels
    ax.set_title('Top 10 Games by Percentage of Total Earnings in the US', fontsize=14)
    ax.set_xlabel('Percentage of Global Earnings', fontsize=12)
    ax.set_ylabel('Top 10 US Games since 2015', fontsize=12)
    
    # Adjust subplot parameters
    plt.subplots_adjust(left=0.15)



    
def main():
    df = get_Esports_frame()
    make_fig_1(df)
    make_fig_2(df)
    make_fig_3(df)
    plt.show()

if __name__ == "__main__":
    main()