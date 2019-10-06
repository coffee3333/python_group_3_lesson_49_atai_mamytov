from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.models import Tracker, Type, Status

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trackers'] = Tracker.objects.all()
        return context

class TaskTrackerView(TemplateView):
    template_name = 'TaskTrack.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_track_pk = self.kwargs.get('pk')
        context['tracker'] = get_object_or_404(Tracker, pk=task_track_pk)
        return context