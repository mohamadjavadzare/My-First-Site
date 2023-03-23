from django.shortcuts import render

# Create your views here.

def blog_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single_view(request):
    context = {'author':'Mikey', 'title':'Mikey has finished his first django project' , 'content':'Hello World! I just finished my first django project successfully.\nBy the way, my real name is Mohmamad Javad Zare, but you can call me Mikey!\nThat\'s all.'}
    return render(request, 'blog/blog-single.html', context)