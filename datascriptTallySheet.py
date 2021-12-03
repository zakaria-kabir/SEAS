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
     #Faculty_t
    df = df.drop_duplicates(subset=["FACULTY_FULL_NAME"])
    data = df.values.tolist()
    # print(data)
    for i in data[0:]: 
        facultyID,facultyName = i[11].split("-")
        if pd.isna(facultyID) and pd.isna(facultyName):
            continue
        print(facultyID,facultyName)

    #hello world 11


populatedata('Autumn', '2020')
populatedata('Autumn', '2021')
populatedata('Spring', '2020')
populatedata('Spring', '2021')
populatedata('Summer', '2021')
