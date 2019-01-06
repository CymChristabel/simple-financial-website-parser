import requests
import json
import time

class Securities():
    def __init__(self, start_time, end_time):
        # Init values
        self.url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/securities?rand=0.2547440873167026&page=0&size=99999999'
        self.payload = {
            "foundDateFrom": start_time,
            "foundDateTo": end_time
        }
        self.headers = {
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
        
    def post(self):
        # Fetching data
        print('Start fetching data...')

        s_time = time.time()
        res = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)
        res.raise_for_status()

        print('Fetching complete, time: %s seconds' % (time.time() - s_time))

        # Convert data to list
        

        securities_list = json.loads(res.text)['content']
        print('%s number of results found' % len(securities_list))

        print('Generating data as list...')

        res = [['产品名称', 
                '产品编码', 
                '管理机构', 
                '设立日期', 
                '到期日', 
                '投资类型', 
                '是否分级',
                '成立规模（万元)',
                '投资者总数',
                '托管机构']]

        for item in securities_list:
            if item['dqr'] == '9999-12-31':
                item['dqr'] = '无固定存续期限'

            res.append([
                item['cpmc'],
                item['cpbm'],
                item['gljg'],
                item['slrq'],
                item['dqr'],
                item['tzlx'],
                item['sffj'],
                item['clgm'],
                item['clscyhs'],
                item['tgjg']
            ])
        
        print('Data generated')

        return res