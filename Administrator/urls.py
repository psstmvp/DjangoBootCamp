
from django.urls import path , include
from Administrator import views

app_name="Admin"

urlpatterns = [
    path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"),
    path('DeleteAdmin/<int:did>',views.DeleteAdmin,name="DeleteAdmin"),
]
