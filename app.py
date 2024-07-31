
import streamlit as st
import pickle
import pandas as pd
import requests



movie_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_df.head()

def get_poster(movie_id):
  API_KEY = '86a33d8e11186e5252c98b258758ba67'
  response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}')
  data = response.json()
  return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def fetch_recommendations(movie):
    try:
        index = movie_df[movie_df['original_title'] == movie].index[0]
        distances = similarity[index]
        top_movies_indices = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]

        recommended_titles = []
        recommended_posters = []
        for idx, _ in top_movies_indices:
            movie_id = movie_df.iloc[idx]['id']
            recommended_titles.append(movie_df.iloc[idx]['original_title'])
            recommended_posters.append(get_poster(movie_id))

        return recommended_titles, recommended_posters
    except IndexError:
        # Handle case where the movie is not found
        return [], []

st.title('Movie Recommendation System')

# Movie selection
selected_movie = st.selectbox('Choose a movie:', options=movie_df['original_title'].values)

if st.button('Show Recommendations'):
    recommendations, posters = fetch_recommendations(selected_movie)

    # Display recommendations in columns
    cols = st.columns(5)
    for i, (title, poster) in enumerate(zip(recommendations, posters)):
        with cols[i]:
            st.image(poster, caption=title)