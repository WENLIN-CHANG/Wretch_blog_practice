from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, "pages/home.html")


# FBV
# def about(request):
#     return render(request, "pages/about.html")

# CBV
class AboutView(TemplateView):
    template_name = "pages/about.html"


# def contact(request):
#     return render(request, "pages/contact.html")

class ContactView(TemplateView):
    template_name = "pages/about.html"


def test(request):
    return render(request, "pages/test.html")

def pricing(request):
    return render(request, "pages/pricing.html")
