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
    
    df_user = pd.merge(df_c, df_silo_m, left_on = 'seq', right_on = 'farm_id',how='left')
    # df_user = df_user.drop(columns=['gender','user_email','auth','date_of_birth','is_activate','user_password','logo','last_name','lat',
    #                                 'animal_type','lon','first_name','animal_cnt','api_key','user_id','status','address','token','cdt',
    #                                 'company_seq','coordinate','phone','agency_seq','short','normal','large','farm_id','silo_sn',
    #                                 ],axis=1)
    # df_sd = df_silo_m['silodata']
    # for i in range(1, len(df_sd.index)) :
    #     if df_sd.loc[i,'silodata'] != [] :
    #         df_farm_temp = pd.DataFrame.from_dict([df_sd['silodata']])
    #         df_farm = pd.concat([df_silo_m, df_farm_temp])
    df_sd = df_silo_m['silodata']
    df_sd = df_sd.T
    st._legacy_table(df_sd)


