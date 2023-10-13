from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Machine
from .serializers import MachineSerializer, TOSerializer, ComplaintSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import *
from rest_framework.permissions import IsAuthenticated

class MachineList(APIView):
    """
    List all todos, or create a new todo.
    """

    def get(self, request, format=None):
        todos = Machine.objects.all()
        serializer = MachineSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        machines = Machine.objects.filter(number_machine=request.data)
        tech_research = TO.objects.filter(car__number_machine=request.data)
        complaints = Complaint.objects.filter(car_complaint__number_machine=request.data)
        print(complaints)
        print(request.user)
        serializer = MachineSerializer(machines, many=True)
        serializer_TO = TOSerializer(tech_research, many=True)
        serializer_complaint = ComplaintSerializer(complaints, many=True)

        print(request.user)
        if request.user.is_authenticated:
            return Response([{'TO': serializer_TO.data}, {'Machine': serializer.data}, {'Complaint': serializer_complaint.data}])
        else:
            return Response({'Machine': serializer.data})


class MachineDetail(APIView):
    """
    Retrieve, update or delete a todo instance.
    """

    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = MachineSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = MachineSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def user(request):
    return Response({
        'data': UserSerializer(request.user).data
    })