#from seasapp.models import *
import django
import pandas as pd
import os
from query import *
#from string import digits

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
# # Reading data from excel
# df = pd.read_excel('Tally Sheet For Summer 2021.xlsx', skiprows=3)
# df = df.iloc[:-1]

# data = df.values.tolist()

# count=0
# for i in data:
#     if int(i[6]) in range (1,11):
#         count+=1

# print(count)
# a=iub_revenue(2020,2021,"Spring")
# print(a[0],a[1],a[2])

l = ['1','2','3']
a=3
print([l[i:i+a] for i in range(0, len(l), 3)])

# a = [((1,), (2,), (4,), (5,)), ((10,), (12,), (14,), (15,))]

# for i in a:
#     x = [item for t in i for item in t]
        
#     print(x)
