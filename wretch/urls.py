from django.contrib import admin
from django.urls import path, include
from pages.views import about, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path('articles/', include("articles.urls"))
]