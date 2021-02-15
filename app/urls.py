from django.urls import path, include
from app.views import ProfesorCreate 

app_name = 'app'

urlpatterns = [
    path('', ProfesorCreate.as_view(),name="inicio"),
]
