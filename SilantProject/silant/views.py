from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class MachineList(ListView):
    model = Machine
    template_name = 'flatpages/machine_list.html'
    context_object_name = 'machine'
    paginate_by = 3


