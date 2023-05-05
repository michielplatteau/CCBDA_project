from django.urls import path

from . import views



urlpatterns = [
    path('another-path/', views.home),
    path('model_retrieve/', views.test_model_view),
    path('', views.home)
]
