import django
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
#Course_T
    df = df.drop_duplicates(subset=["CourseID"])
    data = df.values.tolist()
    for i in data[0:]:
        if pd.isna(i[1])==False:
            course = Course_T(CourseID=i[1], CourseName=i[10],CreditHour=i[4])
            course.save()


#CO_OFFERED_COURSE_T ,  CoOfferedCourseID 
            coList=i[2].split(",")
            for j in coList:
                print(j)

#CO_OFFERED_COURSE_T 

            coList=i[2].split(",")
            for j in coList:

                coCourse=CO_OFFERED_COURSE_T(CourseID=i[1],CoOfferedCourseID=j)
                coCourse.save()


