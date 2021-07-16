from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm
from django.urls import reverse

# Create your views here.


def landing_page(request):
    return render(request,'landing.html')

def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, 'leads/leads_list.html', context)


def lead_detail(request, id):
    lead = Lead.objects.get(id=id)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():          
            form.save()
            return redirect(reverse('leads:leads_list'))
        else:
            pass

    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request,id):
    
    lead = Lead.objects.get(id=id)
    
    form = LeadModelForm(request.POST or None,instance=lead)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('leads:leads_detail',args=[lead.id]))
        else:
            pass

    context = {
        "lead": lead,
        "form": form,
    }

    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, id):

    lead = Lead.objects.get(id=id)
    lead.delete()    

    return redirect(reverse('leads:leads_list'))
