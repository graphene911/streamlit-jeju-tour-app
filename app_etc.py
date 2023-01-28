import streamlit as st
import pandas as pd
import requests


def run_etc() :
    
    url = 'http://topping.io:8000/API/silos/error_silo?user_seq=8'

    response = requests.get(url).json()

    df = pd.DataFrame.from_dict(response)
    
    st.title('Error Device (선진제외전체)')
    st.subheader('(Count :' + ' ' + str(df['sn'].count()) + ')')
    st.image('data/#fc6858_line.png', width = 1753)
    
    st._legacy_table(df)

