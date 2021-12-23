# #from seasapp.models import *
# import django
# import pandas as pd
# import os
# from query import *
# import numpy as np
# #from string import digits
import sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

# django.setup()
# # # Reading data from excel
# # df = pd.read_excel('Tally Sheet For Summer 2021.xlsx', skiprows=3)
# # df = df.iloc[:-1]

# # data = df.values.tolist()

# # count=0
# # for i in data:
# #     if int(i[6]) in range (1,11):
# #         count+=1

# # print(count)
# # a=iub_revenue(2020,2021,"Spring")
# # print(a[0],a[1],a[2])

# # l = ['1','2','3']
# # a=3
# # print([l[i:i+a] for i in range(0, len(l), 3)])

# # a = [((1,), (2,), (4,), (5,)), ((10,), (12,), (14,), (15,))]

# # for i in a:
# #     x = [item for t in i for item in t]

# #     print(x)
# # l = [['1', '2', '3'], ['4', '2', '3']]
# # for i in l:
# #     print(l.index(i))

# # number = 2

# # l = ['1', '2', '3']
# # m = ['1', '2', '4']

# # l.insert(0,m)
# # m=[]
# # print(l)

# lst1 = [1, 3, 5, 7, 9, 11]
# list2 = lst1
# list2.append(6)
# print(list2)
# print(lst1)
# # m = []
# # while lst1 != []:
# #     m.append(lst1[:2])
# #     lst1 = lst1[2:]
# # print(m)
# # B = np.reshape(lst1, (-1, 2))
# # print(B)
def convert(string):
    li = list(string.split(" "))
    return li


str = sys.argv[1]
listoffiles = convert(str)
print()
