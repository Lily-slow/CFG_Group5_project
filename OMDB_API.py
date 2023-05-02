import requests
import json

api_key = '69590d9a'
title = 'John Wick'

url = f'http://www.omdbapi.com/?apikey={api_key}&t={title}&type=movie&r=json'

response = requests.get(url)

movie_data = json.loads(response.text)

imdb_rating = movie_data['imdbRating']
rotten_tomatoes_rating = movie_data['Ratings'][1]['Value']
metacritic_rating = movie_data['Ratings'][2]['Value']

print(f"IMDb rating: {imdb_rating}")
print(f"Rotten Tomatoes rating: {rotten_tomatoes_rating}")
print(f"Metacritic rating: {metacritic_rating}")
