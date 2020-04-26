from django.urls import path
from .views import (
    TimelineList, 
    TimelineCreate,
    TimelineDetail
)


urlpatterns = [
    path('', TimelineList.as_view()),
    path('create/',TimelineCreate.as_view()),
    path('<int:pk>/', TimelineDetail.as_view()),
]