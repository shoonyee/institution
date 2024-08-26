from django.urls import path

from . import views

urlpatterns = [
    path("get_courses/", views.get_courses, name="get_courses"),
]
