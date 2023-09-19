from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ItemForm, Item
from django.urls import reverse

# Create your views here.

# def show_item()
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Tsabit Coda R', # Nama kamu
        'class': 'PBP C', # Kelas PBP kamu

        'items': items
    }

    return render(request, "main.html", context)

def show_home(request1):
    context = {
        'name': 'Diamonds',
        'date_added': 'Today!',
        'price' : '19$',
        'description' : 'An useful item for purchasing things',
        'date_expired' : '19 December  2023',
        'amount' : '10 MORE !!!'
    }

    return render(request1, "home.html", context)

def create_Item(request):
    message = ''
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_Item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
