from django.conf import urls
from . import views
from django.urls import path
urlpatterns=[

    path('',views.translator,name="translator_view")


]
