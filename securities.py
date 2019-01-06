import requests
import json
import sys
import datetime

def time_validation(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

# Read argument values
assert len(sys.argv) == 4
start_time, end_time, output_filename = sys.argv[1], sys.argv[2], sys.argv[3]

time_validation(start_time)
time_validation(end_time)

url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/securities?rand=0.2547440873167026&page=0&size=3'

payload = {
    "foundDateFrom": start_time,
    "foundDateTo": end_time
}

headers = {
    'Connection': 'keep-alive',
    'Content-Length': '110',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://gs.amac.org.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/pof/securities/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': "zh-CN,zh;q=0.9,nl;q=0.8,en;q=0.7"
}

r = requests.post(url, data=json.dumps(payload), headers=headers)

d = json.loads(r.text)
print(d['content'][0]['cpmc'])