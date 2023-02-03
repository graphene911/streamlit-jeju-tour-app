import streamlit as st
import pandas as pd
import requests


def run_etc() :
    
    url = 'http://topping.io:8000/API/silos/error_silo?user_seq=8'

    response = requests.get(url).json()

    df = pd.DataFrame.from_dict(response)
    
    st.title('Error Device (선진제외전체)')
    
    st.image('data/#fc6858_line.png', width = 1753)
    df.to_csv('data/aimbelab_df_error_device_etc.csv', encoding='utf-8-sig')
    
    df = pd.read_csv('data/aimbelab_df_error_device_etc.csv',encoding='utf-8-sig', index_col=0)

    df = df.rename(columns={'agency':'대리점','farm':'농장명','address':'주소','silo_seq':'사일로 seq',
                            'silo':'사일로명','sn':'시리얼넘버','RecordTime':'마지막 측정시간'})

    st.subheader('(Count :' + ' ' + str(df['농장명'].count()) + ')')
    st._legacy_table(df)

    