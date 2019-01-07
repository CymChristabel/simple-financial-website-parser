import requests
import json
import time
from html.parser import HTMLParser
import re

class Fund():
    class FundHTMLParser(HTMLParser):
        data_list = []
        def handle_data(self, data):
            self.data_list.append(data)
    
    def __init__(self, start_time, end_time):
        self.url = 'http://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.23497223040268844&page=0&size=99999999'
        self.detail_url = 'http://gs.amac.org.cn/amac-infodisc/res/fund/account/'
        self.payload = {
            "foundDateFrom": start_time,
            "foundDateTo": end_time
        }
        self.headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://gs.amac.org.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Content-Type': 'application/json',
            'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/fund/account/index.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': "zh-CN,zh;q=0.9,nl;q=0.8,en;q=0.7"
        }

    def post(self):
        # Fetching data
        print('Start fetching data...')

        s_time = time.time()
        res = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        res.raise_for_status()

        # Convert data to list
        
        fund_list = json.loads(res.text)['content']
        print('%s number of results found' % len(fund_list))

        print('Generating data as list...')

        res = [['专户名称', 
                '备案编码', 
                '管理人名称', 
                '托管人名称', 
                '备案日期', 
                '合同期限', 
                '设立时募集资金总额（万元）',
                '是否分级',
                '成立时投资者数量']]
                
        for item in fund_list:
            r = requests.get(self.detail_url + item['id'] + '.html')
            # Successfully fetched website
            if r.status_code == 200:
                # Preprocess data
                r.encoding = 'utf-8'
                idx_start = r.text.find('<tbody>')
                idx_end = r.text.find('</tbody>')
                text_extracted = re.sub(r'[\n\t\s]*', '', r.text[idx_start: idx_end + 8])

                # Extract data from HTML
                fund_html_parser = self.FundHTMLParser()
                fund_html_parser.data_list = []
                fund_html_parser.feed(text_extracted)
                
                res.append(fund_html_parser.data_list[1::2])

            # If not
            else:
                print('Cannot fetch ' + item['id'])
        
        print('Data generated')
        print('Total time cost: %s seconds' % (time.time() - s_time))

        return res

        