from django.db import models

class cityNameDB(models.Model):
    city = models.CharField(max_length=40)
    def __str__(self):
        return self.city
    @staticmethod
    def delete_all():
        cityNameDB.objects.all().delete()
