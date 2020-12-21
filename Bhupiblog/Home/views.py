from django.shortcuts import render, HttpResponse, redirect
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blogpost, Blogcomment
from news.models import Newspost

# Create your views here.
def Home(request):
    myposts = Newspost.objects.all().order_by('-pub_date')
    context = {'myposts': myposts}
    return render(request, 'blog/Home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly.")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message saved successfully.")
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')





# for signup
def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for error inputs
        if len(username)<3 or len(username)>10:
            messages.error(request, "username should contain 3 to 10 characters. ")
            return redirect('Home')

        if not username.isalnum():
            messages.error(request, "username should contains only letters and numbers.")
            return redirect('Home')


        if pass1 != pass2:
            messages.error(request, "passwords do not match.")
            return redirect('Home')


        #create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your bhupiblog account has been successfully created.")
        return redirect('Home')

    else:
        return HttpResponse('404 - Not Found')

def Logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('Home')



def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('Home')
        else:
            messages.error(request, "Invalid username and password. Please try again")
            return redirect('Home')
    else:
        return HttpResponse('404 - Not Found')


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


def newspost(request, slug):
    post = Newspost.objects.filter(slug=slug).first()
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

