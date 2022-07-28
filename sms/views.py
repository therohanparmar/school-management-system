

from rest_framework.decorators import APIView
from rest_framework.response import Response

from .serializer import *
from .models import *
from .utils import *

'''Function Based API's'''

# Create your views here.

# @api_view(['GET'])

# def get_department(request):
#     department_objs = Department.objects.all()
#     serializer = DepartmentSerializer(department_objs, many = True)

#     return Response({
#         'status': True,
#         'message': 'Department Data Fatched',
#         'data': serializer.data
#     })


# @api_view(['POST'])
# def post_department(request):
#     try:
#         data = request.data
#         serializer = DepartmentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'message' : "Add Department Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
#     })

# @api_view(['POST'])
# def post_department_choice(request):
#     try:
#         data = request.data
#         serializer = DepartmentChoiceSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'message' : "Add Department Choice Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_department(request):
#     try:
#         data = request.data
#         print(data.get('department_id'))
#         if not data.get('department_id'):
#             return Response({
#                 'status': False,
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Department.objects.get(department_id = data.get('department_id'))
#         serializer = DepartmentSerializer(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
#         'data':{}
#     })


# @api_view(['GET'])

# def get_students(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)

#     return Response({
#         'status': True,
#         'message': 'Students Data Fatched',
#         'data': serializer.data
#     })

# @api_view(['POST'])
# def post_student(request):
#     try:
#         data = request.data
#         serializer = StudentSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response({
#                 'status':True,
#                 'message' : "Add Student Successful ",
#                 'data':serializer.data
#             })

#         print(data)
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Something Went Wrong",
#     })

# @api_view(['PATCH'])

# def patch_student(request):
#     try:
#         data = request.data
#         print(data.get('student_id'))
#         if not data.get('student_id'):
#             return Response({
#                 'status': False,
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
#         'data':{}
#     })

# @api_view(['DELETE'])

# def delete_student(request):
#     try:
#         data = request.data
#         print(data.get('student_id'))
#         if not data.get('student_id'):
#             return Response({
#                 'status': False,
#                 'message':'ID is required',
#                 'data' : {}
#             })
#         obj = Student.objects.get(student_id = data.get('student_id'))
#         serializer = Student(obj, data=data,partial=True)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response({
#                 'status':True,
#                 'message' : "Success Data ",
#                 'data':serializer.data
#             })
#         return Response({
#             'status':False,
#             'message' : "Fields Invalid Data ",
#             'data':serializer.errors
#         })
#     except Exception as e:
#         print(e)
#     return Response({
#         'status': False,
#         'message' : "Invalid ID",
#         'data':{}
#     })


'''Class Based API's'''

# Student API (GET, POST, PUT, DELETE)


class StudentAPI(APIView):

    # Student GET Request
    def get(self, request):
        data_obj = Student.objects.filter()
        return Response(create_response([obj.get_student_data() for obj in data_obj], True, 200, "Success"))

    # Student POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = StudentSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, "Invalid Data"))
        student_instance = Student.objects.create(**serializer_instance.validated_data)
        return Response(create_response(student_instance.get_student_data(), True, 201, "Success"))

    # Student PUT Request
    def put(self, request):

        serializer_instance = StudentSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        student_instance = Teacher.objects.filter(
            id=request.data.get('id')).last()

        if not student_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('enrollment'):
            student_instance.fname = serializer_instance.validated_data.get(
                'enrollment')
        if serializer_instance.validated_data.get('fname'):
            student_instance.fname = serializer_instance.validated_data.get(
                'fname')
        if serializer_instance.validated_data.get('lname'):
            student_instance.lname = serializer_instance.validated_data.get(
                'lname')
        if serializer_instance.validated_data.get('email'):
            student_instance.email = serializer_instance.validated_data.get(
                'email')
        if serializer_instance.validated_data.get('password'):
            student_instance.email = serializer_instance.validated_data.get(
                'password')
        if serializer_instance.validated_data.get('mobile_no'):
            student_instance.mobile_no = serializer_instance.validated_data.get(
                'mobile_no')
        if serializer_instance.validated_data.get('parent'):
            student_instance.email = serializer_instance.validated_data.get(
                'parent')
        if serializer_instance.validated_data.get('dob'):
            student_instance.dob = serializer_instance.validated_data.get(
                'dob')
        if serializer_instance.validated_data.get('joining_date'):
            student_instance.email = serializer_instance.validated_data.get(
                'joining_date')
        if serializer_instance.validated_data.get('course'):
            student_instance.email = serializer_instance.validated_data.get(
                'course')
        if serializer_instance.validated_data.get('subject'):
            student_instance.email = serializer_instance.validated_data.get(
                'subject')
        if serializer_instance.validated_data.get('is_active'):
            student_instance.is_active = serializer_instance.validated_data.get(
                'is_active')
        student_instance.save(update_fields=['enrollment', 'fname', 'lname', 'email', 'password',
                              'mobile_no', 'parent', 'dob', 'joining_date', 'course', 'subject', 'is_active'])
        return Response(create_response(student_instance.get_student_data(), True, 200, "Success"))

    # Student DELETE Request

    def delete(self, request):

        serializer_instance = StudentSerializer(data=request.data)
        if not serializer_instance.get('student_id'):
            return Response(create_response({}, False, 400, "ID not available"))

        obj = Student.objects.get(
            student_id=serializer_instance.get('student_id'))
        if serializer_instance.is_valid():
            serializer_instance.delete()
            return Response(create_response(serializer_instance.data, True, 200, 'Success'))
        return Response(create_response(serializer_instance.errors, False, 'Error'))

# Parent API (GET, POST)


class ParentAPI(APIView):

    # Parent GET Request
    def get(self, request):
        data_obj = Parent.objects.filter()
        return Response(create_response([obj.get_parent_data() for obj in data_obj], True, 200, "Success"))

    # Parent POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = ParentSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, "Invalid Data"))
        parent_instance = Parent.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(parent_instance.get_parent_data(), True, 201, "Success"))

    # Parent PUT Request

    def put(self, request):

        serializer_instance = ParentSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        parent_instance = Parent.objects.filter(
            id=request.data.get('id')).last()

        if not parent_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('fname'):
            parent_instance.fname = serializer_instance.validated_data.get(
                'fname')
        if serializer_instance.validated_data.get('lname'):
            parent_instance.lname = serializer_instance.validated_data.get(
                'lname')
        if serializer_instance.validated_data.get('email'):
            parent_instance.email = serializer_instance.validated_data.get(
                'email')
        if serializer_instance.validated_data.get('mobile_no'):
            parent_instance.mobile_no = serializer_instance.validated_data.get(
                'mobile_no')
        if serializer_instance.validated_data.get('dob'):
            parent_instance.dob = serializer_instance.validated_data.get('dob')
        if serializer_instance.validated_data.get('is_active'):
            parent_instance.is_active = serializer_instance.validated_data.get(
                'is_active')
        parent_instance.save(
            update_fields=['fname', 'lname', 'email', 'mobile_no', 'dob', 'is_active'])
        return Response(create_response(parent_instance.get_parent_data(), True, 200, "Success"))


# Teacher API (GET, POST)


class TeacherAPI(APIView):

    # Teacher GET Request
    def get(self, request):
        data_obj = Teacher.objects.filter()
        return Response(create_response([obj.get_teacher_data() for obj in data_obj], True, 200, "Success"))

    # Teacher POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = TeacherSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, "Invalid Data"))
        teacher_instance = Teacher.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(teacher_instance.get_teacher_data(), True, 201, "Success"))

    # Teacher PUT Request
    def put(self, request):

        serializer_instance = TeacherSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        teacher_instance = Teacher.objects.filter(
            id=request.data.get('id')).last()

        if not teacher_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('fname'):
            teacher_instance.fname = serializer_instance.validated_data.get(
                'fname')
        if serializer_instance.validated_data.get('lname'):
            teacher_instance.lname = serializer_instance.validated_data.get(
                'lname')
        if serializer_instance.validated_data.get('email'):
            teacher_instance.email = serializer_instance.validated_data.get(
                'email')
        if serializer_instance.validated_data.get('mobile_no'):
            teacher_instance.mobile_no = serializer_instance.validated_data.get(
                'mobile_no')
        if serializer_instance.validated_data.get('dob'):
            teacher_instance.dob = serializer_instance.validated_data.get(
                'dob')
        if serializer_instance.validated_data.get('is_active'):
            teacher_instance.is_active = serializer_instance.validated_data.get(
                'is_active')
        teacher_instance.save(
            update_fields=['fname''lname', 'email', 'mobile_no', 'dob', 'is_active'])
        return Response(create_response(teacher_instance.get_teacher_data(), True, 200, "Success"))


# Classroom API (GET, POST)


class ClassroomAPI(APIView):

    # Classroom GET Request
    def get(self, request):
        data_obj = Classroom.objects.filter()
        return Response(create_response([obj.get_classroom_data() for obj in data_obj], True, 200, "Success"))

    # Classroom POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid ID'))

        serializer_instance = ClassroomSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        classroom_instance = Classroom.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(classroom_instance.get_classroom_data(), True, 201, "Success"))

    # Class PUT Request
    def put(self, request):

        serializer_instance = ClassroomSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        classroom_instance = Classroom.objects.filter(
            id=request.data.get('id')).last()

        if not classroom_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('section'):
            classroom_instance.fname = serializer_instance.validated_data.get(
                'section')
        if serializer_instance.validated_data.get('remarks'):
            classroom_instance.lname = serializer_instance.validated_data.get(
                'remarks')
        if serializer_instance.validated_data.get('teacher'):
            classroom_instance.email = serializer_instance.validated_data.get(
                'teacher')
        if serializer_instance.validated_data.get('is_active'):
            classroom_instance.is_active = serializer_instance.validated_data.get(
                'is_active')
        classroom_instance.save(
            update_fields=['section', 'remarks', 'teacher', 'is_active'])
        return Response(create_response(classroom_instance.get_classroom_data(), True, 200, "Success"))


# Grade API (GET, POST)


class GradeAPI(APIView):

    # Grade GET Request
    def get(self, request):
        data_obj = Grade.objects.filter()
        return Response(create_response([obj.get_grade_data() for obj in data_obj], True, 200, "Success"))

    # Grade POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = GradeSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        grade_instance = Grade.objects.create(
            **serializer_instance.validated_data)
        print(grade_instance)
        return Response(create_response(grade_instance.get_grade_data(), True, 201, "Success"))

    # Grade PUT Request

    def put(self, request):

        serializer_instance = GradeSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        grade_instance = Grade.objects.filter(id=request.data.get('id')).last()

        if not grade_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('grade'):
            grade_instance.grade = serializer_instance.validated_data.get(
                'grade')
        grade_instance.save(update_fields=['grade'])
        return Response(create_response(grade_instance.get_grade_data(), True, 200, "Success"))

        # return put_req(Grade, GradeSerializer, request)

# Attendance API (GET, POST)


class AttendanceAPI(APIView):

    # Attendance GET Request
    def get(self, request):
        data_obj = Attendance.objects.filter()
        print([obj.get_attendance_data() for obj in data_obj])
        return Response(create_response([obj.get_attendance_data() for obj in data_obj], True, 200, "Success"))

    # Attendance POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = AttendanceSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        attendance_instance = Attendance.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(attendance_instance.get_attendance_data(), True, 201, "Success"))

    # Attendence PUT Request
    def put(self, request):

        serializer_instance = AttendanceSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        attendance_instance = Attendance.objects.filter(
            id=request.data.get('id')).last()

        if not attendance_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('date'):
            attendance_instance.date = serializer_instance.validated_data.get(
                'date')
        if serializer_instance.validated_data.get('student'):
            attendance_instance.student = serializer_instance.validated_data.get(
                'student')
        if serializer_instance.validated_data.get('remarks'):
            attendance_instance.remarks = serializer_instance.validated_data.get(
                'remarks')
        if serializer_instance.validated_data.get('is_active'):
            attendance_instance.is_active = serializer_instance.validated_data.get(
                'is_active')
        attendance_instance.save(
            update_fields=['date', 'student', 'remarks', 'is_active'])
        return Response(create_response(attendance_instance.get_attendance_data(), True, 200, "Success"))


# ClassroomStudent API (GET, POST)
class ClassroomStudentAPI(APIView):

    # Classroom Student GET Request
    def get(self, request):
        data_obj = ClassroomStudent.objects.filter()
        return Response(create_response([obj.get_classroomstudent_data() for obj in data_obj], True, 200, "Success"))

    # ClassroomStudent POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid ID'))

        serializer_instance = ClassroomStudentSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        classroomstudent_instance = ClassroomStudent.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(classroomstudent_instance.get_classroomstudent_data(), True, 201, "Success"))

    # ClassroomStudent PUT Request

    def put(self, request):

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        serializer_instance = ClassroomStudentSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        classroomstudent_instance = ClassroomStudent.objects.filter(
            id=request.data.get('id')).last()

        if not classroomstudent_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('classroom'):
            classroomstudent_instance.classroom = serializer_instance.validated_data.get(
                'classroom')
        if serializer_instance.validated_data.get('student'):
            classroomstudent_instance.student = serializer_instance.validated_data.get(
                'student')
        classroomstudent_instance.save(update_fields=['classroom', 'student'])
        return Response(create_response(classroomstudent_instance.get_classroomstudent_data(), True, 200, "Success"))


# ExamType API (GET, POST)


class ExamTypeAPI(APIView):

    # ExamType GET Request
    def get(self, request):
        data_obj = ExamType.objects.filter()
        return Response(create_response([obj.get_examtype_data() for obj in data_obj], True, 200, "Success"))

    # ExamType POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = ExamTypeSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        examtype_instance = ExamType.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(examtype_instance.get_examtype_data(), True, 201, "Success"))

    # ExamType PUT Request

    def put(self, request):

        serializer_instance = ExamTypeSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        examtype_instance = ExamType.objects.filter(
            id=request.data.get('id')).last()

        if not examtype_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('name'):
            examtype_instance.name = serializer_instance.validated_data.get(
                'name')
        if serializer_instance.validated_data.get('description'):
            examtype_instance.description = serializer_instance.validated_data.get(
                'description')
        examtype_instance.save(update_fields=['name', 'description'])
        return Response(create_response(examtype_instance.get_examtype_data(), True, 200, "Success"))


# Course API (GET, POST)
class CourseAPI(APIView):

    # Course GET Request
    def get(self, request):
        data_obj = Course.objects.filter()
        return Response(create_response([obj.get_course_data() for obj in data_obj], True, 200, "Success"))

    # Course POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = CourseSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        course_instance = Course.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(course_instance.get_course_data(), True, 201, "Success"))

    # Course PUT Request
    def put(self, request):

        serializer_instance = CourseSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        course_instance = Course.objects.filter(
            id=request.data.get('id')).last()

        if not course_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('name'):
            course_instance.name = serializer_instance.validated_data.get(
                'name')
        if serializer_instance.validated_data.get('description'):
            course_instance.description = serializer_instance.validated_data.get(
                'description')
        if serializer_instance.validated_data.get('fees'):
            course_instance.fees = serializer_instance.validated_data.get(
                'fees')
        course_instance.save(update_fields=['name', 'description', 'fees'])
        return Response(create_response(course_instance.get_course_data(), True, 200, "Success"))


#  Exam API (GET, POST)


class ExamAPI(APIView):

    # Exam GET Request
    def get(self, request):
        data_obj = Exam.objects.filter()
        return Response(create_response([obj.get_exam_data() for obj in data_obj], True, 200, "Success"))

    # Exam POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = ExamSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        exam_instance = Exam.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(exam_instance.get_exam_data(), True, 201, "Success"))

    # Exam PUT Request

    def put(self, request):

        serializer_instance = ExamSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        exam_instance = Exam.objects.filter(id=request.data.get('id')).last()

        if not exam_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('type'):
            exam_instance.type = serializer_instance.validated_data.get('type')
        if serializer_instance.validated_data.get('title'):
            exam_instance.title = serializer_instance.validated_data.get(
                'title')
        if serializer_instance.validated_data.get('course'):
            exam_instance.course = serializer_instance.validated_data.get(
                'course')
        exam_instance.save(update_fields=['type', 'title', 'course'])
        return Response(create_response(exam_instance.get_exam_data(), True, 200, "Success"))


#  Subject API (GET, POST)


class SubjectAPI(APIView):

    # Subject GET Request
    def get(self, request):
        data_obj = Subject.objects.filter()
        return Response(create_response([obj.get_subject_data() for obj in data_obj], True, 200, "Success"))

    # Subject POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = SubjectSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        subject_instance = Subject.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(subject_instance.get_subject_data(), True, 201, "Success"))

    # Subject PUT Request

    def put(self, request):

        serializer_instance = SubjectSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        subject_instance = Subject.objects.filter(
            id=request.data.get('id')).last()

        if not subject_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('name'):
            subject_instance.name = serializer_instance.validated_data.get(
                'name')
        if serializer_instance.validated_data.get('code'):
            subject_instance.code = serializer_instance.validated_data.get(
                'code')
        if serializer_instance.validated_data.get('course'):
            subject_instance.course = serializer_instance.validated_data.get(
                'course')
        subject_instance.save(update_fields=['name', 'code', 'course'])
        return Response(create_response(subject_instance.get_subject_data(), True, 200, "Success"))


#  ExamResult API (GET, POST)
class ExamResultAPI(APIView):

    # ExamResult GET Request
    def get(self, request):
        data_obj = ExamResult.objects.filter()
        return Response(create_response([obj.get_examresult_data() for obj in data_obj], True, 200, "Success"))

    # ExamResult POST Request
    def post(self, request):

        if not request.data:
            return Response(create_response({}, False, 400, 'Invalid Data'))

        serializer_instance = ExamResultSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, "Invalid Data"))
        examresult_instance = ExamResult.objects.create(
            **serializer_instance.validated_data)
        return Response(create_response(examresult_instance.get_examresult_data(), True, 201, "Success"))

    # ExamResult PUT Request
    def put(self, request):

        serializer_instance = ExamResultSerializer(data=request.data)

        if not request.data.get('id'):
            return Response(create_response({}, False, 400, 'Invalid ID'))

        if not serializer_instance.is_valid():
            return Response(create_response(serializer_instance.errors, False, 400, 'Error'))

        examresult_instance = ExamResult.objects.filter(
            id=request.data.get('id')).last()

        if not examresult_instance:
            return Response(create_response({}, False, 400, "ID not valid"))
        if serializer_instance.validated_data.get('exam'):
            examresult_instance.exam = serializer_instance.validated_data.get(
                'exam')
        if serializer_instance.validated_data.get('student'):
            examresult_instance.student = serializer_instance.validated_data.get(
                'student')
        if serializer_instance.validated_data.get('course'):
            examresult_instance.course = serializer_instance.validated_data.get(
                'course')
        if serializer_instance.validated_data.get('subject'):
            examresult_instance.subject = serializer_instance.validated_data.get(
                'subject')
        if serializer_instance.validated_data.get('marks'):
            examresult_instance.marks = serializer_instance.validated_data.get(
                'marks')
        if serializer_instance.validated_data.get('is_pass'):
            examresult_instance.is_active = serializer_instance.validated_data.get(
                'is_pass')
        examresult_instance.save(
            update_fields=['exam', 'student', 'course', 'subject', 'marks', 'is_pass'])
        return Response(create_response(examresult_instance.get_examresult_data(), True, 200, "Success"))


#  AdminSection API (GET)

# AdminSection GET Request
class AdminSectionAPI(APIView):

    def get(self, request):
        data_obj = AdminSection.objects.filter()
        return Response(create_response([obj.get_adminsection_data() for obj in data_obj], True, 200, "Success"))
