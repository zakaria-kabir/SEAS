import django
import pandas as pd
import os
import datascriptRevenue as rev

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *



# Reading data from revenue excel
df = rev.populate('Revenue.xlsx', 'Data')

# Section_T
# faculty is kept null
# SectionCapacity null
dfsection = df[["Sec", "Semester", "Year", "CourseID",
                "stuNo", "ST_MW", "size", "BLOCKED"]].drop_duplicates()
data = dfsection.values.tolist()
for i in data:
    secidpk = "Sec " + str(i[0]) + " "+i[3]+" "+i[1]+" "+str(i[2])
    # print(secidpk)
    courseIDfk = Course_T.objects.get(pk=i[3])
    if str(i[7]).find('B') == 0 or str(i[7]).find('b') == 0:
        i[7] == 'B'
    else:
        i[7] == ""
    section = Section_T(SectionID=secidpk, SectionNum=i[0], CourseID=courseIDfk, Semester=i[1],
                        Year=i[2], SectionEnrolled=i[4], MaxSize=i[6], Day=i[5], Blocked=i[7])
    section.save()




def populatedata(sem, year):
    # Reading data from excel
    filename = 'Tally Sheet For '+sem+' '+year+'.xlsx'
    df = pd.read_excel(filename, skiprows=3)
    # Section_T
    ##faculty is kept null
    ##SectionCapacity null
    dfsection = df[["Sec", "Semester", "Crs", "Year", "CourseID", "stuNo", "ST_MW", ]].drop_duplicates()
    data = dfcourse.values.tolist()







populatedata('Autumn', '2020')
populatedata('Autumn', '2021')
populatedata('Spring', '2020')
populatedata('Spring', '2021')
populatedata('Summer', '2021')
