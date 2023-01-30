import requests
import random
import time
import os

bitc = int('0')
balance = int('10000')
def time_():
    global price2
    time.sleep(10)
    while True:
        response = requests.get('https://www.blockchain.com/ru/ticker')
        response_json = response.json()
        price3 = float(response_json["USD"]["last"])
        y = (float(price3) - float(price2))
        if y > 0.05:
            sellbtc()

def sellbtc():
    global bitc, balance

    response = requests.get('https://www.blockchain.com/ru/ticker')
    response_json = response.json()
    price4 = float(response_json["USD"]["last"])
    t = bitc * price4
    bitc = bitc - bitc
    balance += t
    balance_now = balance
    a = bitc
    v = balance
    p = (10000 - float(balance))
    balance_now = balance + p
    os.system('cls')
    print(f"""
    BTC  {a}             USD {v}             DIFF {p}
    PRICE BUY {price2}       PRICE SELL {price4}       BALANCE {balance_now}
    """)


    time.sleep(10)
    torgses()


def torgses():
    global bitc, balance, price2

    response = requests.get('https://www.blockchain.com/ru/ticker')
    response_json = response.json()
    price = float(response_json["USD"]["last"])
    price2 = price
    buy = random.randint(5000, 10000)
    balance_now = balance
    balance = balance - buy
    btc = (buy / price)
    bitc = bitc + btc
    a = bitc
    v = balance
    os.system('cls')
    print(f"""
    BTC  {a}             USD {v}             DIFF 0.0
    PRICE BUY {price2}       BALANCE {balance_now}
    """)

    time_()

torgses()

