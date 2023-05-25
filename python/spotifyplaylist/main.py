import requests
from bs4 import BeautifulSoup
import re
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials


sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="",
        client_secret="",
        cache_path="spotifyplaylist/.cache"
    )
)
user_id = sp.current_user()["id"]

def get_user_input():
    try:
        date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        if not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date):
            raise ValueError
    except ValueError:
        print("Please enter a date in the format YYYY_MM_DD")
        get_user_input()
    else:
        return date

user_response = get_user_input()

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_response}")
site_html = response.text
soup = BeautifulSoup(site_html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
song_uris = []
year = user_response.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_response} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)








