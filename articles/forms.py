from django import forms
from . import models

#this is where we define model forms
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields=['title','body','slug','thumb']