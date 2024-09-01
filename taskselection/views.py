from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from taskselection.models import Task
from taskselection.serializers import TaskSerializer
from rest_framework.views import APIView
#from channels import Group #Katy doesn't work


def index(request):
    latest_task_list = Task.objects.order_by("code")[:]
    context = {"latest_task_list" : latest_task_list}
    return render(request, "taskselection/index.html", context) #
    #return HttpResponse(latest_task_list)

# def availableTaskList(request, APIView):
#     tasks = Task.objects.filter(sv=None)
#     serializer = TaskSerializer(tasks, many=True)
#     return JsonResponse(serializer.data, safe=False)

