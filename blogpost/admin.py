from django.contrib import admin

from blogpost.models import *

# Register your models here.

admin.site.register(QuestionAnswer)

admin.site.register(ServiceCenter)
admin.site.register(StorePoints)


admin.site.register(MediaBlog)
admin.site.register(BlogPost)
admin.site.register(Video)


admin.site.register(OfferCategory)
admin.site.register(Offer)
