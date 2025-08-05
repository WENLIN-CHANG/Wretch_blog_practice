from django.urls import path
# from .views import about, home, contact
from . import views

app_name = "pages"

urlpatterns = [
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact")
]
