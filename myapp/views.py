from django.shortcuts import render
from myapp.models import Tank, Attachment, Machine, Crew, Companie
from django.views.generic import ListView, DetailView

def index(request):
    num_tanks = Tank.objects.all().count()
    tanks = Tank.objects.order_by('creation_date')[:5]
    context = {
        'num_tanks': num_tanks,
        'tanks': tanks,
    }
    return render(request, 'index.html', context=context)

def osadka(request):
    crews = Crew.objects.all().count()
    context = {
        'crews': crews,
    }
    return render(request, 'tanky/osadka.html', context=context)

class TankListView(ListView):
    model = Tank
    context_object_name = 'tanks_list'
    template_name = 'tanky/list.html'

class OsadkaListView(ListView):
    model = Tank
    context_object_name = 'osadkas_list'
    template_name = 'tanky/osadka.html'

class CompanyDetailView(DetailView):
    model = Companie
    context_object_name = 'company_detail'
    template_name = 'company/detail.html'

class OsadkaDetailView(DetailView):
    model = Machine
    context_object_name = 'osadka_detail'
    template_name = 'osadka/detail.html'