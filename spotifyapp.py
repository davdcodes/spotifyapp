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

# Initialize SpotifyOAuth
sp_oauth = SpotifyOAuth(client_id=CLIENTID,
                         client_secret=CLIENTSECRET,
                         redirect_uri=REDIRECT,
                         scope=SCOPE,
                         show_dialog=True)

# Initialize session state to track login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Step 1: Check if the user is already logged in
if st.session_state['logged_in']:
    # If logged in, display user information
    token_info = sp_oauth.get_cached_token()
    
    if token_info:
        sp = spotipy.Spotify(auth_manager=sp_oauth)
        user = sp.current_user()
        st.success(f"Logged in as {user['display_name']} ({user['email']})")
        st.image(user['images'][0]['url'] if user['images'] else None, width=100)
    else:
        # If no token info, clear login state and prompt for login
        st.session_state['logged_in'] = False
        st.session_state['token_info'] = None
        st.markdown("### Session expired. Please log in again.")
        st.experimental_rerun()
else:
    # If not logged in, show login prompt
    auth_url = sp_oauth.get_authorize_url()
    st.markdown(f"""
        ### 👋 Welcome!  
        Please [log in to Spotify]({auth_url}) to continue.
    """)

    # After the user logs in, capture the token
    token_info = sp_oauth.get_access_token(st.experimental_get_query_params().get('code', [None])[0])

    if token_info:
        st.session_state['logged_in'] = True
        st.session_state['token_info'] = token_info
        st.experimental_rerun()  # Refresh the page to proceed with the user's session