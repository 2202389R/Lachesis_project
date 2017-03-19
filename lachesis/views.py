from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage' : "This app was developed with the authors as well as the readers in mind."}
    return render(request, 'lachesis/index.html', context=context_dict)
def about(request):
    return HttpResponse("This is the about page. <a href='/lachesis/'>View index page</a>")
