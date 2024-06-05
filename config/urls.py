from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('tweetapp/', include('tweetapp.urls')),
    path('', RedirectView.as_view(url='/tweetapp/')),
]
