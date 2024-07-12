from django.urls import path
from .views import SalesReportListView

urlpatterns = [
    path('sales-reports/', SalesReportListView.as_view(), name='sales-report-list'),
]
