from django.db import models

# Create your models here.
class Entrepreneur(models.Model):
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.business_name