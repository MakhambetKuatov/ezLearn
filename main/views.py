from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'main/home.html')


def lessons(request):
    return render(request, 'main/lessons.html')


def profile(request):
    return render(request, 'main/profile.html')


def product(request):
    return render(request, 'main/product.html')