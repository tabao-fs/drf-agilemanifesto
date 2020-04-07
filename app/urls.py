from django.urls import path

from app import views

urlpatterns = [
    path('agilemanifesto', views.AgileManifesto.as_view()),
    path('agilemanifesto/values', views.AgileManifestoValues.as_view()),
    path('agilemanifesto/principles', views.AgileManifestoPrinciples.as_view()),
]
