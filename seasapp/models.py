from django.db import models

# Create your models here.


class School_T(models.Model):
    SchoolTitle = models.CharField(max_length=5, primary_key=True)
    SchoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.SchoolTitle


class Department_T(models.Model):
    DeptID = models.CharField(max_length=6, primary_key=True)
    DeptName = models.CharField(max_length=50, null=True)
    SchoolTitle = models.ForeignKey(School_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.DeptID


class Faculty_T(models.Model):
    FacultyID = models.IntegerField(primary_key=True)
    FacultyName = models.CharField(max_length=50)
    DeptID = models.ForeignKey(Department_T, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.FacultyID


class Course_T(models.Model):
    CourseID = models.CharField(max_length=7, primary_key=True)
    CourseName = models.CharField(max_length=100)
    CreditHour = models.IntegerField()
    DeptID = models.ForeignKey(Department_T, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseID


class CoOfferedCourse_T(models.Model):
    OfferedCourseID = models.ForeignKey(Course_T, on_delete=models.CASCADE, null=True, related_name="OfferedCourseID")
    Coofferredwith = models.ForeignKey(Course_T, on_delete=models.CASCADE, null=True, related_name="Coofferredwith")

    class Meta:
        unique_together = (("OfferedCourseID", "Coofferredwith"),)


class Room_T(models.Model):
    RoomID = models.CharField(max_length=9, primary_key=True)
    RoomCapacity = models.IntegerField()

    def __str__(self):
        return self.RoomID


class Section_T(models.Model):
    SectionID = models.CharField(max_length=40, primary_key=True)
    SectionNum = models.IntegerField()
    Semester = models.CharField(max_length=6)
    Year = models.IntegerField()
    CourseID = models.ForeignKey(Course_T, on_delete=models.CASCADE)
    FacultyID = models.ForeignKey(Faculty_T, null=True, on_delete=models.CASCADE)
    SectionCapacity = models.IntegerField(null=True)
    SectionEnrolled = models.IntegerField(null=True)
    StartTime = models.TimeField(null=True)
    EndTime = models.TimeField(null=True)
    Day = models.CharField(max_length=10, null=True)
    RoomID = models.ForeignKey(Room_T, null=True, on_delete=models.CASCADE)
    Blocked = models.CharField(max_length=3, null=True)
    #MaxSize = models.IntegerField(null=True)

    class Meta:
        unique_together = (("SectionNum", "Semester", "Year", "CourseID"),)

    def __str__(self):
        return str(self.SectionNum)

class uploadedfiles(models.Model):
    File_to_upload = models.FileField(upload_to='Resources/')


