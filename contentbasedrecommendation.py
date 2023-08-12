import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

music_df = pd.read_csv("music.csv")

# Normalize the music features using Min-Max scaling
scaler = MinMaxScaler()
music_features = music_df[['Danceability',
                           'Energy', 
                           'Key', 
                           'Loudness',
                           'Mode',
                           'Speechiness',
                           'Acousticness',
                           'Instrumentalness',
                           'Liveness', 
                           'Valence',
                           'Tempo']].values
music_features_scaled = scaler.fit_transform(music_features)

def content_based_recommendations(input_song_name, num_recommendations=5):
    if input_song_name not in music_df['Track Name'].values:
        print(f"'{input_song_name}' not found in the dataset. Please enter a valid song name.")
        return

    # Get the index of the input song in the music DataFrame
    input_song_index = music_df[music_df['Track Name'] == input_song_name].index[0]

    # Calculate the similarity scores based on music features (cosine similarity)
    similarity_scores = cosine_similarity([music_features_scaled[input_song_index]],
                                          music_features_scaled)

    # Get the indices of the most similar songs
    similar_song_indices = similarity_scores.argsort()[0][::-1][1:num_recommendations + 1]

    # Get the names of the most similar songs based on content-based filtering
    content_based_recommendations = music_df.iloc[similar_song_indices][['Track Name',
                                                                         'Artists',
                                                                         'Album Name',
                                                                         'Release Date',
                                                                         'Popularity']]

    return content_based_recommendations

st.header("Content-Type")
text = st.selectbox('Select movie you want recommendation for', 
                    music_df['Track Name'].values)

if st.button("Recommend"):
    df = content_based_recommendations(text)
    st.dataframe(df)