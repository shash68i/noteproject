from django.db import models
from django.contrib.auth import get_user_model

class Remember(models.Model):
    DURATION_CHOICES = (
        ('L','Few Days'),
        ('M', 'Weeks or Months'),
        ('H', 'May new in Future'),
    )

    author = models.ForeignKey(get_user_model(),related_name='reminds', 
        on_delete=models.CASCADE)
    duration = models.CharField(max_length=1, choices=DURATION_CHOICES)
    topic = models.CharField(max_length=255)
    resources = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic[:30]

    class Meta:
        ordering = ('-created',)