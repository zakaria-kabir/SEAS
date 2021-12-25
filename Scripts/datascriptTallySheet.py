import django
import pandas as pd
import os
from string import digits

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
import sys
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seas.settings')
import django
django.setup()
from seasapp.models import *


def populatedata(filename):
    # Reading data from excel
    tempfile = filename[0: filename.index(".")]
    #print(filename)
    sem=tempfile.rsplit('_', 2)[1]
    year = tempfile.rsplit('_', 2)[2]
    #print(sem,year)
    df = pd.read_excel(filename, skiprows=3)
    df = df.iloc[:-1]
    df['Semester'] = sem
    df['Year'] = year


# School_T
    #df = df.drop_duplicates(subset=["SCHOOL_TITLE"])
    #data = df.values.tolist()
    school1 = School_T(
        SchoolTitle="SETS", SchoolName="School of Engineering, Technology & Sciences")
    school2 = School_T(SchoolTitle="SLASS",
                       SchoolName="School of Liberal Arts & Social Sciences")
    school3 = School_T(SchoolTitle="SBE", SchoolName="School of Business")
    school4 = School_T(SchoolTitle="SPPH",
                       SchoolName="School of Pharmacy and Public Health")
    school5 = School_T(SchoolTitle="SELS",
                       SchoolName="School of Environment and Life Sciences")
    school1.save()
    school2.save()
    school3.save()
    school4.save()
    school5.save()


#Room_T
    #df = df.drop_duplicates(subset=["ROOM_ID"])
    dfroom = df[["ROOM_ID", "ROOM_CAPACITY"]]
    data = dfroom.values.tolist()
    for i in data[0:]:
        if pd.isna(i[0]) == False:
            room = Room_T(RoomID=i[0], RoomCapacity=i[1])
            room.save()

# #Department_T
#     #datascriptRevenue


# #Faculty_T
    dffaculty = df["FACULTY_FULL_NAME"]
    data = dffaculty.values.tolist()
    for i in data[0:]:
        if pd.isna(i) == False and i.split('-')[0] != 'T001' and i.split('-')[0] != 'T004':
            Faculty = Faculty_T(FacultyID=int(i.split(
                '-')[0]), FacultyName=i.split('-')[1].translate(str.maketrans('', '', digits)))
            Faculty.save()


# Course_T
    # datascriptRevenue


# #CoOfferedCourse_T
    # datascriptRevenue

    return df
