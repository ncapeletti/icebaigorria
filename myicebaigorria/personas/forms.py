from django import forms

from .models import Persons

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persons
        fields = ('idpersona', 'nombre','apellido','observaciones','fechanac',)
        