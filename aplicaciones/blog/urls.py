from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name = 'index'),
    path('<slug:slug>', DetallePost, name = 'detalle_post'),
    path('general/', General, name = 'general'),
    path('villena/', Villena, name = 'villena'),
    path('nacional/', Nacional, name = 'nacional'),
    path('otros/', Otros, name = 'otros'),
]
