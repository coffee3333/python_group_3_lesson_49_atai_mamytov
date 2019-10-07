from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm

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


class TaskTrackerCraeteView(View):
    def get(self, request, *args, **kwargs):
        form = TrackerForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            Tracker.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


class TaskTrackerUpdateView(View):
    def get(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        form = TrackerForm(data = {
            'summary':task_tracker.summary,
            'description':task_tracker.description,
            'status':task_tracker.status,
            'type':task_tracker.type
        })
        context = {
            'task_tracker': task_tracker,
            'form': form
        }
        return render(request, 'update.html', context)

    def post(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            task_tracker.summary = request.POST.get('summary')
            task_tracker.description = request.POST.get('description')
            task_tracker.Status = request.POST.get('status')
            task_tracker.Type = request.POST.get('type')
            task_tracker.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'task_tracker': task_tracker, 'form': form})

    def get_odject(self, pk):
        task_tracker = get_object_or_404(Tracker, pk = pk)
        return task_tracker



# def article_update_view(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'update.html', context={'article': article})
#     elif request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.author = request.POST.get('author')
#         article.text = request.POST.get('text')
#
#         errors = {}
#         if not article.title:
#             errors['title'] = 'Title should not be empty!'
#         elif len(article.title) > 200:
#             errors['title'] = 'Title should be 200 symbols or less!'
#
#         if not article.author:
#             errors['author'] = 'Author should not be empty!'
#         elif len(article.author) > 40:
#             errors['author'] = 'Author should be 40 symbols or less!'
#
#         if not article.text:
#             errors['text'] = 'Text should not be empty!'
#         elif len(article.text) > 3000:
#             errors['text'] = 'Text should be 3000 symbols or less!'
#
#         if len(errors) > 0:
#             return render(request, 'update.html', context={
#                 'errors': errors,
#                 'article': article
#             })
#
#         article.save()
#         return redirect('article_view', pk=article.pk)

# def book_create_view(request, *args, **kwargs):
#     if request.method == 'GET':
#         form = BookForm()
#         return render(request, 'create.html', context={'form': form})
#     elif request.method == 'POST':
#         form = BookForm(data=request.POST)
#         if form.is_valid():
#             Books.objects.create(
#                 name_author=form.cleaned_data['name_author'],
#                 mail_author=form.cleaned_data['mail_author'],
#                 entry=form.cleaned_data['entry']
#             )
#             return redirect('index')
#         else:
#             return render(
