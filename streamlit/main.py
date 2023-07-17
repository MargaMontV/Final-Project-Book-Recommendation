import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
        page_title="Book Recommending APP",
)

# Cargar el CSS personalizado
def load_css():
    with open('../css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Llamar a la función para cargar el CSS y el toml
load_css()

books_df = pd.read_csv('../data/books_clean.csv')

# Load your custom design image
title_image = "../book_logo_title.jpg"

# Display the image as the app title
st.image(title_image)
st.title("Book Recommending APP")

st.markdown("""
 * Use the left menu to select your books preferences
 * Your recommendations will appear below, You can click on the cover to see the whole book info
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
    df_ratings_count = df_pages[df_pages["Ratings count"] <= 50000]
else:
    df_ratings_count = df_pages[df_pages["Ratings count"] >= 50001]                                    

#Filter 4
published = st.sidebar.selectbox('Do you prefer to read a recent book or a classic?',
                                     ('Recent', 'Classic'))
if published == "Classic":
    df_published = df_ratings_count[df_ratings_count['First published'] <= 2017]
else:
    df_published = df_ratings_count[df_ratings_count['First published'] >= 2018]

df_sample = df_published.sample(n=3).reset_index()

col1, col2, col3 = st.columns(3)

def show_images(df):
    for index, row in df.iterrows():
        st.markdown("[![Imagen](" + row["Cover image"] + ")]("+row["Book url"]+")")
        st.markdown(row["Title"] + " " + "by" + " " + row["Author"])

with col1:
    show_images(pd.DataFrame(df_sample.iloc[[0]]))
with col2:
    show_images(pd.DataFrame(df_sample.iloc[[1]]))
with col3:
    show_images(pd.DataFrame(df_sample.iloc[[2]]))

st.button("Shuffle")

