from django.urls import path
from .views import AgentCreateView, AgentDeleteView, AgentDetailsView, AgentListView, AgentUpdateView

app_name = "agents"

urlpatterns = [
    path("", AgentListView.as_view(), name="agent-list"),
    path("<int:pk>/", AgentDetailsView.as_view(), name="agent-detail"),
    path("<int:pk>/update/", AgentUpdateView.as_view(), name="agent-update"),
    path("<int:pk>/delete/", AgentDeleteView.as_view(), name="agent-delete"),
    path("create/", AgentCreateView.as_view(), name="agent-create"),
]
