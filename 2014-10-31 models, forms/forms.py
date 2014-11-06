from django.forms import ModelForm, Textarea
from students.models import Student, Lesson

class StudentForm(ModelForm):
    class Meta:
        model = Student
        #fields = ['first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth']
        #fields = '__all__'
        exclude = ['middle_name']
        error_messages = {
            'name': {
                'max_length': "This writer's name is too long."
            },
        }

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        #fields = "__all__"
        widgets = {
            'title': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
