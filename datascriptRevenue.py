import django
import pandas as pd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *

def populate(filename,sheet_name):
    # Reading data from excel
    df = pd.read_excel(filename, sheet_name=sheet_name)


    # Department_T
    dfdept = df["Dept"]
    data = dfdept.values.tolist()
    for i in data:
        if i == "CSE" or i == "cse" or i == "EEE" or i == "eee" or i == "PhySci" or i == "PHYSCI" or i == "physci" or i == "Physci":
            schooltitlefk = School_T.objects.raw('''
                SELECT SchoolTitle
                FROM seasapp_School_T
                WHERE SchoolTitle = 'SETS';
            ''')
            dept = Department_T(DeptID=i, SchoolTitle=schooltitlefk[0])
            dept.save()

        schooltitlefk1 = School_T.objects.raw('''
            SELECT SchoolTitle
            FROM seasapp_School_T
            WHERE SchoolTitle IN ('SLASS','SBE','SPPH','SELS')
            ORDER BY SchoolTitle;
        ''')
        dept2 = Department_T(DeptID="SBE", SchoolTitle=schooltitlefk1[0])
        dept3 = Department_T(DeptID="SELS", SchoolTitle=schooltitlefk1[1])
        dept4 = Department_T(DeptID="SLASS", SchoolTitle=schooltitlefk1[2])
        dept5 = Department_T(DeptID="SPPH", SchoolTitle=schooltitlefk1[3])
        dept2.save()
        dept3.save()
        dept4.save()
        dept5.save()


    offered_cooffered_set = set()
    #Course_T
    dfcourse = df[["CourseID", "COFFERED_WITH", "Crs",
               "COURSE_NAME", "Dept"]].drop_duplicates()
    data = dfcourse.values.tolist()
    for i in data:
        if pd.isna(i[0]) == False and pd.isna(i[1]) == False:
            coofferedwithlist = i[1].split(',')
            for j in coofferedwithlist:
                coursespair = i[0], j
                offered_cooffered_set.update([coursespair])
                for singlecourse in coursespair:
                    CourseIDfk = Department_T.objects.raw('''
                        SELECT DeptID
                        FROM seasapp_Department_T
                        ORDER BY DeptID;
                    ''')
                    if i[4] == "CSE":
                        dept0course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[0])
                        dept0course.save()
                    elif i[4] == "EEE":
                        dept1course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[1])
                        dept1course.save()
                    elif i[4] == "PhySci":
                        dept2course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[2])
                        dept2course.save()
                    elif i[4] == "SBE":
                        dept3course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[3])
                        dept3course.save()
                    elif i[4] == "SELS":
                        dept4course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[4])
                        dept4course.save()
                    elif i[4] == "SLASS":
                        dept5course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[5])
                        dept5course.save()
                    elif i[4] == "SPPH":
                        dept6course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[6])
                        dept6course.save()
                    else:
                        dept7course = Course_T(
                            CourseID=singlecourse, CourseName=i[3], CreditHour=i[2])
                        dept7course.save()


    # CoOfferedCourse_T
    offered_cooffered_list = list(offered_cooffered_set)
    for k in offered_cooffered_list:
        coursefk1 = Course_T.objects.get(pk=k[0])
        coursefk2 = Course_T.objects.get(pk=k[1])
        coofferedcourse = CoOfferedCourse_T(
        OfferedCourseID=coursefk1, Coofferredwith=coursefk2)
        coofferedcourse.save()


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
    
    
    
    return df