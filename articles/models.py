from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True) # when an article is created it is automatically populate this field
    thumb = models.ImageField(default='default.png',blank=True)
    #add in author later
    
    def __str__(self) : # displays the string representation of fields
        return self.title
    
    def snippet(self):
        return self.body[0:70]+'....' # displays only 50 characters on the article page and .... in the end