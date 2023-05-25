from django.urls import path

from . import views



urlpatterns = [
    path('another-path/', views.home),
    path('model_retrieve/', views.test_model_view),
    # path('test/', views.graphs),
    path('', views.home),
    path('test2/', views.index2),
    path('test_interactive_graphs/', views.index3)
]
