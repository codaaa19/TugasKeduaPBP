from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Tsabit Coda R',
        'class': 'PBP C'
        # 'item' : ''
    }

    return render(request, "main.html", context)