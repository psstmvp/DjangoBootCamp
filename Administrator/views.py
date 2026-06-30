from django.shortcuts import render,redirect

from Administrator.models import *
# Create your views here.
def AdminRegistration(request):
    ## Select Query 
    admindata = tbl_admin.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        ## Insert Query..
        tbl_admin.objects.create(admin_name=name,
                                 admin_email=email,
                                 admin_contact=contact,
                                 admin_password=password)
        return render(request,'Administrator/AdminRegistration.html',{'admindata':admindata})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'admindata':admindata})

def DeleteAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('Administrator:AdminRegistration')