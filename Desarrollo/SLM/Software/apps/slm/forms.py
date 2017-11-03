from django import forms

from apps.common.models import Distrito
from .models import Reserva, InstrumentoRegistrado, Local, TipoDocumento, GeneroMusical, Instrumento


class ReservaForm(forms.ModelForm):

    fecha_reserva = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        })
    )
    hora_inicio = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'timepicker',
            'id': 'hora_inicio'
        })
    )
    hora_fin = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'timepicker',
            'id': 'hora_fin'
        })
    )
    instrumentos = forms.ModelMultipleChoiceField(
        required=False,
        queryset=InstrumentoRegistrado.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2'
        })
    )
    cantidad_personas = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })
    )
    local = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        empty_label='Seleccione un local'
    )
    # Campos de usuarios en caso sea la primera vez que se registra, solo el numero de identidad y
    # el tipo son requeridos
    nombres = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    apellido_paterno = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    apellido_materno = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    tipo_doc = forms.ModelChoiceField(
        required=False,
        queryset=TipoDocumento.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    nro_doc = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    distrito = forms.ModelChoiceField(
        required=False,
        queryset=Distrito.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    genero_favorito = forms.ModelChoiceField(
        required=False,
        queryset=GeneroMusical.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    instrumento_favorito = forms.ModelChoiceField(
        required=False,
        queryset=Instrumento.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    artista_favorito = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'hora_inicio', 'hora_fin', 'cantidad_personas', 'local']
