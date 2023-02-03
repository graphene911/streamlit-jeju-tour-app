import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import plotly.express as px
import json


def run_report_nh() :
    st.title('서울축산농협 모니터링 보고서')
    
    st.info('실시간 사료 소비량 모니터링과 AI 분석을 통해사료 소진일을 예측합니다.')
    st.subheader('')
    st.image('data/#fc6858_line.png', width = 1753)
    st.subheader('사료소진 임박 사일로 리스트')

    response = requests.get('http://topping.io:8000/API/silos/user/dashboard?user_seq=28').json()

    df = pd.DataFrame(response)
    df = df.drop(columns=['agency_cnt','silo_cnt','farm_cnt','required_per_cnt','chart_cnt','chart_per'], axis=1)
    df = df.T
    df_c = df[['seq','company_name']]
    df_c = df_c.reset_index(drop=True)
    df_silos = df['silo']
    df_silos = df_silos.reset_index(drop=True)
    for i in df_silos:
        df_silo = pd.DataFrame(i)
    df_silo_m = df_silo.drop(columns=['silo_sn','silo_height', 'silo_diameter', 'memo', 'food_category', 'silo_capacity', 'farm_id',
                                    'silo_middle_height','silodata' ,'silo_middle_diameter','seq','binstatus', 'charge_per'])
    df_silo_m['silo_type'] = df_silo_m['silo_type'].astype('int64')
    df_sd = df_silo['silodata']
    df_sd= df_sd.to_list()
    df_sd = pd.DataFrame(df_sd)
    # df_sd['silo_type'] = df_sd['silo_type'].astype('int64')

    df_silo = pd.merge(df_silo_m,df_sd, left_on='silo_type', right_on='seq', how='left')
    df_silo = df_silo.drop(columns=['silo_type', 'seq','h1','h2','h3','h4','display','d','siloType'])
    df = df_silo.drop_duplicates()
    df['사일로 종류 및 톤수'] = df['companyName'] + " " + df['size'] + "t"
    df = df.rename(columns={'silo_name':'사일로명','food_name':'사료명칭','per':'잔량','expect_day':'예상소진일'})
    df = df[['사일로명','사일로 종류 및 톤수','사료명칭','잔량','예상소진일']]
    df = df.reset_index()
    df = df.drop(columns='index')
    df = df[df['잔량'] <= 30]
    st._legacy_table(df)


