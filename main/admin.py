from django.contrib import admin
from .models import (
    Post,
    News,
    Hududlar, 
    NavbarName,
    PhotoArxiv,
    VideoArxiv,
    WebSiteName,
    NavbarItems,
    HeaderSlider,
    BackgroundImage,
    BackgroundImageForNews,
    BackgroundImageForAreas,
)

# Register your models here

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Hududlar)
admin.site.register(PhotoArxiv)
admin.site.register(VideoArxiv)
admin.site.register(NavbarName)
admin.site.register(WebSiteName)
admin.site.register(NavbarItems)
admin.site.register(HeaderSlider)
admin.site.register(BackgroundImage)
admin.site.register(BackgroundImageForNews)
admin.site.register(BackgroundImageForAreas)
