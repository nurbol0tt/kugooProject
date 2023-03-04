from django.db import models

from product.models.category_models import Status


class Addition(models.Model):
    subItem = models.CharField(max_length=55)

    def __str__(self):
        return self.subItem


class Menu(models.Model):
    title = models.CharField(max_length=55)
    subItem = models.ForeignKey(
        Addition,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class MediaBanner(models.Model):
    image = models.ImageField()


class PlaceCategory(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=125)
    image = models.ManyToManyField(
        MediaBanner,
        related_name="product_image"
    )
    status_category = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="banner_status_category"
    )
    place_category = models.ForeignKey(
        PlaceCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="banner_place_category"
    )


class TypeCategory(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class TechnologyCategory(models.Model):
    titleType = models.CharField(max_length=55)

    def __str__(self):
        return self.titleType


class ForWhomCategory(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class SubItems(models.Model):
    titleType = models.ForeignKey(
        TechnologyCategory,
        on_delete=models.SET_NULL,
        null=True

    )
    subItems = models.ManyToManyField(
        ForWhomCategory,
        related_name='form_whom_list'
    )


class CatalogCategory(models.Model):
    title = models.ForeignKey(
        TypeCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    subItems = models.ManyToManyField(
        SubItems
    )
