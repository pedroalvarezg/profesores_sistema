from django.shortcuts import render, get_object_or_404, redirect
from .models import Materia, Profesor, Tema
from .forms import ReporteForm
def index(request):
    profesores = Profesor.objects.all()
    return render(request, 'profes/index.html', {'profesores': profesores})

def editar_reporte(request, semestre, grupo):
    print(semestre)
    try:
        semestre = int(semestre)
    except ValueError:
        return render(request, 'profes/error.html', {'mensaje': 'La matrícula del profesor debe ser un número entero'})

    profesor = get_object_or_404(Profesor, pk=semestre)
    temas = Tema.objects.filter(materia=profesor.materia)

    if request.method == 'POST':
        form = ReporteForm(request.POST, profesor=profesor)
        if form.is_valid():
            form.save(profesor)
            return redirect('index')
    else:
        form = ReporteForm(profesor=profesor, initial={
            f'tema_{tema.id}': tema.id in profesor.temas_vistos.all().values_list('id', flat=True)
            for tema in temas
        })

        
    return render(request, 'profes/editar_reporte.html', {'profesor': profesor, 'temas': temas, 'form':form})


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
