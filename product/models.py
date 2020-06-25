from django.db import models
from account.models import Account
from  ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    minimumprice= models.FloatField()
    postdate = models.DateField(auto_now=True)
    lastbiddate = models.DateField()
    cover_image = models.ImageField(upload_to='converimage/')
    dayused = models.PositiveIntegerField(blank=True,null=True)
    conditionaldescription = RichTextField()
    description = RichTextField()
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title