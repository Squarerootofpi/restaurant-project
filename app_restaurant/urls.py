from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('', views.indexPageView, name="index"),
    path('api/all/', views.getAll, name="get-all"),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/random/', views.getRandom, name="get-random"),
    path('api/search/', views.searchAvailable, name="search-available"),

]


