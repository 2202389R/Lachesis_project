from django import forms
from django.contrib.auth.models import User
from lachesis.models import Story, Genre, UserProfile

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the genre name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Genre
        fields = ('name',)

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the story.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    first_visit = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    last_visit = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Story
        exclude = ('genre',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
