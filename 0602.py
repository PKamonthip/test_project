import requests
url = 'https://notify-api.line.me/api/notify'
token = 'uzoA2ha8byDxFzU72IEZVCQvu6K6HEWhr1TiB0CpqV6'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'Hello LINE Notify with Kamonthip'
r = requests.post(url, headers=headers, data={'message':msg})
print(r.text)
