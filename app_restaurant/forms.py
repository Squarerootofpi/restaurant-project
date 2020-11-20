from django import forms

class RecommendationsForm(forms.Form):
    cost = forms.CharField(max_length=100)
    cuisine = forms.CharField(max_length=100)
    health_factor = forms.CharField(max_length=100)
    wait_time = forms.IntegerField(required=False)
    travel_time = forms.IntegerField(required=False)    
    drive_through = forms.BooleanField(required=False)

#outline of form for collecting number of users 
class NumUsersForm(forms.Form):
    numUsers = forms.IntegerField(required=True)

#form for search 
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

# Cost
# Cuisine
# Health factor
# Wait time
# Travel time (we will attempt to implement as time allows) 
# HasDriveThrough
