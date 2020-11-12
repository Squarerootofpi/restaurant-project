from django.urls import path
# from .views import indexPageView, getAll, getRandom, searchAvailable,getRecommendation
from . import views
urlpatterns = [
    path('', views.indexPageView, name="index"),
    path('api/all/', views.getAll, name="get-all"),
    path('api/recommendations/', views.getRecommendation, name="get-recommendation"),
    path('api/random/', views.getRandom, name="get-random"),
    path('api/search/<str:query>/', views.searchAvailable, name="search-available"),
    path('api/othersite/', views.redirectToBetterSite, name="myed-redir"),

]


