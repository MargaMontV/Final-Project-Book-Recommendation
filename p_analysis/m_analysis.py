import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Cargar el CSS personalizado
def load_css():
    with open('./css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Read the csv with the scraped and cleaned books
def read_csv(path):
    return pd.read_csv(path)

#Book Filter 1 by genre
def filter_genre(df_1):
    genre = st.sidebar.selectbox(
    'Which genre would you like to read?',
    ("Adult Fiction", "Biography", "Business", "Chick-Lit", "Childrens", 
              "Comics", "Contemporary", "Crime", "Fantasy", "Fiction", 
              "Graphic Novels", "Historical Fiction", "History", "Horror", "Humor", 
              "LGBT", "Literary Fiction", "Memoir", "Mystery", "New Adult", 
              "Nonfiction", "Paranormal", "Poetry", "Romance", "Science", 
              "Science Fiction", "Self-Help", "Suspense", "Thriller", "Travel", "Young Adult"))
    
    return df_1[df_1["Genre"] == genre]

#Book Filter 2 by pages
def filter_pages(df_2):
    pages = st.sidebar.selectbox("Would you like to read a short book or a long book?",
                             ("Short", "Long"))
    try:
        if pages == "Short":
            return df_2[df_2["Pages"] <= 350]
        else:
            return df_2[df_2["Pages"] >= 351]
    except ValueError:
        st.error("Please choose another category. There are no books with this set of characteristics.")


#Book Filter 3 by ratings count
def filter_ratings_count(df_3):
    ratings_count = st.sidebar.selectbox("Would you like to read a popular book or a hidden gem?",
                                     ("Popular", "Hidden gem"))
    try:
        if ratings_count == "Hidden gem":
            return df_3[df_3["Ratings count"] <= 70000]
        else:
            return df_3[df_3["Ratings count"] >= 70001]
    except ValueError:
        st.error("Please choose another category. There are no books with this set of characteristics.")                                  

#Book Filter 4 by year published
def filter_published(df_4):
    published = st.sidebar.selectbox("Do you prefer to read a recent book or a classic?",
                                     ("Recent", "Classic"))
    try:
        if published == "Classic":
            return df_4[df_4["First published"] <= 2012]
        else:
            return df_4[df_4["First published"] >= 2013]
    except ValueError:
        st.error("Please choose another category. There are no books with this set of characteristics.")

#Create a sample of 3 books
def sample_df(df_s):
    try:
        return df_s.sample(n=3).reset_index()
    except ValueError:
        st.error("Please choose another category. There are no books with this set of characteristics.")

#Create columns so the recommendations will appear side by side
col1, col2, col3 = st.columns(3)

#Function to link the cover image with the url
def show_images(df):
    for index, row in df.iterrows():
        st.markdown("[![Imagen](" + row["Cover image"] + ")]("+row["Book url"]+")")
        st.markdown(row["Title"] + " " + "by" + " " + row["Author"])

