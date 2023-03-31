from django.urls import path 
from .views import TutorView, ListTuturesPDF, ListTuturesPDFCH

urlpatterns=[
    path('tutores/', TutorView.as_view(), name='tutores_list'),
    path('tutores/<int:id>', TutorView.as_view(), name='tutores_process'),
    path('listar-tutores-pdf/', ListTuturesPDF.as_view(), name='tutores_list_pdf'),
    path('pdf-chucho/', ListTuturesPDFCH.as_view(), name='pdf-chucho')
]