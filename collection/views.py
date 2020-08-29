from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class CoinsView(ListView):
    model = Coin
    template_name = 'collection/index.html'
    context_object_name = 'coins'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CoinsView, self).get_context_data()
        context['title'] = 'Все монеты'
        return context

class PostByGroup(ListView):
    model = Coin
    template_name = 'collection/index.html'
    context_object_name = 'coins'

    def get_queryset(self):
        return Coin.objects.filter(group__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostByGroup, self).get_context_data()
        context['title'] = 'self.title'
        return context

class CoinDetailView(DetailView):
    model = Coin
    template_name = 'collection/сoinDetailView.html'
    context_object_name = 'coin'

    def get_context_data(self, **kwargs):
        context = super(CoinDetailView, self).get_context_data()
        context['title'] = 'self.title'
        return context