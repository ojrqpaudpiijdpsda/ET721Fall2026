'''
Lab 7: 
Jiaxi Pang
Sep 28, 2026
'''

import pandas as pd

#Example DataFrame

dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict_)

print(df.head())
print(df.mean())

from static import get_teams
nba_teams = get_teams()

print(nba_teams)
print(f'First 2 Teams:  {nba_teams[:2]}')

# convert list to dictionary into a DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

#filter the row that contains the warriors nickname
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']

print(df_warriors)

#filter the id
id_warriors = df_warriors[['id']].values[0][0]
print(f'id of warriors = {id_warriors}')


#working with external api

import requests
'''
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cfcoursesdata/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
# save the download file as Golden_State.pkl
file_name = "Golden_State.pkl"
print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Download failed.")

games = pd.read_pickle(file_name)
print(games.head())

warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contrains('@ ')]

#calculate averages
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f'Warriors home average {home_avg_plus}')
print(f'Warriors away average {away_avg_plus}')
print(f'Warriors home points average {home_avg_pts}')
print(f'Warriors away points average {away_avg_pts}')
'''

print('\n Lab Exercise')

url = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"

response = requests.get(url)
if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print('Download Complete')
else:
    print('Download Failed')

games = pd.read_csv(file_name)
print(games.head())

man_city_vs_chelsea = games[
    ((games['HomeTeam'] == 'Man City') & (games['AwayTeam'] == 'Chelsea')) |
    ((games['HomeTeam'] == 'Chelsea') & (games['AwayTeam'] == 'Man City'))
]

print(man_city_vs_chelsea)

man_city_points = []
chelsea_points = []

for index, row in man_city_vs_chelsea.iterrows():
    if row['FTR'] == 'D':
        man_city_points.append(1)
        chelsea_points.append(1)
    elif row['FTR'] == 'H':
        if row['HomeTeam'] == 'Man City':
            man_city_points.append(3)
            chelsea_points.append(0)
        else:
            man_city_points.append(0)
            chelsea_points.append(3)
    elif row['FTR'] == 'A':
        if row['AwayTeam'] == 'Man City':
            man_city_points.append(3)
            chelsea_points.append(0)
        else:
            man_city_points.append(0)
            chelsea_points.append(3)

print(f"Man City average points: {sum(man_city_points) / len(man_city_points)}")
print(f"Chelsea average points: {sum(chelsea_points) / len(chelsea_points)}")