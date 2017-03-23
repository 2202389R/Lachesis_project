from django import forms
from lachesis.models import Genre, Story, Segment, UserProfile, UserSegment
from django.contrib.auth.models import User
import datetime

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the Genre name.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Genre
        fields = ('name',)

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.CharField(widget=forms.HiddenInput(), initial=User)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        exclude = ('genre',)

class SegmentForm(forms.ModelForm):
    segment_number = forms.CharField(widget=forms.HiddenInput())
    segment_text = forms.CharField(max_length=10000)
    pub_date = forms.DateTimeField(initial=datetime.date.today())
    closed = forms.BooleanField(widget=forms.HiddenInput(), initial=False)
    option1 = forms.CharField(max_length=1000, help_text="Please enter option 1")
    option2 = forms.CharField(max_length=1000, help_text="Please enter option 2")
    option1votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    option2votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Segment
        exclude = ('story',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
