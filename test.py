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
# print(resources_usage("SBE", "Spring", 2020))



s = ["B-", "b-0",'B',"-1","0"]

for i in s:

    if i.find('B') == -1 and i.find('b') == -1:
        i='B'
    else:
        i=None
    print(i)
