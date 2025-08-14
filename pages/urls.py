from django.urls import path
from . import views
from articles.views import index
from .views import AboutView, ContactView

app_name = "pages"

urlpatterns = [
    path("about/", AboutView.as_view(), name="about"),
    path("", index, name="home"),
    path("test/", views.test, name="test"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("pricing/", views.pricing, name="pricing"),
]
