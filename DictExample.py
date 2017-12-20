#!/usr/bin/env python

def myDictEx():
    prices = {
             "Google" : 888.8,
             "Apple" :  777.7,
             "Microsoft" : 666.6
            }
    p = prices.get("DHL", 0.0)
    print(p)

    pList = list(prices)

    del prices["Microsoft"]

    print(prices)

if __name__ == "__main__":
    myDictEx()
