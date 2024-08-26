from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Course

def get_courses(request):
    courses =list(Course.objects.values('title', 'id'))
    return JsonResponse({'courses': courses})