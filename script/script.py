import requests

players_url = 'http://127.0.0.1:8080/chess_players/'
tournaments_url = 'http://127.0.0.1:8080/tournaments/'
partitications_url = 'http://127.0.0.1:8080/partitipations/'

chess_players = [
    {"initials": "Rafael Savoyan", "country": "Georgia", "elo": 1000, "title": None},
    {"initials": "John Doe", "country": "US", "elo": 1200, "title": "Just a player"},
    {"initials": "Magnus Carlsen", "country": "Norway", "elo": 2831, "title": "GM"},
    {"initials": "Fabiano Caruana", "country": "US", "elo": 2805, "title": "GM"},
    {"initials": "Hikaru Nakamura", "country": "US", "elo": 2808, "title": "GM"},
    {"initials": "Ian Nepomniachtchi", "country": "Russia", "elo": 2755, "title": "GM"},
    {"initials": "Levon Aronian", "country": "US", "elo": 2747, "title": "GM"},
    {"initials": "Evgeniy Najer", "country": None, "elo": 2637, "title": "GM"},
    {"initials": "May Cassowary", "country": "France", "elo": 1954, "title": "IM"},
    {"initials": "Breeze Gosling", "country": "Canada", "elo": 1654, "title": None},
    {"initials": "Willie Box", "country": None, "elo": 1200, "title": None},
    {"initials": "Shelvasi Madaoro", "country": "China", "elo": 1845, "title": "IM"},
    {"initials": "Arieie Aelsinore", "country": "Italy", "elo": 1771, "title": "FM"},
    {"initials": "Timos Catell", "country": None, "elo": 956, "title": None},
    {"initials": "Remedios Zavaleta", "country": "Mexico", "elo": 884, "title": None},
    {"initials": "Nikolai Mamaev", "country": None, "elo": 1984, "title": "IM"},
    {"initials": "Junjun Huai", "country": "China", "elo": 2140, "title": "FM"},
    {"initials": "Klodian Vlachaki", "country": "Greece", "elo": 1248, "title": None},
    {"initials": "Tim Farfoot", "country": None, "elo": 754, "title": "Glorb"},
    {"initials": "Elrond Halfelven", "country": None, "elo": 1754, "title": "FM"},
    {"initials": "Luthien Tinuviel", "country": "New Zealand", "elo": 944, "title": None},
    {"initials": "Roboute Guilliman", "country": None, "elo": 2122, "title": "UM"},
    {"initials": "Rogal Dorn", "country": "Germany", "elo": 1488, "title": "BT"},
    {"initials": "Bobby Fischer", "country": "US", "elo": 2917, "title": "GM"},
    {"initials": "Garry Kasparov", "country": "Russia", "elo": 2851, "title": "GM"},
    {"initials": "David Yayloyan", "country": "Armenia", "elo": 1354, "title": "BOI"}
]

tournaments = [
    {"country": "US", "city": "New York", "start_date": "2020-01-01", "title": "New Year's Open", "min_elo": 1200, "max_elo": 1400},
    {"country": "Russia", "city": "Moscow", "start_date": "2017-06-12", "title": "Moscow Open", "min_elo": 1500, "max_elo": None},
    {"country": "Italy", "city": "Rome", "start_date": "2023-03-01", "title": "Roman Holiday", "min_elo": 1000, "max_elo": 2000},
    {"country": "France", "city": "Paris", "start_date": "2012-04-05", "title": "Parisian Spring", "min_elo": 800, "max_elo": None},
    {"counrty": "China", "city": "Beijing", "start_date": "2005-05-25", "title": "Great Wall Open", "min_elo": 2000, "max_elo": 2300},
    {"country": "US", "city": "Los Angeles", "start_date": "2019-06-15", "title": "City of Angels", "min_elo": 1100, "max_elo": 1600},
    {"country": "Russia", "city": "St. Petersburg", "start_date": "2022-07-01", "title": "White Nights", "min_elo": 0, "max_elo": None},
    {"country": "Italy", "city": "Venice", "start_date": "2018-08-02", "title": "Carnivale", "min_elo": 700, "max_elo": 1500},
    {"country": "France", "city": "Nice", "start_date": "2024-09-01", "title": "Riviera Open", "min_elo": 2400, "max_elo": 2800},
    {"country": "China", "city": "Shanghai", "start_date": "2016-10-01", "title": "Pearl of the Orient", "min_elo": 2100, "max_elo": 2500},
    {"country": "US", "city": "San Francisco", "start_date": "2011-11-18", "title": "Golden Gate", "min_elo": 1600, "max_elo": 2000},
    {"country": "Russia", "city": "Vladivostok", "start_date": "2020-12-09", "title": "Far East Open", "min_elo": 400, "max_elo": 1000},
    {"country": "Finland", "city": "Helsinki", "start_date": "2023-09-15", "title": "Fashion Week", "min_elo": 2500, "max_elo": None},
    {"country": "Germany", "city": "Berlin", "start_date": "2022-08-01", "title": "Oktoberfest", "min_elo": 2600, "max_elo": None}
]

partitipations = [
    {"chess_player_id": 8, "tournament_id": 12, "partition_number": 6, "place": 18},
    {"chess_player_id": 7, "tournament_id": 12, "partition_number": 2, "place": 3},
    {"chess_player_id": 6, "tournament_id": 12, "partition_number": 1, "place": 5},
    {"chess_player_id": 4, "tournament_id": 12, "partition_number": 19, "place": 7},
    {"chess_player_id": 5, "tournament_id": 12, "partition_number": 14, "place": 2},
    {"chess_player_id": 3, "tournament_id": 12, "partition_number": 25, "place": 1},
    {"chess_player_id": 3, "tournament_id": 13, "partition_number": 11, "place": 2},
    {"chess_player_id": 5, "tournament_id": 13, "partition_number": 6, "place": 5},
    {"chess_player_id": 7, "tournament_id": 13, "partition_number": 7, "place": 4},
    {"chess_player_id": 6, "tournament_id": 5, "partition_number": 15, "place": 3},
    {"chess_player_id": 7, "tournament_id": 5, "partition_number": 29, "place": 1},
    {"chess_player_id": 11, "tournament_id": 3, "partition_number": 54, "place": 48},
    {"chess_player_id": 2, "tournament_id": 3, "partition_number": 102, "place": 100},
    {"chess_player_id": 18, "tournament_id": 3, "partition_number": 88, "place": 94},
    {"chess_player_id": 26, "tournament_id": 3, "partition_number": 12, "place": 2},
    {"chess_player_id": 23, "tournament_id": 3, "partition_number": 67, "place": 25},
    {"chess_player_id": 10, "tournament_id": 9, "partition_number": 48, "place": 167},
    {"chess_player_id": 20, "tournament_id": 9, "partition_number": 27, "place": 119},
    {"chess_player_id": 13, "tournament_id": 9, "partition_number": 105, "place": 4},
    {"chess_player_id": 12, "tournament_id": 9, "partition_number": 184, "place": 67},
    {"chess_player_id": 9, "tournament_id": 9, "partition_number": 79, "place": 4},
    {"chess_player_id": 16, "tournament_id": 9, "partition_number": 98, "place": 49},
    {"chess_player_id": 22, "tournament_id": 9, "partition_number": 62, "place": 3},
    {"chess_player_id": 17, "tournament_id": 9, "partition_number": 154, "place": 1},
    {"chess_player_id": 19, "tournament_id": 8, "partition_number": 57, "place": 68},
    {"chess_player_id": 15, "tournament_id": 8, "partition_number": 47, "place": 10},
    {"chess_player_id": 21, "tournament_id": 8, "partition_number": 28, "place": 54},
    {"chess_player_id": 14, "tournament_id": 8, "partition_number": 69, "place": 3},
    {"chess_player_id": 1, "tournament_id": 8, "partition_number": 25, "place": 1},
    {"chess_player_id": 21, "tournament_id": 4, "partition_number": 215, "place": 300},
    {"chess_player_id": 14, "tournament_id": 4, "partition_number": 295, "place": 56},
    {"chess_player_id": 1, "tournament_id": 4, "partition_number": 150, "place": 228},
    {"chess_player_id": 11, "tournament_id": 4, "partition_number": 305, "place": 6},
    {"chess_player_id": 2, "tournament_id": 4, "partition_number": 67, "place": 9},
    {"chess_player_id": 18, "tournament_id": 4, "partition_number": 87, "place": 89},
    {"chess_player_id": 26, "tournament_id": 4, "partition_number": 69, "place": 2},
    {"chess_player_id": 23, "tournament_id": 4, "partition_number": 124, "place": 3},
    {"chess_player_id": 19, "tournament_id": 4, "partition_number": 97, "place": 1},
    {"chess_player_id": 15, "tournament_id": 4, "partition_number": 328, "place": 12},
    {"chess_player_id": 22, "tournament_id": 6, "partition_number": 18, "place": 1},
    {"chess_player_id": 17, "tournament_id": 6, "partition_number": 22, "place": 3},
    {"chess_player_id": 1, "tournament_id": 2, "partition_number": 8, "place": 3},
    {"chess_player_id": 2, "tournament_id": 2, "partition_number": 16, "place": 2},
    {"chess_player_id": 11, "tournament_id": 2, "partition_number": 36, "place": 4},
    {"chess_player_id": 18, "tournament_id": 2, "partition_number": 12, "place": 6},
    {"chess_player_id": 26, "tournament_id": 2, "partition_number": 6, "place": 1},
    {"chess_player_id": 23, "tournament_id": 2, "partition_number": 28, "place": 2},
    {"chess_player_id": 10, "tournament_id": 2, "partition_number": 47, "place": 1}
]

pets = [
    {"Dog name": "Bim", "Cat name": None},
    {"Dog name": None, "Cat name": "Eifer tower"},
    {"Dog name": "Goldie", "Cat name": "Bronzie"},
    {"Dog name": "Archie", "Cat name": None},
    {"Dog name": "Archie", "Cat name": "Peach"},
    {"Dog name": "Rex", "Cat name": None},
    {"Dog name": "Honey", "Cat name": "Bun"},
    {"Dog name": "Bob", "Cat name": "Lavander"},
    {"Dog name": "Ralf", "Cat name": "Garry"},
    {"Dog name": None, "Cat name": None},
    {"Dog name": None, "Cat name": "Chelsea"},
    {"Dog name": "Willow", "Cat name": "Pillow"},
    {"Dog name": "Snow", "Cat name": "White"},
    {"Dog name": "Butterball", "Cat name": "Ritchie"},
    {"Dog name": "Brownie", "Cat name": None},
    {"Dog name": "Rex", "Cat name": "Luna"},
    {"Dog name": "Lord", "Cat name": "Lady"},
    {"Dog name": "Bing chilling", "Cat name": "Min min"},
    {"Dog name": None, "Cat name": "Meow meow"},
    {"Dog name": "Mastermind", "Cat name": None},
    {"Dog name": "Cupcake", "Cat name": "Muffin"},
    {"Dog name": None, "Cat name": None},
    {"Dog name": "Mot", "Cat name": "Tom"},
    {"Dog name": "Richard", "Cat name": "Nicole"},
    {"Dog name": "Graph", "Cat name": "Murzik"},
    {"Dog name": "Ritchie", "Cat name": None}
]

def add_chess_player(player):
    try:
        response = requests.post(players_url, json=player)
        response.raise_for_status()
        print("Added successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error adding player: {e}")

def add_tournament(tournament):
    try:
        response = requests.post(tournaments_url, json=tournament)
        response.raise_for_status()
        print("Added successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error adding tournament: {e}")

def add_partitipation(partitipation):
    try:
        response = requests.post(partitications_url, json=partitipation)
        response.raise_for_status()
        print("Added successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error adding partitipation: {e}")

def add_pet(pet, id):
    try:    
        response = requests.put(f"{players_url}{id}", json={"pet": pet})
        response.raise_for_status()
        print("Added successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error adding data: {e}")

# for player in chess_players:
#     add_chess_player(player)

# for tournament in tournaments:
#     add_tournament(tournament)

# for partitipation in partitipations:
#     add_partitipation(partitipation)

for i in range(1, len(pets) + 1):
    add_pet(pets[i - 1], i)