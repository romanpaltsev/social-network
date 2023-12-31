from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from posts.views import PostListView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path('profile/', include('profiles.urls', namespace="profile")),
    path('post/', include('posts.urls', namespace="post")),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "core"