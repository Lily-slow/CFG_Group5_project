import base64
import requests

CLIENT_ID = '6ba3cb129f79430c8bd49d63c559bc6d'
CLIENT_SECRET = 'df7b48e8c38c4a359935acbfd85ca1ae'

# Concatenate the client ID and secret into a single string
client_creds = f'{CLIENT_ID}:{CLIENT_SECRET}'

# Encode the client credentials using base64
client_creds_b64 = base64.b64encode(client_creds.encode())

# Define the headers for the token endpoint request
token_url = 'https://accounts.spotify.com/api/token'
headers = {'Authorization': f'Basic {client_creds_b64.decode()}'}

# Define the data to be sent with the token endpoint request
data = {'grant_type': 'client_credentials'}

# Send the token endpoint request
response = requests.post(token_url, headers=headers, data=data)

# Get the access token from the response
access_token = response.json()['access_token']

song_name = 'Stairway to Heaven'
artist_name = 'Led Zeppelin'

# Define the search endpoint URL
search_url = 'https://api.spotify.com/v1/search'

# Define the headers for the API request, including the access token
headers = {'Authorization': f'Bearer {access_token}'}

# Define the parameters for the search endpoint request
params = {'q': f'{song_name} artist:{artist_name}', 'type': 'track'}

# Send the API request
response = requests.get(search_url, headers=headers, params=params)

# Extract the track ID from the response
track_id = response.json()['tracks']['items'][0]['id']

# Define the track endpoint URL
track_url = f'https://api.spotify.com/v1/tracks/{track_id}'

# Send the API request
response = requests.get(track_url, headers=headers)

# Extract the track information from the response
track_info = response.json()
print(track_info['name'])
print(track_info['artists'][0]['name'])
print(track_info['album']['name'])
print(track_info['popularity'])