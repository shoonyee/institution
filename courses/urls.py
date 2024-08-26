from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("get_courses", views.get_courses, name="get_courses"),
    path("",
            TemplateView.as_view(template_name="application.html"),
            name="app"
        ),
]