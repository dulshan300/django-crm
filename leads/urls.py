from django.urls import path
from leads.views import lead_detail, lead_update, leads_list, lead_create, lead_delete

app_name = "leads"

urlpatterns = [
    path('', leads_list, name="leads_list"),
    path('<int:id>/', lead_detail, name="leads_detail"),
    path('<int:id>/update', lead_update, name="leads_update"),
    path('<int:id>/delete', lead_delete, name="leads_delete"),
    path('create/', lead_create, name="leads_create"),
]
