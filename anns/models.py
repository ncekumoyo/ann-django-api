from django.db import models
from entities.models import Entity
from departments.models import Department

class Ann(models.Model):
    date_created = models.DateField(auto_created=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    venue = models.CharField(max_length=100, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)

    def __str__(self):
        return self.title
