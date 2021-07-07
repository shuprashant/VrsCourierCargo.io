from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('services/Air', views.air, name="Air"),
    path('services/Road', views.road, name="Road"),
    path('services/Local-Shifting', views.shifting, name="Shifting"),
    path('services/Packers-Movers', views.packing, name="Packers"),
    path('services/Warehouse', views.warehouse, name="Warehouse"),
    path('services/Supply-Chain-Management', views.supply, name="Supply"),
    path('gallery', views.gallery, name="gallery")
]
