import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time 


covid_api = 'https://covid19.th-stat.com/api/open/today'
r_covid = requests.get(covid_api)
r_covid.encoding = 'utf-8'

def line_notify_message_covid(message_covid):
	playload_covid = {'message' :message_covid}
	return line_notify_covid(playload_covid)

def line_notify_covid(playload_covid):
    url = 'https://notify-api.line.me/api/notify'
    token = 'uzoA2ha8byDxFzU72IEZVCQvu6K6HEWhr1TiB0CpqV6'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}
    return requests.post(url, headers=headers, data=playload_covid)

def covid_check():
    line_notify_message_covid('จำนวนผู้ติดเชื้อ Covid - 19 ประจำวันที่'
    + str(r_covid.json()['UpdateDate']) + '\n'
    + 'ผู้ป่วยสะสม:' + str(r_covid.json()['Confirmed']) +'\n'
    + 'ผู้ป่วยหายแล้ว:' + str(r_covid.json()['Recovered']) + '\n'
    + 'ผู้ป่วยที่อยู่ รพ.:' + str(r_covid.json()['Hospitalized']) +'\n'
    + 'ผู้ป่วยใหม่:' + str(r_covid.json()['NewConfirmed']) + '\n'
    + 'เสียชีวิต:' + str(r_covid.json()['Deaths'])
    )
covid_check()
