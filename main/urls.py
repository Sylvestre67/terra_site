from django.urls import path

from .views import IndexView, NameList, NameDetail

urlpatterns = [
    path('', IndexView.as_view()),
    path('baby_names/', NameList.as_view(), name='name-list'),
    path('baby_names/<str:name>/<pk>', NameDetail.as_view(), name='name-detail'),
]