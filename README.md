# Spotify Music Recommendation System

This project implements a hybrid music recommendation system using Streamlit, a popular Python library for creating interactive web applications. The recommendation system combines content-based recommendations with popularity-based scoring to provide personalized suggestions for music tracks.

![App View](https://github.com/Mohshaikh23/Spotify-Music-Recommendation-System/blob/7cd93ca94cbb1db778f1549c8517cdd31e9f496f/songs%20recommend.png)

## Table of Contents

- [Spotify Music Recommendation System](#spotify-music-recommendation-system)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)

## Overview

The Spotify Music Recommendation System utilizes a hybrid approach to provide song recommendations based on user preferences. The system combines content-based recommendations, which leverage the features of songs, with a popularity-based scoring mechanism to ensure diversity and relevance in suggestions.

## Requirements

- Python (>=3.6)
- pandas
- numpy
- datetime
- streamlit
- [contentbasedrecommendation](https://link-to-content-based-recommendation-repo.com) (Replace with the actual link to your content-based recommendation module)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Mohshaikh23/Spotify-Music-Recommendation-System.git
   
cd Spotify-Music-Recommendation-System
```

2. Install the required packages:

```bash
  pip install -r requirements.txt
```

3. Download music.csv file containing your music data.

4. Usage

Run the Streamlit app:
```bash
  streamlit run app.py
```

4. Access the application in your web browser at http://localhost:8501.

Select a song from the dropdown menu and click the "Recommend" button to get hybrid music recommendations.

References
```bash
Streamlit: https://www.streamlit.io/ 
```

Replace the placeholders with your actual repository name, links, and other relevant information. This `README.md` template gives users an overview of your project, installation instructions, and usage guidelines. You can also include any additional sections that provide more context about your project, how to contribute, or any other information you think would be helpful.
