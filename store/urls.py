from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [path('il8n/', include('django.conf.urls.i18n'))]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('products.urls')),
    path('', home, name='home'),
    path('', include('users.urls'))
)
# Static files 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)