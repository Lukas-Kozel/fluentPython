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


def deco(fcn):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('rwunning target()')
    
target()
print(target)

print('--------------------------------------------------')

registry = []

def register(fcn):
    print('running register(%s)' % fcn)
    registry.append(fcn)
    return fcn

@register
def f1():
    print('running f1()')
    

@register
def f2():
    print('running f2()')
    

def f3():
    print('running f3()')
    
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
    
if __name__ == '__main__':
    main()
    

print('------------------------------------------------------------------------')

from chapter6_classic_Strategz import *
promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos) 
