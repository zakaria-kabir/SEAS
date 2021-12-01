import django
from numpy.lib.function_base import select
import pandas as pd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *
#Reading data from excel
df = pd.read_excel('Revenue.xlsx', sheet_name="Data")

#Department_T
df = df.drop_duplicates(subset=["Dept"])
data = df.values.tolist()
for i in data[0:16]:
    if i[15] == "CSE" or i[15] == "cse" or i[15] == "EEE" or i[15] == "eee" or i[15] == "PhySci" or i[15] == "PHYSCI" or i[15] == "physci" or i[15] == "Physci":
        schooltitlefk = School_T.objects.raw('''
            SELECT SchoolTitle
            FROM seasapp_School_T
            WHERE SchoolTitle = 'SETS'
        ''')
        dept = Department_T(DeptID=i[15], SchoolTitle=schooltitlefk[0])
        dept.save()


