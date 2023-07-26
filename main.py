#Imports
import streamlit as st
import pandas as pd
from p_analysis import m_analysis as man

#Call the function to load the CSS
man.load_css()

#Read the csv with the scraped and cleaned books
books_df = man.read_csv('./data/books_clean.csv')

#Load the custom design image
title_image = "./book_logo_title.jpg"

#Display the image as the app title and the title
st.image(title_image)

#Give instructions to the user of how the app works
st.markdown("""
 * This is an app for book recommendations.
 * Use the left menu to select your books preferences.
 * Your recommendations will appear below. 
 * You can click on the cover to see the whole book info.
""")

#Book Filter 1 by genre
df_genre = man.filter_genre(books_df)

#Book Filter 2 by pages
df_pages = man.filter_pages(df_genre)

#Book Filter 3 by ratings count
df_ratings_count = man.filter_ratings_count(df_pages)                                 

#Book Filter 4 by year published
df_published = man.filter_published(df_ratings_count)

#Create a sample of 3 books
df_sample = man.sample_df(df_published)


#Create columns so the recommendations will appear side by side
col1, col2, col3 = st.columns(3)

#Apply to the columns the function to link the cover image with the url
with col1:
    man.show_images(pd.DataFrame(df_sample.iloc[[0]]))
with col2:
    man.show_images(pd.DataFrame(df_sample.iloc[[1]]))
with col3:
    man.show_images(pd.DataFrame(df_sample.iloc[[2]]))

#Include a shuffle button for the user
st.button("Shuffle")

