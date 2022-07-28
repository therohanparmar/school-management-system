from django.contrib import admin
# from .models import *
from sms import models as sms_model

# Register your models here.

admin.site.register(sms_model.Classroom)
admin.site.register(sms_model.Attendance)
admin.site.register(sms_model.ClassroomStudent)
admin.site.register(sms_model.Course)
admin.site.register(sms_model.Exam)
admin.site.register(sms_model.ExamResult)
admin.site.register(sms_model.ExamType)
admin.site.register(sms_model.Grade)
admin.site.register(sms_model.Parent)
admin.site.register(sms_model.Student)
admin.site.register(sms_model.Teacher)
admin.site.register(sms_model.AdminSection)
admin.site.register(sms_model.Subject)
admin.site.register(sms_model.Choice)

# @admin.register(Classroom)
# class ClassroomAdmin(admin.ModelAdmin):
#     list_display = ['classroom_id','year','grade_id','section','status','remarks','teacher_id']

# @admin.register(Grade)
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ['grade_id','grade_name']

# @admin.register(Cource)
# class CourceAdmin(admin.ModelAdmin):
#     list_display = ['cource_id','cource_name','cource_description']

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['student_id','student_email','student_password','student_fname','student_lname','student_date_of_birth','student_mobile_no','parent_id','student_date_of_join','student_status']

# @admin.register(Parent)
# class ParentAdmin(admin.ModelAdmin):
#     list_display = ['parent_id','parent_email','parent_password','parent_fname','parent_lname','parent_date_of_birth','parent_mobile_no','parent_status']

# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ['attendance_date','student_id','attendance_status','attendance_remarks']

# @admin.register(Classroom_Student)
# class Classroom_StudentAdmin(admin.ModelAdmin):
#     list_display = ['classroom_id','student_id']

# @admin.register(Exam_Type)
# class Exam_TypeAdmin(admin.ModelAdmin):
#     list_display = ['exam_type_id','exam_type_name','exam_type_description']

# admin.register(Exam)
# class ExamAdmin(admin.ModelAdmin):
#     list_display = ['exam_id','exam_type_id']

# admin.register(Exam_Result)
# class Exam_ResultAdmin(admin.ModelAdmin):
#     list_display = ['exam_id','student_id','cource_id','exam_result_marks','exam_result_status']

# admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['teacher_id','teacher_email','teacher_password','teacher_fname','teacher_lname','teacher_date_of_birth','teacher_mobile_no','teacher_status']

# admin.register(Department)
# class DepartmentsAdmin(admin.ModelAdmin):
#     list_display = ['department_id','department_name']
