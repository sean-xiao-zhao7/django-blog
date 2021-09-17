from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)    

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)   
    email = models.EmailField(null=True) 

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])    
    tags = models.ManyToManyField(Tag, related_name='tags')
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    
