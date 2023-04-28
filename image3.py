import pandas as pd
import matplotlib.pyplot as plt
        

def get_data(fn):
    df = pd.read_csv(fn, encoding='utf_8', encoding_errors='replace')
    return df

df = get_data("ESport_Earnings.csv")

title = "Game Titles by Release Date"

fps_df = df.loc[df['Genre'] == 'First-Person Shooter']
fps_counts = fps_df.groupby(['Releaseyear']).count()

moba_df = df.loc[df['Genre'] == 'Multiplayer Online Battle Arena']
moba_counts = moba_df.groupby(['Releaseyear']).count()

fight_df = df.loc[df['Genre'] == 'Fighting Game']
fight_counts = fight_df.groupby(['Releaseyear']).count()



# Shit for regression graph
# m, b = np.polyfit(list(df['PlayerNo']), list(df['TotalMoney']), 1)

plt.plot(fight_counts.index, fight_counts, color = 'red')
plt.plot(moba_counts.index, moba_counts, color = 'blue')
plt.plot(fps_counts.index, fps_counts, color = 'limegreen')
plt.plot([1993, 1993], [1, 7], color='white')
plt.plot([2020, 2020], [5, 16], color='white')
plt.title(title, fontsize=18)
plt.xlabel("Year",fontsize=18)
plt.ylabel("Number of Games", fontsize=16)
plt.text(1993, 8, 'TMNT: Tournament Fighters (1993)', ha='left', color='white')
plt.text(2020, 16.2, 'COD: Warzone (2020)', ha='right', color='white')

plt.legend(['Fighting Games', 'Battle Arenas', 'FPS Games'], loc = 'upper left')

plt.gca().get_legend().legendHandles[1].set_color('blue')
plt.gca().get_legend().legendHandles[2].set_color('limegreen')

plt.gcf().subplots_adjust(bottom=0.3)
plt.gca().set_facecolor('black')

plt.show()
