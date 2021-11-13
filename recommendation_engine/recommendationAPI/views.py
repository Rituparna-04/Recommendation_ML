from django.shortcuts import render
from .models import Tblcourseratings, Tblcourseinfo

# Create your views here.

def viewCourseList(request):
    courses = Tblcourseinfo.objects.all().order_by('CourseId')
    return render(request, 'index.html', {'courses': courses})

