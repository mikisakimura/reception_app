from django.urls import path
from backend.api import views

urlpatterns = [
    path("backend/", views.ListView.as_view(), name="list"),
    path("backend/<int:pk>/", views.DetailView.as_view(), name="detail"),
]