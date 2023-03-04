from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class EquipmentCategory(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class TypeTireCategory(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title


