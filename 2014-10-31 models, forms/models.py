from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.db import models



def validate_grade(value):
    if value < 0:
        raise ValidationError(u'Grade must be greater than 0')


GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)

class Human(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField(null=True)

    class Meta:
        abstract = True


class Student(Human):
    studying = models.BooleanField(default=True)
    login = models.CharField(max_length=30, blank=True, validators=[validate_slug])
    email = models.EmailField(max_length=254, blank=True)
    grade = models.SmallIntegerField(null=True, validators=[validate_grade])

    def num_of_kids(self):
        return len(self.children)

    class Meta:
        db_table = "students"
        unique_together = ("first_name", "middle_name", "last_name", "date_of_birth")


class Question(models.Model):
    student = models.ForeignKey(Student, related_name="this_guy_stupid_questions", null=True, on_delete=models.SET_NULL)
    question_text = models.CharField(max_length=200, default="I've forgotten my question...")
    date_of_question = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'student'
        db_table = "questions"


class Child(Human):
    student = models.ForeignKey(Student, related_name="children", null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'children'
        verbose_name_plural = 'children'

class Lesson(models.Model):
    students = models.ManyToManyField(Student, through='Attendance') #cause don't created
    title = models.CharField(max_length=100)


class Attendance(models.Model):
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    date = models.DateTimeField(null=True)






