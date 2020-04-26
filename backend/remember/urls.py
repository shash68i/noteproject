from django.urls import path
from .views import (
    RememberCreate,
    RememberList,
    RememberDetail
)


urlpatterns = [
    path('', RememberList.as_view()),
    path('create/',RememberCreate.as_view()),
    path('<int:pk>/', RememberDetail.as_view()),
]