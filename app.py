import streamlit as st
import pickle
import pandas as pd
import requests
from imdb import IMDb


def get_WatchProviders(movie_id):
    response=requests.get("https://api.themoviedb.org/3/watch/providers/movie/"+movie_id+"?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data =response.json()
    for i in data:
        print(data[i])
    # providers=data["provider_name"]
    #return providers

def get_overview(movie_id):
    movie_id = movie_id
    response = requests.get("https://api.themoviedb.org/3/movie/"+movie_id+"?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    overviews=data['overview']
    return overviews


def fetch_posters(movie_id):
    movie_id = movie_id
    response = requests.get("https://api.themoviedb.org/3/movie/"+movie_id+"?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    full_path=""
    if data['poster_path']!=None:
        full_path = "https://image.tmdb.org/t/p/w500" + data['poster_path']
    return full_path
    
def get_cast(movies_id):
    movie_id = movies_id
    response = requests.get("https://api.themoviedb.org/3/movie/"+movie_id+"/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    casts=[]
    for i in data['cast']:
        casts.append(i['name'])

    ''.join(casts)
    return casts


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters=[]
    actors=[]
    overviews=[]
    for i in movie_list:
        movies_id = str(movies.iloc[i[0]].id)
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_posters(movies_id))
        actors.append(get_cast(movies_id))
        overviews.append(get_overview(movies_id))
    

    

    return recommended_movies, recommended_movies_posters,actors,overviews

st.header('Movies Recommender System')
movies_dict = pickle.load(open('new_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('new_similarity.pkl', 'rb'))




movie_listi = movies['title'].values
movie_listi = sorted(movie_listi)

selected_movie = st.selectbox(
    "select a movie from the dropdown", movie_listi)




if st.button('Recommend Me'):
    names, posters,actors,overviews= recommend(selected_movie)
    #ins=0
    # for i in names:
    #     ins = int(ins) + 1
    #     ins = str(ins)
    #     st.subheader(ins+" ->  "+i)
    
    
    with open('style.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    col1, col2, col3 = st.columns(3)
    with col1:
        
        
        if posters[0]!=None:
            st.image(posters[0])
        st.caption(names[0])
        st.subheader('Overview')
        st.write(overviews[0])
        st.subheader('Casts')
        f=0
        for i in actors[0]:
            if(f>=5):
                break
            f+=1
            st.text(i)

        
    with col2:
        
        if posters[1]!=None:
            st.image(posters[1])
        st.caption(names[1])
        st.subheader('Overview')
        st.write(overviews[1])
        st.subheader('Casts')
        f=0
        for i in actors[1]:
            if(f>=5):
                break
            f+=1
            st.text(i)
       
        
    with col3:
        if posters[2]!=None:
            st.image(posters[2])
        st.caption(names[2])
        st.subheader('Overview')
        st.write(overviews[2])
        st.subheader('Casts')
        f=0
        for i in actors[2]:
            if(f>=5):
                break
            f+=1
            st.text(i)
        
    col4,col5=st.columns(2) 
    with col4:
        if posters[3]!=None:
            st.image(posters[3])
        st.caption(names[3])
        st.subheader('Overview')
        st.write(overviews[3])
        st.subheader('Casts')
        f=0
        for i in actors[3]:
            if(f>=5):
                break
            f+=1
            st.text(i)
        
    with col5:
        if posters[4]!=None:
            st.image(posters[4])
        st.caption(names[4])
        st.subheader('Overview')
        st.write(overviews[4])
        st.subheader('Casts')
        f=0
        for i in actors[4]:
            if(f>=5):
                break
            f+=1
            st.text(i)

