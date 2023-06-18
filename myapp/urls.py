from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('tanks/', views.TankListView.as_view(), name='tanks'),
 path('osadkas/', views.OsadkaListView.as_view(), name='osadkas'),
 path('tanks/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
 path('osadkas/<int:pk>/', views.OsadkaDetailView.as_view(), name='osadka_detail'),
]
