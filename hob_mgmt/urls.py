from django.urls import path
from hob_mgmt import views

urlpatterns = [
    path('', views.InputView.as_view(), name='input'),
    path('list/', views.ListView.as_view(), name='list'),
    path('add/', views.AddView.as_view(), name='add'),
    path('send/', views.SendView.as_view(), name='send'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

]
