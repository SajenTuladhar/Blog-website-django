from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article) # lets django know that we want to see article in the admin section