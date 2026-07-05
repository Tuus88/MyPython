# test2 = open("E:\\Python\\python_learning\\test2.txt", "w")
# test2.readline()

import pandas
print(pandas.read_csv("E:\\Python\\python_learning\\data\\cibc.csv"))
data = pandas.read_csv("E:\\Python\\python_learning\\data\\cibc.csv")
print(data[0:5][0:2])

print(data.loc[:, ["2026-02-20", '68.48']])
print(data.loc[100:1000, ["2026-02-20", 'PURCHASE INTEREST']])

data = pandas.read_json('E:\\Python\\python_learning\\data\\module3.json')
print(data)
print(data.loc[[1,3],['Title', 'Rating']])
print(data.to_json(orient='records', lines=True))

# xldata = pandas.read_excel('E:\\Python\\python_learning\\data\\D083 Field Operations Area Frac Notifications - Master List.xlsx')
# print(xldata)
# # print(xldata.loc[1:8888,['Well Licence Number', 'Licensee Name', 'BA Code' ]])

# xdata = pandas.read_excel('E:\\Python\\python_learning\\data\\Customer.xlsx')

# print(xdata.loc[0:5, ['Customer Name', 'Customer Type', 'Customer Status']])

import pandas as pd
newurl = "https://catalogue.data.gov.bc.ca/dataset/a96153e2-21a5-4e70-8625-cca770f01fbd/resource/d736a9ac-6aa9-4ff4-91e9-412f383e19b4/download/bc_fin_2021_supplement_estimates.xls"
pd.read_excel(newurl)