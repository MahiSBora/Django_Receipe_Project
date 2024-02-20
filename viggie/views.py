from django.shortcuts import render,redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login_page/")
def home(request):
    return render(request,'home.html')

@login_required(login_url="/login_page/")
def view_receipi(request):
    queryset = Receipe.objects.all()
    if request.method=="POST":
        data = request.POST
        print(data.get("receipe_name"))
        print(data.get("receipe_description"))
        print(request.FILES.get("receipe_img"))
        Receipe.objects.create(receipe_name=data.get("receipe_name"),receipe_description=data.get("receipe_description"),receipe_img=request.FILES.get("receipe_img"))

        return redirect('/viggie')

    if request.GET.get('search_field'):
        filter_item=request.GET.get('search_field')
        queryset = queryset.filter(receipe_name__icontains=filter_item)


    my_dict = {'rr':queryset}
    return render(request,'receipies.html',context=my_dict)

@login_required(login_url="/login_page/")
def delete_item(request,id):
    Receipe.objects.get(id=id).delete()
    return redirect('/viggie')

@login_required(login_url="/login_page/")
def update_item(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method=='POST':
        data = request.POST
        name = data.get('receipe_name')
        desc = data.get('receipe_description')
        img = request.FILES.get('receipe_img')

        queryset.receipe_name= name
        queryset.receipe_description = desc
        queryset.receipe_img = img
        queryset.save()
        print('hoga re le baba')

        return redirect('/viggie')
    else:
        queryset = Receipe.objects.get(id=id)
        my_dict={'iteminfo':queryset}
        return render(request,'update.html',context=my_dict)

@login_required(login_url="/login_page/")
def register(request):

    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        user = User.objects.filter(username=name)
        if user.exists():
            messages.warning(request, "User alrady exists.")
            return redirect('/register')
        user = User.objects.create_user(username=name, email=email)
        user.set_password(raw_password=password)

        user.save()
        messages.success(request,'account created successfully')
        return redirect('/register')
    return render(request,'register.html')

def login_page(request):

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(username=name)
        if not user.exists():
            messages.success(request, 'Invalid user name')
            return redirect("/login_page")

        check_pass = authenticate(username= name , password=password)
        if check_pass is None:
            messages.success(request, 'Invalid password')
            return redirect("/login_page")
        else:
            login(request,user=check_pass)
            return redirect("/viggie")


    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page')