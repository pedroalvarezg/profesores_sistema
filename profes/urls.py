from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('editar-reporte/<int:matricula>/<str:grupo>/', views.editar_reporte, name='editar_reporte'),
    path('descargar-reportes/', views.descargar_reportes, name= 'descargar_reportes'),
    path('restaurar-reportes/', views.restaurar_reportes, name= 'restaurar_reportes'),
]
