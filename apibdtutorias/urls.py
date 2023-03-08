from django.urls import path 
from .views import TutorView, ListTuturesPDF

urlpatterns=[
    path('tutores/', TutorView.as_view(), name='tutores_list'),
    path('tutores/<int:id>', TutorView.as_view(), name='tutores_process'),
    path('listar-tutores-pdf/', ListTuturesPDF.as_view(), name='tutores_list_pdf')
]