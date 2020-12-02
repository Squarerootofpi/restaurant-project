from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def indexPageView(request) :
    # sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    # return HttpResponse(sOutput)
    data = Restaurant.objects.all()

    context = {
        "all_restaurants" : data
    }
    return render(request, 'app_restaurant_templates/index.html', context)

def getAll(request):
    """
    This returns all the available restaurants.
    """
    return HttpResponse('getAll')

    
def getRandom(request):
    """
    This returns a random restaurant.
    """
    return HttpResponse('getRandom')

    
def searchAvailable(request):
    """
    This returns search results from the available restaurants.
    """
    return HttpResponse('searchAvailable')

    
def getRecommendation(request):
    """
    This returns a recommended restaurant.
    """
    return HttpResponse('getRecommendation')