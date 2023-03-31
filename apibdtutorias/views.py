from pathlib import Path
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from django.template.loader import get_template
from weasyprint import CSS, HTML
from django.http import HttpResponse
from django.conf import settings

from BDTutoriasAPI import settings

from .models import Tutor
import json 
import os
from pathlib import Path


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
        SEP_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias'/'static' / 'img' / 'SEP.jpg'
        ITA_path = Path(settings.BASE_DIR) /'.'/'apibdtutorias'/'static' / 'img' / 'ITA2.png'
        css_url = './apibdtutorias/static/apibdtutorias/css/estilos.css'
        data = {
            'tutores': tutores,
            'cantidadtutores': tutores.count(),
            'CSS_url': css_url,
            'SEP_url': SEP_path.as_uri(),
            'ITA_url': ITA_path.as_uri(),
        }
        template = get_template("TAbla.html")
        html = template.render(data)
        pdf = HTML(string=html).write_pdf(
            stylesheets=[CSS(css_url)],
            
        )
        return HttpResponse(pdf, content_type='application/pdf')