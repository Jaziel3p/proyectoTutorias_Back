from pathlib import Path
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from weasyprint import CSS, HTML
from django.http import HttpResponse
from django.conf import settings
from BDTutoriasAPI import settings
from BDTutoriasAPI import settings
from .models import Tutor, Almuno, HorasAlumno
import json 
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import jwt
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, OutstandingToken, BlacklistedToken
from django.contrib.auth.models import User
from django.db import transaction


# Create your views here.

class TutorView(View):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if(id>0):
            tutor=list(Tutor.objects.filter(id=id).values()) #Se pasa a lista para que pueda ser convertido a Json
            if len(tutor)>0:
                tutores = tutor[0]
                datos={'message': "Success", 'tutor': tutores}
            else:
                datos={'message':"Tutor not found..."}
            return JsonResponse(datos)
        else:
            tutor=list(Tutor.objects.values())
            if len(tutor)>0:
                datos={'message':"Success",'tutor':tutor}
            else:
                datos={'message':"Tutores not found."}
            return JsonResponse(datos)

    def post(self,request):
        # print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Tutor.objects.create(rfc=jd['rfc'], periodo=jd['periodo'], carrera=jd['carrera'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self,request,rfc):
        jd=json.loads(request.body)
        tutor=list(Tutor.objects.filter(rfc=rfc).values())
        if len(tutor)>0:
            tutor=Tutor.objects.get(rfc=rfc)
            tutor.rfc = jd['rfc']
            tutor.periodo = jd['periodo']
            tutor.carrera = jd['carrera'] 
            tutor.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Tutor not found..."}
        return JsonResponse (datos)
      
    def delete(self,request,id):
        tutor=list(Tutor.objects.filter(id=id).values())
        if len(tutor)>0: 
            Tutor.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message': "Tutor not found..."}
        return JsonResponse(datos)
    


class ListTuturesPDF(View):
    def get(self, request, *args, **kwargs):
        tutores = Tutor.objects.all()

        SEP_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias' / 'static' / 'img' / 'SEP.jpg'
        ITA_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias' / 'static' / 'img' / 'ITA2.png'

        data = {
            'tutores': tutores,
            'cantidadtutores': tutores.count(),
            'SEP_url': SEP_path.as_uri(),
            'ITA_url': ITA_path.as_uri(),
        }
        template = get_template("reporteTutor.html")
        html = template.render(data)
        css_url = './apibdtutorias/static/apibdtutorias/css/reporteTutor.css'

        pdf = HTML(string=html).write_pdf(stylesheets=[CSS(css_url)],)

        return HttpResponse(pdf, content_type='application/pdf')
    
class ListTuturesPDFCH(View):
    def get(self, request, *args, **kwargs):
        tutores = Tutor.objects.all()
        almuno = Almuno.objects.all()
        horasAlumno = HorasAlumno.objects.all()
        SEP_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias'/'static' / 'img' / 'SEP.jpg'
        ITA_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias'/'static' / 'img' / 'ITA2.png'
        css_url = './apibdtutorias/static/apibdtutorias/css/estilos.css'
        data = {
            'tutores': tutores,
            'almunos':almuno,
            'indice': almuno.count(),
            'horasAlumno':horasAlumno,
            'cantidadtutores': tutores.count(),
            'CSS_url': css_url,
            'SEP_url': SEP_path.as_uri(),
            'ITA_url': ITA_path.as_uri(),
        }
        template = get_template("TAbla.html")
        html = template.render(data)    
        pdf = HTML(string=html).write_pdf(stylesheets=[CSS(css_url)],

        )
        return HttpResponse(pdf, content_type='application/pdf')
  


class LoginAPIView(APIView):
    def post(self, request):
        no_de_control = request.data.get('no_de_control')
        nip = request.data.get('nip')

        # Verificar si los datos requeridos están presentes
        if not no_de_control or not nip:
            return Response({'error': 'No se proporcionaron el no_de_control y/o nip'}, status=status.HTTP_400_BAD_REQUEST)

        # Realizar la validación de los datos enviados al API de la universidad
        url = 'http://127.0.0.1:8000/api/Alumnos/'
        params = {
            'no_de_control': no_de_control,
            'nip': nip
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Verifica si la respuesta es exitosa
            data = response.json()

            # Verificar si los datos del estudiante son válidos
            if len(data) == 1 and 'no_de_control' in data[0] and 'nip' in data[0] and 'apellido_paterno' in data[0] and 'apellido_materno' in data[0] and 'nombre_alumno' in data[0]:
                alumno_data = data[0]
                no_de_control = alumno_data['no_de_control']
                nip = alumno_data['nip']
                nombre_de_usuario = alumno_data['nombre_alumno']
                apellidoP_de_usuario = alumno_data['apellido_paterno']
                apellidoM_de_usuario = alumno_data['apellido_materno']

                # Verificar si el alumno está registrado en la base de datos
                try:
                    alumno = Almuno.objects.get(no_de_control=no_de_control)
                except Almuno.DoesNotExist:
                    # Si el alumno no está registrado, crear una nueva instancia de User y Almuno
                    user = User(username=nombre_de_usuario)
                    user.set_unusable_password()
                    user.save()

                    alumno = Almuno(user=user, no_de_control=no_de_control, nip=nip)
                    alumno.save()

                # Verificar si el usuario ya tiene un token válido en la tabla 'outstanding'
                tokens = OutstandingToken.objects.filter(user=alumno.user)
                print("este es el TOKEEEEEN!!!",tokens.first())

                if tokens.exists():
                    # Si hay tokens asociados al usuario, utilizar el primero
                    token = tokens.first()
                    refresh = RefreshToken(token)
                    access = AccessToken(token)

                    token_data = {
                        'refresh': str(refresh),
                        'access': str(access),
                        'nombre_de_usuario': nombre_de_usuario,
                        'apellidoP_de_usuario': apellidoP_de_usuario,
                        'apellidoM_de_usuario': apellidoM_de_usuario,
                    }

                    return Response(token_data, status=status.HTTP_200_OK)
                else:
                    # El usuario no tiene tokens válidos en la tabla 'outstanding', generar uno nuevo
                    refresh = RefreshToken.for_user(alumno.user)
                    access = AccessToken.for_user(alumno.user)

                    token_data = {
                        'refresh': str(refresh),
                        'access': str(access),
                        'nombre_de_usuario': nombre_de_usuario,
                        'apellidoP_de_usuario': apellidoP_de_usuario,
                        'apellidoM_de_usuario': apellidoM_de_usuario,
                    }

                    return Response(token_data, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'Datos inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as e:
            # Manejo de errores en caso de que la solicitud falle
            print(f'Error al obtener los datos del estudiante: {e}')
            if hasattr(e, 'response') and e.response:
                print(f'Respuesta del servidor: {e.response.content}')
            return Response({'error': 'Error en la solicitud al API de la universidad'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'No se proporcionó el token de actualización'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            outstanding_token = OutstandingToken.objects.filter(token=refresh_token).first()
        
            if outstanding_token:
                # token = RefreshToken(refresh_token)
                # # token.blacklist()

                outstanding_token.delete()

                return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'El token de actualización no existe'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(str(e))
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

