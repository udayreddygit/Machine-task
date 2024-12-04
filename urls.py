from django.urls import path
from .views import ClientListCreateView, ClientDetailUpdateDeleteView, ProjectListCreateView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailUpdateDeleteView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
]
