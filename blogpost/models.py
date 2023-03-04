from django.db import models


class MediaBlog(models.Model):
    image = models.ImageField()


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    external_photo = models.ImageField()
    inside_photo = models.ManyToManyField(
        MediaBlog
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    description = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title


class OfferCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    image = models.ImageField(
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        OfferCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="banner_place_category"
    )

    def __str__(self):
        return self.title


class ServiceCenter(models.Model):
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=25)
    mode = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class StorePoints(models.Model):
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
