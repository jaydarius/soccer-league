import csv
from collections import OrderedDict

def writer(*teams):
    with open("teams.txt", "a") as file:
        file.write(teams+"\n")
    

if __name__ == "__main__":
    ex_players = []
    inex_players = []

    # Make a list of players from soccer_players.csv
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # Categorize Experienced players
    for row in rows:
        if row['Soccer Experience'] == 'YES':
            ex_players.append(row)

    # Categorize Inexperienced players
    for row in rows:
        if row['Soccer Experience'] == 'NO':
            inex_players.append(row)

    # Assign players to 3 teams
    sharks = ex_players[0:3] + inex_players[0:3]
    raptors = ex_players[3:6] + inex_players[3:6]
    dragons = ex_players[6:9] + inex_players[6:9]

    # For dictionary in my list, print the value for the dictionary's name
    for dicty in sharks:
        print(dicty['Name'])
    # Write to teams.txt