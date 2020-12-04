from django.shortcuts import render
from django.http import HttpResponse
from app_restaurant.models import Restaurant
import random
import re
from django.db.models.functions import Length
from django.db.models import Q
from itertools import chain

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
        "allCuisines" : uniqueData,
        "numPeople" : sNumPeople
    }
    return render(request, f'app_recommendation_templates/recommendation_forms{sNumPeople}.html', context)


def recFinal(request, iNumPeople):
    i=1
    lPriceRange = []
    lRating = []
    aCuisine = []

    #For loop that grabs variables from each participant
    for i in range(1, iNumPeople+1):
        lPriceRange.append(int(request.GET[f'cost{i}']))
        lRating.append(int(request.GET[f'rating{i}']))
        aCuisine.append(request.GET.getlist(f'cuisine{i}'))
    

    
    lACuisine = list(chain.from_iterable(aCuisine))

    priceRange = sum(lPriceRange)/int(iNumPeople)
    rating = sum(lRating)/int(iNumPeople)
    
    

    data = Restaurant.objects.filter(Q(price_range__lte=priceRange), Q(rating__gte=rating), Q(cuisine1__in=lACuisine) | Q(cuisine2__in=lACuisine) | Q(cuisine3__in=lACuisine))
    # data = Restaurant.objects.filter(Q(cuisine1__in=aCuisine) | Q(cuisine2__in=aCuisine) | Q(cuisine3__in=aCuisine))
    
    
    context = {
        'filtered_restaurants' : data,
        'checkedCuisine' : lACuisine,
        'average_price' : priceRange,
        'average_rating' : rating
    }

    return render(request, 'app_recommendation_templates/final_recommendations.html', context)