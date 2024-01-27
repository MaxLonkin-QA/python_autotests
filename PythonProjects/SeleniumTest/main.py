"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '9401d31568f76e2fc492f8ad7ff87864'
          }
body = {
"name": "generate",
"photo": "generate"
    }

#body = {
    #"pokemon_id": "28672",
    #"name": "Пура",
    #"photo": "https://dolnikov.ru/pokemons/albums/004.png"
#}

#body = {
    #"pokemon_id": "28637"
#}
response = requests.post(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5) 
print(response) 

#response = requests.put(url=f'{URL}/pokemons',json=body,headers=HEADER,timeout=5)
#print(response)

#response = requests.post(url=f'{URL}/trainers/add_pokeball',json=body,headers=HEADER,timeout=5)
#print(response)
