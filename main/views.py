from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Diamonds',
        'date_added': 'Today!',
        'price' : '19$',
        'description' : 'An useful item for purchasing things',
        'date_expired' : '19 December  2023',
        'amount' : '10 MORE !!!'
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