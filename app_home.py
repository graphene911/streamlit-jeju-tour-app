import streamlit as st
import pandas as pd
import requests



def run_home() :
    
    url = 'http://topping.io:8000/API/silos/error_silo?user_seq=30'
    response = requests.get(url).json()

    df = pd.DataFrame.from_dict(response)
    df = df.rename(columns={'agency':'대리점','farm':'농장명','address':'주소','silo_seq':'사일로 seq',
                            'silo':'사일로명','sn':'시리얼넘버','RecordTime':'마지막 측정시간'})
    st.title('Error Device (선진)')
    
    menu = ['전체','여주축우대리점','상주대리점', '영주북부대리점', '예산대리점', '영동대리점']
    choice = st. selectbox('대리점 선택', menu)
    st.image('data/#fc6858_line.png', width = 1753)
    df.to_csv('data/aimbelab_df_error_device.csv', encoding='utf-8-sig')
    
    df = pd.read_csv('data/aimbelab_df_error_device.csv',encoding='utf-8-sig', index_col=0)
    # st._legacy_table(df)
    # # st._legacy_table(df.sort_values(['RecordTime'], ascending= False, ))
    
    if choice == menu[0] :
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        
        with open("data/aimbelab_df_error_device.csv", "rb") as file:
            btn = st.download_button(
                label="Download CSV File",
                data=file,
                file_name="Error Device.csv",
                mime="application/octet-stream")
        
        st._legacy_table(df)
        
        
    elif choice == menu[1] :
        df = df[df['대리점'] == '여주축우대리점']
        df = df.reset_index()
        df = df.drop(columns='index')
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        st._legacy_table(df)

    elif choice == menu[2] :
        df = df[df['대리점'] == '상주대리점']
        df = df.reset_index()
        df = df.drop(columns='index')
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        st._legacy_table(df)

    elif choice == menu[3] :
        df = df[df['대리점'] == '영주북부대리점']
        df = df.reset_index()
        df = df.drop(columns='index')
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        st._legacy_table(df)

    elif choice == menu[4] :
        df = df[df['대리점'] == '예산대리점']
        df = df.reset_index()
        df = df.drop(columns='index')
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        st._legacy_table(df)

    elif choice == menu[5] :
        df = df[df['대리점'] == '영동대리점']
        df = df.reset_index()
        df = df.drop(columns='index')
        st.subheader('(Count :' + ' ' + str(df['시리얼넘버'].count()) + ')')
        st._legacy_table(df)