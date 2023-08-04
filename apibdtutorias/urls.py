<<<<<<< HEAD
from django.urls import path 
from .views import TutorView, ListTuturesPDF, ListTuturesPDFCH, reporteSemestralCoord
=======
from django.urls import path
from .views import TutorView, ListTuturesPDF, ListTuturesPDFCH, LoginAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
>>>>>>> chucho

urlpatterns = [
    path('tutores/', TutorView.as_view(), name='tutores_list'),
    path('tutores/<int:id>/', TutorView.as_view(), name='tutores_process'),
    path('listar-tutores-pdf/', ListTuturesPDF.as_view(), name='tutores_list_pdf'),
    path('pdf-chucho/', ListTuturesPDFCH.as_view(), name='pdf-chucho'),
<<<<<<< HEAD
    path('reporteSemestralCoord/', reporteSemestralCoord.as_view(), name='reporteSemestralCoord_pdf'),
]
=======
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
>>>>>>> chucho
