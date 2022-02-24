import json
from decouple import config
import http.client, urllib.parse

class GetNews:
    API_KEY = config('API_KEY')
    LIMIT = config('NEWS_LIMIT')

    dataList = []

    def __init__(self):
        self.conn = http.client.HTTPConnection('api.mediastack.com')

    def getNews(self):
        params = urllib.parse.urlencode(
            {
                'access_key' : self.API_KEY,
                'categories' : '-general',
                'sort' : 'published_desc',
                'limit' : self.LIMIT,
                'countries' : 'in'
            }
        )

        self.conn.request('GET', '/v1/news?{}'.format(params))

        res = self.conn.getresponse()
        data = res.read().decode('utf-8')

        for i in range(0,int(self.LIMIT)):
            interData = json.loads(data)['data'][i]['title']
            self.dataList.insert(int(self.LIMIT),interData)

        return self.dataList




