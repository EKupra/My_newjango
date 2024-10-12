from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description', 'price']
    template_name = 'items/item_form.html'

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description', 'price']
    template_name = 'items/item_form.html'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'items/item_confirm_delete.html'
    success_url = reverse_lazy('item-list')
from django.shortcuts import render

# Create your views here.
