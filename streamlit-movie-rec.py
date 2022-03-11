import ast

import pandas as pd
import streamlit as st

st.set_page_config(page_title='BigDL Movie Recommendation System',
                   layout='wide')

st.image("https://bigdl-project.github.io/img/bigdl_logo.png", width=400)
df = pd.read_csv("resources/cache.csv")

st.write("""
# BigDL Movie Recommendation System
In this implementation, we have used **bigDL** framework for training a movie recommendation system.
""")

st.subheader('BigDL')
st.write("""
BigDL is a distributed deep learning library for Apache Spark; with BigDL, users can write their deep learning applications as standard Spark programs, which can directly run on top of existing Spark or Hadoop clusters.
""")

if st.button('Press to generate insights from data'):
    st.markdown('**1.1. Glimpse of the cached Recommendations**')
    st.table(df.head(2))

    st.markdown('**1.2. Layers of Neural Network**')
    st.image("resources/layers.png", width=1200)

    st.markdown('**1.3. Number of unique users**')
    st.info(len(df))

    st.markdown('**1.4. Number of unique Movies**')
    movie_list = []


    def f(x):
        list_obj = ast.literal_eval(x['name'])
        movie_list.extend(list_obj)


    df.apply(lambda x: f(x), axis=1)
    st.info(len(movie_list))

    st.markdown('**1.5. Sample Movie Names**')
    st.info((movie_list)[0:10])

    st.markdown('**1.6. Number of unique Genres**')
    set_genre = set()


    def f(x):
        list_obj = ast.literal_eval(x['Genre'])
        set_genre.update(list_obj)


    df.apply(lambda x: f(x), axis=1)
    st.info(len(set_genre))
    st.markdown('**1.7. Sample Genre Names**')
    st.info((list(set_genre))[0:10])

with st.sidebar.header('1. Select UserID'):
    userID = st.sidebar.slider('UserID', min_value=1, max_value=6040, step=1)

with st.sidebar.header('2. Select Multiple Genre'):
    genres = st.sidebar.multiselect(
        'What are your favorite genres',
        ['Musical', 'Romance', 'Drama', 'Animation', 'Comedy', 'Fantasy', 'Children', 'Action', 'Sci-Fi', 'Horror',
         'Adventure', 'Thriller'])

with st.sidebar.header('3. Number of movie recommendations'):
    num_rec = st.sidebar.slider('Number of Recommendations', min_value=1, max_value=20, step=1)

if st.sidebar.button('Press to generate recommendations'):
    st.info("Generating recommendations for userID : " + str(userID))
    filtered_df = df[df['user'] == userID]


    def f(x):
        return ast.literal_eval(x['name'])


    filtered_df['name'] = filtered_df.apply(lambda x: f(x), axis=1)


    def f(x):
        return ast.literal_eval(x['Genre'])


    filtered_df['Genre'] = filtered_df.apply(lambda x: f(x), axis=1)

    res_list = []


    def f(x):
        for i, n in enumerate(x['Genre']):
            for g in genres:
                if g in n:
                    res_list.append(x['name'][i])


    if genres != None and len(genres) > 0:
        filtered_df.apply(lambda x: f(x), axis=1)
        st.table(res_list[0:num_rec])
    else:
        st.table(filtered_df.name.tolist()[0][0:num_rec])
