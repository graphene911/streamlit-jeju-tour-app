import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import plotly.express as px


def run_report() :
    
    st.title('선진사료 모니터링 보고서')

    response = requests.get('http://topping.io:8000/API/silos/user/dashboard?user_seq=30').json()

    df = pd.DataFrame.from_dict(response)

    df_a = df['company']['agency']

    df_a = pd.DataFrame(df_a)
    # st.dataframe(df)
    df = df.T

    df_am = pd.merge(df, df_a, left_on = 'seq', right_on = 'company_seq', how = 'left')
    df_ams = df_am[['company_name_x', 'company_name_y', 'company_seq_y', 'farm','seq_y']]
    df_farm = pd.DataFrame(df_a.loc[0,'farm'])
    
    for i in range(1, len(df_a.index)) :
        if df_a.loc[i,'farm'] != [] :
            df_farm_temp = pd.DataFrame(df_a.loc[i,'farm'])
            df_farm = pd.concat([df_farm, df_farm_temp])

    df_farm = df_farm.reset_index(drop=True)
    df_farm = df_farm.rename(columns={'seq':'farm_id_x','company_name':'f_company_name'})
    df_farm_x = pd.merge(df_ams, df_farm, left_on = 'seq_y', right_on = 'agency_seq', how = 'left')
    df_silo = pd.DataFrame(df_farm.loc[0,'silo'])

    for i in range(1, len(df_farm.index)) :
        df_silo_temp = pd.DataFrame(df_farm.loc[i,'silo'])
        df_silo = pd.concat([df_silo, df_silo_temp])

    # df_silo = df_silo.reset_index(drop=True)
    df_silo = df_silo.reset_index(drop=True)
    df_silo['farm_id'] = df_silo['farm_id'].astype('int64')
    df_silo = df_silo.rename(columns={'silodata':'silo_data', 'seq' : 'silo_seq'})
    df_sd = df_silo['silo_data']
    df_sd_d = df_sd.to_list()
    df_sd_d = pd.DataFrame(df_sd_d)
    # df = pd.merge(df_silo, df_sd_d, left_on = 'silo_type', right_on = 'siloType', how = 'left')
    df_s = pd.concat([df_silo, df_sd_d], axis = 1)
    df = pd.merge(df_farm_x,df_s, left_on = 'farm_id_x', right_on = 'farm_id', how = 'left')
    df = df.drop(['company_name_x','farm', 'gender', 'user_email', 'auth', 'date_of_birth','is_activate', 'user_password',
                'logo', 'lat', 'animal_type', 'lon', 'api_key', 'status','animal_cnt','user_id', 'address', 'coordinate',
                'phone', 'token','cdt','silo','silo_type','silo_height','silo_diameter','memo','food_category','silo_capacity',
                'silo_middle_height','silo_middle_diameter','silo_seq', 'silo_sn', 'binstatus', 'silo_data', 'siloType',
                'h1','h3','display','seq','d','h2','h4','company_seq_y','seq_y','agency_seq','farm_id_x','company_seq',
                'farm_id','last_name', 'first_name'], axis= 1)

    df = df.replace("", np.NaN)
    # df = df.fillna('-')
    df['규격'] = df['companyName'] + " " + df['size'] + "t"
    df = df.fillna(999)
    df = df.astype({'expect_day' :'int'})
    df['expect_day'] = df['expect_day'].replace(999, '판단불가')
    # if df['expect_day'] != '판단불가' :
    #     df['expect_day'] = df['expect_day'] + '일'
    df['per'] = round(df['per'])
    df['avg_per'] = round(df['avg_per'])
    
    # if df['expect_day'] == None :
    #     df['expect_day'] = '판단불가'
    # else :
    #     df['expect_day'] = round(df['expect_day'])
    
    # df['잔량(예상소진일)'] = str(df['per']) + "%" + "(" + df['expect_day'] + ")"
    df = df[['company_name_y', 'f_company_name', 'silo_name', '규격', 'food_name', 'per', 'expect_day']]
    # df = df.groupby(['company_name_y','f_company_name'],  as_index=False)
    # 'per' : '잔량', 'expect_day' : '예상소진일',
    df = df.rename(columns={'company_name_y':'대리점', '규격':'사일로 종류 및 톤수' ,'f_company_name' : '농장명', 'food_name' : '사료명칭',
                            'per' : '잔량', 'expect_day' : '예상소진일','silo_name' : '사일로명'})

    # df['잔량(예상소진일)'] = df['잔량'] + '' + "%" + '' + df['예상소진일']


    df.to_csv('data/aimbelab_df.csv', encoding='utf-8-sig')
    
    df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)

    # df = df.style.format({ 'A': '{:,.2f}'.format, 'B': '{:,.2%}'.format,})
    # df_t = df[df['예상소진일'] != '판단불가']
    
    # st.dataframe(df)
    st.info('실시간 사료 소비량 모니터링과 AI 분석을 통해사료 소진일을 예측합니다.')
    st.subheader('')
    menu = ['여주축우대리점','상주대리점', '영주북부대리점', '예산대리점', '영동대리점']
    choice1 = st. selectbox('대리점 선택', menu)
    
    st.image('data/#fc6858_line.png', width = 1753)
    st.subheader('사료소진 임박 농장 리스트')
    
    
    
    if choice1 == menu[0] :
        df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)
        df_s = df[df['대리점'] == '여주축우대리점']
        df_s = df_s[df_s['잔량'] <= 30]
        # df_s = df_s[ df_s['예상소진일'] != "판단불가"]
        df_u = df[df['잔량'] > 30]
        df_pc = [len(df_s.index), len(df_u.index)]
        df_p = len(df_s.index)/len(df.index) * 100
        
        st._legacy_table(df_s)
        # , width=1069, height=808
        
        fig1 = px.pie(df_pc)
        # st.plotly_chart(fig1)


    elif choice1 == menu[1] :
        df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)
        # df_t = df_t[df_t['대리점'] == '상주대리점']
        # df_t = df_t[df_t['잔량'] <= 30]
        df = df[df['대리점'] == '상주대리점']
        df_s = df[df['잔량'] <= 30]
        df_u = df[df['잔량'] > 30]
        df_pc = [len(df_s.index), len(df_u.index)]
        df_p = len(df_s.index)/len(df.index) * 100
        st._legacy_table(df_s)
        fig1 = px.pie(df_pc)
        # st.plotly_chart(fig1)
    
    elif choice1 == menu[2] :
        df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)
        df = df[df['대리점'] == '영주북부대리점']
        df_s = df[df['잔량'] <= 30]
        df_u = df[df['잔량'] > 30]
        df_pc = [len(df_s.index), len(df_u.index)]
        df_p = len(df_s.index)/len(df.index) * 100
        st._legacy_table(df_s)
        fig1 = px.pie(df_pc)
        # st.plotly_chart(fig1)
    
    elif choice1 == menu[3] :
        df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)
        df = df[df['대리점'] == '예산대리점']
        df_s = df[df['잔량'] <= 30]
        df_u = df[df['잔량'] > 30]
        df_pc = [len(df_s.index), len(df_u.index)]
        df_p = len(df_s.index)/len(df.index) * 100
        st._legacy_table(df_s)
        fig1 = px.pie(df_pc)
        # st.plotly_chart(fig1)
    
    elif choice1 == menu[4] :
        df = pd.read_csv('data/aimbelab_df.csv',encoding='utf-8-sig', index_col=0)
        df = df[df['대리점'] == '영동대리점']
        df_s = df[df['잔량'] <= 30]
        df_u = df[df['잔량'] > 30]
        df_pc = [len(df_s.index), len(df_u.index)]
        df_p = len(df_s.index)/len(df.index) * 100
        
        st._legacy_table(df_s)
        # fig1 = px.pie(df_pc)
        # st.plotly_chart(fig1)


