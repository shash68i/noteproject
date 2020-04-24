from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('notes/',include(notes.urls)),
    path('timeline/',include(timeline.urls)),
    path('remember/',include(remember.urls)),
    path('users/',include(users.urls)),

]
