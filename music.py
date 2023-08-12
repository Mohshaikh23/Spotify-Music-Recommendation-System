from extraction import get_trending_playlist_data
from API import access_token
import pandas as pd

playlist_id = '37i9dQZF1DX76Wlfdnj7AP'

# Call the function to get the music data from the playlist and store it in a DataFrame
music_df = get_trending_playlist_data(playlist_id, access_token)

# # Display the DataFrame
music_df.to_csv("music.csv", index=False)

