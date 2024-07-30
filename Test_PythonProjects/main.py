import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '383ad1f93fccf964dbc3e27e80f61ca4'
HEADER = {'Content-Type':'application/json', 'trainer_token': '383ad1f93fccf964dbc3e27e80f61ca4'}


body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "45764",
    "name": "Ponchik",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "45764"
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)
print(response_change.status_code)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
print(response_catch.status_code)

