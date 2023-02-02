import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import plotly.express as px


def run_report_nh() :
    st.title('서울축산농협 모니터링 보고서')

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
    df_silo_m = df_silo.drop(columns=['silo_height', 'silo_diameter', 'memo', 'food_category', 'silo_capacity',
                                    'silo_middle_height', 'silo_middle_diameter','seq','binstatus', 'charge_per'])

    df_sd = pd.DataFrame(df_silo['silodata'])
    for i in range(0, df_sd['silodata']) :
        df_sd_c = pd.DataFrame(df_silo.loc[i,'silodata'])
        df_sd = pd.merge(df_silo_m, df_sd_c, left_on = 'silo_type', right_on = 'type',how='left')
    # df_sd = pd.DataFrame(df_silo.loc[0,'silodata'])
    
    # for i in range(0, len(df_silo_m.index)) :
    #     df_silo_temp = pd.DataFrame(df_silo_m.loc[i,'silo'])
    #     df_silo = pd.concat([df_c, df_silo_temp])

    
    # df_sd = df_silo_m['silodata']

    # df_user = pd.merge(df_c, df_silo_m, left_on = 'seq', right_on = 'farm_id',how='left')

    
    st._legacy_table(df_sd_c)


