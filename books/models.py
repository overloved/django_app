from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
    	return self.name

    # default order_by 
    class Meta:
    	ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

# Customized manager of Book, contains custom funtions
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()

# first define the manager subclass
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(author="Dahl")

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    objects = models.Manager() # the default manager
    dahl_objects = DahlBookManager() # the specific manager