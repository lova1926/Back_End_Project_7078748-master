from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Goal {self.id} by {self.user.username}"




