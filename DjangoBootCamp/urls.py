
from django.urls import path , include

urlpatterns = [

    path('Basics/',include('Basics.urls')),
    path('Administrator/',include('Administrator.urls')),
   
   
]
