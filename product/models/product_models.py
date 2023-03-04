from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta

from product.models.category_models import Status
from product.models.misc_models import TypeCategory, TechnologyCategory, ForWhomCategory


class GuaranteeCategory(models.Model):
    title = models.CharField(max_length=55)
    price = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )


class AdditionalServicesCategory(models.Model):
    title = models.CharField(max_length=55)
    price = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    discount = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )


class GiftWrappingCategory(models.Model):
    title = models.CharField(max_length=125)
    expires_at = models.DateTimeField()

    def set_expiration_time(self, hours=0, minutes=0, seconds=0):
        now = datetime.now()
        expiration_time = now + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.expires_at = expiration_time

    def is_expired(self):
        return datetime.now() > self.expires_at


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Category(models.Model):
    feature = models.ManyToManyField(
        'KeyFeatures',
        null=True
    )
    guarantee = models.ForeignKey(
        GuaranteeCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    additional_services = models.ForeignKey(
        AdditionalServicesCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    gift_wrapping = models.ForeignKey(
        GiftWrappingCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    tech_category = models.ForeignKey(
        TypeCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    catalog_category = models.ForeignKey(
        TechnologyCategory,
        # 'TitleProduct'
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.ManyToManyField(
        ForWhomCategory,
        related_name="product_type_category"
    )


class WhatsIncluded(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class KeyFeatures(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


# Final
class AboutProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    included = models.ManyToManyField(
        WhatsIncluded,
        blank=True,
    )
    key_features = models.ManyToManyField(
        KeyFeatures,
        blank=True,
    )


class NameCharacter(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


# Final
class ValueCharacter(models.Model):
    description = models.CharField(max_length=255)
    key_features = models.ForeignKey(
        NameCharacter,
        on_delete=models.SET_NULL,
        null=True
    )


# Final
class Media(models.Model):
    image = models.ImageField(blank=True)


class PaymentCategory(models.Model):
    title = models.CharField(max_length=55)


class DeliveryCategory(models.Model):
    title = models.CharField(max_length=255)


# Final
class DeliveryPayment(models.Model):
    payment = models.ForeignKey(
        PaymentCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    delivery = models.ForeignKey(
        DeliveryCategory,
        on_delete=models.SET_NULL,
        null=True
    )


class Warranty(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


class VersionMax(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )


class Comment(models.Model):
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        "Messages",
        max_length=5000
    )
    parent = models.ForeignKey(
        'self', verbose_name="Parent",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children"
    )
    product = models.ForeignKey(
        "Product",
        verbose_name="product",
        on_delete=models.CASCADE,
        null=True,
        related_name="reviews"
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    # def __str__(self):
    #     return f"{self.username} - {self.product}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ManyToManyField(
        Media,
        blank=True,
    )
    about_product = models.ForeignKey(
        AboutProduct,
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    character = models.ManyToManyField(
        ValueCharacter,
        blank=True
    )
    status = models.ManyToManyField(
        Status,
        blank=True
    )
    deliver_payment = models.ForeignKey(
        DeliveryPayment,
        on_delete=models.SET_NULL,
        null=True
    )
    warranty = models.ManyToManyField(
        Warranty,
        blank=True
    )
    version_max = models.ForeignKey(
        VersionMax,
        on_delete=models.SET_NULL,
        null=True
    )
    color = models.ManyToManyField(
        Color,
        blank=True
    )
    bought = models.IntegerField(
        default=0
    )
    article = models.CharField(max_length=55)
    in_stock = models.BooleanField(default=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="product_user"
    )
    likes = models.ManyToManyField(
        User,
        related_name='product_likes',
        default=[0]
    )
    views = models.IntegerField(default=0)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
