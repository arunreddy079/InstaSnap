from django.shortcuts import render
from instagram.client import InstagramAPI

# Create your views here.

api = InstagramAPI(access_token='',client_id='',client_secret='')

def index(request):
    result = api.tag_recent_media(tag_name='hello')
    media = result[0]
    stuff = []
    for m in media:
        stuff.append(m.images['standard_resolution'].url)

    print(stuff)

    return render(request,'slideshow/index.html',{'stuff':stuff})
