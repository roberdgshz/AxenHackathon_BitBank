from django.views.generic import TemplateView
from django.shortcuts import render

from django.db import connection

# Create your views here.
class ViewHome(TemplateView):
    template_name = '_general/home.html'

class ViewAbout(TemplateView):
    template_name = '_general/about.html'

class ViewLegal(TemplateView):
    template_name = '_general/legal.html'

def ViewQuerys(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM listar_cuentas();" )
        resultados = cursor.fetchall()
    
    cuentas = [
        {"AccountID": fila[0], "AccountUsername": fila[1], "AccountEmail": fila[2]}
        for fila in resultados
    ]
    
    return render(request, '_general/test.html', {'results':cuentas})