from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse

from todo_list.logic import mail_sending
from .models import list,User
from .forms import ListForm,UserForm
from django.contrib import messages

from django.template.loader import get_template
import time
from todo_list import logic
from django.core.cache import cache
cache.clear()



email="aa"
def welcome(request):
    return render(request, 'welcome.html', {"title": "Home"})
def signup_view(request):
    if request.method == "POST":
        name =request.POST.get("name")
        email = request.POST.get("username")
        mobile = request.POST.get("mobile")
        password= request.POST.get("password")
        conf_password = request.POST.get("confirm_password")
        print(name,email,password,mobile,conf_password)
        if(password==conf_password):
            try:
                user = User(Name=name,Email=email,Mobile=mobile,Password=password)
                user.save()
                messages.success(request, ('sucess'))
                return render(request, 'home.html',{'username':name})
            except Exception as e:
                print(e)
        else:
            messages.success(request, ('password and confirm password not match'))


        return render(request, 'home.html')
def login_view(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User.objects.filter(Email=username).first()
        if user:
            if user.Password==password:
                request.session['user'] = username
                return render(request, 'home.html',{'username':user.Name})

            else:
                return render(request, 'welcome.html', {"error": "invalid password"})
        else:
            return render(request, 'welcome.html', {"error": "Invalid mobile"})
    return render(request, 'welcome.html', {"error": "Invalid mobile"})
def home(request):
    if request.method =='POST':
        # form = ListForm(request.POST or None)
        # if form.is_valid():
        #     form.save()
            all_items = list.objects.all
            messages.success(request, ('Item has been added to List'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})
def Email_Subscription(request):
    if request.method == "POST":
        mail =request.POST.get("mail")
        all_items = list.objects.all
        task_list = []
        for m in list.objects.filter(completed="False"):
            task_list.append(m.item)
        try:
            #subsciption = mail_id(mail=mail)
            #subsciption.save()
            #mail_sending(subsciption.mail,task_list)
            # boom = 59
            # while boom > 0:
            #     time.sleep(1)
            #     print(boom)
            #     boom -= 1
            messages.success(request, ('Email subscription is sucessfully activated'))
            return render(request, 'home.html', {'all_items': all_items})
        
        except:
            return HttpResponse("Something went wrong with database")
    else:
        all_items = list.objects.all 
        return render(request, 'home.html', {'all_items': all_items})
    boom = 59
    while boom > 0:
        time.sleep(1)
        print(boom)
        boom -= 1


def delete(request,list_id):
    item =list.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item Has Been Deleted"))
    return redirect('home')
def cross_off(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed =True
    item.save()
    return redirect('home')

def Uncross(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed =False
    item.save()
    return redirect('home')
def edit(request,list_id):
    if request.method =='POST':
        item = list.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to List'))
            return redirect('home')
    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})