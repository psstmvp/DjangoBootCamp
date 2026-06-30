from django.shortcuts import render

from Administrator.models import *
# Create your views here.
def AdminRegistration(request):
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        tbl_admin.objects.create(admin_name=name,
                                 admin_email=email,
                                 admin_contact=contact,
                                 admin_password=password)
        return render(request,'Administrator/AdminRegistration.html')
    else:
        return render(request,'Administrator/AdminRegistration.html')

