from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia, Profesor, Tema
from .forms import ReporteForm
from django.db.models import Count, F
def index(request):
    profesores = Profesor.objects.all()
    for profesor in profesores:
        temas_vistos = profesor.temas_vistos.all()
        total_temas = Tema.objects.filter(materia=profesor.materia).count()
        porcentaje_avance = temas_vistos.count() / total_temas * 100
        profesor.porcentaje_avance = porcentaje_avance
    return render(request, 'profes/index.html', {'profesores': profesores})

def editar_reporte(request, matricula, grupo):
    print(matricula)
    try:
        matricula = int(matricula)
    except ValueError:
        return render(request, 'profes/error.html', {'mensaje': 'La matrícula del profesor debe ser un número entero'})

    profesor = Profesor.objects.filter(matricula=matricula, grupo=grupo).first()
    temas = Tema.objects.filter(materia=profesor.materia)
    porcentaje = 0

    if request.method == 'POST':
        form = ReporteForm(request.POST, profesor=profesor)
        if form.is_valid():
            form.save(profesor)
            temas_vistos = profesor.temas_vistos.all()
            total_temas = temas.count()
            porcentaje = temas_vistos.count() / total_temas * 100
        
            
            return redirect('index')
    else:
        form = ReporteForm(profesor=profesor, initial={
            f'tema_{tema.id}': tema.id in profesor.temas_vistos.all().values_list('id', flat=True)
            for tema in temas
        })
        temas_seleccionados = len([k for k, v in request.POST.items() if k.startswith('tema_') and v == 'on'])

    return render(request, 'profes/editar_reporte.html', {'profesor': profesor, 'temas': temas, 'form':form, 'porcentaje_avance': porcentaje})


def detalle_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    materia = profesor.materia
    temas = Tema.objects.filter(materia=materia)
    context = {
        'profesor': profesor,
        'materia': materia,
        'temas': temas,
    }
    return render(request, 'profes/detalle_profesor.html', context)
