from django import forms
from lachesis.models import Genre, Story, Segment, UserProfile, UserSegment
from django.contrib.auth.models import User

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Story
        fields = ('name',)

class StoryForm(forms.ModelForm):
    id = forms.IntegerField(max_length=99)
    title = forms.CharField(max_length=128, help_text="Please enter the title of the story.")
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.ForeignKey(User)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Story
        exclude = ('story',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
