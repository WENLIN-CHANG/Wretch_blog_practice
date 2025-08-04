from django.shortcuts import render

def home(request):
    lottery_num = [1, 3, 5, 7, 9]
    return render(request, "home.html", { "lucky": lottery_num})


def about(request):
    return render(request, "about.html")
