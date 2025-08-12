from django.urls import path
from . import views
from comments import views as comment_view

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:id>", views.detail, name="detail"),
    path("<int:id>/edit", views.edit, name="edit"),
    path("<int:id>/comments", comment_view.create, name="create_comment"),
    path("<int:id>/like", views.like, name="like"),
]
