
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('portfolios/', include('portfolios.urls')),
    path('projects/', include('projects.urls')),
    path('interactions/', include('interactions.urls')),
    path('notifications/', include('notifications.urls'))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
