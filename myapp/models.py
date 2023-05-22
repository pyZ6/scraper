from django.db import models

class Links(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=500, null=True, blank=True)
    linkk = models.CharField(max_length=500, null=True, blank=True)