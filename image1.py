import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(fn):
    df = pd.read_csv(fn, encoding='utf_8', encoding_errors='replace')
    return df

df = get_data("ESport_Earnings.csv")

title = "No. Players versus Total Prize Money\n For Tournaments under $10m"

m, b = np.polyfit(list(df['PlayerNo']), list(df['TotalMoney']), 1)

plt.plot(df['PlayerNo'], df['TotalMoney'], 'o')
plt.plot(df['PlayerNo'], df['PlayerNo']*m + b, 'black')
plt.title(title)
plt.xlabel("Player Count", fontsize = 18)
plt.ylabel("Total Prize Money (Per Million USD)", fontsize = 16)
plt.xticks(rotation=45, ha='right')
plt.gcf().subplots_adjust(bottom=0.3)

plt.show()