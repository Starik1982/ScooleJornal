from django.urls import path
from .views import (login,
                    check_in_view,
                    registration,
                    entrance,
                    logout)

urlpatterns = [
    path('check_in/', check_in_view),
    path('logout/', logout),
    path('entrance/', entrance),
    path('registration/', registration),
    path('', login),

]