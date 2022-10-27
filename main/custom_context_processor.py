from .models import (
    News,
    Masjid,
    Hotels,
    NavbarName,
    PlacesName,
    PhotoArxiv,
    AboutAreas,
    RelaxPlaces,
    WebSiteName,
    NavbarItems,
    NavbarAreasUz,
    HeaderSliders,
    BackgroundImage,
    ArtAndMemorials,
    CafeAndResutaran,
    BackgroundImageForArt,
    BackgroundImageForCafe,
    BackgroundImageForNews,
    BackgroundImageForAreas,
    BackgroundImageForHotel,
    BackgroundImageForRelax,
    BackgroundImageForPhotos,
    BackgroundImageForMasjid,
    BackgroundImageForShrines 
)

def common_variables(request):
    web_name = WebSiteName.objects.last()
    aboutareas = AboutAreas.objects.all()
    areas_uz = NavbarAreasUz.objects.all()
    BgFon = BackgroundImage.objects.last()
    navbarName0 = NavbarName.objects.all()[0]
    navbarName1 = NavbarName.objects.all()[1]
    navbarName2 = NavbarName.objects.all()[2]
    bg_art = BackgroundImageForArt.objects.last()
    bg_cafe = BackgroundImageForCafe.objects.last()
    bg_news = BackgroundImageForNews.objects.last()
    bg_areas = BackgroundImageForAreas.objects.last()
    bg_relax = BackgroundImageForRelax.objects.last()
    bg_hotel = BackgroundImageForHotel.objects.last()
    bg_photo = BackgroundImageForPhotos.objects.last()
    bg_masjid = BackgroundImageForMasjid.objects.last()
    news = News.objects.all().order_by('-add_time')[:8]
    bg_shrines = BackgroundImageForShrines.objects.last()
    masjid = Masjid.objects.all().order_by('-add_time')[:8]
    news_left = News.objects.all().order_by('-add_time')[:4]
    photos = PhotoArxiv.objects.all().order_by('-add_time')[:7]
    shrines = PlacesName.objects.all().order_by('-add_time')[:8]
    slideshow = PhotoArxiv.objects.all().order_by('-add_time')[:100]
    navbaritems = NavbarItems.objects.all().order_by('-add_time')[:3]
    headerslider = HeaderSliders.objects.all().order_by('-add_time')[:4]

    context = {
        'news':news,
        'bgArt':bg_art,
        'bgfon': BgFon,
        'photos':photos,
        'masjid':masjid,
        'bgNews':bg_news,
        'bgCafe':bg_cafe,
        'bgAreas':bg_areas,
        'bgHotel':bg_hotel,
        'bgPhoto':bg_photo,
        'bgRelax':bg_relax,
        'shrines': shrines,
        'nav0':navbarName0, 
        'nav1':navbarName1, 
        'nav2':navbarName2,
        'areas':aboutareas,
        'areas_uz':areas_uz,
        'web_name': web_name,
        'bgMasjid':bg_masjid,
        'news_left':news_left,
        'slideshow':slideshow,
        'bgShrines':bg_shrines,
        'navbaritems':navbaritems,
        'headerslider':headerslider,
    }
    return context
