from django.contrib import admin
from django.urls import path, include

from users.views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('register/',UserCreate.as_view()),
    path('api-notes/',include('notes.urls')),
    path('api-timeline/',include('timeline.urls')),
    path('api-remember/',include('remember.urls')),
    # path('users/',include('users.urls')),

]
