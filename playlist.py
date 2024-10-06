from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# environment variables- spotify id and secret
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

#Redirect url change accordingl;y
REDIRECT_URI = "http://localhost:8888/callback/"
# auth
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope))

# mood and genre
def get_mood_tracks(mood):
    mood_genre_map = {
        'happy': ['Pop', 'Dance', 'Indie'],
        'sad': ['Acoustic', 'Ballad', 'Singer-Songwriter'],
        'motivated': ['Hip-Hop', 'Rock', 'EDM'],
        'relaxed': ['Jazz', 'Lofi', 'Chill'],
        'angry': ['Metal', 'Hard Rock', 'Punk'],
        'excited': ['Electronic', 'Pop', 'Alternative'],
        'nostalgic': ['Classic Rock', 'Oldies', '90s'],
        'romantic': ['R&B', 'Soul', 'Love Songs'],
        'energetic': ['Upbeat Pop', 'Workout', 'EDM'],
        'focused': ['Classical', 'Ambient', 'Minimalism'],
    }
    return mood_genre_map.get(mood.lower(), ['Top 50', 'Mixed Genres'])

def create_playlist(mood):
    user_id = sp.current_user()['id']
    playlist_name = f"{mood.capitalize()} Vibes"
    
    # Create playlist
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_id = playlist['id']

    # Get genres based on mood
    genres = get_mood_tracks(mood)
    
    # R&D on songs according to genre
    track_uris = []
    for genre in genres:
        results = sp.search(q=f'genre:{genre}', type='track', limit=10)
        tracks = results['tracks']['items']
        track_uris += [track['uri'] for track in tracks]

    # Add songs to the created playlist
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"Playlist '{playlist_name}' created successfully with tracks from genres: {', '.join(genres)}!")

if __name__ == '__main__':
    mood = input("Enter your mood (happy, sad, motivated, relaxed, angry, excited, nostalgic, romantic, energetic, focused): ").lower()
    create_playlist(mood)
