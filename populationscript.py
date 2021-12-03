import django
import pandas as pd
import os
from string import digits

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *

# Reading data from excel
df1 = pd.read_excel('Revenue.xlsx', sheet_name="Data")

def populatedata(sem, year):
    # Reading data from excel
    filename = 'Tally Sheet For '+sem+' '+year+'.xlsx'
    df = pd.read_excel(filename, skiprows=3)


#Room_T
    #df = df.drop_duplicates(subset=["ROOM_ID"])
    dfroom = df[["ROOM_ID", "ROOM_CAPACITY"]]
    data = dfroom.values.tolist()
    for i in data[0:]:
        if pd.isna(i[0])==False:
            room = Room_T(RoomID=i[0], RoomCapacity=i[1])
            room.save()


#School_T
    #df = df.drop_duplicates(subset=["SCHOOL_TITLE"])
    #data = df.values.tolist()
    school1 = School_T(SchoolTitle="SETS", SchoolName="School of Engineering, Technology & Sciences")
    school2 = School_T(SchoolTitle="SLASS", SchoolName="School of Liberal Arts & Social Sciences")
    school3 = School_T(SchoolTitle="SBE", SchoolName="School of Business")
    school4 = School_T(SchoolTitle="SPPH", SchoolName="School of Pharmacy and Public Health")
    school5 = School_T(SchoolTitle="SELS", SchoolName="School of Environment and Life Sciences")
    school1.save()
    school2.save()
    school3.save()
    school4.save()
    school5.save()


#Department_T
    #datascriptRevenue


#Faculty_T
    dffaculty = df["FACULTY_FULL_NAME"]
    data = dffaculty.values.tolist()
    for i in data[0:]:
        if pd.isna(i) == False and i.split('-')[0] != 'T001' and i.split('-')[0] != 'T004':
            Faculty = Faculty_T(FacultyID=int(i.split('-')[0]), FacultyName=i.split('-')[1].translate(str.maketrans('', '', digits)))
            Faculty.save()


# Course_T
    #dfcourse = df[["COFFER_COURSE_ID","COFFERED_WITH", "CREDIT_HOUR", "COURSE_NAME"]]
    #data = dfcourse.values.tolist()
    #for i in data:
        #if pd.isna(i[0]) == False and pd.isna(i[1]) == False:
            #coofferedwithlist=i[1].split(',')
            #for j in coofferedwithlist:
                #coursespair = i[0], j
                #for singlecourse in coursespair:
                    #course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2])
                    #course.save()
    #datascriptRevenue


#CoOfferedCourse_T
    #datascriptRevenue





populatedata('Autumn', '2020')
populatedata('Autumn', '2021')
populatedata('Spring', '2020')
populatedata('Spring', '2021')
populatedata('Summer', '2021')





# Department_T
dfdept = df1["Dept"]
data = dfdept.values.tolist()
for i in data[0]:
    if i[0] == "CSE" or i[0] == "cse" or i[0] == "EEE" or i[0] == "eee" or i[0] == "PhySci" or i[0] == "PHYSCI" or i[0] == "physci" or i[0] == "Physci":
        schooltitlefk = School_T.objects.raw('''
            SELECT SchoolTitle
            FROM seasapp_School_T
            WHERE SchoolTitle = 'SETS';
        ''')
        dept = Department_T(DeptID=i[0], SchoolTitle=schooltitlefk[0])
        dept.save()

schooltitlefk = School_T.objects.raw('''
        SELECT SchoolTitle
        FROM seasapp_School_T
        WHERE SchoolTitle IN ('SLASS','SBE','SPPH','SELS')
        ORDER BY SchoolTitle;
    ''')
dept2 = Department_T(DeptID="SBE", SchoolTitle=schooltitlefk[0])
dept3 = Department_T(DeptID="SELS", SchoolTitle=schooltitlefk[1])
dept4 = Department_T(DeptID="SLASS", SchoolTitle=schooltitlefk[2])
dept5 = Department_T(DeptID="SPPH", SchoolTitle=schooltitlefk[3])
dept2.save()
dept3.save()
dept4.save()
dept5.save()





offered_cooffered_set = set()
# Course_T
dfcourse = df1[["CourseID", "COFFERED_WITH", "Crs", "COURSE_NAME", "Dept"]].drop_duplicates()
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
                    dept0course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[0])
                    dept0course.save()
                elif i[4] == "EEE":
                    dept1course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[1])
                    dept1course.save()
                elif i[4] == "PhySci":
                    dept2course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[2])
                    dept2course.save()
                elif i[4] == "SBE":
                    dept3course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[3])
                    dept3course.save()
                elif i[4] == "SELS":
                    dept4course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[4])
                    dept4course.save()
                elif i[4] == "SLASS":
                    dept5course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[5])
                    dept5course.save()
                elif i[4] == "SPPH":
                    dept6course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2], DeptID=CourseIDfk[6])
                    dept6course.save()
                else:
                    dept7course = Course_T(CourseID=singlecourse, CourseName=i[3], CreditHour=i[2])
                    dept7course.save()
            




# CoOfferedCourse_T
offered_cooffered_list = list(offered_cooffered_set)
for k in offered_cooffered_list:
    coursefk1 = Course_T.objects.get(pk=k[0])
    coursefk2 = Course_T.objects.get(pk=k[1])
    #coofferedcourse = CoOfferedCourse_T(OfferedCourseID=coursefk1, Coofferredwith=coursefk2)
    #coofferedcourse.save()




# Section_T
##faculty is kept null
##SectionCapacity null
#dfsection = df[["Sec", "Semester", "Crs", "Year", "CourseID", "stuNo", "ST_MW", ]].drop_duplicates()
#data = dfcourse.values.tolist()
