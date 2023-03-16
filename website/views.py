from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse('<h1 style="background-color:powderblue; color=blue;font-family:courier;font-size=600%;text-align:center">Home Page\n<p>hello world!</p></h1>')


def about_view(request):
    return JsonResponse({'Name':'mmd javad' , 'Last name': 'Zare' , 'Nickname': 'Mikey' , 'Birthday':'3/28/2002'})


def contact_view(requset):
    pass

