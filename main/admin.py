from django.contrib import admin
from custom_user.forms import NewPost
from .models import (
    Post,
    News,
    AboutUs,
    Hududlar, 
    Document,
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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'navbaritem', 'uz_title', 'add_time')
    list_filter = ('author', 'navbaritem', 'add_time')
    search_fields = ('uz_title__startwith', 'ru_title__startwith', 'en_title__startwith', )
    ordering = ('-add_time', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'navbar', 'navbaritem', 'uz_title', 'add_time')
    list_filter = ('author', 'navbar', 'navbaritem', 'add_time')
    search_fields = ('uz_title__startwith', 'ru_title__startwith', 'en_title__startwith', )
    ordering = ('-add_time', )


@admin.register(Hududlar)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('id', 'navbar', 'navbaritem', 'uz_title', 'add_time')
    list_filter = ('author', 'navbar', 'navbaritem', 'add_time')
    search_fields = ('uz_title__startwith', 'ru_title__startwith', 'en_title__startwith', )
    ordering = ('-add_time', )


@admin.register(NavbarName)
class NavbarNameAdmin(admin.ModelAdmin):
    list_display = ('uz_name', 'ru_name', 'en_name', 'slug')
    


@admin.register(HeaderSlider)
class HeaderSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'uz_title', 'add_time')
    list_filter = ('add_time', )
    search_fields = ('uz_title__startwith', 'ru_title__startwith', 'en_title__startwith', )
    ordering = ('-add_time', )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'navbar', 'title_uz', 'add_time')
    list_filter = ('navbar', 'add_time')
    search_fields = ('title_uz__startwith', 'title_ru__startwith', 'title_en__startwith')
    ordering = ('-add_time', )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'navbar', 'title_uz', 'add_time')
    list_filter = ('navbar', 'add_time')
    search_fields = ('title_uz__startwith', 'title_ru__startwith', 'title_en__startwith')
    ordering = ('-add_time', )


admin.site.register(PhotoArxiv)
admin.site.register(VideoArxiv)
admin.site.register(WebSiteName)
admin.site.register(NavbarItems)
admin.site.register(BackgroundImage)
admin.site.register(BackgroundImageForNews)
admin.site.register(BackgroundImageForAreas)
