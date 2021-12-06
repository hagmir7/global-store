from django.urls import path
from .views import *

urlpatterns = [
    path('settings/', settings, name='settings'),
    path('language/', language, name='language'),
    path('stores/', stores, name='stores'),
    path('create-store/', create_store, name='create_store'),
    path('store/<int:id>/', store, name='store'),
    path('update-store/<int:id>/', update_store , name='update_store')

]