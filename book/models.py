from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField(max_length=50, verbose_name='e-mail', blank=True)

    def get_absolute_url(self):
        return reverse('AuthorDetail', args=(self.pk,))

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
    publisher = models.ForeignKey(Publisher)
    published_date = models.DateField()
    
    def __str__(self):
        return self.name