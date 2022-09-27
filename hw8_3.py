from datetime import datetime as dt
from datetime import timedelta
import requests as rq



def getinfo (url,min_day,max_day):
    params = dict(fromdate = min_day,todate = max_day,tagged = 'Python', site = 'stackoverflow')
    req = rq.get(url, params=params)

    return req.json()

if __name__ == '__main__':

    today = dt.replace(dt.now(),hour=0,minute=0,second=0,microsecond=0 )
    yesterday = today - timedelta(days=2)
    yesterday = round(yesterday.timestamp())
    today = round(today.timestamp())
    print(today)
    print(yesterday)

    url = 'https://api.stackexchange.com/questions'
    print(getinfo(url=url,min_day=yesterday,max_day=today))