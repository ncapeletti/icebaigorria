from django.shortcuts import render
from django.utils import timezone
from .models import Persons


# Create your views here.
def personas_list(request):
    personas = Persons.objects.all
    return render(request, 'personas/personas_list.html', {'personas': personas})

