def outer_fcn():
    message = "lol, wtf"
    
    def inner_fcn():
        print(message)
    
    return inner_fcn

def divider(y):
    def divide(x):
        return x/y
    return divide

d1 = divider(5)
print(d1(20))


from datetime import datetime
from typing import Any

def log_datetime(fcn):
    
    def wrapper():
        print(f'Function: {fcn.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        fcn()
    return wrapper


@log_datetime
def daily_backup():
    
    print('Daily backup job finished')


daily_backup()


import requests

class LimitQuery:
    
    def __init__(self, fcn):
        self.fcn = fcn
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.fcn(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return
        

@LimitQuery
def get_coin_price(limit):
    
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    
    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"
    
    

print(get_coin_price(6))
print(get_coin_price(6))
print(get_coin_price(6))
print(get_coin_price(6))
print(get_coin_price(6))
print(get_coin_price(6))


