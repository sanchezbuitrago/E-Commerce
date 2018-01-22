from django.shortcuts import render, HttpResponse,redirect
from django.template import loader
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from models import LinkedInUser
from forms import CustomUserCreationForm, LinkedInUserCreationForm


# Create your views here.

def createuserlinkedin(request):
    if request.method == 'POST':
        form = LinkedInUserCreationForm(request.POST)
        if form.is_valid():
            userlinkedin = form.save()
            userlinkedin.save()
            return redirect('/')
        else:
            print "Formulario no valido"
    else:
        form = LinkedInUserCreationForm
        
    template = loader.get_template('usuarios/linkedinuser_form.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context,request))

def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action',None)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        if action == 'login':
            user = authenticate(username=username, password=password)
            if user==None:
                context = {
                    'mensaje':'Usuario o contrasena incorrectos'
                }
                return render(request,'login.html',context)
            else:
                login(request,user)

            return redirect('/productos/')
    context = {}
    return render(request,'login.html',context)

