from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Machine
from .serializers import *
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User, Group
class MachineList(APIView):
    """
    List all todos, or create a new todo.
    """

    def get(self, request, format=None):
        queryset = {}
        user_request = request.user.id
        print(user_request)
        permission_class = (IsAuthenticated,)
        auto = Machine.objects.filter(client_model__user_id=user_request)
        serializer = MachineSerializer(auto, many=True)
        return Response({'Machine': serializer.data} )

    def post(self, request, format=None):
        print(request.data)
        machines = Machine.objects.filter(number_machine=request.data)
        tech_research = TO.objects.filter(car__number_machine=request.data)
        complaints = Complaint.objects.filter(car_complaint__number_machine=request.data)
        group = Group.objects.filter(user=request.user)
        serializer_group = GroupSerializer(group, many=True)
        serializer = MachineSerializer(machines, many=True)
        serializer_TO = TOSerializer(tech_research, many=True)
        serializer_complaint = ComplaintSerializer(complaints, many=True)

        print(request.user)
        if request.user.is_authenticated:
            return Response(
                [{'TO': serializer_TO.data}, {'Machine': serializer.data}, {'UpdateComplaint': serializer_complaint.data}, {'Group': serializer_group.data}])
        else:
            return Response({'Machine': serializer.data[0]})


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
        print(request.query_params)
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


class TOList(APIView):

    def get(self, request, format=None):
        TO_list = TO.objects.all()
        serializer_to = TOSerializer(TO_list, many=True)
        return Response(serializer_to.data)

    def post(self, request, format=None):
        serializer = TOSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'TO': serializer.data})


class ServiceCompanyList(APIView):
    def get(self, request):
        company_list = Service.objects.all()

        serializer_service = ServiceSerializer(company_list, many=True)
        return Response({'Service': serializer_service.data})




class Vidi_TOList(APIView):
    def get(self, request):
        vidi_list =Vidi_TO.objects.all()
        serializer_vidi = ServiceSerializer(vidi_list, many=True)

        return Response({'Vidi_TO': serializer_vidi.data})

class TOApiUpdate(UpdateAPIView):
    queryset = TO.objects.all()
    serializer_class = TOSerializer


class ComplaintList(APIView):
    def post(self, request, format=None):
        serializer = ComplaintSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'UpdateComplaint': serializer.data})


class UselList(APIView):
    def get(self, request):
        usel_list = Usel_Refusal.objects.all()
        serializer_usel = ServiceSerializer(usel_list, many=True)
        return Response({'Usels': serializer_usel.data})

class RecoveryList(APIView):
    def get(self, request):
        recovery_list = Recovery.objects.all()
        serializer_recovery = RecoverySerializer(recovery_list, many=True)
        return Response({'Recovery': serializer_recovery.data})

class ComplaintApiUpdate(UpdateAPIView):
        queryset = Complaint.objects.all()
        serializer_class = ComplaintSerializer

@api_view(['POST'])
def new_machine(request):
    if request.method == 'POST':
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnicList(APIView):
    def get(self, request):
        company_list = Technica.objects.all()

        serializer_service = TechicSerializer(company_list, many=True)
        return Response({'Technic': serializer_service.data})

class EngineList(APIView):
    def get(self, request):
        list = Engine.objects.all()

        serializer_engine = EngineSerializer(list, many=True)
        return Response({'Engine': serializer_engine.data})


class TransimisiaList(APIView):
    def get(self, request):
        company_list = Transmisia.objects.all()

        serializer_service = TransmisiaSerializer(company_list, many=True)
        return Response({'Transmisia': serializer_service.data})


class LeadList(APIView):
    def get(self, request):
        company_list = Lead.objects.all()

        serializer_service = LeadSerializer(company_list, many=True)
        return Response({'Lead': serializer_service.data})


class SteerableBridgeList(APIView):
    def get(self, request):
        company_list = Steerable_Bridge.objects.all()

        serializer_service = SteerableBridgeSerializer(company_list, many=True)
        return Response({'Steerable_bridge': serializer_service.data})


class ClientList(APIView):
    def get(self, request):
        company_list = Client.objects.all()
        serializer_service = ClientSerializer(company_list, many=True)
        return Response({'Clients': serializer_service.data})


class UpdateMachine(UpdateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer