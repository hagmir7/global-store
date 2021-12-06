from django.db import models
from django.contrib.auth.models import User
from django.utils.regex_helper import Choice
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from products.models import Ipaddrisse
from django.urls import reverse





# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', default='user.png', null=True, blank=True)
    cover = models.ImageField(upload_to='cover/', default='cover.png', null=True, blank=True)
    phone = models.IntegerField(default=0)
    gander = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True)
    last_visit = models.DateTimeField(auto_now_add=True)
    verification = models.BooleanField(default=False)
    update = models.DateTimeField(auto_now=True)
    earning = models.FloatField(default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(Ipaddrisse, related_name='profile_views', blank=True)
    is_seller = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True)
    is_privet = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('update_profile', args=[self.id])




    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.date.strftime("%d-%m-%Y")}'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username))
        return super().save(*args, **kwargs)
    