# guybilbe/urls.py
from django.urls import path
from .views import RenderHTMLPlayer # We are about to make this view in next step.

urlpatterns = [
    # This is our URL int id attribute we later get with KWARGS.
    path("/<int:id>", RenderHTMLPlayer.as_view(), name="podcasts-player"),
    # id is automatically generated on created new Podcast so if you have
    # uploaded your first file via admin you should have one podcast with id=1
]
