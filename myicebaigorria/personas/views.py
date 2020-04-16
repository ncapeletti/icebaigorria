from django.shortcuts import render

# Create your views here.
def personas_list(request):
    return render(request, 'personas/personas_list.html', {})