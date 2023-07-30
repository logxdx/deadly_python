import requests
from bs4 import BeautifulSoup
import time

# Fetch the HTML content of the Spotify web player page
url = 'https://open.spotify.com/?utm_source=pwa_install'  # Replace with the actual URL of the Spotify web player

previous_song = None

while True:
    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    for data in soup.findAll('div', class_='deomraqfhIAoSB3SgXpu'):
        print(data)

    # Find the element that contains the now playing data
    now_playing_element = soup.find('div', class_='deomraqfhIAoSB3SgXpu')  # Replace with the appropriate element for Spotify's web player

    # Extract the relevant data
    song_title = now_playing_element.find('a', draggable="false").text
    artist_name = now_playing_element.find('span', class_='artist-name').text

    # Check if the song has changed
    if (song_title, artist_name) != previous_song:
        print('Now Playing:')
        print('Song:', song_title)
        print('Artist:', artist_name)
        print('---')
        previous_song = (song_title, artist_name)

    # Wait for a specific interval before checking for updates again
    time.sleep(10)  # Wait for 10 seconds before the next check
