from django.db import connection
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
import sys
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seas.settings')
import django
django.setup()
from seasapp.models import *

with connection.cursor() as c:
    c.execute('''
    CREATE OR REPLACE VIEW joinedtable AS
    SELECT *
    FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
    ''')


def classroom_requirement_course_offer(Sem, Year):
    #have to change SectionEnrolled -> SectionCapacity->noo neeeedddddd
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*) AS Sections
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 1 AND 10
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 11 AND 20
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 21 AND 30
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 31 AND 35
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 36 AND 40
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 41 AND 50
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 51 AND 55
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable 
        WHERE SectionEnrolled BETWEEN 56 AND 65
        AND semester = "{}"
        AND YEAR ={}


        '''.format(Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year))
        sections=[]
        col = cursor.fetchall()
        for i in col:
            for j in i:
                sections.append(j)
    return (sections)


def enrollment_wise_course_school(School, Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 1 AND 10

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 11 AND 20

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 21 AND 30

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 31 AND 35

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 36 AND 40

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 41 AND 50

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 51 AND 55

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 56 AND 60

        UNION ALL

        SELECT COUNT(*)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled > 60

        '''.format(School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year))

        col = cursor.fetchall()
    return col


def resources_usage(School, Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT SUM(sectionEnrolled) AS Sum
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={}

        UNION ALL

        SELECT AVG(sectionEnrolled)
        FROM joinedtable
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={}

        UNION ALL

        SELECT AVG(roomCapacity)
        FROM joinedtable
        JOIN seasapp_room_t
        ON RoomID_id= RoomID
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={}

        UNION ALL

        SELECT AVG(roomCapacity)-Avg(sectionEnrolled) AS difference
        FROM joinedtable
        JOIN seasapp_room_t
        ON RoomID_id= RoomID
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={}

        UNION ALL

        SELECT ((AVG(roomCapacity)-Avg(sectionEnrolled))/AVG(RoomCapacity))*100 AS percentage
        FROM joinedtable
        JOIN seasapp_room_t 
        ON RoomID_id= RoomID
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={}

        '''.format(School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year))

        row = cursor.fetchall()
    return row


def details_enrollment(School, Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT SectionEnrolled, COUNT(*) AS school
        FROM joinedtable 
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year = {} AND SectionEnrolled BETWEEN 1 AND 100 
        GROUP BY SectionEnrolled
        ORDER BY SectionEnrolled ASC;
        '''.format(School, Sem, Year))

        col = cursor.fetchall()
    return col


def iub_revenue(Yearfrom, Yearto, School):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT Year,Semester,SUM(groupbycredit.sum)
        FROM
            (
                SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
                FROM joinedtable
                WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN {} AND {} AND SchoolTitle_id = "{}"
                GROUP BY Year,Semester,Credithour
            ) AS groupbycredit
        GROUP BY Year,Semester
        ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");
        '''.format(Yearfrom, Yearto, School))

        col = cursor.fetchall()

    return col


def iub_revenue_total(Yearfrom, Yearto):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT Year,Semester,SUM(groupbycredit.sum)
        FROM
            (
                SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
                FROM joinedtable
                WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN {} AND {} AND SchoolTitle_id IN ('SBE', 'SELS', 'SETS', 'SLASS', 'SPPH')
                GROUP BY Year,Semester,Credithour
            ) AS groupbycredit
        GROUP BY Year,Semester
        ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");
        '''.format(Yearfrom, Yearto))

        row = cursor.fetchall()

    return row


def SETS_revenue(Yearfrom, Yearto, Dept):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT Year,Semester,SUM(groupbycredit.sum)
        FROM
            (
                SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
                FROM joinedtable
                WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN {} AND {} AND SchoolTitle_id = "SETS" AND DeptID = "{}"
                GROUP BY Year,Semester,Credithour
            ) AS groupbycredit
        GROUP BY Year,Semester
        ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");
        '''.format(Yearfrom, Yearto, Dept))

        col = cursor.fetchall()

    return col


def roomsizelist():
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT roomcapacity,COUNT(roomcapacity)
        FROM seasapp_room_t
        GROUP BY roomcapacity
        ORDER BY roomcapacity;
        ''')

        col = cursor.fetchall()

    return col
