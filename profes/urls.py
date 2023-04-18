from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar-reporte/<int:semestre>/<str:grupo>/', views.editar_reporte, name='editar_reporte'),
]
