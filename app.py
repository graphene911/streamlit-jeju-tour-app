import streamlit as st
from app_home import run_home
from app_etc import run_etc
from app_report import run_report
from app_report_nh import run_report_nh
from app_mqtt import run_mqtt


def main() :
    
    st.set_page_config(layout="wide")

    menu = ['Error Device(선진)', 'Error Device(선진제외전체)' ,'Myfeed Report(선진)', 'Myfeed Report(서울축산농협)','data_list']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_etc()
    elif choice == menu[2] :
        run_report()
    elif choice == menu[3] :
        run_report_nh()
    elif choice == menu[4] :
        # Streamlit 앱 구성
        st.title("Silo List")

        silo_sn = st.text_input("Enter Silo SN")
        start_date = st.date_input("Enter start date")
        end_date = st.date_input("Enter end date")

        if st.button("Get Data List"):
            run_mqtt(silo_sn, start_date, end_date)
        


if __name__ == '__main__' :
    main()