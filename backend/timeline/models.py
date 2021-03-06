from django.db import models
from django.contrib.auth import get_user_model


class Timeline(models.Model):

    GOAL_CHOICES = (
        ('L', 'Longterm'),
        ('S', 'Shortterm'),
    )
    STATUS_CHOICES = (
        ('O','Ongoing'),
        ('E', 'Ended'),
        ('D', 'Dropped')
    )

    author = models.ForeignKey(get_user_model(),related_name='timeline', 
        on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    goal_term = models.CharField(max_length=1, choices=GOAL_CHOICES)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)