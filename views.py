from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from HR_App.models import UserType


class IndexView(TemplateView):
    template_name='index.html'

class LoginView(TemplateView):
    template_name = 'login.html'
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        password = request.POST['password']
        users = authenticate(username=username,password=password)
        if users is not None:
            login(request,users)
            if users.last_name == '1':
                if users.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=users.id).type == "trainee":
                    return redirect('/trainee')
                else:
                    return redirect('/mentor')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})