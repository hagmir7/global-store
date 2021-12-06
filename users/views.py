from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as login_process
from users.forms import UserCreationForm, UserLoginForm, UpdateProfileForm, UserUpdateInfo
from users.models import Profile
from django.views.generic import UpdateView
# from django.views.generic import ListView, UpdateView, DeleteView,  DetailView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

def update_profile(request):
    return render(request, 'update-profile.html')

def profile(request):
    return render(request, 'profile.html')


def login(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user = authenticate(username=username, password=password)
                login_process(request, user)
                return redirect('home')
            else:
                print('not auth')
        else:
            print('not valide') 
    return render(request, 'registration/login.html')


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            if new_user is not None:
                if new_user.is_active:
                    login_process(request, new_user)
                    return redirect('home')
    context = {'form':form}
    return render(request, 'registration/signin.html', context)



def profile(request,slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile':profile}
    return render(request, 'profile.html', context)




def update_profile(request,username):
    profile = get_object_or_404(Profile, username=username)
    context = {'profile':profile}
    return render(request, 'profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'update-profile.html'
    form_class = UpdateProfileForm

    # success_message = _('Profile updated successfully!')

    

    def get_context_data(self,*arge, **kwargs):
        # if self.request.user == self.model.user:
        if self.request.method == "POST":
            messages.success(_('Profile updated successfully!'))
            
        context =  super(UpdateProfile, self).get_context_data(*arge, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['title'] = _('Update profile')
        context['profile'] = profile
        return context   


def update_info(request):
    confirm = False
    if request.method == 'POST':
        form = UserUpdateInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            confirm = True
    else:
        form = UserUpdateInfo(instance=request.user)
    context = {'form': form, 'confirm':confirm, 'title': _("Contact information")}
    return render(request, 'update-info.html', context)



class PasswordChange(PasswordChangeView):
    template_name = 'password-reset/change-password.html'
    success_url = reverse_lazy('home')

def posword_reset_done(request):
    context = {'title':_("Password reset has been sent")}
    return render(request, 'password-reset/reset-password-done.html', context)
    




