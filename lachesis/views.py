from lachesis.forms import GenreForm
from lachesis.forms import StoryForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lachesis.models import Genre
from lachesis.models import Story, Segment
from lachesis.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime


def index(request):
    genre_list = Genre.objects.order_by('-views')[:5]
    story_list = Story.objects.order_by('-votes')[:5]
    context_dict = {'genres': genre_list, 'stories': story_list}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'lachesis/index.html', context_dict)
    return response

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    print(request.method)
    print(request.user)
    response = render(request, 'lachesis/about.html', context_dict)
    return response


def show_genre(request, genre_name_slug):
	context_dict = {}

	try:
		genre = Genre.objects.get(slug=genre_name_slug)
		
		stories = Story.objects.filter(genre=genre)
		context_dict['stories'] = stories
		context_dict['genre'] = genre

	except Genre.DoesNotExist:
		context_dict['genre'] = None
		context_dict['stories'] = None

	return render(request, 'lachesis/genre.html', context_dict)

def add_genre(request):
    form = GenreForm()

    if request.method == 'POST':
        form = GenreForm(request.POST)

        if form.is_valid():
            gen = form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'lachesis/add_genre.html', {'form': form})

def add_story(request, genre_name_slug):
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
    except Genre.DoesNotExist:
        genre = None

    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            if genre:
                story = form.save(commit=False)
                story.genre = genre
                story.author = request.user
                story.votes = 0
                story.save()
                return show_genre(request, genre_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'genre': genre}
    
    return render(request, 'lachesis/add_story.html', context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'lachesis/register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Lachesis account is disabled.")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("invalid login details supplied.")

    else:
        return render(request, 'lachesis/user_login.html', {})

@login_required
def restricted(request):
    return render(request, 'lachesis/restricted.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        votes = 1
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits
