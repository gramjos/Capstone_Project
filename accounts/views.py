from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

# password already in database ?
from django.db import IntegrityError

# use customly created form
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm

def signupaccount(request):
    # first check whether the request received is a GET or POST request
    ## If it is a GET request, it means that it's a user navigating to the signup form via the localhost:8000/accounts/signupaccount URL
    if request.method == 'GET':

        return render(request, 'signupaccount.html', {'form':UserCreateForm})

    # But if it's a POST request, it means that it's a form submission to create a new user, so we move to the else block to create a new user
    else:

        if request.POST['password1'] == request.POST['password2']:  # do enter password and enter password again input boxes is match? 
            
            try : 

                user = User.objects.create_user( request.POST['username'], password= request.POST['password1'])               
                # inserts the new user into the database
                user.save()

                login(request, user)

                return redirect('home')
            
            except IntegrityError :
                return render(request,'signupaccount.html', {'form':UserCreateForm,'error':'Username already taken. Choose new username.'})

        else:
            return render(request, 'signupaccount.html', {'form':UserCreateForm, 'error':'Passwords do not match'})
        
def logoutaccount(request):        
    logout(request)
    return redirect('home')

def loginaccount(request):    

    if request.method == 'GET':
        ## if the user clicks on Login on the navbar – and we render loginaccount.html.
        return render(request, 'loginaccount.html', {'form':AuthenticationForm})

    else:   # POST request

        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])  

        if user is None:   # successful login attempt? - NO!

            return render(request,'loginaccount.html',{'form': AuthenticationForm(), 'error': 'username and password donot match'})

        else:   # successful login attempt? - YES!

            login(request,user)

            return redirect('home')