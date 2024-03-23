from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Podcast

# Create your views here.
def home(request):
    return render(request,'index.html')
# BB
def accueil(request):
    return render(request,'./bb/ACCUEIL.html')
def janvier(request):
    return render(request,'./bb/JANVIER.html')
def fevrier(request):
    return render(request,'./bb/FEVRIER.html')
def mars(request):
    return render(request,'./bb/MARS.html')
def avril(request):
    return render(request,'./bb/AVRIL.html')
def mai(request):
    return render(request,'./bb/MAI.html')
def juin(request):
    return render(request,'./bb/JUIN.html')
def juillet(request):
    return render(request,'./bb/JUILLET.html')
def aout(request):
    return render(request,'./bb/AOUT.html')
def septembre(request):
    return render(request,'./bb/SEPTEMBRE.html')
def octobre(request):
    return render(request,'./bb/OCTOBRE.html')
def novembre(request):
    return render(request,'./bb/NOVEMBRE.html')
def decembre(request):
    return render(request,'./bb/DECEMBRE.html')
# DG
def JANUARY(request):
    return render(request,'./dg/JANUARY.html')
def FEBRUARY(request):
    return render(request,'./dg/FEBRUARY.html')
def MARCH(request):
    return render(request,'./dg/MARCH.html')
def APRIL(request):
    return render(request,'./dg/APRIL.html')
def MAY(request):
    return render(request,'./dg/MAY.html')
def JUNE(request):
    return render(request,'./dg/JUNE.html')
def JULY(request):
    return render(request,'./dg/JULY.html')
def AUGUST(request):
    return render(request,'./dg/AUGUST.html')
def SEPTEMBER(request):
    return render(request,'./dg/SEPTEMBER.html')
def OCTOBER(request):
    return render(request,'./dg/OCTOBER.html')
def NOVEMBER(request):
    return render(request,'./dg/NOVEMBER.html')
def DECEMBER(request):
    return render(request,'./dg/DECEMBER.html')
# JP
def January(request):
    return render(request,'./jp/January.html')
def February(request):
    return render(request,'./jp/February.html')
def March(request):
    return render(request,'./jp/March.html')
def April(request):
    return render(request,'./jp/April.html')
def May(request):
    return render(request,'./jp/May.html')
def June(request):
    return render(request,'./jp/June.html')
def July(request):
    return render(request,'./jp/July.html')
def August(request):
    return render(request,'./jp/August.html')
def September(request):
    return render(request,'./jp/September.html')
def October(request):
    return render(request,'./jp/October.html')
def November(request):
    return render(request,'./jp/November.html')
def December(request):
    return render(request,'./jp/December.html')
def AnglaisAudio(request):
    return render(request,'AnglaisAudio.html')

class RenderHTMLPlayer(TemplateView):
    template_name = "JANVIER.html"
    model = Podcast
    #...
    def get(self, request, *args, **kwargs):
        # Let's get our id from URL
        id = self.kwargs.get('id')

        # then we use this id to find corresponding podcast
        podcast = Podcast.objects.filter(id=id).first()

        # We obtain URL for saved media file.
        podcast_uri = '/media' + \
            request.build_absolute_uri(podcast.file.url).split('media')[1]

        # We finally return the track URL in the context.
        # It's needed to load audio via audio player.
        #context = {'track_url': track_uri}
        #return render(request, self.template_name, context)
    #{% static '' %}
    #dashboard
    

