from django.shortcuts import render
from .models import Database
# Create your views here.
def Index(request):
    return render(request,'index.html')

def Contact_Info(request):
    if request.method == "POST":
        Firstname = request.POST.get('FirstName')
        Lastname = request.POST.get('LastName')
        Email = request.POST.get('EmailAddress')
        phone_no = request.POST.get('MobileNumber')
        message = request.POST.get('Message')

        # Validate required fields
        if not Firstname:
            return render(request, 'index.html', context={'error': 'First Name is required.'})
        if not Email:
            return render(request, 'index.html', context={'error': 'Email is required.'})
        if not phone_no:
            return render(request, 'index.html', context={'error': 'Phone number is required.'})

        # Save to the database
        obj = Database
        obj.FirstName=Firstname
        obj.LastName=Lastname
        obj.Email_id=Email
        obj.Phone_No=phone_no
        obj.Message=message
        obj.save()

        return render(request, 'index.html', context={'obj': 'Successfully Sent!'})
    return render(request, 'index.html')


# def Contact_Info(request):
#     Firstname = request.POST.get('Firstname')
#     Lastname = request.POST.get('Lastname')
#     Email= request.POST.get('EmailAddress')
#     phone_no= request.POST.get('MobileNumber')
#     message=request.POST.get('Message')
#     obj=Database()
#     obj.FirstName=Firstname
#     obj.LastName=Lastname
#     obj.Email_id=Email
#     obj.Phone_No=phone_no
#     obj.Message=message
#     obj.save()
#     return render(request,'index.html',context={'object':'Successfully Sended!'})