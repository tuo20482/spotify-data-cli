import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

ice_spice_uri = 'spotify:artist:3LZZPxNDGDFVSIPqf4JuEf'

results = spotify.artist_top_tracks(artist_id=ice_spice_uri, country="US")
for track in results['tracks']:
    print(track['name'])
