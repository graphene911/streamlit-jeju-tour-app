import streamlit as st
import pandas as pd
import requests


# run_mqtt 함수 정의
def run_mqtt(silo_sn, start_date, end_date):
    

    url = 'http://20.214.200.233:8000/API/silos/get_silo_list2?silo_sn={}&start_date={}&end_date={}'.format(silo_sn, start_date, end_date)
    response = requests.get(url).json()
    # response_json = response.json() # JSON으로 변환
    df = pd.DataFrame(response)
    df = df.sort_values(by='RecordTime', ascending=False)
    df.reset_index()
    df.to_csv('data/DATA_LIST.csv', encoding='utf-8-sig')
    with open("data/DATA_LIST.csv", "rb") as file:
        st.download_button(
                    label="Download CSV File",
                    data=file,
                    file_name="data_list.csv",
                    mime="application/octet-stream")
    
    st._legacy_table(df)


