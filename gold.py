import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import time 

gold_url = 'https://www.goldtraders.or.th/default.aspx'
r_gold = requests.get(gold_url)
r_gold.encoding = 'utf-8' 
sub = BeautifulSoup(r_gold.text) 

#x = '{"id":"DetailPlace_uc_goldprices1_lblAsTime"}'
#y = json.loads(x)

def line_notify_sms_gold(message):
    pload_gold = {'messsge':message}
    return line_notify_gold(pload_gold)

def line_notify_gold(pload_gold, file=None):
    URL = 'https://notify-api.line.me/api/notify'
    token = 'uzoA2ha8byDxFzU72IEZVCQvu6K6HEWhr1TiB0CpqV6'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}
    return requests.post(URL, headers=headers, data=pload_gold, files=file)

def gold_check():
    line_notify_sms_gold('ราคาทองคำ 96.5% ประจำวันที่' 
        + sub.find(id='DetailPlace_uc_goldprices1_lblAsTime').text +'\n'
        + 'ราคาทองคำแท่งขายออก:' + sub.find(id='DetailPlace_uc_goldprices1_lblBLSell').text +'\n'
        + 'ราคาทองคำแท่งรับซื้อ:' + sub.find(id='DetailPlace_uc_goldprices1_lblBLBuy').text + '\n'
        + 'ราคาทองคำรูปประพรรณขายออก:' + sub.find(id='DetailPlace_uc_goldprices1_lblOMSell').text +'\n'
        + 'ราคาทองคำรูปประพรรณขายรับซื้อ:' + sub.find(id='DetailPlace_uc_goldprices1_lblOMBuy').text)
    
gold_check()

