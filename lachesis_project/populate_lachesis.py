import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'lachesis_project.settings')

import django
django.setup()
from lachesis.models import Genre, Story

def populate():
    # First, we will create lists of dictionaries containing the pages
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    fairytales = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/", "views": 35}]

    drama_stories = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 42}]

    other_stories = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/", "views": 72}]

    gens =  {"Fairy Tales": {"stories": fairytales, "views": 128, "likes": 64},
            "Drama": {"pages": drama_stories, "views": 64, "likes": 32},
            "Other ": {"pages": other_stories, "views": 32, "likes": 16}}

    # If you want to add more genres or stories,
    # add them to the dictionaries above.

    # The code below goes through the gens dictionary, then adds each genre,
    # and then adds all the associated stories for that genre.

    for gen, gen_data in gens.items():
        g = add_gen(gen, gen_data["views"], gen_data["likes"])
        for s in gen_data["stories"]:
            gen_page(g, s["title"], s["url"])

    # Print out the categories we have added.
    for g in Genre.objects.all():
        for s in Story.objects.filter(genre=g):
            print("- {0} - {1}".format(str(g), str(s)))

def add_story(gen, title, url, views=0):
    s = Story.objects.get_or_create(genre=gen, title=title)[0]
    s.url=url
    s.views=views
    s.save()
    return s

def add_gen(name, views=0, likes=0):
    g = Genre.objects.get_or_create(name=name)[0]
    g.views=views
    g.likes=likes
    g.save()
    return g

# Start execution here!
if __name__ == '__main__':
    print("Starting Lachesis population script...")
    populate()
