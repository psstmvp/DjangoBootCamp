from django.shortcuts import render

# Create your views here.

def Sum(request):
    if request.method == "POST":
        num1 = int(request.POST.get("txt_num1"))
        num2 = int(request.POST.get("txt_num2"))
        result = num1+num2
        return render(request,"Basics/Sum.html",{"Result":result})
    else:
        return render(request,"Basics/Sum.html")

        