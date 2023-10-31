from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import IndexPage


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "core"