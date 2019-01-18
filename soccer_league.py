import csv
from collections import OrderedDict

def writer():
    pass


if __name__ == "__main__":

    # reader
    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        # add inexperienced players
        inex_players = {player: info for player, info in zip(range(28), rows) if info['Soccer Experience'] == 'NO'}
        popped = inex_players.popitem()

        # add only experienced players to teams
        sharks = {player: info for player, info in zip(range(1,7), rows[0:7]) if info['Soccer Experience'] == 'YES'}
        for i, o in inex_players.items():
            sharks[i] = o
        raptors = {player: info for player, info in zip(range(1,7), rows[6:13]) if info['Soccer Experience'] == 'YES'}
        dragons = {player: info for player, info in zip(range(1,7), rows[12:19]) if info['Soccer Experience'] == 'YES'}
    
            
    print(sharks)
