from django.shortcuts import render
from cities.models import City
from django.views.generic.detail import DetailView
from .forms import CityForm, HomeCityForm

__all__ = ('home', 'CityDetailView', )


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
