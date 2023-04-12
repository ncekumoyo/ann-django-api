from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)

    def __str__(self):
        return self.name
