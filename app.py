import streamlit as st
import altair as alt
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import json
from streamlit_folium import folium_static
import folium
def main() :
    
    st.set_page_config(layout="wide")
    
    st.title('Streamlit jeju tour app')
    
    menu = ['관광지', '여행추천코스', '숙박', '음식점']
    choice1 = st. selectbox('메뉴 선택', menu)
    
    if choice1 == menu[0] :
        
        jt = pd.read_csv('data/df1.csv', index_col=0)
                
        tour_serch = st.text_input('관광지 검색')
        result = jt.loc[ jt['명칭'] .str.contains(tour_serch) ]
                
        c1, c2 = st.columns(2)
               
        with c1 :
            c1.header('위치')
            st.map(result)

        with c2 :
            c2.header("내용")
            column_list = result.columns
            column_list = st.multiselect('컬럼을 선택해 원하시는 정보를 찾아보세요', column_list)
            if len(column_list) != 0 :
                st.dataframe(result[column_list])
            
            st.info('마우스를 가져가면 가려진 내용전체가 보입니다.')
        
        st.title('')
        st.header('제주도 관광지 지역별 보기')
        jt2 = jt[['명칭','주소','개요','문의 및 안내','쉬는날','이용시간','주차시설','유모차 대여 여부','애완동물 동반 가능 여부']]
        
        menu2 = ['제주시','서귀포시']
        choice2 = st.selectbox('지역 선택', menu2)
        if choice2 ==menu2[0] :
            st.dataframe(jt2.loc[jt2['주소'].str.contains('제주시')])
        else :
            st.dataframe(jt2.loc[jt2['주소'].str.contains('서귀포시')])
    

        if result == None :
            
            map_jeju2 = folium.Map(location=['33.3445','126.5364'], zoom_start=10)
            folium_static(map_jeju2)

        else :    
            loc = result[['lat','lon']] # 위도(N), 경도(E)
            # 지도 정의
            map_jeju = folium.Map(loc, zoom_start=14)
        
            # 포인트 마커 추가

            for i in range(len(result)):
                folium.Marker(list(result.iloc[i][['lat', 'lon']]),
                popup=result.iloc[i][['명칭','문의 및 안내']],
                icon=folium.Icon(color='blue')).add_to(map_jeju)

            folium_static(map_jeju)
        
        


    if choice1 == menu[1] :
        st.subheader('여행 추천코스')
        jtc = pd.read_csv('data/jeju_tour_course.csv', index_col= 0)
        
        st.dataframe(jtc)

        tour_course_serch = st.text_input('코스 검색')
        result1 = jtc.loc[ jtc['명칭'] .str.contains(tour_course_serch) ]
                
        c1, c2 = st.columns(2)
               
        with c1 :
            c1.header('위치')
            st.map(result1)

        with c2 :
            c2.header("내용")
            column_list = result1.columns
            column_list = st.multiselect('컬럼을 선택해 원하시는 정보를 찾아보세요', column_list)
            if len(column_list) != 0 :
                st.dataframe(result1[column_list])
            
            st.info('마우스를 가져가면 가려진 내용전체가 보입니다.')








    if choice1 == menu[2] :
        st.subheader('숙박업소')
        jh = pd.read_csv('data/jeju_hotel.csv', index_col=0)
        

        hotel_serch = st.text_input('관광지 검색')
        result2 = jh.loc[ jh['명칭'] .str.contains(hotel_serch) ]
                
        c3, c4 = st.columns(2)
               
        with c3 :
            c3.header('위치')
            st.map(result2)

        with c4 :
            c4.header("내용")
            column_list3 = result2.columns
            column_list3 = st.multiselect('컬럼을 선택해 원하시는 정보를 찾아보세요', column_list3)
            if len(column_list3) != 0 :
                st.dataframe(result2[column_list3])
            
            st.info('마우스를 가져가면 가려진 내용전체가 보입니다.')
        st.title('')
        st.subheader('제주도 숙박업소 지역별 보기')
        
        jh2 = jh[['명칭','주소','개요','주차 가능','조리 가능','체크인','체크아웃','예약 안내']]

        menu3 = ['제주시','서귀포시']
        choice3 = st.selectbox('지역 선택', menu3)
        if choice3 ==menu3[0] :
            st.dataframe(jh2.loc[jh2['주소'].str.contains('제주시')])
        else :
            st.dataframe(jh2.loc[jh2['주소'].str.contains('서귀포시')])


    if choice1 == menu[3] :
        st.subheader('음식점')
        jr = pd.read_csv('data/jeju_rest.csv', index_col=0)
         

        rest_serch = st.text_input('음식점 검색')
        result3 = jr.loc[ jr['명칭'] .str.contains(rest_serch) ]
                
        c5, c6 = st.columns(2)
               
        with c5 :
            c5.header('위치')
            st.map(result3)

        with c6 :
            c6.header("내용")
            column_list4 = result3.columns
            column_list4 = st.multiselect('컬럼을 선택해 원하시는 정보를 찾아보세요', column_list4)
            if len(column_list4) != 0 :
                st.dataframe(result3[column_list4])
            
            st.info('마우스를 가져가면 가려진 내용전체가 보입니다.')
        st.title('')
        st.subheader('제주도 음식점 지역별 보기')
        

        jr2 = jr[['명칭','주소','개요','문의 및 안내','영업시간','대표메뉴','취급메뉴','상세정보']]

        menu3 = ['제주시','서귀포시']
        choice3 = st.selectbox('지역 선택', menu3)
        if choice3 ==menu3[0] :
            st.dataframe(jr2.loc[jr2['주소'].str.contains('제주시')])
        else :
            st.dataframe(jr2.loc[jr2['주소'].str.contains('서귀포시')])


if __name__ == '__main__' :
    main()