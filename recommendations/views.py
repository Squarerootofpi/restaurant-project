from django.shortcuts import render
from django.http import HttpResponse
from app_restaurant.models import Restaurant
import random
import re
from django.db.models.functions import Length

def getRecommendation(request):
    """
    This returns the starting form specifying the group size for getting a recommendation.
    """
    return render(request, 'app_recommendation_templates/get_recommendations.html')

def recForm(request):
    sNumPeople = request.POST['people']
    data1 = Restaurant.objects.values_list('cuisine1')
    data1 = list(data1)
    data2 = Restaurant.objects.values_list('cuisine2')
    data2 = list(data2)
    data3 = Restaurant.objects.values_list('cuisine3')
    data3 = list(data3)
    combinedData = data1 + data2 + data3
    setData = set(combinedData)
    uniqueData = (list(setData))
    i=0
    for i in range(len(uniqueData)):
        holder = str(uniqueData[i])
        uniqueData[i] = re.sub('[\W_]+', '', holder)

    context = {
        "allCuisines" : uniqueData
    }
    return render(request, f'app_recommendation_templates/recommendation_forms{sNumPeople}.html', context)


def recFinal(request):
    priceRange = request.GET['cost1']
    rating = request.GET['rating1']
    aCuisine = request.GET.getlist('cuisine[]')
    print(aCuisine)

    data = Restaurant.objects.filter(price_range__lte=priceRange, rating__gte=rating)

    context = {
        'filtered_restaurants' : data,
        'checkedCuisine' : aCuisine 
    }

    return render(request, 'app_recommendation_templates/final_recommendations.html', context)