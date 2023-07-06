from django.shortcuts import render, redirect

# Create your views here.
from .models import analysis
from .models import data
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from . forms import DataForm, analysisform, CreateUserForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    data_plot = data.objects.all()
    ana = analysis.objects.all()

    x = [x.which_day for x in data_plot]
    y = [y.happiness_score for y in data_plot]
    z = [z.tasks for z in data_plot]

    
        
    
    if request.method == 'POST':
    
    
        if 'submit-form' in request.POST:

            form = DataForm(request.POST or None)
    
        
            if form.is_valid():
                form.save()

                return redirect('index')


        elif 'submit-form1' in request.POST:
            form1 = analysisform(request.POST)
            if form1.is_valid():
                itemValue = form1.cleaned_data['analysis_day']

                form1.save()

                print(itemValue)
                
                
                

    else:
            
            form = DataForm()

            form1= analysisform()
                
    context = {
        "data_plot":data_plot,
        "form":form,
        "form1":form1,
        'x':x,
        'y':y,
        'z':z,
        

        }
    return render(request, 'chart/pageone.html', context)







def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + user)
            return redirect('login')
    context = {'form':form}



    return render(request,'chart/register.html', context)
    
def loginPage(request):

    if request.method == "POST":
        username =request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request,'chart/login.html')

    return render(request,'chart/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')