from django.shortcuts import render

posts = [
    {
        'author' : 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First Blog Post Content',
        'date_posted': 'March 15, 2019'
    },
    {
        'author' : 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Secod Blog Post Content',
        'date_posted': 'March 17, 2019'
    },
]

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})