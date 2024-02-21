from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True) # when an article is created it is automatically populate this field
    #add in thumbnail later
    #add in author later
    
    def __str__(self) : # displays the string representation of fields
        return self.title