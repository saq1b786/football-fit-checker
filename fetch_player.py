import requests


url = "https://v3.football.api-sports.io/players"

headers = {
  'x-apisports-key': 'eeee8418303d65fa230206eacef65a5c'
}


def get_team_id(team_name):

  team_endpoint = "https://v3.football.api-sports.io/teams"

  params = {
    'search': team_name
  }
  response = requests.get(team_endpoint, headers=headers, params=params)
  data = response.json()
  return data['response'][0]['team']['id']

def get_leagues_for_team(team_id, season='2023'):
  league_endpoint = "https://v3.football.api-sports.io/leagues"

  params = {
    'team': team_id, 
    'season': season
  }

  response = requests.get(league_endpoint, headers=headers, params=params)
  data = response.json()
  return data['response']


def choose_league(leagues):
    print("Leagues found for this team this season:")

    for i, league_info in enumerate(leagues, 1):
        league = league_info['league']
        print(f"{i}: {league['name']}")




    choice = int(input("Choose a league by number: "))
    return leagues[choice - 1]['league']['id']


def get_player_stats(player_name, team_id, league_id, season='2023'):
    player_endpoint = "https://v3.football.api-sports.io/players"
    params = {
        'search': player_name,
        'team': team_id,
        'league': league_id,
        'season': season
    }
    response = requests.get(player_endpoint, headers=headers, params=params)
    return response.json()

def main():
    team_name = input("Choose a team: ")
    player_name = input("Choose a player: ")

    team_id = get_team_id(team_name)
    leagues = get_leagues_for_team(team_id)
    league_id = choose_league(leagues)

    player_data = get_player_stats(player_name, team_id, league_id)

    print(player_data)

if __name__ == "__main__":
    main()



""" def search_player():
  search_player_name = input('choose a player: ')
  return search_player_name

player_name = search_player()

def search_team():
  search_team_name = input('choose a team: ')

  team_endpoint = "https://v3.football.api-sports.io/teams"


  params = {
    'search': search_team_name

  }

  response = requests.get(team_endpoint, headers=headers, params=params)

  team_data = response.json()
  team_id = team_data['response'][0]['team']['id']


  league_endpoint = "https://v3.football.api-sports.io/leagues"

  league_params = {
    'team': team_id, 
    'season': '2023'
  }

  league_data = requests.get(league_endpoint, headers=headers, params=league_params)

  league_id = league_data.json()['response'][0]['league']['id']


  return team_id, league_id

team_id, league_id = search_team()

    
params = {
  'search': player_name,
  'season': '2023', 
  'team': team_id, 
  'league': league_id
  
  
}

response = requests.get(url,headers=headers, params=params)

data = response.json()

print(data) """