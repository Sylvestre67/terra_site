from django.views.generic import DetailView, TemplateView, ListView

from .models import Name


class IndexView(TemplateView):
    template_name = 'index.html'


class NameDetail(DetailView):
    template_name = 'baby_name_detail.html'
    context_object_name = 'name'
    queryset = Name.objects.all()

    def get_queryset(self):
        """Filter name on given param"""
        return self.queryset.filter(name=self.kwargs.get('name'))


class NameList(ListView):
    context_object_name = 'baby_names'
    queryset = Name.objects.all()
    template_name = 'baby_names.html'


class GenderDetail(DetailView):
    context_object_name = 'name'
    queryset = Name.objects.all()


class StateDetail(DetailView):
    context_object_name = 'name'
    queryset = Name.objects.all()