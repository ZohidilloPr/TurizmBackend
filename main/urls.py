from django.urls import path

from main.views import (
    test, 
    testPk, 
    testAll,
    NewsOne,
    #classes
    NewsList,
    AreasList,
    AreasDetail,
)

urlpatterns = [
    path('', test),
    path('pk/', testPk),
    path('all/', testAll),
    path('news/', NewsList.as_view(), name="newslist"),
    path('news/<slug>/', NewsOne, name="newsone"),
    path('areas/', AreasList.as_view(), name="areaslist"),
    path('areas/<slug>/', AreasDetail.as_view(), name="areadetail"),
]