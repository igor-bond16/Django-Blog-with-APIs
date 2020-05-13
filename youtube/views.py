from django.shortcuts import render
import requests
from isodate import parse_duration

# Create your views here.
def videos(request):
    API_KEY = 'AIzaSyBYejsp4RvsQptxM_eR-MmFgXFTpX6EJtk'
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    return render(request,'youtube/video.html')