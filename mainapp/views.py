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


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_Computer(request):
    return add_item(request, ComputerForm)


def add_IT(request):
    return add_item(request, ITForm)


def add_Mechanical(request):
    return add_item(request, MechanicalForm)


def add_Electronics(request):
    return add_item(request, ElectronicsForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_Computer(request, pk):
    return edit_item(request, pk, Computer, ComputerForm)


def edit_IT(request, pk):
    return edit_item(request, pk, IT, ITForm)


def edit_Mechanical(request, pk):
    return edit_item(request, pk, Mechanical, MechanicalForm)

def edit_Electronics(request, pk):
    return edit_item(request, pk, Electronics, ElectronicsForm)


def delete_Computer(request, pk):

    template = 'index.html'
    Computer.objects.filter(id=pk).delete()

    items = Computer.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_IT(request, pk):

    template = 'index.html'
    IT.objects.filter(id=pk).delete()

    items = IT.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Mechanical(request, pk):

    template = 'index.html'
    Mechanical.objects.filter(id=pk).delete()

    items = Mechanical.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Electronics(request, pk):

    template = 'index.html'
    Electronics.objects.filter(id=pk).delete()

    items = Electronics.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)