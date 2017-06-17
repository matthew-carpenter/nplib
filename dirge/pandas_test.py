#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


dataframe = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
             "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
             "area": [8.516, 17.10, 3.286, 9.597, 1.221],
             "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dataframe)
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print
print(brics)
print

house_prices = pd.read_csv('/home/matthew/PycharmProjects/nplib/strongai/machine_learning/housing_prices.csv')

print house_prices


def main():
    pass


# Execute as a script
if __name__ == '__main__':
    main()
