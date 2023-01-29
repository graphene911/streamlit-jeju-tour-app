import streamlit as st
from app_home import run_home
from app_etc import run_etc
from app_report import run_report
from app_report_nh import run_report_nh

def main() :
    
    st.set_page_config(layout="wide")

    menu = ['Error Device(선진)', 'Error Device(선진제외전체)' ,'Myfeed Report(선진)' ]
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_etc()
    elif choice == menu[2] :
        run_report()


if __name__ == '__main__' :
    main()