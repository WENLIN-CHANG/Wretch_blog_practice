from django.shortcuts import render

def home(request):
    lottery_num = [1, 3, 5, 7, 9]
    return render(request, "pages/home.html", { "lucky": lottery_num})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
