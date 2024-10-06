# Spotify_Mood_Playlist_Generator
This Python script creates Spotify playlists based on your current mood. It automatically selects genres that match your mood and populates a new playlist with relevant songs.
# Features
- Creates playlists based on 10 different moods
- Automatically selects appropriate genres for each mood
- Uses Spotify Web API to search for tracks and create playlists
- Supports public playlist creation

# Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- A Spotify account
- Spotify Developer credentials (Client ID and Client Secret)
# Installation
1. Clone this repository:
   ```
   git clone https://github.com/Cosmic2003/Spotify_mood_playlist.git
   cd Spotify_mood_playlist
   ```
2. Install required dependencies:
   ```
   pip install spotipy
   pip install spotipy python-dotenv
   ```
3. Create a ```.env``` file in the project root directory and add your Spotify API credentials:
   ```
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   ```
# How to Get Spotify API Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in the app details:
   - App name: Your choice (e.g., "Mood Playlist Generator")
   - App description: Brief description of your app
   - Redirect URI: Set to ```http://localhost:8888/callback/```
5. Once created, go to settings, you'll see your Client ID and you can click to reveal your Client Secret
6. Copy these credentials to your ```.env``` file
# Usage
1. Run the script:
   ```
   python playlist.py
   ```
2. Enter your current mood when prompted. Current available moods are:
   - happy
   - sad
   - motivated
   - relaxed
   - angry
   - excited
   - nostalgic
   - romantic
   - energetic
   - focused
   Change the available moods in the script according to your own needs
3. The script will create a new playlist on your Spotify account with songs matching your mood!
# How It Works
1. The script uses the ```spotipy``` library to interact with the Spotify Web API
2. When you input a mood, it maps that mood to a set of genres using the ```get_mood_tracks``` function
3. It then searches for tracks within those genres
4. A new playlist is created with your mood as the title
5. The selected tracks are added to the playlist
# Mood to Genre Mapping
| **Mood**        | **Genres**                        |
|-----------------|-----------------------------------|
| **Happy**       | Pop, Dance, Indie                 |
| **Sad**         | Acoustic, Ballad, Singer-Songwriter|
| **Motivated**   | Hip-Hop, Rock, EDM                |
| **Relaxed**     | Jazz, Lofi, Chill                 |
| **Angry**       | Metal, Hard Rock, Punk            |
| **Excited**     | Electronic, Pop, Alternative      |
| **Nostalgic**   | Classic Rock, Oldies, 90s         |
| **Romantic**    | R&B, Soul, Love Songs             |
| **Energetic**   | Upbeat Pop, Workout, EDM          |
| **Focused**     | Classical, Ambient, Minimalism    |
# Acknowledgements
- [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/) - Python client for the Spotify Web API
- [python-dotenv](https://pypi.org/project/python-dotenv/) - For managing environment variables
