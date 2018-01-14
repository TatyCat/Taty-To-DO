from django.db import models
from django.utils import timezone

class Todo(models.Model): 
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default = timezone.now)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.text
