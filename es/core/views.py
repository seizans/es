# coding=utf8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from haystack.query import SearchQuerySet

from core.models import Note


class HomeView(CreateView):
    model = Note
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context

home = HomeView.as_view()


def es(request):
    query = SearchQuerySet().all().models(Note)
    print ''
    print ''
    print ''
    print query
    for r in query:
        print r
    print ''
    print ''
    print ''
    return render(request, 'es.html', {'query': query})
