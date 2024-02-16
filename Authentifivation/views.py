from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Authentifivation.models import myUser2,myUser1


# Create your views here.
def home(request):
    return render(request,'index.html')
def registrationPage(request):
    if request.method=='POST':
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']
        password=request.POST['tbPass']

        my_user=myUser1(name=name,email=email,mobile=mobile,password=password)
        my_user.save()


        return render(request,'loginPage.html',{"muser":my_user})
    else:
        return render(request,'registrationPage.html')

    return render(request,'registrationPage.html')
def loginPage(request):
    if request.method=='POST':
        email=request.POST['tbEmail']
        password=request.POST['tbPass']
        myuse=myUser1.objects.filter(email=email,password=password)
        if myuse.exists():
            myuse1=myUser1.objects.get(email=email,password=password)
            return render(request,'successpage.html', {'mydata1': myuse1})
        else:
            messages.error(request,'invalid Details')
            return render(request,'loginPage.html')


    return render(request,'loginPage.html')
def editForm(request):
    id=request.GET['id']
    muser=getOneUSerDetails(id)
    return render(request,'registrationpage.html',{'muser':muser})
def editOneUser(request):
    if request.method=='POST':
        id=request.POST["tbId"]
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']
        password=request.POST['tbPass']

        my_user=myUser1.objects.get(id=id)
        my_user.name=name
        my_user.email=email
        my_user.mobile=mobile
        my_user.password=password
        my_user.save()
        myuse=getOneUSerDetails(id)
        myData1 = myuse
        return render(request,'successpage.html',{'mydata1':myData1})

def getOneUSerDetails(id):
    oneUserDetails=myUser1.objects.get(id=id)
    return oneUserDetails
