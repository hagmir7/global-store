from django.contrib import messages
from django.contrib.messages.api import success
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.utils.translation import gettext as _
from .models import Store
from .forms import CreateStore
from django.views.generic import UpdateView
from django.urls import reverse_lazy
def home(request):
    return render(request, 'home.html')


def settings(request):
    return render(request, 'pages/settings.html')

def language(request):
    return render(request, 'pages/language.html')

def stores(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'pages/stores.html', context)



def create_store(request):
    form = CreateStore()
    if request.method == 'POST':
        form = CreateStore(request.POST, files=request.FILES)
        if form.is_valid:
            new = form.save(commit=False)
            new.user = request.user
            if Store.objects.filter(name=new.name):
                messages.warning(request, _("There is a registred store with this name"))
                return redirect('create_store')
            else:
                new.save()
                return redirect('home')
    context = {'form': form}
    return render(request, 'pages/create-store.html', context)


def store(request,id):
    store = get_object_or_404(Store, id=id,)
    stores = Store.objects.all()
    context = {'store':store,'stores':stores}
    return render(request, 'pages/store.html', context)



class UpdateStore(UpdateView):
    model = Store
    template_name = 'pages/update-store.html'
    form_class = CreateStore

def update_store(request, id):
    store = get_object_or_404(Store, id=id)
    form = CreateStore(instance=store)
    if request.method == 'POST':
        form = CreateStore(request.POST, files=request.FILES)
        if form.is_valid():
            form = store.update()
    context = {'form':form, 'store':store}
    return render(request, 'pages/update-store.html', context)

