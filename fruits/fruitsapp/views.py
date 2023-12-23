from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MyFruit

import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm, LoginForm, AddFruit, UpdateFruit
# Create your views here.

def index(request):
    return render(request, 'fruitsapp/index.html', context={})

def dashboard(request):
    return render(request, 'dashboard.html')

def category(request):
    return render(request, 'fruitsapp/category.html', context={})

def allfruits(request):

    all_fruits = MyFruit.objects.all()
    request.session['previous_url'] = request.get_full_path()
    return render(request, 'fruitsapp/allfruits.html', context={'all_fruits': all_fruits})

def aggregate(request):
    return render(request, 'fruitsapp/aggregate.html', context={})

def multiple(request):
    return render(request, 'fruitsapp/multiple.html', context={})

def dryfruits(request):
    return render(request, 'fruitsapp/dryfruit.html', context={})

def simplefruits(request):
    return render(request, 'fruitsapp/simplefruit.html', context={})

def fleshyfruits(request):
    return render(request, 'fruitsapp/fleshyfruit.html', context={})


# create the register views

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(reverse("login"))
    
    context = {'form': form}

    return render(request, 'fruitsapp/register.html', context)

# login a user
'''
def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect(reverse("register"))

    context = {'form': form}

    return render(request, 'fruitsapp/my-login.html', context)
''' 
 # show all fruits
def show_fruits(request):

    show_fruit = MyFruit.objects.all()
    request.session['previous_url'] = request.get_full_path()
    return render(request, 'fruitsapp/view_fruits.html', {'show_fruit': show_fruit})

# add fruits
def add_fruit(request):

    form = AddFruit()

    if request.method == 'POST':

        form = AddFruit(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('view_fruits')

    return render(request, 'fruitsapp/add_fruit.html', {'form': form})

# show single fruit
def single_fruit(request, pk):

    fruit = MyFruit.objects.get(id=pk)

    return render(request, 'fruitsapp/single_fruit.html', {'fruit': fruit})

# update the fruits information
def update_fruit(request, pk):

    new_fruit = MyFruit.objects.get(id=pk)

    form = UpdateFruit(instance=new_fruit)
    if request.method == "POST":
                    
        form = UpdateFruit(request.POST, request.FILES, instance=new_fruit)
        
        if form.is_valid():
            # check if the image in the form changed
            if 'image' in form.changed_data:
                try:
                    os.remove(new_fruit.image.path)
                except FileNotFoundError:
                    print("File not found:", new_fruit.image.path)
                
                # if os.path.exists(new_fruit.image.path):
                # os.remove(new_fruit.image.path)

            form.save()

            return redirect("go_back")
       

    return render(request, 'fruitsapp/update_fruits.html', {'form': form})        

# to go back to the previous url
def go_back(request):
    previous_url = request.session.get('previous_url', '/')
    return redirect(previous_url)

# logout a user

def user_logout(request):

    auth.logout(request)

    return redirect(reverse("login"))