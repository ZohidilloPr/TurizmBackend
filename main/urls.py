from django.urls import path
from main.models import PhotoArxiv

from main.views import (
    test, 
    testPk, 
    testAll,
    PostType,
    PostView,
    #classes
    NewsList,
    NewsDetail,
    AreaList,
    AreaDetail,
    PhotosList,
)

urlpatterns = [
    # for test
    path('', test),
    path('pk/', testPk),
    path('all/', testAll),
    path('posts/<slug>/', PostType, name="poststype"),
    path('post/<slug>/', PostView, name="postview"),
    # for news

    path('news/', NewsList.as_view(), name='newslist'),
    path('news/<slug>/', NewsDetail.as_view(), name='newsdetail'),
    # for areas
    
    path('areas/', AreaList.as_view(), name="areaslist"),
    path('areas/<slug>', AreaDetail.as_view(), name="areadetail"),
    # for photo albom

    path('photos/', PhotosList.as_view(), name="photoslist"), 

]