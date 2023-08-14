from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def receipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = data.get('image')

        Receipe.objects.create(name=name, description=description, image=image)

    return render(request, "receipe.html", {"page": "Add Receipe"})


def read_receipe(request):
    receipe = Receipe.objects.all()
    return render(request, "read_receipe.html", {'receipe': receipe, "page": "Receipe List"})


def delete_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/read-receipe')
