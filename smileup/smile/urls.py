from django.urls import path
from . import views

urlpatterns = [
    path('smile/', views.smile, name='smile'),
]