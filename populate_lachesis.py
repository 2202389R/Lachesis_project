import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Lachesis_group_project.settings')
import django
django.setup()
from lachesis.models import Genre, Story, Segment

def populate():
     # First, we will create lists of dictionaries containing the pages
     # we want to add into each genre.
     # Then we will create a dictionary of dictionaries for our genres.
     # This might seem a little bit confusing, but it allows us to iterate
     # through each data structure, and add the data to our models.

     fairytale_stories = [
          {"title": "Cinderella", "author": "Charles Perrault",
           "completed": True, "votes": 54}]

     gens = {"Fairy Tales":{"stories":fairytale_stories, "votes":54}}

     segments = {"Cinderella":{{"segment":1, "text": "hi", "Published": "2015-03-21",
          "closed": True, "option1": "yes", "option2": "no", "option1votes": 34,
                    "option2votes":65}, {"segment":2, "text": "bye", "Published": "2015-04-21",
          "closed": True, "option1": "haha", "option2": "oh", "option1votes": 34,
                    "option2votes":65}}}


      # The code below goes through the gens dictionary, then adds each genre,
      # and then adds all the associated stories for that genre.
      # if you are using Python 2.x then use gens.iteritems() see
      # http://docs.quantifiedcode.com/python-anti-patterns/readability/
      # for more information about how to iterate over a dictionary properly.


     for gen, gen_data in gens.items():
         g = add_gen(gen,gen_data["votes"])
         for s in gen_data["stories"]:
             add_story(g, s["title"],s["author"], s["completed"])

     for se in segments.items():
          if segments[se] == s["title"]:
               add_segment(segments[se],segments[se]["segment"],
                    segments[se]["text"], segment[se]["pub_date"],
                    segment[se]["option1"],segment[se]["option2"],
                    segment[se]["option1votes"],segment[se]["option2votes"])
     
     for s in Story.objects.all():
         for se in segments.items():
              
             add_segment(s, se["text"], se["pub_date"], se["option1"], se["option2"],
                         se["option1votes"], se["option2votes"])

     #print out the categories we have added
     for g in Genre.objects.all():
        for s in Story.objects.filter(genre=g):
            print ("- {0} - {1}".format(str(g),str(s)))

def add_segment(story, segment, text, pub_date=datetime.date.today, option1,
                option2, option1votes= 0, option2votes=0):
    s = Segment.objects.get_or_create(story=story, segment=segment, segment_text=text, pub_date=pub_date,
                                      option1=option1, option2=option2,
                                      option1votes=option1votes, option2votes=option2votes)[0]
    s.save()
    return s

def add_story(gen, title, author, completed = False, votes = 0):
    s = Story.objects.get_or_create(genre=gen, title = title, author=author, completed=completed, votes=votes)[0]
    s.save()
    return s

def add_gen(name,votes=0):
    g = Genre.objects.get_or_create(name=name,votes=votes)[0]
    g.save()
    return g

#Start execution here!
if __name__ == '__main__':
    print("Starting lachesis population script...")
    populate()
