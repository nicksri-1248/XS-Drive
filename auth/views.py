from django.views import View
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from auth import forms



# Create your views here.
class Login(LoginView):
    template_name = 'auth/login.html'


class Logout(LogoutView):
    template_name = 'auth/logout.html'

class ContactUs(TemplateView):
    template_name = 'auth/contactus.html'

class Signup(View):
    def get(self, request):
        context = {
            "form": forms.SignUpForm()
        }
        return render(request, 'auth/signup.html', context)

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        context = {
            "form": form
        }
        return render(request, 'auth/signup.html', context)