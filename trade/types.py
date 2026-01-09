import graphene
from graphene_django import DjangoObjectType
from .models import Student, Course

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("id", "name")
        
class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "age", "course")