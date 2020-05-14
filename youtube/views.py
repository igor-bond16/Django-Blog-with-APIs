from django.shortcuts import render
import requests
from isodate import parse_duration
from django.core.paginator import Paginator

# Create your views here.
def videos(request):
    videos = []
    if request.method == 'POST':
        API_KEY = 'AIzaSyBYejsp4RvsQptxM_eR-MmFgXFTpX6EJtk'
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        search_params = {
            'part':'snippet',
            'q':request.POST['search'],
            'key':API_KEY,
            'maxResults':50,
            'type':'video',
            }    
        video_ids = []   
        r = requests.get(search_url,search_params)
        results = r.json()['items']
        for result in results:
            video_ids.append(result['id']['videoId'])

        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        parametor_list = ['snippet','contentDetails']
        video_params = {
            'part':parametor_list,
            'key':API_KEY,
            'id':','.join(video_ids),
            'maxResults':10
            }
        r = requests.get(video_url,video_params)
        results2 = r.json()['items']

        
        for result in results2:
            results =  {
                'title':result['snippet']['title'],
                'id':result['id'],
                'url':f'https://www.youtube.com/watch?v={result["id"]}',
                'duration':int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
             #   'likes':result['contentDetails']['like']['kind']
                'thumbnail':result['snippet']['thumbnails']['default']['url']
            }
            print(str(result['contentDetails']['like']['kind']))
            videos.append(results)
    else:
        videos = []
    return render(request,'youtube/video.html',{'videos':videos})