import streamlit as st




def main() :
    st.title('Streamlit jeju tour app')
    
    menu = ['관광지', '여행추천코스', '숙박', '음식점']
    st. selectbox('메뉴 선택', menu)
    
    





if __name__ == '__main__' :
    main()