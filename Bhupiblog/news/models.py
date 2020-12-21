from django.db import models

# Create your models here.
class Newspost(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=10000, default="")
    slug1 = models.CharField(max_length=400, default='')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='news/images', default="")

    def __str__(self):
        return self.title[0:20]