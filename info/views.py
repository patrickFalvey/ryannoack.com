from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Gig, Bio, Video

# Create your views here.
def home(request):
    context = {}
    context['Gigs'] = Gig.objects.all()
    context['BioWords'] = Bio.objects.all()
    urls = Video.objects.all()
    for url in urls: 
        if url.active:
            context['video_url'] = url.url.replace('/watch?v=','/embed/')
            return render_to_response("info/index.html", context)
    else:
        if len(urls) > 0:
            context['video_url'] = urls[0].url.replace('/watch?v=','/embed/')
        else:
            context['video_url'] = 'https://www.youtube.com/embed/Z49zpEWgUA4'           
    
    return render_to_response("info/index.html", context)
 