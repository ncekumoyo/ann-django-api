from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Entities"

    def __str__(self):
        return self.name
