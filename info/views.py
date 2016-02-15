from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Gig, Bio

# Create your views here.
def home(request):
    return render_to_response("info/index.html", {"Gigs": Gig.objects.all(), "BioWords": Bio.objects.all()})
