from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")


def test(request):
    return render(request, "pages/test.html")

def pricing(request):
    return render(request, "pages/pricing.html")
