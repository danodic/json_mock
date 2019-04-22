import requests

# Do the request and get the response
response = requests.get('https://my-json-server.typicode.com/danodic/json_mock/request_track_list')

# Assert the response code
assert(response.status_code == 200)

# Convert response to a dictionary
data = response.json()

# Do the asserts
assert(data['artist'] == 'The Beatles')
assert(len(data['tracklist']) == 3)

# Assert one of the tracks
assert(data['tracklist'][0]['name'] == 'Yellow Submarine')
assert(data['tracklist'][0]['length'] == '2:39')
