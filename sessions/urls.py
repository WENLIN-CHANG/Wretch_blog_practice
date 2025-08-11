from django.urls import path
from . import views

app_name = "sessions"

urlpatterns = [
    path("", views.new, name="new"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
]
