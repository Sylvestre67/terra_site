from django.views.generic import DetailView, TemplateView

from .models import Name


class IndexView(TemplateView):
    template_name = 'index.html'


class PublisherDetail(DetailView):

    context_object_name = 'name'
    queryset = Name.objects.all()