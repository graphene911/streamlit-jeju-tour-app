import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import plotly.express as px


def run_report_nh() :
    
    
    # with open( "data/style.css" ) as css:
    #     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
    
    st.title('서울축산농협 모니터링 보고서')

    response = requests.get('http://topping.io:8000/API/silos/user/dashboard?user_seq=28').json()

    df = pd.DataFrame(response)
    df = df.drop(columns=['agency_cnt','silo_cnt','farm_cnt','required_per_cnt','chart_cnt','chart_per'], axis=1)
    df = df.T
    df_c = df[['seq','company_name']]
    df_silos = df['silo']
    df_silo = pd.DataFrame(df.loc[0,'silo'])

    for i in range(1, len(df.index)) :
        df_silo_temp = pd.DataFrame(df.loc[i,'silo'])
        df_silo = pd.concat([df_silo, df_silo_temp])


