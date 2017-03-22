from django import forms
from lachesis.models import Genre, Story, Segment, UserProfile, UserSegment
from django.contrib.auth.models import User

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    stories = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Genre
        fields = ('name',)

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.ForeignKey(User)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        exclude = ('genre',)

class SegmentForm(forms.ModelForm):
    id = forms.IntegerField(max_length=99)
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.ForeignKey(User)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

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
        fields = ('picture')
