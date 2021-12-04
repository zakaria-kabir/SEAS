--Enrolment wise course distribution among the schools
SELECT *
FROM seasapp_department_t AS D INNER JOIN seasapp_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN seasapp_section_t AS S ON CourseID=CourseID_id

WHERE SchoolTitle_id="SETS" AND Semester="Summer" AND Year=2021 AND SectionEnrolled BETWEEN 1 AND 10;
#LIMIT 50;



--
 