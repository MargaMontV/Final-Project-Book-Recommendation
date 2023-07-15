import streamlit as st
import pandas as pd
import numpy as np

st.title('Book Recommending APP')

option = st.selectbox(
    'Which genre would you like to read?',
    (' ', 'Fantasy', 'Science Fiction'))

st.write('You selected:', option)
