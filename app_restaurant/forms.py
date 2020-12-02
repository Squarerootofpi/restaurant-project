from django import forms

class RecommendationsForm(forms.Form):
    cost = forms.CharField(max_length=100)
    cuisine = forms.CharField(max_length=100)
    health_factor = forms.CharField(max_length=100)
    wait_time = forms.IntegerField(required=False)
    travel_time = forms.IntegerField(required=False)    
    drive_through = forms.BooleanField(required=False)

# Cost
# Cuisine
# Health factor
# Wait time
# Travel time (we will attempt to implement as time allows) 
# HasDriveThrough
