
import graphene
from core.types import StudentType, CourseType
from core.model import Students,Course
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    students=graphene.List(StudentType)
    courses = graphene.List(CourseType)
    
    @login_required
    def resolve_students(root, info):
        return Student.objects.all()
    
        
    @login_required
    def resolve_courses(root,info):
        return Courses.objects.all()