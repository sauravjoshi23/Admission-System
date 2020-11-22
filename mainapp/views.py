from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index(request):
	return render(request, 'index.html')

def display_Computer(request):
	items = Computer.objects.all()
	context = {
		'items' : items,
		'header' : "Computer Department"
	}
	return render(request, 'index.html', context)

def display_IT(request):
	items = IT.objects.all()
	context = {
		'items' : items,
		'header' : "IT Department"
	}
	return render(request, 'index.html', context)

def display_Mechanical(request):
	items = Mechanical.objects.all()
	context = {
		'items' : items,
		'header' : "Mechanical Department"
	}
	return render(request, 'index.html', context)

def display_Electronics(request):
	items = Electronics.objects.all()
	context = {
		'items' : items,
		'header' : "Electronics Department"
	}
	return render(request, 'index.html', context)


def add_Computer(request):
    if request.method == "POST":
        form = ComputerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_Computer')

    else:
        form = ComputerForm()
        return render(request, 'add_new.html', {'form' : form})


def add_IT(request):
    if request.method == "POST":
        form = ITForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_IT')

    else:
        form = ITForm()
        return render(request, 'add_new.html', {'form' : form})


def add_Mechanical(request):
    if request.method == "POST":
        form = MechanicalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_Mechanical')

    else:
        form = MechanicalForm()
        return render(request, 'add_new.html', {'form' : form})


def add_Electronics(request):
    if request.method == "POST":
        form = ElectronicsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_Electronics')

    else:
        form = ElectronicsForm()
        return render(request, 'add_new.html', {'form' : form})


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


def delete_Computer(request, pk):

    Computer.objects.filter(id=pk).delete()

    items = Computer.objects.all()

    return redirect('display_Computer')


def delete_IT(request, pk):

    IT.objects.filter(id=pk).delete()

    items = IT.objects.all()

    return redirect('display_IT')


def delete_Mechanical(request, pk):

    Mechanical.objects.filter(id=pk).delete()

    items = Mechanical.objects.all()

    return redirect('display_Mechanical')


def delete_Electronics(request, pk):

    Electronics.objects.filter(id=pk).delete()

    items = Electronics.objects.all()

    return redirect('display_Electronics')