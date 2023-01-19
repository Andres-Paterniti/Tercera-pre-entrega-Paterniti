from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)


class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)
    email = forms.EmailField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    dni = forms.CharField(max_length=32)
    profesion = forms.CharField(max_length=128)