from django.urls import path
from pdf_app import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('profile/<uuid:pk>/', views.ProfileDetail.as_view()),
]
