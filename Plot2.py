
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
from scipy import stats

#read the csv file into a pandas dataframe
df = pd.read_csv("Esport_Earnings.csv", encoding='ISO-8859-1')

#filter the data frame to only show the games with "FIFA" in the GameName
fifa_df = df[(df["GameName"].str.contains("FIFA")) & (df["Releaseyear"] >= 2010)]


#create a scatter plot for each game name
fig, ax = plt.subplots()
for name in fifa_df["GameName"].unique():
    game_df = fifa_df[fifa_df["GameName"] == name]
    ax.scatter(game_df["Releaseyear"], game_df["TotalMoney"], label=name)
    for i, txt in enumerate(game_df["GameName"].values):
        ax.annotate(txt, (game_df["Releaseyear"].values[i], game_df["TotalMoney"].values[i]))

#add labels to the axes
ax.set_xlabel("Release Year")
ax.set_ylabel("Total Money Earned (in USD)")

#set x-axis limits to start from 2010 to 2020
start_year = 2010
end_year = 2020
ax.set_xlim(start_year, end_year)

#set y-axis formatter to show values in USD
#set y-axis formatter to show values in USD with a decimal point
def usd_format(x, pos):
    if x < 500000:
        return '${:.1f}K'.format(x/1000)
    else:
        return '${:.1f}M'.format(x/1000000)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(usd_format))


#add a regression line
import numpy as np
from sklearn.linear_model import LinearRegression

X = fifa_df["Releaseyear"].values.reshape(-1,1)
Y = fifa_df["TotalMoney"].values.reshape(-1,1)

reg = LinearRegression().fit(X, Y)
Y_pred = reg.predict(X)

plt.plot(X, Y_pred, color='red')


#add a title to the plot
ax.set_title("Total Money Earned vs Release Year for FIFA Games")

#add a legend
ax.legend()

#display the plot
plt.show()
