from django.db import models
from custom_user.models import CustomUser
# Create your models here.

# max_length
# verbose_name

# globals varible
l = 200
m = models
M = m.Model

statusUz = (
    ('tuman', 'tuman'),
    ('shaxar', 'shaxar')
)
statusRu = (
    ('город', 'город'),
    ('район', 'район')
)
statusEn = (
    ('city', 'city'),
    ('district', 'district')
)

class AutoDate(M):
    uz_name = m.CharField(max_length=l)
    ru_name = m.CharField(max_length=l, null=True, blank=True)
    en_name = m.CharField(max_length=l, null=True, blank=True)
    add_time = m.DateTimeField(auto_now_add=True)
    post_view = m.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.uz_name

class BlogsBase(M):
    """ Hamma Postlar uchun asosiy qismlar """
    author = m.ForeignKey(CustomUser, on_delete=m.CASCADE)
    post_img = m.ImageField(upload_to='posts/')
    uz_title = m.CharField(max_length=l)
    ru_title = m.CharField(max_length=l, null=True, blank=True)
    en_title = m.CharField(max_length=l, null=True, blank=True)
    uz_description = m.CharField(max_length=100)
    ru_description= m.CharField(max_length=l, null=True, blank=True)
    en_description= m.CharField(max_length=l, null=True, blank=True)
    uz_post = m.TextField()
    ru_post = m.TextField(null=True, blank=True)
    en_post = m.TextField(null=True, blank=True)
    slug = m.SlugField(max_length=l, unique=True)
    post_view = m.IntegerField(default=0, null=True, blank=True)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uz_title

class Address(M):
    author = m.ForeignKey(CustomUser, on_delete=m.CASCADE)
    name = m.CharField(max_length=l)
    phone = m.IntegerField()
    extra_phone = m.IntegerField(null=True)
    email = m.EmailField(max_length=l, null=True)
    web_site = m.URLField(max_length=l, null=True)
    uz_address = m.CharField(max_length=l)
    en_address = m.CharField(max_length=l)
    ru_address = m.CharField(max_length=l)

    def __str__(self):
        return self.name

class NavbarName(M):
    """ Navbar nomi """
    uz_name = m.CharField(max_length=l)
    ru_name = m.CharField(max_length=l, null=True, blank=True)
    en_name = m.CharField(max_length=l, null=True, blank=True)
    add_time = m.DateTimeField(auto_now_add=True)
    post_view = m.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.uz_name

class NavbarAreasUz(M):
    """ Tuman va shaxarlar lang=uz """
    uz_name = m.CharField(max_length=l, unique=True)
    status = m.CharField(max_length=l, choices=statusUz)
    navbar = m.ForeignKey(NavbarName, on_delete=m.CASCADE)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uz_name

class NavbarAreasRu(M):
    """ Tuman va shaxarlar lang=ru """
    ru_name = m.CharField(max_length=l, unique=True)
    status = m.CharField(max_length=l, choices=statusRu)
    navbar = m.ForeignKey(NavbarName, on_delete=m.CASCADE)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ru_name

class NavbarAreasEn(M):
    """ Tuman va shaxarlar lang=en """
    en_name = m.CharField(max_length=l, unique=True)
    status = m.CharField(max_length=l, choices=statusEn)
    navbar = m.ForeignKey(NavbarName, on_delete=m.CASCADE)
    add_time = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en_name

class NavbarItems(AutoDate):
    """ Boshqa navbarlar uchun items """
    navbar = m.ForeignKey(NavbarName, on_delete=m.CASCADE)

    def __str__(self):
        return super().__str__()

class PlacesName(AutoDate):
    """ "#Diqqatga sazovor joylar" uchun """
    navbarname = m.ForeignKey(NavbarName, on_delete=m.SET_NULL, null=True)
    def __str__(self):
        return super().__str__()


class WebSiteName(AutoDate):
    logo = m.ImageField(upload_to='logo/', default='default/logo.png')
    """ NavBardagi web site nomi """
    def __str__(self):
        return super().__str__()

class HeaderSliders(BlogsBase):
    """ Bosh sahifadagi Slider uchun """

    def __str__(self):
        return super().__str__()

class News(BlogsBase):
    """ Yangiliklar uchun """

    def __str__(self):
        return super().__str__()

class AboutAreas(BlogsBase):
    """ Hududlar xaqida malumot uchun """

    def __str__(self):
        return super().__str__()

class PhotoArxiv(AutoDate):
    """ Gallareya uchun modal """
    photo = m.ImageField(upload_to="photo_arxiv/")
    def __str__(self):
        return super().__str__()
    
class Masjid(BlogsBase):
    """ Masjid va Madrasalar """

    def __str__(self):
        return super().__str__()

class CafeAndResutaran(Address):
    """ Kafe va Restaranlar """

    def __str__(self):
        return super().__str__()

class Hotels(Address):
    """ Mehmonxonalar """
    hotel_img = m.ImageField(upload_to='hotels_images/', default='default/hotel.jpg')
    hotel_description_uz = m.TextField()
    hotel_description_ru = m.TextField()
    hotel_description_en = m.TextField()

    def __str__(self):
        return super().__str__()

class RelaxPlaces(Address):
    """ Dam olish maskanlari """
    place_img = m.ImageField(upload_to='hotels_images/', default='default/hotel.jpg')
    place_description_uz = m.TextField()
    place_description_ru = m.TextField()
    place_description_en = m.TextField()

    def __str__(self):
        return super().__str__()

class ArtAndMemorials(BlogsBase):
    """ San'at va Yodgorliklar """
    def __str__(self):
        return super().__str__()

class BackgroundImage(M):
    bg_img = m.ImageField(upload_to='backgroundImage/')

    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForNews(M):
    """ Yangiliklar bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForNews/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForAreas(M):
    """ Hududlar bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForAreas/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForMasjid(M):
    """ Masjid bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForMasjid/')
    
    def __str__(self):
        return str(self.bg_img)    
    
class BackgroundImageForPhotos(M):
    """ Rasmlar bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForPhotos/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForShrines(M):
    """ Ziyoratgohlar bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForShrines/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForCafe(M):
    """ Kafe bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForCafe/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForHotel(M):
    """ Mehmonxona bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForHotel/')
    
    def __str__(self):
        return str(self.bg_img)
    
class BackgroundImageForRelax(M):
    """ Dam olish maskanlari bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForRelax/')
    
    def __str__(self):
        return str(self.bg_img)
    
    
class BackgroundImageForArt(M):
    """ San'at va yodgorliklar bo'limiga rasm """
    bg_img = m.ImageField(upload_to='BackgroundImageForRelax/')
    
    def __str__(self):
        return str(self.bg_img)
    