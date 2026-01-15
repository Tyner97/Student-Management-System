import graphene
from trade.types import StudentType, CourseType
from trade.models import Student, Course
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)
    courses = graphene.List(CourseType)

    @login_required
    def resolve_students(self, info):
        return Student.objects.all()

    @login_required
    def resolve_courses(self, info):
        return Course.objects.all()
