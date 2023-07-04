from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "facialRocognitionUrls"


urlpatterns = [
    path('', views.IndexView.as_view(), name='indexPage'),
    path('about', views.AboutView.as_view(), name='aboutPage'),
    path('account', views.AccountView.as_view(), name='accountPage'),
    path('bed', views.BedView.as_view(), name='bedPage'),
    path('chair', views.ChairView.as_view(), name='chairPage'),
    path('contacts', views.ContactsView.as_view(), name='contactsPage'),
    path('desk', views.DeskView.as_view(), name='deskPage'),
    path('face', views.FaceView.as_view(), name='facePage'),
    path('sofa', views.SofaView.as_view(), name='sofaPage'),
    path('wordrope', views.WordropeView.as_view(), name='wordropePage'),

]



urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
