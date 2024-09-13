from django.urls import path
from .views import SummaryAPIView, QueryPatentView

urlpatterns = [
    path('summary', SummaryAPIView.as_view(), name='summary'),
    path('query', QueryPatentView.as_view(), name='query'),
]
