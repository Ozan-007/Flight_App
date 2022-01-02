from django.urls import path
from django.urls.conf import include

from accounts.views import ListCreateAccountView, RetrieveUpdateDestroyAccountView

urlpatterns = [
    path('', ListCreateAccountView.as_view(), name="List & Create"),
    path('<int:pk>', RetrieveUpdateDestroyAccountView.as_view(), name="Retrieve Update Delete"),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
