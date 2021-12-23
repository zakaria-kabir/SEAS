import django
import pandas as pd
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
import sys
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seas.settings')
import django
django.setup()
from seasapp.models import *

def populate(filename,sheet_name):
    # Reading data from excel
    print(filename)
    df = pd.read_excel(filename, sheet_name=sheet_name)

# Department_T
    dfdept = df["Dept"].drop_duplicates()
    data = dfdept.values.tolist()
    for i in data:
        if i == "CSE" or i == "cse" or i == "EEE" or i == "eee" or i == "PhySci" or i == "PHYSCI" or i == "physci" or i == "Physci":
            schooltitlefk = School_T.objects.raw('''
                SELECT SchoolTitle
                FROM seasapp_School_T
                WHERE SchoolTitle = 'SETS'
            ''')
            dept = Department_T(DeptID=i, SchoolTitle=schooltitlefk[0])
            dept.save()

        schooltitlefk1 = School_T.objects.raw('''
            SELECT SchoolTitle
            FROM seasapp_School_T
            WHERE SchoolTitle IN ('SLASS','SBE','SPPH','SELS')
            ORDER BY SchoolTitle
        ''')
        dept2 = Department_T(DeptID="SBE", SchoolTitle=schooltitlefk1[0])
        dept3 = Department_T(DeptID="SELS", SchoolTitle=schooltitlefk1[1])
        dept4 = Department_T(DeptID="SLASS", SchoolTitle=schooltitlefk1[2])
        dept5 = Department_T(DeptID="SPPH", SchoolTitle=schooltitlefk1[3])
        dept2.save()
        dept3.save()
        dept4.save()
        dept5.save()
    
    
    return df

