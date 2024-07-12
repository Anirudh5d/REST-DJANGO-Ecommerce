from rest_framework import generics
from .models import SalesReport
from .serializers import SalesReportSerializer
from django.shortcuts import render



class SalesReportListView(generics.ListAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    

def sales_report(request):
    reports = SalesReport.objects.all()
    return render(request, 'analytics/sales_report.html', {'reports': reports})

