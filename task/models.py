from django.db import models
from category.models import TaskCategoryModel
# Create your models here.


class TaskMode(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_complited = models.BooleanField(default=False)
    task_assign_Date = models.DateField()
    category = models.ManyToManyField(TaskCategoryModel)

    def __str__(self):
        return self.title
