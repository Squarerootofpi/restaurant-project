from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RecommendationsForm

# Create your views here.
def indexPageView(request) :
    # sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    # return HttpResponse(sOutput)
    form =  RecommendationsForm()
    return render(request, 'app_restaurant_templates/index.html', {'form': form})

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


def getRecommendationDemo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecommendationsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            return redirect('index')
    # if a GET (or any other method) we'll create a blank form
    #else:
     #   form =  RecommendationsForm()
    #return render(request, 'app_restaurant_templates/index.html', {'form': form})