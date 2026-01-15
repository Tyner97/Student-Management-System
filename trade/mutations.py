import graphene
import graphql_jwt
from trade.models import Student, Course
from trade.types import StudentType


class CreateStudent(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
        course_id = graphene.Int(required=True)

    def mutate(self, info, name, age, course_id):
        if age < 0:
            raise Exception("Age cannot be negative")

        course = Course.objects.get(id=course_id)
        student = Student.objects.create(
            name=name,
            age=age,
            course=course
        )
        return CreateStudent(student=student)


class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()

    # JWT mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
