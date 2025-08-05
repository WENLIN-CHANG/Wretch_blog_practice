from django.urls import path
# from .views import about, home, contact
from . import views

urlpatterns = [
    path("about/", views.about),
    path("", views.home),
    path("contact/", views.contact)
]
