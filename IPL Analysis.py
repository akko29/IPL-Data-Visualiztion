
# coding: utf-8

# In[291]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Match.csv')
df_copy = df.copy()
df = df[['Season_Year','match_winner']]
df.sort_values('match_winner',ascending=True,inplace=True)
df.drop([605,611,241,486,511],inplace=True)
# chennai = np.array(df[df['match_winner']=='Chennai Super Kings'].index)
# kolkata = np.array(df[df['match_winner']=='Kolkata Knight Riders'].index)
# rajasthan = np.array(df[df['match_winner']=='Rajasthan Royals'].index)
# mumbai = np.array(df[df['match_winner']=='Mumbai Indians'].index)
# hyderabad = np.array(df[(df['match_winner']=='Sunrisers Hyderabad') | (df['match_winner']=='Deccan Chargers')].index)
# pune = np.array(df[(df['match_winner']=='Rising Pune Supergiants') | (df['match_winner']=='Pune Warriors')].index)
# gujarat = np.array(df[df['match_winner']=='Gujarat Lions'].index)
# punjab = np.array(df[df['match_winner']=='Kings XI Punjab'].index)
# delhi = np.array(df[df['match_winner']=='Delhi Daredevils'].index)
# bangalore = np.array(df[df['match_winner']=='Royal Challengers Bangalore'].index)
# kerala = np.array(df[df['match_winner']=='Kochi Tuskers Kerala'].index)
teams = ['Chennai Super Kings',
 'Delhi Daredevils',
 'Kings XI Punjab',
 'Kolkata Knight Riders',
 'Mumbai Indians',
 'Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad']
# plt.gca().axis([0,600,0,50])

# plt.hist(chennai,color='yellow')
# x = list(df['match_date'].groupby(df['match_winner']))
# x[0][1].index
# a = df.groupby('match_winner').count()
win_dict = (df['match_winner'].value_counts()).to_dict()
# win_dict = {'mumbai': count[0],'chennai': count[1],'kolkata':count[2],'bangalore':count[3],'punjab':count[4],'rajasthan':count[5],'delhi':count[6],'hyderabad':count[7]+count[8],'pune':count[9]+count[11],'gujarat':count[10]}
win_dict['Sunrisers Hyderabad'] = win_dict['Sunrisers Hyderabad'] + win_dict['Deccan Chargers'] 
del win_dict['Deccan Chargers']
del win_dict['Gujarat Lions']
del win_dict['Rising Pune Supergiants']
del win_dict['Pune Warriors']
del win_dict['Kochi Tuskers Kerala']
total_matches = (df_copy['Team1'].value_counts()+df_copy['Team2'].value_counts()).to_dict()
total_matches['Sunrisers Hyderabad'] = total_matches['Sunrisers Hyderabad'] + total_matches['Deccan Chargers'] 
del total_matches['Deccan Chargers']
del total_matches['Gujarat Lions']
del total_matches['Rising Pune Supergiants']
del total_matches['Pune Warriors']
del total_matches['Kochi Tuskers Kerala']
win_per = []
win_dict
for i in teams:
#     print(total_matches[ind])
    x = (win_dict[i]/total_matches[i])*100
    win_per.append(x)


# In[302]:


# cpick = mcol.LinearSegmentedColormap.from_list("My_ColorMap",['yellow','red','magenta','purple','blue','blue','red','orange'])
# c = cm.ScalarMappable(cmap=cpick)
colors = ['yellow','red','magenta','purple','cyan','blue','#950000','orange']

sns.barplot(teams,win_per,palette = colors,zorder=3)
plt.gca().grid(zorder=0)
plt.xlabel('Teams(IPL)')
plt.ylabel('Win %')
plt.title('Cummulative Win % of IPL Teams during 2008-17')
plt.xticks(rotation='90')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.show()
