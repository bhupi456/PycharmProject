from django.shortcuts import render, redirect
from .models import Blogpost, Blogcomment
from django.contrib import messages
from blog.templatetags import extras



# Create your views here.

def index(request):
    myposts = Blogpost.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'myposts': myposts})

def education(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Educational':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def technology(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Technology' or post.category == 'Science':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})



def motivational(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Motivational':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def gadgets(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Gadgets':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def sportsfitness(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Sports' or post.category == 'Fitness':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def beautyfashion(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Beauty' or post.category == 'Fashion':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def automobiles(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Automobiles':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def religious(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.subcategory == 'Religious':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def political(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Political':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})


def historical(request):
    myposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    for post in posts:
        if post.category == 'Historical':
            myposts.append(post)
    return render(request, 'blog/index.html', {'myposts': myposts})



def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postID = request.POST.get("postID")
        post = Blogpost.objects.get(post_id=postID)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = Blogcomment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "your comment posted successfully")
        else:
            parent = Blogcomment.objects.get(sno=parentSno)
            comment = Blogcomment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "your reply posted successfully")

    return redirect(f"/{ post.slug}")







def blogpost(request, slug):
    post = Blogpost.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=post, parent=None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)

    relposts = []
    posts = Blogpost.objects.all().order_by('-pub_date')
    count = 0
    for item in posts:

        if count == 10:
            break
        else:
            if item.category == post.category and item.post_id != post.post_id:
                relposts.append(item)
                count = count + 1
    context = {'post': post, 'comments': comments, 'user': request.user, 'repDict': repDict, 'relposts': relposts}
    return render(request, 'blog/blogpost.html', context)


# News system
