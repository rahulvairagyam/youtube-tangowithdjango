'''
Created on Jul 19, 2017

@author: jwang02
'''

from django import forms
from rango.models import Category, Course
from django.forms.widgets import SelectDateWidget


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    description = forms.CharField(max_length=256, required=False, help_text="Please enter the description of the category.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    status = forms.BooleanField(label='Status',
                               required=False, 
                               help_text="Is this category still active?")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name', 'description', )

class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the course title.")
    summary = forms.CharField(max_length=128, required=False, help_text="Please enter the course summary.")
    url = forms.URLField(max_length=200, help_text="Please enter the course web page URL.")
    phone = forms.CharField(max_length=15, help_text="Please enter the course registration phone number")
    startingdate = forms.DateField(label='Starting Date: ', widget=SelectDateWidget(), help_text="Please set the course starting date.")
    status = forms.BooleanField(label='Status',
                               required=False, 
                               help_text="Is this category still active?")
    hascertification = forms.BooleanField(label='Has Certification Test? ',
                               required=False, 
                               help_text="Please check here if the course offers certification test.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        #or specify the fields to include (i.e. not include the category field)
        fields = ('title', 'url', 'summary', 'phone', 'startingdate',)
