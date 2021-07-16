from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm
from django.urls import reverse

# Create your views here.


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def landing_page(request):
#     return render(request, 'landing.html')


class LeadListView(ListView):
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    # This object will pass an 'object_list' in to the context.
    # we can use context_object_name to rewrite default return object name
    context_object_name = "leads"


# def leads_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }

#     return render(request, 'leads/leads_list.html', context)


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    # This object will pass an 'object_list' in to the context.
    # we can use context_object_name to rewrite default return object name
    context_object_name = "lead"


# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:leads_list")
    
    def form_valid(self, form):
        # TODO Send Email
        send_mail(
            subject="A Leader has been Created",
            message="Please goto the dashboard to see all the leads",
            from_email="ceylondev@gmail.com",
            recipient_list=['abavira@gmail.com']
        ) 
        return super(LeadCreateView, self).form_valid(form)


# def lead_create(request):
#     form = LeadModelForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('leads:leads_list'))
#         else:
#             pass

#     context = {
#         "form": form
#     }
#     return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leads_detail', args=[self.queryset[0].id])


# def lead_update(request, pk):

#     lead = Lead.objects.get(id=pk)

#     form = LeadModelForm(request.POST or None, instance=lead)

#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('leads:leads_detail', args=[lead.id]))
#         else:
#             pass

#     context = {
#         "lead": lead,
#         "form": form,
#     }

#     return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:leads_list')

# def lead_delete(request, pk):

#     lead = Lead.objects.get(id=pk)
#     lead.delete()

#     return redirect(reverse('leads:leads_list'))
