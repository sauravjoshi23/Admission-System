from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')





@login_required(login_url='login')
def index(request):
	return render(request, 'index.html')

@login_required(login_url='login')
def invalid(request):
    return render(request, 'invalid.html')

@login_required(login_url='login')
def display_Computer(request):
	items = Computer.objects.all()
	context = {
		'items' : items,
		'header' : "Computer Department"
	}
	return render(request, 'index.html', context)

@login_required(login_url='login')
def display_IT(request):
	items = IT.objects.all()
	context = {
		'items' : items,
		'header' : "IT Department"
	}
	return render(request, 'index.html', context)

@login_required(login_url='login')
def display_Mechanical(request):
	items = Mechanical.objects.all()
	context = {
		'items' : items,
		'header' : "Mechanical Department"
	}
	return render(request, 'index.html', context)

@login_required(login_url='login')
def display_Electronics(request):
	items = Electronics.objects.all()
	context = {
		'items' : items,
		'header' : "Electronics Department"
	}
	return render(request, 'index.html', context)

@login_required(login_url='login')
def add_Computer(request):
    if request.method == "POST":
        form = ComputerForm(request.POST)
        data = request.POST.dict()
        name = data.get("name")
        percentage = data.get("percentage")
        status = data.get("status")
        #print(status, name, percentage)
        #print(request.user.id)


        if form.is_valid():
            if status == "Admit" and request.user.id != 2:
                return redirect('invalid')
            else: 
                form.save()
                return redirect('display_Computer')

    else:
        form = ComputerForm()
        return render(request, 'add_new.html', {'form' : form})

@login_required(login_url='login')
def add_IT(request):
    if request.method == "POST":
        form = ITForm(request.POST)
        data = request.POST.dict()
        name = data.get("name")
        percentage = data.get("percentage")
        status = data.get("status")
        #print(status, name, percentage)
        #print(request.user.id)

        if form.is_valid():
            if status == "Admit" and request.user.id != 2:
                return redirect('invalid')
            else: 
                form.save()
                return redirect('display_IT')

    else:
        form = ITForm()
        return render(request, 'add_new.html', {'form' : form})

@login_required(login_url='login')
def add_Mechanical(request):
    if request.method == "POST":
        form = MechanicalForm(request.POST)
        data = request.POST.dict()
        name = data.get("name")
        percentage = data.get("percentage")
        status = data.get("status")
        #print(status, name, percentage)
        #print(request.user.id)

        if form.is_valid():
            if status == "Admit" and request.user.id != 2:
                return redirect('invalid')
            else: 
                form.save()
                return redirect('display_Mechanical')

    else:
        form = MechanicalForm()
        return render(request, 'add_new.html', {'form' : form})

@login_required(login_url='login')
def add_Electronics(request):
    if request.method == "POST":
        form = ElectronicsForm(request.POST)
        data = request.POST.dict()
        name = data.get("name")
        percentage = data.get("percentage")
        status = data.get("status")
        #print(status, name, percentage)
        #print(request.user.id)

        if form.is_valid():
            if status == "Admit" and request.user.id != 2:
                return redirect('invalid')
            else: 
                form.save()
                return redirect('display_Electronics')

    else:
        form = ElectronicsForm()
        return render(request, 'add_new.html', {'form' : form})

@login_required(login_url='login')
def edit_Computer(request, pk):
    item = get_object_or_404(Computer, pk=pk)

    if request.method == "POST":
        form = ComputerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_Computer')
    else:
        form = ComputerForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})

@login_required(login_url='login')
def edit_IT(request, pk):
    item = get_object_or_404(IT, pk=pk)

    if request.method == "POST":
        form = ITForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_IT')
    else:
        form = ITForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})

@login_required(login_url='login')
def edit_Mechanical(request, pk):
    item = get_object_or_404(Mechanical, pk=pk)

    if request.method == "POST":
        form = MechanicalForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_Mechanical')
    else:
        form = MechanicalForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})

@login_required(login_url='login')
def edit_Electronics(request, pk):
    item = get_object_or_404(Electronics, pk=pk)

    if request.method == "POST":
        form = ElectronicsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_Electronics')
    else:
        form = ElectronicsForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})

@login_required(login_url='login')
def delete_Computer(request, pk):

    Computer.objects.filter(id=pk).delete()

    items = Computer.objects.all()

    return redirect('display_Computer')

@login_required(login_url='login')
def delete_IT(request, pk):

    IT.objects.filter(id=pk).delete()

    items = IT.objects.all()

    return redirect('display_IT')

@login_required(login_url='login')
def delete_Mechanical(request, pk):

    Mechanical.objects.filter(id=pk).delete()

    items = Mechanical.objects.all()

    return redirect('display_Mechanical')

@login_required(login_url='login')
def delete_Electronics(request, pk):

    Electronics.objects.filter(id=pk).delete()

    items = Electronics.objects.all()

    return redirect('display_Electronics')
