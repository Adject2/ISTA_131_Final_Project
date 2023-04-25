
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load data from CSV file using pandas
data = pd.read_csv('ESport_Earnings.csv', encoding='ISO-8859-1')

# Group data by game and top country, and sum the earnings
grouped_data = data.groupby(['GameName', 'Top_Country'])['Top_Country_Earnings'].sum().reset_index()

# Pivot the data to create a matrix with games as rows and top countries as columns
pivot_data = grouped_data.pivot(index='GameName', columns='Top_Country', values='Top_Country_Earnings')

# Limit to top 10 countries
top_10_countries = pivot_data.sum().sort_values(ascending=False).head(10).index
pivot_data = pivot_data[top_10_countries]

# Limit to top 10 games
top_10_games = pivot_data.sum(axis=1).sort_values(ascending=False).head(10).index
pivot_data = pivot_data.loc[top_10_games]

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(10, 8))
pivot_data.plot(kind='bar', stacked=True, ax=ax)

# Adjust subplots
fig.subplots_adjust(top=0.952, bottom=0.417, left=0.052, right=0.985, hspace=0.2, wspace=0.2)

# Set chart title and axis labels
ax.set_title('Top earning countries by game')
ax.set_xlabel('Game name')
ax.set_ylabel('Total earnings (in millions of USD)')

# Shrink x-axis labels font size
ax.tick_params(axis='x', labelsize=8)

# Show the total earnings above each bar
for i, patch in enumerate(ax.patches):
    # Calculate the total earnings for the current bar
    earnings = patch.get_height()
    # Add the earnings as text above the bar
    ax.text(patch.get_x() + patch.get_width() / 2, patch.get_y() + earnings + 5, '${:,.0f}'.format(earnings), ha='center')

# Set the y-tick formatter to display millions
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000000)))

# Show the chart
plt.show()
