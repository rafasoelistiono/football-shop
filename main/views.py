from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'Football Shop',
        'your_name': 'Rafa Rally Soelistiono',
        'your_class': 'PBP D',
    }
    return render(request, 'main.html', context)
