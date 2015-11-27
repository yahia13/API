from django.shortcuts import render
import json


#view request that opens the json file
def apiview(request):

    with open('apir/sheet1.json') as json_data:
        data = json.load(json_data)

    return render(request, 'view.html', {'data':data})