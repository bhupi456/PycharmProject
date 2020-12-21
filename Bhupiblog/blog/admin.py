from django.contrib import admin

# Register your models here.
from .models import Blogpost, Blogcomment,Category


admin.site.register(Blogpost)
admin.site.register(Blogcomment)
admin.site.register(Category)

