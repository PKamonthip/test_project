import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
web_url = 'https://www.goldtraders.or.th/default.aspx'
r = requests.get(web_url)
r.encoding = 'utf-8'
sub = BeautifulSoup(r.text)


def line_notify_message(message):
    payload = {'message':message}
    return line_notify(payload)
def line_notify(payload, file=None):
    URL = 'https://notify-api.line.me/api/notify'
    Token = 'uzoA2ha8byDxFzU72IEZVCQvu6K6HEWhr1TiB0CpqV6'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+Token}     
    return requests.post(URL, headers=headers, data=payload, files=file) 
def gold_price_check():
    line_notify_message('ราคาทองคำ 96.5% ประจำวันที่'
        + sub.find(id='DetailPlace_uc_goldprices1_lblAsTime').text + '\n'
        + 'ทองคำแท่ง' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + '\n'
        + 'ทองคำรูปพรรณ' + '\n'
        + 'ขายออก : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMSell').text + '\n'
        + 'รับซื้อ : ' + sub.find(id='DetailPlace_uc_goldprices1_lblOMBuy').text)
gold_price_check()
