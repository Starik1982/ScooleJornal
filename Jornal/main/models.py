from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class StudyPeriod(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    start = models.DateField(default=timezone.now, auto_now=False)
    end = models.DateField(default=timezone.now, auto_now=False)
    class Meta:
        verbose_name = 'Четверть'
        verbose_name_plural = 'Четверті'

    def __str__(self):
        return "%s" % (self.title)



class Subject(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

    def __str__(self):
        return "%s" % (self.title)


class SchoolClass(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    year_of_creation = models.DateField(default=timezone.now, auto_now=False)
    class Meta:
        verbose_name = 'Клас'
        verbose_name_plural = 'Класи'

    def __str__(self):
        return "%s" % (self.title)


class Teacher(models.Model):
    foto = models.ImageField(upload_to='images/', blank=True, null=True, default=None,
                               height_field=400, width_field=240)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    second_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    patronymic = models.CharField(max_length=64, blank=True, null=True, default=None)
    class Meta:
        verbose_name = 'Вчитель'
        verbose_name_plural = 'Вчителі'

    def __str__(self):
        return "%s %s %s" % (self.second_name, self.first_name, self.patronymic)


class Student(models.Model):
    foto = models.ImageField(upload_to='images/', blank=True, null=True, default=None,
                               height_field=400, width_field=240)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    school_class = models.ForeignKey(SchoolClass, blank=True, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    second_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    patronymic = models.CharField(max_length=64, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Учень'
        verbose_name_plural = 'Учні'

    def __str__(self):
        return "%s %s %s" % (self.second_name, self.first_name, self.patronymic)



class Grades(models.Model):
    grades = models.CharField(max_length=12, blank=True, null=True, default=None)
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, default=1, blank=True, null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL)
    school_class = models.ForeignKey(SchoolClass, blank=True, null=True, on_delete=models.SET_NULL)
    lesson_date = models.DateField(default=timezone.now, auto_now=False)


    class Meta:
        verbose_name = 'Оцінка'
        verbose_name_plural = 'Оцінки'


    def __str__(self):
        return "%s" % (self.grades)
