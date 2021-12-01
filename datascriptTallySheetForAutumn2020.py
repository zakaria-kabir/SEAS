import django
import pandas as pd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seas.settings")

django.setup()
from seasapp.models import *
#Reading data from excel
df = pd.read_excel('Tally Sheet For Autumn 2020.xlsx', skiprows=3)

#Room_T
df = df.drop_duplicates(subset=["ROOM_ID"])
data = df.values.tolist()
for i in data[7:9]:
    room = Room_T(RoomID=i[7], RoomCapacity=i[8])
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
#None

#
