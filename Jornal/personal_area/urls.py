from django.urls import path
from .views import (personal_area,
                    class_creating,
                    student_creating)

urlpatterns = [
    path('', personal_area),
    path('class_creating/', class_creating),
    path('student_creating/', student_creating, name='student_creat'),

]