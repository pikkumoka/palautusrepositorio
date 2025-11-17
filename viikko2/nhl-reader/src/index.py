from rich.console import Console
from rich.theme import Theme
from rich.table import Table
console = Console(theme=Theme({"input": "bold cyan"}))

import requests
from player import Player

class PlayerReader :
    def __init__(self, url) :
        self.url = url
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats :
    def __init__(self, reader) :
        self.reader = reader

    def top_scorers_by_nationality(self, nationality) :
        nat_players = []

        for player in self.reader.players :
            if player.nationality == nationality.upper() :
                nat_players.append(player)

        nat_players.sort(key=lambda p: p.goals + p.assists, reverse=True)

        return nat_players

def fetch_players_by_season(season, nationality) :
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    return stats.top_scorers_by_nationality(nationality)

def choose_nationality() :
    print("Nationality")
    nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", 
                     "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", 
                     "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]

    while True :
        nat = str(console.input("[magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/" \
        "FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS] : " \
        "Enter XXX to exit "))

        if nat.upper() not in nationalities :
            print("Try again")

        else :
            return nat

def choose_season() :
    print("Season")
    seasons = ["2025-26", "2024-25", "2023-24", "2022-23", "2021-22", "2020-21", "2019-20", "2018-19"]

    while True :
        season = str(console.input("[2025-26/2024-25/2023-24/2022-23/" \
        "2021-22/2020-21/2019-20/2018-19] : "))
        if season not in seasons :
            print("Try again")

        else :
            return season

def print_info(players, season, nationality) :
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), 
                      str(player.assists), str(player.goals + player.assists))

    console.print(table)

def main():
    while True :
        nat = choose_nationality()
        if nat == "xxx" or nat == "XXX" :
            break
        season = choose_season()
        players = fetch_players_by_season(season, nat)

        print_info(players, season, nat)

main()