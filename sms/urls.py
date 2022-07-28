from urllib.parse import urlparse
from django.urls import path
from .views import *

urlpatterns = [
    # path('get-department/',get_department,name='get_department'),
    # path('post-department/',post_department,name='post_department'),
    # path('patch-department/',patch_department,name='patch_department'),
    # path('get-students/',get_students,name='get_students'),
    # path('post-student/',post_student,name='post_student'),
    # path('patch-student/',patch_student,name='patch_student'),
    # path('delete8-student/',delete_student,name='delete_student'),
    # path('department/', DepartmentAPI.as_view()),
    path('student/', StudentAPI.as_view()),
    path('parent/', ParentAPI.as_view()),
    path('teacher/', TeacherAPI.as_view()),
    path('classroom/', ClassroomAPI.as_view()),
    path('grade/', GradeAPI.as_view()),
    path('attendance/', AttendanceAPI.as_view()),
    path('classroomstudent/', ClassroomStudentAPI.as_view()),
    path('examtype/', ExamTypeAPI.as_view()),
    path('course/', CourseAPI.as_view()),
    path('exam/', ExamAPI.as_view()),
    path('subject/', SubjectAPI.as_view()),
    path('examresult/', ExamResultAPI.as_view()),
    path('adminsection/', AdminSectionAPI.as_view()),
]