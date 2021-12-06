from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_view
from django.utils.translation import gettext as _
urlpatterns = [
    path('update-profile/', login_required(update_profile), name='update_profile'),
    path('<slug:slug>', profile, name='profile'),
    path('login/', login, name='login'),
    path('acounts/register/', register, name='register'),
    path('update-profile/<int:pk>/', login_required(UpdateProfile.as_view()), name='update_profile' ),
    path("update-info/", login_required(update_info), name='update_info'),
    
    # Password Reset
    path('accounts/change-assword/',login_required(PasswordChange.as_view()),name='change_password'),
    path('reset_passaword/', auth_view.PasswordResetView.as_view(template_name='password-reset/reset-password.html',
     title=_('Forgot Password'),success_url = reverse_lazy('password_reset_done_new')), name='reset_password'),
    path('reset_passaword_sent/', posword_reset_done, name='password_reset_done_new'),
    path('accounts/reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password-reset/reset-password-confirm.html', success_url = reverse_lazy('passaword_reset_complet_new')), name='password_reset_confirm'),
    path('reset_passaword_complet/', auth_view.PasswordResetCompleteView.as_view(template_name='password-reset/reset-password-done.html'), name='passaword_reset_complet_new'),
   
    
]
