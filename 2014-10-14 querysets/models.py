from django.db import models

class School(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    school = models.ForeignKey(School)
    name = models.TextField()
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Klass(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Lesson(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    klass = models.ForeignKey(Klass)
    year = models.PositiveSmallIntegerField()
    def __str__(self):
        return " : ".join([self.klass.name, self.teacher.name, self.student.name, str(self.year)])

class Team(models.Model):
    name = models.TextField()
    scored = models.PositiveSmallIntegerField()
    missed = models.PositiveSmallIntegerField()
    def __str__(self):
        return " : ".join([self.name, str(self.scored), str(self.missed)])