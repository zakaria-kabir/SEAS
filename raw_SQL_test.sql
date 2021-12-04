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