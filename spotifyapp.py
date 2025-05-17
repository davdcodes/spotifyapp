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
if "token_info" not in st.session_state:
    token_info = auth_manager.get_cached_token()
    if not token_info:
        auth_url = auth_manager.get_authorize_url()
        st.write("Please log in to Spotify: ")
        st.markdown(f"[Login to Spotify]({auth_url})")
    else:
        st.session_state.token_info = token_info


if "token_info" in st.session_state:
    sp = spotipy.Spotify(auth_manager = auth_manager)
    user = sp.current_user()
    st.success(f"Loggin in as {user['display_name']}")