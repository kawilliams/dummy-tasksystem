from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from taskselectionPolls.models import Task
from taskselectionPolls.serializers import TaskSerializer
from rest_framework.views import APIView
#from channels import Group #Katy doesn't work


def index(request):
    #latest_task_list = Task.objects.order_by("code")[:20]
    #context = {"latest_task_list" : latest_task_list}
    #return render(request, "tasksystem/index.html", context)
    return HttpResponse("Hello, world. You're at the Katy index.")

# def availableTaskList(request, APIView):
#     tasks = Task.objects.filter(sv=None)
#     serializer = TaskSerializer(tasks, many=True)
#     return JsonResponse(serializer.data, safe=False)

