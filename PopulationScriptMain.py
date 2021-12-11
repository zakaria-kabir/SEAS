import django
import pandas as pd
import os
import datascriptRevenue as rev
import datascriptTallySheet as tallysheet
from django.core.exceptions import ObjectDoesNotExist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *


# Delete if exists
School_T.objects.all().delete()
Department_T.objects.all().delete()
Faculty_T.objects.all().delete()
Course_T.objects.all().delete()
CoOfferedCourse_T.objects.all().delete()
Room_T.objects.all().delete()
Section_T.objects.all().delete()

# Reading data from revenue excel
dft1 = tallysheet.populatedata('Spring', '2021')
dft2 = tallysheet.populatedata('Summer', '2021')
dfr = rev.populate('Revenue.xlsx', 'Data')
dft4 = tallysheet.populatedata('Autumn', '2020')
dft3 = tallysheet.populatedata('Autumn', '2021')
dft5 = tallysheet.populatedata('Spring', '2020')



dfr = dfr.rename(columns={"RoomSize": "ROOM_CAPACITY",
                 "Sec": "SECTION", "CourseID": "COFFER_COURSE_ID", "stuNo": "ENROLLED", "Crs": "CREDIT_HOUR", "size": "CAPACITY"})

dataframes = [dft1, dft2, dfr,dft3, dft4, dft5]
dfconcat = pd.concat(dataframes)
dfconcat = dfconcat.astype(object).where(pd.notnull(dfconcat), None)

offered_cooffered_set = set()
#Course_T
dfcourse = dfconcat[["COFFER_COURSE_ID", "COFFERED_WITH", "CREDIT_HOUR",
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



# #Room_T
#     #df = df.drop_duplicates(subset=["ROOM_ID"])
# dfroom = dfconcat[["ROOM_ID", "ROOM_CAPACITY"]]
# data = dfroom.values.tolist()
# for i in data[0:]:
#     if pd.isna(i[0]) == False:
#         room = Room_T(RoomID=i[0], RoomCapacity=i[1])
#         room.save()



# Section_T
# faculty is kept null

dfsection = dfconcat[["SECTION", "Semester", "Year", "COFFER_COURSE_ID",
                      "ENROLLED", "ST_MW", "BLOCKED", "CAPACITY", "STRAT_TIME", "END_TIME", "ROOM_ID"]]
dfsection = dfsection.drop_duplicates(subset=("SECTION", "Semester", "Year", "COFFER_COURSE_ID"))
data = dfsection.values.tolist()

for i in data:
    if pd.isna(i[3])==False:
        secidpk=str(int(i[0])) + " " +i[3]+" "+i[1]+" "+str(int(i[2]))
        courseIDfk=Course_T.objects.get(pk=i[3])
        try:
            rooomIDfk=Room_T.objects.get(pk=i[10])
        except ObjectDoesNotExist:
            rooomIDfk=None

        if str(i[6]).find('B') == 0 or str(i[6]).find('b') == 0:
            i[6] = 'B'
        else:
            i[6] = None

        if str(i[8]).find(':') == -1:
            i[8]=None

        if str(i[9]).find(':') == -1:
            i[9]=None

        section=Section_T(SectionID=secidpk, SectionNum=i[0], CourseID=courseIDfk, Semester=i[1],
                          Year=i[2], SectionEnrolled=i[4], Day=i[5], Blocked=i[6], SectionCapacity=i[7], StartTime=i[8], EndTime=i[9], RoomID=rooomIDfk)
        section.save()
    
    








