import django
import pandas as pd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *

def populatedata(sem, year):
    # Reading data from excel
    filename = 'Tally Sheet For '+sem+' '+year+'.xlsx'
    df = pd.read_excel(filename, skiprows=3)

    #Room_T
    df = df.drop_duplicates(subset=["ROOM_ID"])
    data = df.values.tolist()
    for i in data[0:]:
        if pd.isna(i[7])==False:
            room = Room_T(RoomID=i[7], RoomCapacity=i[8])
            room.save()

    #School_T
    #df = df.drop_duplicates(subset=["SCHOOL_TITLE"])
    #data = df.values.tolist()
    school1 = School_T(
    SchoolTitle="SETS", SchoolName="School of Engineering, Technology & Sciences")
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
    #None

    #Section_T
    df = df.drop_duplicates(subset=["SECTION"])
    data = df.values.tolist()
    for i in data[0:]:
        if pd.isna(i[3])==False:
            courseidfk = Course_T.objects.get
            # ('''
        #     SELECT CourseID
        #     FROM seasapp_Course_T
        #     WHERE CourseID='CIS101'
        # ''')
            facultyidfk = Faculty_T.objects.get
        #     ('''
        #     SELECT FacultyID
        #     FROM seasapp_Faculty_T
        # ''')
            section = Section_T(SectionNum=i[3],Year=year,Semester=sem,CourseID=courseidfk,FacultyID=facultyidfk,SectionCapacity=i[5],SectionEnrolled=i[6],StartTime=i[12],
            EndTime=i[13], Day=[14], Blocked=i[9])
            section.save()
            # print(pd)

populatedata('Autumn', '2020')
populatedata('Autumn', '2021')
populatedata('Spring', '2020')
populatedata('Spring', '2021')
populatedata('Summer', '2021')

