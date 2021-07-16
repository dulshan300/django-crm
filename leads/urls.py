from django.urls import path
from leads.views import (
    # lead_detail,
    # lead_update,
    # leads_list,
    # lead_create,
    # lead_delete,
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="leads_list"),
    path('<int:pk>/', LeadDetailView.as_view(), name="leads_detail"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name="leads_update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="leads_delete"),
    path('create/', LeadCreateView.as_view(), name="leads_create"),
]
