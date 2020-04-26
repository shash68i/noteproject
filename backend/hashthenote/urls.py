from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register/',UserCreate.as_view()),
    path('login/',obtain_auth_token),
    path('api-notes/',include('notes.urls')),
    path('api-timeline/',include('timeline.urls')),
    path('api-remember/',include('remember.urls')),

]
