import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import requests
import plotly.express as px
import json
from bs4 import BeautifulSoup


def run_mqtt() :
    url = 'https://www.aimbelab.com/mqtt.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # html_code = soup.prettify()
    program_names = soup.select('td > p > a')
    
    for tag in program_names:
	    print(tag.get_text())
        # print(tag_text)
    # print(html_code)
    # articles = soup.find_all('div', {'class': 'cluster_text'})

    # for article in articles:
    #     title = article.find('SN').get_text().strip()
    #     link = article.find('SN')['href']
    #     print(title)
    #     print(link)
    # return tag_text