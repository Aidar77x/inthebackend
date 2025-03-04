from django.urls import path
from .views import TableListView, AvailableTablesView

urlpatterns = [
    path('', TableListView.as_view(), name='table-list'),
    path('available/', AvailableTablesView.as_view(), name='available-tables'),
]