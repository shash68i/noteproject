from django.urls import path
from .views import (
    NoteTopicList, 
    NoteTopicCreate,
    NoteTopicDetail,
    NoteList,
    NoteCreate,
    NoteDetail,
)


urlpatterns = [
    path('topics/', NoteTopicList.as_view()),
    path('topics/create/', NoteTopicCreate.as_view()),
    path('topics/<int:pk>/', NoteTopicDetail.as_view()),
    path('', NoteList.as_view()),
    path('create/',NoteCreate.as_view()),
    path('<int:pk>/', NoteDetail.as_view()),
]