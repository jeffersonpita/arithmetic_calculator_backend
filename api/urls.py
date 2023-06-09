from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name ='home'),
    path('operation/', views.OperationView.as_view(), name ='operation'),
    path('records/', views.RecordView.as_view(), name ='records'),
    path('records/<int:id>/', views.RecordView.as_view(), name ='record_delete'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
]