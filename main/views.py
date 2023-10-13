from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ItemForm, Item
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound

# Create your views here.

# def show_item()
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user = request.user)
    context = {
        'name': request.user.username, 
        'items': items,
        'last_login': request.COOKIES['last_login'],
        'pembuat' : 'Tsabit Coda R - PBP C'
    }

    return render(request, "main.html", context)

def create_Item(request):
    # message = ''
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome Gamers! Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.date.today()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def kurang_amount(request,id):
    barang_check = Item.objects.get(pk=id)
    if barang_check.amount > 1:
        barang_check.amount -= 1
        barang_check.save()
    else:
        barang_check.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def tambah_amount(request,id):
    barang_check = Item.objects.get(pk=id)
    barang_check.amount += 1
    barang_check.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def hapus_item(request,id):
    barang_check = Item.objects.get(pk=id)
    barang_check.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_product_json(request):
    data = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', data))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Item(name=name, price=price, description=description,amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def kurang_amount_ajax(request,id):
    barang_check = Item.objects.get(pk=id)
    if barang_check.amount > 1:
        barang_check.amount -= 1
        barang_check.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        barang_check.delete()
    # return HttpResponseRedirect(reverse('main:show_main'))
    return HttpResponse(b"NOT CREATED", status=201)

@csrf_exempt
def tambah_amount_ajax(request,id):
    barang_check = Item.objects.get(pk=id)
    barang_check.amount += 1
    barang_check.save()
    # return HttpResponseRedirect(reverse('main:show_main'))
    return HttpResponse(b"ADD", status=201)

@csrf_exempt
def hapus_item_ajax(request,id):
    barang_check = Item.objects.get(pk=id)
    barang_check.delete()
    return HttpResponseRedirect(reverse('main:show_main'))