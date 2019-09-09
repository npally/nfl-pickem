from bs4 import BeautifulSoup
import requests
import csv

CSV_FILE = "records.csv"

abb_dict = {'New Orleans Saints': 'NO', 'Pittsburgh Steelers': 'PIT', 'New England Patriots': 'NE',
            'Tampa Bay Buccaneers': 'TB', 'Philadelphia Eagles': 'PHI', 'Atlanta Falcons': 'ATL', 'Cleveland Browns': 'CLE',
            'Cincinnati Bengals': 'CIN', 'Oakland Raiders': 'OAK', 'Buffalo Bills': 'BUF', 'New York Giants':
            'NYG', 'Detroit Lions': 'DET', 'Los Angeles Rams': 'LAR', 'Carolina Panthers': 'CAR', 'San Francisco 49ers': 'SF',
            'Indianapolis Colts': 'IND', 'Seattle Seahawks': 'SEA', 'Arizona Cardinals': 'ARI', 'Houston Texans': 'HOU',
            'Tennessee Titans': 'TEN', 'Jacksonville Jaguars': 'JAX', 'Chicago Bears': 'CHI', 'Los Angeles Chargers': 'LAC',
            'Miami Dolphins': 'MIA', 'New York Jets': 'NYJ', 'Baltimore Ravens': 'BAL', 'Kansas City Chiefs': 'KC',
            'Denver Broncos': 'DEN', 'Washington Redskins': 'WAS', 'Green Bay Packers': 'GB', 'Minnesota Vikings': 'MIN', 'Dallas Cowboys': 'DAL'}


d = {}
nfl_teams_list = []
afc_stats_list = []
nfc_stats_list = []

# custom functions

# Gets stats from each conference table


def get_stats(conf, new_list):
    for team in conf:
        nl = []
        stats = team.find_all("td")

        for stat in stats:
            nl.append(stat.text)
        if len(nl) > 1:
            new_list.append(nl)

    return new_list

# For cleaning strings


def clean(s):
    bc = ['+', '*', ]
    ns = ""
    for c in s:
        if c in bc:
            ns += ""
        else:
            ns += c

    return ns


source = 'https://www.pro-football-reference.com/years/2019/'
page = requests.get(source)

soup = BeautifulSoup(page.text, 'lxml')

table_body = soup.find_all('tbody')
afc = table_body[0]
nfc = table_body[1]

# Get a list of teams
teams = soup.find_all("th", class_="left")[1:]

for team in teams:
    team = team.text.strip()
    t = clean(team)
    if len(t) > 2:
        nfl_teams_list.append(t)

# Scraping for AFC teams
afc_teams = afc.find_all('tr')[1:]
afc_stats_list = get_stats(afc_teams, afc_stats_list)


# Scraping for NFC teams
nfc_teams = nfc.find_all('tr')[1:]
nfc_stats_list = get_stats(nfc_teams, nfc_stats_list)


#  Lists get converted into final dictionary
x = 0
for i in range(32):
    if i < 16:
        d[nfl_teams_list[i]] = afc_stats_list[i][:5]

    if i > 15:
        d[nfl_teams_list[i]] = nfc_stats_list[x][:5]
        x += 1

# Creates CSV_File with scraped data

with open(CSV_FILE, mode='w') as csv_file:
    fieldnames = ['team_name', 'abb', 'wins', 'losses', 'ties', 'points_for']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for key, value in d.items():
        writer.writerow(
            {'team_name': key,
             'abb': abb_dict[key],
             'wins': value[0],
             'losses': value[1],
             'ties': value[2],
             'points_for': value[4]})
