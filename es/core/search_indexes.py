# coding=utf8

from celery_haystack.indexes import CelerySearchIndex
from django.utils import timezone
from haystack import indexes

from .models import Note


class NoteIndex(CelerySearchIndex, indexes.INdexable):
    text = indexes.CharField(document=True, use_template=True)

    title = indexes.IntegerField(model_attr='title')
    author = indexes.IntegerField(model_attr='author')

    created = indexes.DateTimeField(model_attr='created')
    updated = indexes.DateTimeField(model_attr='updated')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(updated__lte=timezone.now())
