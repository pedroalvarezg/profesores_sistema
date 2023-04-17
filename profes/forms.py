from django import forms
from .models import Profesor, Tema

class ReporteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        profesor = kwargs.pop('profesor')
        super().__init__(*args, **kwargs)

        temas = Tema.objects.filter(materia=profesor.materia)
        for tema in temas:
            self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre.strip(), required=False)
            # self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre.strip().replace(':', '') + ' ', required=False)
            # self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre.strip(), required=False)
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=f"{tema.nombre.strip()}&nbsp;", required=False)
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre.strip(), required=False)
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=f"{tema.nombre.strip()} | ", required=False)
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre.strip() + ' ', required=False)
            #self.fields[f'tema_{tema.id}'] = forms.BooleanField(label=tema.nombre, required=False)

    def save(self, profesor):
        temas_vistos = []
        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith('tema_') and field_value:
                tema_id = int(field_name[5:])
                temas_vistos.append(tema_id)

        profesor.temas_vistos.set(temas_vistos)
        profesor.save()
