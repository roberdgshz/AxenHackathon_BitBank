from django.shortcuts import render

from django.db import connection

# Create your views here.
def ViewNotificationList(request, user):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT auditlogid, auditlogdescription, auditlogtime, audittypeid_id FROM auditlog WHERE auditlogaccountid_id = 
                       (SELECT accountid FROM account WHERE accountusername = %s);""",[user])
        resultados = cursor.fetchall()

    notificaciones = [
        {"id": fila[0], "description":fila[1], "time":fila[2], "type":fila[3]}
        for fila in resultados
    ]

    return render(request, 'notifications/notifications_list.html', {'logs':notificaciones})

def ViewNotification(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT auditlogid, auditlogdescription, auditlogtime, audittypeid_id FROM auditlog WHERE auditlogid = %s",
                       [id])
        resultado = cursor.fetchone()
    if resultado :
        notificacion = {"id":resultado[0],"description":resultado[1],"time":resultado[2],"type":resultado[3]}

    return render(request, 'notifications/notification.html', {'log':notificacion})