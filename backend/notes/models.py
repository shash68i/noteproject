from django.db import models
from django.contrib.auth.models import User

class NoteTopic(models.Model):
    author = models.ForeignKey(User,related_name='notetopic', 
        on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic[:30]

    class Meta:
        ordering = ('-created',)



class Note(models.Model):
    author = models.ForeignKey(User,related_name='notes',
        on_delete=models.CASCADE)
    notetopic = models.ForeignKey(NoteTopic, related_name='notes',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    takeway = models.TextField()
    tech_detail = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ('-created',)