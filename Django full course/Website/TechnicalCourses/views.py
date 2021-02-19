from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Allcourses


def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('TechnicalCourses/courses.html')
    context={
        'ac':ac,
    }

    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    try:
        course=Allcourses.objects.get(pk=couse_id)
    except Allcourses.DoesNotExits:
        raise Http404("course Not Available")
    return HttpResponse()
