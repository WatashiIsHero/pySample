from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('tweetapp/', include('tweetapp.urls')),
    path('', RedirectView.as_view(url='/tweetapp/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)