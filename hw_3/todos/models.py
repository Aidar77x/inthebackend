from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)  # False - невыполнено, True - выполнено

    def _str_(self):
        return self.title

# Create your models here.
