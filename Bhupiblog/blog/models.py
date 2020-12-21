from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.category_name


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.CharField(default='', max_length=50)
    content1 = models.TextField(max_length=5000, default="", blank=True)
    pub_date = models.DateField()
    slug = models.CharField(max_length=200, default='')
    thumbnail = models.ImageField(upload_to='media/images', default="", blank=True)
    thumbnail1 = models.ImageField(upload_to='media/images', default="", blank=True)
    thumbnail2 = models.ImageField(upload_to='media/images', default="", blank=True)

    def __str__(self):
        return self.title + " By " + self.writer



class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    pub_time = models.DateTimeField(default=now)

    def __str__(self):
        return "comment by " + self.user.username
