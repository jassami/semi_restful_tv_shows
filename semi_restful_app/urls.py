from typing import ValuesView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>', views.show_info),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/new', views.new),
    path('shows/<int:show_id>/destroy', views.destroy),
]
