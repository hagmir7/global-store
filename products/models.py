from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Product images 
class Image(models.Model):
    image = models.ImageField(upload_to="ProductImages")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date


# IP Addriss modes
class Ipaddrisse(models.Model):
    ip = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ip

# Product Size 
class Size(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size

# Product Color
class Color(models.Model):
    color = models.CharField(max_length=100)
    code = models.CharField(max_length=60)

    def __str__(self):
        return self.color

# Product Category
class Categore(models.Model):
    name_en = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CateImage')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_en

# Store type
class StoreType(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Store Model
class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="StoreAvatar")
    cover = models.ImageField(upload_to="StoreCover")
    follow = models.ManyToManyField(User, related_name='store_followers')
    type = models.CharField(max_length=100, blank=True, null=True)
    views = models.ManyToManyField(Ipaddrisse, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.SlugField()


    def __str__(self):
        return self.name
    
    # slugify the Slug
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)


# Shiping type
Shiping = [
    ('NO', 'Not Selected'),
    ('M', 'Free'),
    ('F', 'Buy'),
]

# Products Model
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='product_store')
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    olde_price = models.FloatField(default=0)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    description = models.TextField()
    body = models.TextField()
    tags = models.CharField(max_length=200)
    views = models.ManyToManyField(Ipaddrisse, related_name="veiws")
    cart = models.ManyToManyField(User, blank=True, related_name='add_to_cart')
    like = models.ManyToManyField(User, blank=True, related_name='like_product')
    save_product = models.ManyToManyField(User, related_name="save_product")
    date = models.DateTimeField(auto_now_add=True)
    shiping_info = models.TextField(blank=True, null=True)
    size = models.ManyToManyField(Size, related_name='product_size', blank=True)
    color = models.ManyToManyField(Color, related_name="product_color")
    category = models.ForeignKey(Categore, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=1, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_global = models.BooleanField(default=False)
    is_g = models.FloatField(blank=True, null=True, verbose_name='g ')
    is_kg = models.FloatField(blank=True, null=True, verbose_name='Kg ')
    shiping_type = models.CharField(choices=Shiping, max_length=30, default=1)
    shiping_price = models.FloatField(default=0, blank=True, null=True)


    def __str__(self):
        return self.name

    # slugify the Slug
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)



# Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    customer =  models.CharField(max_length=100)
    phone  = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name="customer_order")
    confirm = models.BooleanField(default=False)
    not_confirm = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.products
    
    






