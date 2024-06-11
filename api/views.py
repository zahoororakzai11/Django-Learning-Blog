import json
from django.shortcuts import render
from django.forms.models import model_to_dict  # return python data to dictionary form
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from products.models import Products
from products.serializers import ProductSerializer


# Create your views here.
@api_view(["POST", "GET"])
def api_home(request, *args, **kwargs):
    # request -->HttpRequest--> Django

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        # print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    # model_data = Products.objects.all().order_by("?").first()
    # instance = Products.objects.all().order_by('?').first()
    # if instance:
    #     data = ProductSerializer(instance).data
    # return Response(data)
    # data = {}
    # if model_data:
    #     data = model_to_dict(model_data,fields=['id','title','price']) # return python data in to dictionary

    # json_data_str = json.dump(data)
    # data['id'] = model_data.id
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price

    # Serializer

    # body = request.body # byte string to JSON data
    # #print(body)
    # data = {}
    # try:
    #     data = json.loads(body) # string to JSON data --> Python Data
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type

    # return HttpResponse(data,headers={'content-type':'application/json'})
    # return JsonResponse(data)
    # return Response(data)
