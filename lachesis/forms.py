from django import forms
from lachesis.models import Genre, Story, Segment, UserProfile, UserSegment
from django.contrib.auth.models import User
import datetime

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the Genre name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Genre
        fields = ('name',)

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Story
        fields = ('title','genre', 'author')
		

class SegmentForm(forms.ModelForm):
    segment_number = forms.CharField(max_length=128, help_text="Please enter the title of the segment.")
    segment_text = forms.CharField(max_length=10000, help_text="Please enter segment text.")
    option1 = forms.CharField(max_length=1000, help_text="Please enter option 1")
    option2 = forms.CharField(max_length=1000, help_text="Please enter option 2")
    option1votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    option2votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Segment
        exclude = ()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','password',)
