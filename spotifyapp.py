import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os 
import requests

CLIENTID = "7af210f3080f499a8e29c6df06865eb0"
CLIENTSECRET = "305aed74adb64331bb29d595b7915d6c"
REDIRECT = "https://crunchlist.streamlit.app/"
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"


sp_oauth = SpotifyOAuth(client_id = CLIENTID,
                        client_secret = CLIENTSECRET,
                        redirect_uri = REDIRECT,
                        scope = SCOPE)

st.title("Spotify Login")

if st.button("Login with spotify"):
    auth_url = sp_oauth.get_authorize_url()