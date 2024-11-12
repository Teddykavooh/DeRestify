# from django.shortcuts import render -> Default
import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    # return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    # request -> HttpRequest -> Django object
    print("Rada is which!")
    print(request.GET)
    print(request.POST)
    body = request.body # byte str of json data
    data = {}
    try:
        data = json.loads(body) # str -> py dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
