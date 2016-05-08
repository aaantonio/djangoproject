from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    Publisher = models.ForeignKey(Publisher)
    published_date = models.DateField()
    
    def __str__(self):
        return self.name