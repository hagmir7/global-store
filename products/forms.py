from .models import Store
from django import forms
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _




class CreateStore(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'avatar', 'cover', 'type', 'description')

    
    # def clean_name(self):
    #     clean = self.cleaned_data
    #     if Store.objects.filter(name=clean['name']).exists():
    #         raise ValidationError(_('There is a registerd sotre with this name!'))
    #     return clean['name']
