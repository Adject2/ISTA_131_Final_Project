import pandas as pd
import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i] + 2, y[i], ha = 'center')

def get_data(fn):
    df = pd.read_csv(fn, encoding='utf_8', encoding_errors='replace')
    return df

df = get_data("ESport_Earnings.csv")


country_df = df.groupby(['Top_Country']).count()

single_counts = country_df['IdNo'].sort_values(ascending=False)[:10]

print(single_counts)

#print(money_df)

title = "Top 10 Countries by Number of 'Top Country' Occurrences"

colors = [(1-(x*0.1), x*0.1, 1) for x in range(10)]
print(colors)

plt.bar(single_counts.index, single_counts, color=colors)
addlabels(single_counts.index, single_counts)
plt.title(title, fontsize=18)
plt.ylabel("Number of Games as Leading Country", fontsize =16)
plt.xlabel("Country", fontsize = 18)
plt.xticks(rotation=45, ha='right')
plt.gcf().subplots_adjust(bottom=0.3)
plt.gcf().set_facecolor('lightgrey')
plt.show()