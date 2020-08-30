from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class CoinsView(ListView):
    model = Coin
    template_name = 'collection/index.html'
    context_object_name = 'coins'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CoinsView, self).get_context_data()
        context['title'] = 'Монеты.РУ'
        return context

class PostByGroup(ListView):
    model = Coin
    template_name = 'collection/index.html'
    context_object_name = 'coins'

    def get_queryset(self):
        return Coin.objects.filter(group__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostByGroup, self).get_context_data()
        context['title'] = Group.objects.get(slug=self.kwargs['slug'])
        return context

class CoinDetailView(DetailView):
    model = Coin
    template_name = 'collection/сoinDetailView.html'
    context_object_name = 'coin'

    def get_context_data(self, **kwargs):
        context = super(CoinDetailView, self).get_context_data()
        context['title'] = Coin.objects.get(slug=self.kwargs['slug'])
        return context

class Search(ListView):
    template_name = 'collection/index.html'
    context_object_name = 'coins'

    def get_queryset(self):
        return Coin.objects.filter(title__icontains=self.request.GET.get('s')) #Достаем данные из первичной модели по данным из вторичной модели

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context