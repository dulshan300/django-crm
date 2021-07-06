from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.
def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }

    return render(request, 'leads/leads_list.html',context)

def lead_detail(request,id):
    lead = Lead.objects.get(id=id)
    context = {
        'lead':lead
    }
    return render(request, 'leads/lead_detail.html', context)

