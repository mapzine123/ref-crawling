#!/usr/bin/env python3

import configparser
import requests
from bs4 import BeautifulSoup
from running_task import running_task

# url을 통해서 data 가져옴
url = input("url을 입력하세요 : ")

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# HTML 태그 다 빼고 텍스트만 가져옴
data = soup.get_text()

# 데이터 처리
running_task(data)
