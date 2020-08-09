from django.shortcuts import render
from .models import ProjectModel

def home(request):
    projects = ProjectModel.objects.all()
    return render(request,'home.html',{'projects':projects})
