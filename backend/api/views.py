# from django.shortcuts import render -> Default
import json
from django.http import JsonResponse
from products.models import Product

# Create your views here.
def api_home(request, *args, **kwargs):
    # return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    # request -> HttpRequest -> Django object
    # print("Rada is which!")
    # print(request.GET)
    # print(request.POST)
    # body = request.body # byte str of json data
    # data = {}
    # try:
    #     data = json.loads(body) # str -> py dict
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
