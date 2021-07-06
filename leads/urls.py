from django.urls import path
from leads.views import lead_detail, leads_list

app_name = "leads"

urlpatterns = [
    path('', leads_list, name="leads_list"),
    path('<id>', lead_detail, name="leads_detail")
]
