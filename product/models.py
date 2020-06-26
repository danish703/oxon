from django.db import models
from account.models import Account
<<<<<<< HEAD
from ckeditor.fields import RichTextField

product_status = (('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject'))

=======
from  ckeditor.fields import RichTextField
>>>>>>> origin
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
<<<<<<< HEAD
    image = models.ImageField(upload_to = 'category/')
=======
    image = models.ImageField(upload_to='category/')
>>>>>>> origin

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    minimumprice = models.FloatField()
    postdate = models.DateField(auto_now=True)
    lastbiddate = models.DateField()
    cover_image = models.ImageField(upload_to = 'coverimage/')
    dayused = models.PositiveIntegerField(blank=True, null =True)
    description = RichTextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class ProdoctImage(models.Model):
    imageURL = models.ImageField(upload_to='product/')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.imageURL

class Bidding(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    bidingprice = models.FloatField()
    date = models.DateField(auto_now=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=product_status)
=======
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
>>>>>>> origin
