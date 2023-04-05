import requests

pokemon = input('Digite o nome de um Pokémon: ')

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()

print('Pokémon:',response['name'])
print('Altura:',response['height'],'m')
print('Peso:',response['weight'],'kg')