from django.shortcuts import render
from txtoflow import txtoflow
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import base64
import string
import random
import os

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'pcf/index.html')

@csrf_exempt
def generateimg(request):
    text_data = request.POST.get('textData')
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))
    temp_file_path = "./tempdata/{}.jpg".format(res)
    try:
        txtoflow.generate(text_data, outFile=temp_file_path)
        img_file = open(temp_file_path, "rb")
        img_str = base64.b64encode(img_file.read())
        os.remove(temp_file_path)
    except Exception as e:
        img_str = 'Error: ' + str(e)


    return HttpResponse(img_str)
