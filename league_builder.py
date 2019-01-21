import csv

ex_players = []
inex_players = []

# Write teams as <lists> to teams.txt
def teamstxt_writer(teams):
    with open("teams.txt", "a") as file:
        file.write(teams+"\n")

# Concatentate team player data to a string
def create_str(team):
    for player_dict in team:
            string = (player_dict['Name'] + '\n  ' + 'Soccer Experience: ' + player_dict['Soccer Experience'] + ', ' + 'Guardian Name(s): ' + player_dict['Guardian Name(s)'])
            string = (f"{player_dict['Name']}\n  "
                      f"Soccer Experience: {player_dict['Soccer Experience']}, "
                      f"Guardian Name(s): {player_dict['Guardian Name(s)']}"
                      )
            teamstxt_writer(string)

# Write welcome letter to each player
def write_welcome(team_list, team_name):
    for player in team_list:
        filename = player['Name'].replace(" ", "_") + ".txt"
        welcome_letter = (f"Dear {player['Guardian Name(s)']},\n"
                          f"{player['Name']} is now on team {team_name}!\n"
                          "We look forward to fun and fair play.\n"
                          "The first practice is January 26 at 2pm.")
                            
        with open(filename, "a") as file:
            file.write(welcome_letter)
        

if __name__ == "__main__":

    # Make a <list> of players from soccer_players.csv
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

    # Write roster to teams.txt
    teamstxt_writer('== Team Sharks ==\n')
    create_str(sharks)
    teamstxt_writer('\n== Team Raptors ==\n')
    create_str(raptors)
    teamstxt_writer('\n== Team Dragons ==\n')
    create_str(raptors)

    # Write welcome letters to Parent/Guardians
    write_welcome(sharks, 'Sharks')
    write_welcome(raptors, 'Raptors')
    write_welcome(dragons, 'Dragons')
