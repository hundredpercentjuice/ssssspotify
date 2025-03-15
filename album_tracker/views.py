from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class albumListView(generic.ListView):
    model = models.album
    form_class = forms.albumForm


class albumCreateView(generic.CreateView):
    model = models.album
    form_class = forms.albumForm


class albumDetailView(generic.DetailView):
    model = models.album
    form_class = forms.albumForm


class albumUpdateView(generic.UpdateView):
    model = models.album
    form_class = forms.albumForm
    pk_url_kwarg = "pk"


class albumDeleteView(generic.DeleteView):
    model = models.album
    success_url = reverse_lazy("album_tracker_album_list")
