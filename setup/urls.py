from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from setup.views import redirect_to_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='root_redirect'),
    path('', include('users.urls')),
]
