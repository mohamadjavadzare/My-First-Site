from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(requset):
    return render(requset, 'website/contact.html')

def test_view(requset):
    return render(requset, 'website/test.html')
