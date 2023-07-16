import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# Cargar el CSS personalizado
def load_css():
    with open('../css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Llamar a la función para cargar el CSS
load_css()

books_df = pd.read_csv('../data/books_clean.csv')

st.title('Book Recommending APP')

st.markdown("""
 * Use the left menu to select your books preferences
 * Your recommendations will appear below
 * Your can click on the cover to see thenwhole book info
""")

#Filter 1
genre = st.sidebar.selectbox(
    'Which genre would you like to read?',
    ('Adult Fiction', 'Biography', 'Business', 'Chick-Lit', 'Childrens', 
              'Comics', 'Contemporary', 'Crime', 'Fantasy', 'Fiction', 
              'Graphic Novels', 'Historical Fiction', 'History', 'Horror', 'Humor', 
              'LGBT', 'Literary Fiction', 'Memoir', 'Mystery', 'New Adult', 
              'Nonfiction', 'Paranormal', 'Poetry', 'Romance', 'Science', 
              'Science Fiction', 'Self-Help', 'Suspense', 'Thriller', 'Travel', 'Young Adult'))
df_genre = books_df[books_df['Genre'] == genre]

#Filter 2
pages = st.sidebar.selectbox('Would you like to read a short book or a long book?',
                             ('Short', 'Long'))
if pages == "Short":
    df_pages = df_genre[df_genre['Pages'] <= 299]
else:
    df_pages = df_genre[df_genre['Pages'] >= 300]

#Filter 3
ratings_count = st.sidebar.selectbox('Would you like to read a popular book or a hidden gem?',
                                     ('Popular', 'Hidden gem'))
if ratings_count == "Hidden gem":
    df_ratings_count = df_pages[df_pages["Ratings count"] <= 9999]
else:
    df_ratings_count = df_pages[df_pages["Ratings count"] >= 10000]                                    

#Filter 4
published = st.sidebar.selectbox('finally, do you prefer to read a recent book or a classic?',
                                     ('Recent', 'Classic'))
if published == "Classic":
    df_published = df_ratings_count[df_ratings_count['First published'] <= 2017]
else:
    df_published = df_ratings_count[df_ratings_count['First published'] >= 2018]

df_sample = df_published[['Title', 'Author', "Book url", "Cover image"]].sample(n=6)


def show_images(df):
    for index, row in df.iterrows():
        st.markdown(row["Title"] + " " + "by" + " " + row["Author"])
        st.markdown("[![Imagen](" + row["Cover image"] + ")]("+row["Book url"]+")")

show_images(df_sample)


