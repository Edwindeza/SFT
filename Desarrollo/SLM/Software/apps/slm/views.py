from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.slm.models import Cliente
from .forms import ReservaForm


class IndexView(TemplateView):
    template_name = 'index.html'


class ReservaView(FormView):
    template_name = 'reserva.html'
    form_class = ReservaForm
    success_url = reverse_lazy('slm:index')

    def form_valid(self, form):
        reserva = form.save(commit=False)

        nro_doc = form.cleaned_data.get('nro_doc')
        tipo_doc = form.cleaned_data.get('tipo_doc')
        clientes = Cliente.objects.filter(tipo_doc=tipo_doc, nro_doc=nro_doc)

        if clientes.exists():
            cliente = clientes.first()
        else:
            cliente = Cliente.objects.create(tipo_doc=tipo_doc,
                                             nro_doc=nro_doc,
                                             nombres=form.cleaned_data.get('nombres'),
                                             apellido_paterno=form.cleaned_data.get('apellido_paterno'),
                                             apellido_materno=form.cleaned_data.get('apellido_materno'),
                                             distrito=form.cleaned_data.get('distrito'))

            artista_favorito = form.cleaned_data.get('artista_favorito')
            if artista_favorito:
                cliente.artista_favorito = artista_favorito

            genero_favorito = form.cleaned_data.get('genero_favorito')
            if genero_favorito:
                cliente.genero_favorito = genero_favorito

            instrumento_favorito = form.cleaned_data.get('instrumento_favorito')
            if instrumento_favorito:
                cliente.instrumento_favorito = instrumento_favorito

            cliente.save()

        reserva.cliente = cliente
        reserva.save()

        for instrumento in form.cleaned_data.get('instrumentos'):
            reserva.instrumentos.add(instrumento)

        messages.success(self.request, '¡Reserva exitosa!')

        return super(ReservaView, self).form_valid(form)
