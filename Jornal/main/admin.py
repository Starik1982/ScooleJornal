from django.contrib import admin
from .models import *


class TeacherAdmin(admin.TabularInline):
    model = Teacher
    extra = 0


class TeacherAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Teacher._meta.fields]

    class Meta:
        model = Teacher


admin.site.register(Teacher, TeacherAdmin)


class SubjectAdmin(admin.TabularInline):
    model = Subject
    extra = 0


class SubjectAdmin (admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Subject


admin.site.register(Subject, SubjectAdmin)


class SchoolClassAdmin(admin.TabularInline):
    model = SchoolClass
    extra = 0


class SchoolClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SchoolClass._meta.fields]


    class Meta:
        model = SchoolClass


admin.site.register(SchoolClass, SchoolClassAdmin)

class StudentAdmin(admin.TabularInline):
    model = Student
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


    class Meta:
        model = Student


admin.site.register(Student, StudentAdmin)


class GradesAdmin(admin.TabularInline):
    model = Grades
    extra = 0


class GradesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Grades._meta.fields]

    class Meta:
        model = Grades


admin.site.register(Grades, GradesAdmin)

class StudyPeriodAdmin(admin.TabularInline):
    model = StudyPeriod
    extra = 0


class StudyPeriodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudyPeriod._meta.fields]

    class Meta:
        model = StudyPeriod


admin.site.register(StudyPeriod, StudyPeriodAdmin)

