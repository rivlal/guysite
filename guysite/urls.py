"""
URL configuration for guysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guybible.views import home,accueil,janvier,fevrier,mars,avril,mai,juin,juillet,aout,septembre,octobre,novembre,decembre,JANUARY,FEBRUARY,MARCH,APRIL,MAY,JUNE,JULY,AUGUST,SEPTEMBER,OCTOBER,NOVEMBER,DECEMBER,January,February,March,April,May,June,July,August,September,October,November,December
from guybible.views import AnglaisAudio
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home),
    path('accueil/',accueil,name='accueil'),
    path('janvier/',janvier,name='janvier'),
    path('fevrier/',fevrier,name='fevrier'),
    path('mars/',mars,name='mars'),
    path('avril/',avril,name='avril'),
    path('mai/',mai,name='mai'),
    path('juin/',juin,name='juin'),
    path('juillet/',juillet,name='juillet'),
    path('aout/',aout,name='aout'),
    path('septembre/',septembre,name='septembre'),
    path('octobre/',octobre,name='octobre'),
    path('novembre/',novembre,name='novembre'),
    path('decembre/',decembre,name='decembre'),
    path('JANUARY/',JANUARY,name='JANUARY'),
    path('FEBRUARY/',FEBRUARY,name='FEBRUARY'),
    path('MARCH/',MARCH,name='MARCH'),
    path('APRIL/',APRIL,name='APRIL'),
    path('MAY/',MAY,name='MAY'),
    path('JUNE/',JUNE,name='JUNE'),
    path('JULY/',JULY,name='JULY'),
    path('AUGUST/',AUGUST,name='AUGUST'),
    path('SEPTEMBER/',SEPTEMBER,name='SEPTEMBER'),
    path('OCTOBER/',OCTOBER,name='OCTOBER'),
    path('NOVEMBER/',NOVEMBER,name='NOVEMBER'),
    path('DECEMBER/',DECEMBER,name='DECEMBER'),
    path('January/',January,name='January'),
    path('February/',February,name='February'),
    path('March/',March,name='March'),
    path('April/',April,name='April'),
    path('May/',May,name='May'),
    path('June/',June,name='June'),
    path('July/',January,name='July'),
    path('August/',August,name='August'),
    path('September/',September,name='September'),
    path('October/',October,name='October'),
    path('November/',November,name='November'),
    path('December/',December,name='December'),
    path('AnglaisAudio/',AnglaisAudio,name='AnglaisAudio'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
