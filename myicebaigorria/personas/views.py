from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Persons
from .forms import PersonaForm




# Create your views here.
def personas_list(request):
    personas = Persons.objects.all
    return render(request, 'personas/personas_list.html', {'personas': personas})



def persona_new(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persons = form.save(commit=False)
            persons.created_date = timezone.now()
            persons.save()
            personas = Persons.objects.all
            return render(request, 'personas/personas_list.html', {'personas': personas})
            """return redirect('post_detail', pk=post.pk)"""
    else:
        form = PersonaForm()
    return render(request, 'personas/persona_edit.html', {'form': form})  


def persona_edit(request, pk):
    persona = get_object_or_404(Persons, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.created_date = timezone.now()
            persona.save()
            return redirect('persona_detail', pk=persona.pk)
            
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/persona_edit.html', {'form': form})


def persona_detail(request, pk):
    persona = get_object_or_404(Persons, pk=pk)
    return render(request, 'personas/persona_detail.html', {'persona': persona})


