from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
path('', views.getRecommendation, name="get-recommendation"),
path('forms/', views.recForm, name="rec-forms"),
path('final/<int:iNumPeople>', views.recFinal, name="rec-final"),
]