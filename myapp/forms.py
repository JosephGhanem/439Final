from django import forms
from .models import Contact

# Form for creating and updating doctor records
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'speciality', 'city', 'fee', 'rating', 'years_experience']

# Form for the recommendation engine
class RecommendationForm(forms.Form):
    city = forms.CharField(required=False)
    speciality = forms.CharField(required=False)
    max_fee = forms.IntegerField(required=False)
