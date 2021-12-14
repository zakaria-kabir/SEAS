--Enrolment wise course distribution among the schools
SELECT *
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id

WHERE SchoolTitle_id="SETS" AND Semester="Summer" AND Year=2021 AND SectionEnrolled BETWEEN 1 AND 10;
#LIMIT 50;



-- ClassSize
SELECT COUNT(*)
FROM seasapp_section_t 
WHERE SectionCapacity BETWEEN 1 AND 10
AND semester = "Summer"
AND YEAR =2021;
 ---- usage of the resources spring table
 SELECT AVG(RoomCapacity) AS Spring
FROM seasapp_room_t, seasapp_section_t
WHERE Semester = "Spring"

UNION

SELECT AVG(SectionEnrolled)
FROM  seasapp_section_t
WHERE Semester = "Summer"

UNION
 
SELECT AVG(RoomCapacity)- AVG(SectionEnrolled)  
FROM seasapp_room_t, seasapp_section_t
UNION

SELECT (( AVG(RoomCapacity)- AVG(SectionEnrolled))/AVG(RoomCapacity))*100
FROM seasapp_room_t, seasapp_section_t

-- Enrolment table for every school
SELECT SectionEnrolled, COUNT(*) AS SBE
FROM seasapp_course_t c 
INNER JOIN seasapp_department_t d ON c.DeptID_id = d.DeptID
INNER JOIN seasapp_school_t s ON s.SchoolTitle = d.SchoolTitle_id 
INNER JOIN seasapp_section_t sec ON sec.CourseID_id = c.CourseID 
WHERE Schooltitle ="SBE" AND Semester="Spring" AND SectionEnrolled BETWEEN 1 AND 10
GROUP BY SectionEnrolled
HAVING SectionEnrolled > 0
ORDER BY SectionEnrolled ASC;
 -- For checking 
--  SELECT* FROM seasapp_course_t c
-- INNER JOIN seasapp_department_t d ON c.DeptID_id = d.DeptID
-- INNER JOIN seasapp_school_t s ON s.SchoolTitle = d.SchoolTitle_id 
-- INNER JOIN seasapp_section_t sec ON sec.CourseID_id = c.CourseID 
-- WHERE SectionEnrolled = "10" AND Semester="Spring" AND SchoolTitle="SBE"


-- IUB available resources
SELECT RoomCapacity AS ClassSize, Count(*) AS IUB_Resourse , RoomCapacity*Count(*) AS Capacity
FROM seasapp_section_t S INNER JOIN seasapp_room_t R ON S.RoomID_id = R.RoomID
GROUP BY RoomCapacity 
ORDER BY RoomCapacity ;


----- Enrollmentwise Capacity
SELECT Count(SectionNum)
FROM seasapp_section_t
where SectionEnrolled between 1 and 10  11 and 20
------ availability of course offering comparison
Select Count(*)
FROM (Select RoomId
FROM (seasapp_section_t sec INNER JOIN seasapp_room_t r ON sec.RoomID_id = r.RoomID)
where RoomCapacity BETWEEN 20 AND 30 AND Year BETWEEN 2020 AND 2021 
GROUP BY RoomId) AS Room

-- IUB AVAILABLE RESOURCES (part 1)
SELECT s.schoolTitle,SUM(sectionEnrolled)
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021;

--FOR AVERAGE

SELECT s.schoolTitle,AVG(sectionEnrolled)
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021;

--AVG ROOM CAPACITY

SELECT s.schoolTitle,roomID,AVG(roomCapacity)
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021;











--DIFFERENCE

SELECT s.schoolTitle,roomID,AVG(roomCapacity)-Avg(sectionEnrolled) AS difference
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021;

PERCENTAGE

SELECT s.schoolTitle,roomID,(AVG(roomCapacity)-Avg(sectionEnrolled))*100/AVG(RoomCapacity) AS percentage
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SLASS"
AND semester = "Spring"
AND YEAR =2021;
ORDER BY RoomCapacity ;


SELECT SUM(groupbycredit.sum)
FROM 
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum
FROM (seasapp_section_t AS S INNER JOIN seasapp_course_t AS C ON CourseID_id=CourseID)
WHERE Semester="Summer" AND Year=2021 AND DeptID_id="SBE"
GROUP BY CreditHour) AS groupbycredit;



------WORKED---- IUB AVAILABLE RESOURSCES


SELECT SUM(sectionEnrolled) AS RESULTS
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021

UNION
SELECT AVG(sectionEnrolled)
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021
UNION
SELECT AVG(roomCapacity)
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021

UNION

SELECT AVG(roomCapacity)-Avg(sectionEnrolled) AS difference
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021

UNION

SELECT (AVG(roomCapacity)-Avg(sectionEnrolled))*100/AVG(RoomCapacity) AS percentage
FROM seasapp_course_t c
JOIN seasapp_department_t d
ON c.DeptID_id = d.DeptID
JOIN seasapp_school_t s
ON d.SchoolTitle_id = s.SchoolTitle
JOIN seasapp_section_t sec
ON c.CourseID = sec.CourseID_id
JOIN seasapp_room_t r
ON sec.RoomID_id= r.RoomID
WHERE s.schoolTitle = "SBE"
AND semester = "Spring"
AND YEAR =2021;



--------------------------- 
SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                              INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SETS"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");

-----------------------

SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                             INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SETS" AND DeptID = "CSE"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");



--------------------------------------------------------
SELECT *
FROM (
SELECT *
FROM
(SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                             INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SBE"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn")) AS Something S INNER JOIN

SELECT *
FROM
(SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                             INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SETS"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn")) AS NOTHING N
ON S.Semseter = N.Semester) AS EVERYTHING




-- ================================================================================================================================

SELECT *
FROM (
SELECT *
FROM
(SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                             INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SBE"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn")) AS Something INNER JOIN
SELECT *
FROM
(SELECT Year,Semester,SUM(groupbycredit.sum)
FROM
(SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                             INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id
WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id = "SETS"
GROUP BY Year,Semester,Credithour) AS groupbycredit
GROUP BY Year,Semester
ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn")) AS NOTHING
ON S.Semseter = N.Semester) AS EVERYTHING


-- ==================Total revenue cal======
 SELECT Year,Semester,SUM(groupbycredit.sum)
        FROM
            (
                SELECT COUNT(*),credithour, SUM( SectionEnrolled), credithour*SUM( SectionEnrolled) AS sum, Semester,year
                FROM joinedtable
                WHERE Semester IN ("Spring","AUTUMN","SUMMER") AND Year BETWEEN 2009 AND 2021 AND SchoolTitle_id IN ("SBE", "SLASS", "SETS", "SELS", "SPPH")
                GROUP BY Year,Semester,Credithour
            ) AS groupbycredit
        GROUP BY Year,Semester
        ORDER BY Year, FIELD (Semester,"Spring","Summer","Autumn");

