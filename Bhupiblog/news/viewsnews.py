from django.shortcuts import render
from news.models import Newspost


# Create your views here.
def newsindex(request):
    myposts = Newspost.objects.all().order_by('-pub_date')
    context = {'myposts': myposts}
    return render(request, 'blog/newsindex.html', context)

def world(request):
    myposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'World':
            myposts.append(post)
    return render(request, 'blog/newsindex.html', {'myposts': myposts})

def india(request):
    myposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'India':
            myposts.append(post)
    return render(request, 'blog/newsindex.html', {'myposts': myposts})

def educational(request):
    myposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Educational' or post.category == 'Education':
            myposts.append(post)
    return render(request, 'blog/newsindex.html', {'myposts': myposts})

def sportsnews(request):
    myposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Sports':
            myposts.append(post)
    return render(request, 'blog/newsindex.html', {'myposts': myposts})

def technews(request):
    myposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Technology':
            myposts.append(post)
    return render(request, 'blog/newsindex.html', {'myposts': myposts})


def newspost(request, slug1):
    post = Newspost.objects.filter(slug1=slug1).first()
    relposts = []
    posts = Newspost.objects.all().order_by('-pub_date')
    count = 0
    for item in posts:

        if count == 10:
            break
        else:
            if item.category == post.category and item.news_id != post.news_id:
                relposts.append(item)
                count = count+1
    context = {'post': post, 'relposts': relposts}
    return render(request, 'blog/newspost.html', context)
