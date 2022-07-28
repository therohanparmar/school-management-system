from rest_framework import serializers
from .models import *

class ParentSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True,allow_blank=True)
    fname = serializers.CharField(max_length=20,required=False,allow_blank=True)
    lname = serializers.CharField(max_length=20,required=False,allow_blank=True)
    dob = serializers.DateField(required=False)
    mobile_no = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(default=False,required=False)

    class Meta:
        model = Parent
        fields = '__all__'


class TeacherSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    fname = serializers.CharField(max_length=20, required=False,allow_blank=True)
    lname = serializers.CharField(max_length=20, required=False,allow_blank=True)
    dob = serializers.DateField(required = False)
    mobile_no = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(default=False, required=False)

    # class Meta:
    #     model = Teacher
    #     fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    
    section = serializers.CharField(max_length=20,required=False,allow_blank=True)
    is_active = serializers.BooleanField(default=False,required=False)
    remarks = serializers.CharField(max_length = 100,required=False,allow_blank=True)

    class Meta:
        model = Classroom
        fields = ['section','is_active','remarks']


class GradeSerializer(serializers.Serializer):
    
    grade = serializers.CharField(max_length=10,required=False,allow_blank=True)

    class Meta:
        model = Grade
        fields = '__all__'

class StudentSerializer(serializers.Serializer):

    enrollment = serializers.CharField(max_length=50,required=False,allow_blank=True)
    email = serializers.EmailField(max_length=254,required=False,allow_blank=True)
    password = serializers.CharField(max_length=20,required=False,allow_blank=True)
    fname = serializers.CharField(max_length=10,required=False,allow_blank=True)
    lname = serializers.CharField(max_length=10,required=False,allow_blank=True)
    dob = serializers.DateField(required=False)
    mobile_no = serializers.IntegerField(required=False)
    joining_date = serializers.DateField(required=False)
    is_active = serializers.BooleanField(default=False,required=False)

    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.Serializer):
    
    date = serializers.DateField(required=False)
    is_active = serializers.BooleanField(default=False,required=False)
    remarks = serializers.CharField(max_length=100,required=False,allow_blank=True)

    class Meta:
        model = Attendance
        fields = '__all__'



class ClassroomStudentSerializer(serializers.Serializer):
    
    class Meta:
        model = ClassroomStudent
        fields = '__all__'

class ExamTypeSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=15,required=False,allow_blank=True)
    description = serializers.CharField(max_length=100,required=False,allow_blank=True)
    class Meta:
        model = ExamType
        fields = '__all__'


class ChoiceSerializer(serializers.Serializer):
    
    
    sub_cource = serializers.CharField(max_length=20,required=False,allow_blank=True)

    class Meta:
        model = Choice
        fields = '__all__'

class CourseSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=20 ,required=False,allow_blank=True)
    description = serializers.CharField(max_length=100, required=False,allow_blank=True)
    fees = serializers.IntegerField(required=False)

    class Meta:
        model = Course
        fields = '__all__'
   

class ExamSerializer(serializers.Serializer):

    
    title = serializers.CharField(max_length=50, required=False,allow_blank=True)
    # type = serializers.PrimaryKeyRelatedField(many=True,queryset=ExamType.objects.all())
    class Meta:
        model = Exam
        fields = '__all__'    
   

class SubjectSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100,required=False,allow_blank=True)
    code = serializers.IntegerField(required=False)

    class Meta:
        model = Subject
        fields = '__all__'
    
class ExamResultSerializer(serializers.Serializer):
    
    marks = serializers.IntegerField(required=False)
    is_pass = serializers.BooleanField(required=False)

    class Meta:
        model = ExamResult
        fields = '__all__'

class AdminSectionSerializer(serializers.Serializer):
    
    remarks = serializers.CharField(max_length=100,required=False,allow_blank=True)

    class Meta:
        model = ExamResult
        fields = '__all__'
