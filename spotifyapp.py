import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os 
import requests

CLIENTID = "7af210f3080f499a8e29c6df06865eb0"
CLIENTSECRET = "305aed74adb64331bb29d595b7915d6c"
REDIRECT = "https://crunchlist.streamlit.app/"
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"

cache = spotipy.cache_handler.MemoryCacheHandler()

sp_oauth = SpotifyOAuth(client_id = CLIENTID,
                        client_secret = CLIENTSECRET,
                        redirect_uri = REDIRECT,
                        scope = SCOPE,
                        cache_handler = cache,
                        show_dialog = True
)
    
# Step 2: Try to get token
token_info = sp_oauth.get_cached_token()

if token_info:
    # Step 3: Logged in
    sp = spotipy.Spotify(auth_manager = sp_oauth)
    user = sp.current_user()
    st.success(f" Logged in as {user['display_name']} ({user['email']})")
    st.image(user['images'][0]['url'] if user['images'] else None, width=100)
else:
    # Step 4: Not logged in
    auth_url = sp_oauth.get_authorize_url()
    st.markdown(f"""
        ###  Welcome!  
        Please [log in to Spotify]({auth_url}) to continue.
    """)