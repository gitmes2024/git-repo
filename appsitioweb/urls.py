from django.urls import path
from. views import inicio, vconferencia,tipoconf, departamento, sala

# urls de la appsitio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('vconferencia/', vconferencia, name="conferencia"),
    path('tipoconf/', tipoconf, name="tipo"),
    path('departamento/', departamento, name="departamento"),
    path('sala/', sala, name="salon"),

]
