
from django.urls import path

from . import views

urlpatterns = [
    path("", views.links, name='links'),
    path("search", views.link_search, name='link-search'),
    path("create", views.link_create, name='link-create'),
]