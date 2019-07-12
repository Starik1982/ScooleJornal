from django.urls import path
from .views import (personal_area,
                    class_creating,
                    student_creating,
                    class_jornal,
                    grades,
                    load_subject_jornal)

urlpatterns = [
    path('', personal_area, name='personal_area'),
    path('class_creating/', class_creating, name='class_creating'),
    path('student_creating/', student_creating, name='student_creat'),
    path('class_jornal/', class_jornal, name='class_jornal'),
    path('load_subject_jornal/', load_subject_jornal, name='load_subject_jornal'),
    path('grades/', grades, name='grades'),

]