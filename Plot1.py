import pandas as pd
import matplotlib.pyplot as plt

# Read in the data
df = pd.read_csv('Esport_Earnings.csv', encoding='ISO-8859-1')

# Sort the data by total earnings in descending order
df = df.sort_values(by='TotalMoney', ascending=False)

# Create a bar plot
fig, ax = plt.subplots(figsize=(12,6))
fig.subplots_adjust(top=0.94,
bottom=0.095,
left=0.218,
right=0.988,
hspace=0.2,
wspace=0.2)
ax.barh(df['Genre'], df['TotalMoney']/1000000)

# Set the plot title and axis labels
ax.set_title('Total Esport Earnings by Genre')
ax.set_xlabel('Total Earnings (Millions)')
ax.set_ylabel('Genre')

# Display the plot
plt.show()
