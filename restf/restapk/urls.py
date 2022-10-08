from django.urls import path 
from . import views 

urlpatterns = [
    path('query_set',views.query_set, name='query_set'),
    path('addData',views.addData,name='addData'),
    path('<int:pk>/', views.DetailPersonne.as_view(),name='DetailPersonne'),
    path('CreatePersonne',views.CreatePersonne.as_view(), name='CreatePersonne'),
    path('<int:pk>/UpdatePersonne',views.UpdatePersonne.as_view(),name='UpdatePersonne')
]
