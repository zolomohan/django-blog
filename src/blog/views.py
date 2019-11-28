from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'title': 'Post 1',
    'author': 'John Doe',
    'date_posted': '28th November 2019',
    'content': 'Non mollit sint magna dolore sint aute sunt. Occaecat amet commodo minim occaecat tempor esse nulla quis minim. Eiusmod enim sit enim elit velit excepteur et veniam elit nostrud ad est laboris pariatur. Ex officia dolore non dolore officia cupidatat qui cupidatat eu sunt.'
  },
  {
    'title': 'Post 2',
    'author': 'Jack Doe',
    'date_posted': '27th November 2019',
    'content': 'Non mollit sint magna dolore sint aute sunt. Occaecat amet commodo minim occaecat tempor esse nulla quis minim. Eiusmod enim sit enim elit velit excepteur et veniam elit nostrud ad est laboris pariatur. Ex officia dolore non dolore officia cupidatat qui cupidatat eu sunt.'
  }
]

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})