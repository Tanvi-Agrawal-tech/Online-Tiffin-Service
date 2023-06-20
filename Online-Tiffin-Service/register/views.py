from django.shortcuts import render,redirect
from register.models import registration
# import csv
def index(request):
    # return HttpResponse("t")
    return render(request,'project.html')
    
def registration(request):
    #registration=request.GET.get('registration')
    if request.method =='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        number=request.POST.get('number')
        tiffin_center=request.POST.get('tiffin_center')
        Registration = registration(name =name, address=address, email=email,
         number=number, tiffin_center=tiffin_center)
        Registration.save();
        print('Registration Done')
        return redirect('/')
    else:
        Registration=None



    return render(request,'register.html')
    # return render(request,'register.html')
    
    



    # if request.method=='POST':
    #     dict1=request.POST
    #     with open('studata.csv','a')as csvfile:
    #         wrt=csv.writer(csvfile)
    #         for key,value in dict1.items():
    #             wrt.writerow([key,value])
    # return render(request,'register1.html')
# Create your views here.
