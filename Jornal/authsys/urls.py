from django.urls import path
from .views import (login,
                    check_in_view,
                    registration,
                    entrance,
                    logout)

urlpatterns = [
    path('check_in/', check_in_view, name='check_in'),
    path('logout/', logout, name='logout'),
    path('entrance/', entrance, name='entrance'),
    path('registration/', registration, name='registration'),
    path('', login),

]