"""bhupiblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import viewsblog
from news import viewsnews

admin.site.site_header = 'Bhupiblog Admin'
admin.site.site_title = 'Bhupiblog Admin Panel'
admin.site.index_title = 'Welcome to Bhupiblog Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('news/', include('news.urls')),
    path('educational', viewsnews.educational, name='educational'),
    path('world', viewsnews.world, name='world'),
    path('india', viewsnews.india, name='india'),
    path('education', viewsblog.education, name='education'),
    path('sportsnews', viewsnews.sportsnews, name='sportsnews'),
    path('technews', viewsnews.technews, name='technews'),
    path("technology", viewsblog.technology, name="technology"),
    path("gadgets", viewsblog.gadgets, name="gadgets"),
    path("sportsfitness", viewsblog.sportsfitness, name="sportsfitness"),
    path("beautyfashion", viewsblog.beautyfashion, name="beautyfashion"),
    path("motivational", viewsblog.motivational, name="motivational"),
    path("automobiles", viewsblog.automobiles, name="automobiles"),
    path("religious", viewsblog.religious, name="religious"),
    path("political", viewsblog.political, name="political"),
    path("historical", viewsblog.historical, name="historical"),
    path('', include('Home.urls')),
    path("<str:slug>", viewsblog.blogpost, name="blogHome"),
    path("news/<str:slug1>", viewsnews.newspost, name="newsHome"),
    path('blog/postComment', viewsblog.postComment, name='postComment'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


