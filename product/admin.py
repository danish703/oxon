from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Post, Bidding, ProdoctImage

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Bidding)
admin.site.register(ProdoctImage)

# Register your models here.
=======
from .models import Category,Post
# Register your models here.
admin.site.register([Category,Post])
>>>>>>> origin
