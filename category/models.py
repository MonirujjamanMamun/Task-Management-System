from django.db import models
# from task.models import TaskMode

# Create your models here.


class TaskCategoryModel(models.Model):
    name = models.CharField(max_length=60)
    # task = models.ManyToManyField(TaskMode)

    def __str__(self):
        return self.name
