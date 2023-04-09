import streamlit as st
import pandas as pd
import requests
import altair as alt



# run_mqtt 함수 정의
def run_mqtt(silo_sn, start_date, end_date):
    

    url = 'http://20.214.200.233:8000/API/silos/get_silo_list2?silo_sn={}&start_date={}&end_date={}'.format(silo_sn, start_date, end_date)
    response = requests.get(url)
    response_json = response.json() # JSON으로 변환
    df = pd.DataFrame(response_json)
    df = df.sort_values(by='RecordTime', ascending=False)
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    df.to_csv('data/DATA_LIST.csv', encoding='utf-8-sig')
    with open("data/DATA_LIST.csv", "rb") as file:
        st.download_button(
                    label="Download CSV File",
                    data=file,
                    file_name="data_list.csv",
                    mime="application/octet-stream")
    
    df = pd.read_csv('data/DATA_LIST.csv',encoding='utf-8-sig', index_col=0)
    
    st._legacy_table(df)
    df = df[['RecordTime', 'ton', 'Dist']] # 필요한 열만 선택
    # print(df.dtypes)
    df['ton'] = pd.to_numeric(df['ton'], errors='coerce')
    df.set_index('RecordTime', inplace=True)

    # altair line chart 생성
    ton_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('RecordTime', axis=alt.Axis(title='Record Time')),
        y=alt.Y('ton', axis=alt.Axis(title='Ton'))
    ).properties(
        width=800,
        height=400
    )

    dist_chart = alt.Chart(df).mark_line().encode(
        x=alt.X('RecordTime', axis=alt.Axis(title='Record Time')),
        y=alt.Y('Dist', axis=alt.Axis(title='Distance'))
    ).properties(
        width=800,
        height=400
    )
    
    # y 축 범위 설정
    chart = ton_chart.configure_scale(
        y=alt.Scale(domain=(float(df['ton'].min()), float(df['ton'].max())))
    ) & dist_chart.configure_scale(
        y=alt.Scale(domain=(float(df['Dist'].min()), float(df['Dist'].max())))
    )
    st.altair_chart(chart, use_container_width=True)