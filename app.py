

import streamlit as st
import pickle
import pandas as pd
import requests

# ------------------------------
# API Key
# ------------------------------
TMDB_API_KEY = "5f0e56a30148fea6299489a7c7034532"

# ------------------------------
# Fetch movie details from TMDB
# ------------------------------
def fetch_tmdb_data(movie_title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"

    try:
        search_response = requests.get(search_url, timeout=5)
        search_response.raise_for_status()
        search_data = search_response.json()

        if not search_data.get("results"):
            return {
                "poster": "https://via.placeholder.com/500?text=No+Image",
                "title": movie_title,
                "rating": "N/A",
                "overview": "No overview available.",
                "release_date": "N/A",
                "tmdb_link": None
            }

        movie = search_data["results"][0]
        movie_id = movie["id"]
        poster_path = movie.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500?text=No+Image"
        tmdb_link = f"https://www.themoviedb.org/movie/{movie_id}"

        return {
            "poster": poster_url,
            "title": movie.get("title", movie_title),
            "rating": movie.get("vote_average", "N/A"),
            "overview": movie.get("overview", "No overview available."),
            "release_date": movie.get("release_date", "N/A"),
            "tmdb_link": tmdb_link
        }

    except requests.exceptions.RequestException as e:
        print(f"TMDB error: {e}")
        return {
            "poster": "https://via.placeholder.com/500?text=No+Image",
            "title": movie_title,
            "rating": "N/A",
            "overview": "No overview available.",
            "release_date": "N/A",
            "tmdb_link": None
        }

# ------------------------------
# Recommend similar movies
# ------------------------------
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        return []

    distances = similarity_matrix[movie_index]
    recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    results = []
    for i in recommended:
        title = movies.iloc[i[0]].title
        movie_data = fetch_tmdb_data(title)
        results.append(movie_data)
    return results

# ------------------------------
# Load movie data
# ------------------------------
try:
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System (TMDB Version)")

selected_movie_name = st.selectbox(
    "Choose a movie to get recommendations 🎥",
    movies['title'].values
)

if st.button("Get Recommendations"):
    results = recommend(selected_movie_name)

    if results:
        cols = st.columns(5)
        for i in range(len(results)):
            with cols[i]:
                if results[i]['tmdb_link']:
                    st.markdown(f"[![Poster]({results[i]['poster']})]({results[i]['tmdb_link']})", unsafe_allow_html=True)
                else:
                    st.image(results[i]['poster'], use_column_width=True)
                
                st.markdown(f"**{results[i]['title']}**")
                st.caption(f"⭐ {results[i]['rating']} | 📅 {results[i]['release_date']}")
                st.write(results[i]['overview'][:180] + "...")
    else:
        st.warning("⚠️ No recommendations found.")
        