from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
