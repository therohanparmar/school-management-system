
from unicodedata import name
from django.db import models

from sms import constant

# Create your models here.


# Parent Model
class Parent(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.fname


    def get_parent_data (self):
        return ({
            "id":self.id,
            "email":self.email,
            "fname":self.fname,
            "lname":self.lname,
            "dob":self.dob,
            "mobile_no":self.mobile_no,
            "is_active":self.is_active,
        })

# Teacher Model
class Teacher(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.fname;

    def get_teacher_data (self):
        return ({
            "id":self.id,
            "email":self.email,
            "fname":self.fname,
            "lname":self.lname,
            "dob":self.dob,
            "mobile_no":self.mobile_no,
            "is_active":self.is_active,
        })

# classroom Model
class Classroom(models.Model):

    section = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    remarks = models.TextField(max_length=100)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key

    def get_classroom_data (self):
        return ({
            "id":self.id,
            "section":self.section,
            "is_active":self.is_active,
            "remarks":self.remarks,
            "teacher":self.teacher.fname
        })

# Grade Model
class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def get_grade_data (self):
        return ({
            "id": self.id,
            "grade": self.grade
        })


# Exam Type Model
class ExamType(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_examtype_data (self):
        return ({
            "id":self.id,
            "name":self.name,
            "description":self.description
        })

# Choice Model
class Choice(models.Model):
    if name == 'Degree Engineering' or name == 'Diploma Engineering':
        sub_cource = models.CharField(max_length=20, choices=constant.CHOICE_1)      
    elif name == 'B.Sc.':
        sub_cource = models.CharField(max_length=20, choices=constant.CHOICE_1)
    else:
        sub_cource = models.CharField(max_length=20, choices='')
    
    def get_choice_data (self):
        return (
            self.sub_cource
        )
# Course Model   
class Course(Choice,models.Model):

    name = models.CharField(max_length=20, choices=constant.COURSE_CHOICE)
    description = models.TextField()
    fees = models.IntegerField()

    def __str__(self):
        return self.name

    def get_course_data (self):
        return ({
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "fees":self.fees
        })

# Exam Model
class Exam(models.Model):
    type = models.ForeignKey(ExamType, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    
    def get_exam_data (self):
        return ({
            "id":self.id,
            "type":self.type.name,
            "title":self.title,
            "course":self.course.name
        })

# Subject Model
class Subject(models.Model):
    
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)

    def get_subject_data (self):
        return ({
            "id":self.id,
            "name":self.name,
            "code":self.code,
            "course":self.course.name
        })


# Student Model
class Student(models.Model):
    
    enrollment = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    dob = models.DateField(null=True)
    mobile_no = models.IntegerField()
    parent = models.ForeignKey(Parent, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    joining_date = models.DateField() #joining date
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def get_student_data (self):
        return({
            "id":self.id,
            "enrollment":self.enrollment,
            "email":self.email,
            "password":self.password,
            "fname":self.fname,
            "lname":self.lname,
            "dob":self.dob,
            "mobile_no":self.mobile_no,
            "parent":self.parent,
            "joining_date":self.joining_date,
            "course":self.course,
            "subject":self.subject,
            "is_active":self.is_active
        })

# Attendance Model
class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)  #Foreign Key
    is_active = models.BooleanField(default=False)
    remarks = models.TextField()

    def get_attendance_data (self):
        return ({
            "id":self.id,
            "date":self.date,
            "is_active":self.is_active,
            "remarks":self.remarks
        })

# ClassroomStudent Model
class ClassroomStudent(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE) #Foreign Key
    student = models.ForeignKey(Student,  on_delete=models.CASCADE) #Foreign Key

    def get_classroomstudent_data (self):
        return ({
            "id":self.id,
            "classroom":self.classroom.section,
            "student":self.student.fname
        })

# Exam Result Model
class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE) #Foreign Key
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    marks = models.IntegerField()
    is_pass = models.BooleanField()

    def get_examresult_data (self):
        return ({
            "id":self.id,
            "exam":self.exam.name,
            "student":self.subject.fname,
            "course":self.course.name,
            "subject":self.subject.name,
            "marks":self.marks,
            "is_pass":self.is_pass
        })

# Admin Section Model
class AdminSection(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,null=True, blank=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def get_adminsection_data (self):
        return ({
            "id":self.id,
            "student":self.student.fname,
            "course":self.course.name,
            "teacher":self.teacher.fname,
            "remarks":self.remarks
        })
