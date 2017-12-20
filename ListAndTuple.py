#!/usr/bin/env python


def MyStocks():
    filename = "portfolio.csv"
    portfolio = []

    for line in open (filename):
        fields = line.split(",")
        name = fields[0]
        shares = int(fields[1])
        price = float(fields[2])
        stock = (name, shares, price)
        portfolio.append(stock)

    print(portfolio[0])
    print(portfolio[1])


if __name__ == "__main__":
    MyStocks()
