from django.db import models

class Todo(models.Model):
    subject=models.CharField(max_length=20)
    details=models.TextField(default="")
    dueDateTime=models.DateTimeField(blank=True, null=True)
    completed=models.BooleanField(default=False)
