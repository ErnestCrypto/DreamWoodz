from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "facialRocognitionUrls"


urlpatterns = [
    path('home/<str:pk>/', views.home_view, name='indexPage'),
    path('about/<str:pk>/', views.AboutView.as_view(), name='aboutPage'),
    path('account', views.AccountView.as_view(), name='accountPage'),
    path('bed/<str:pk>/', views.BedView.as_view(), name='bedPage'),
    path('chair/<str:pk>/', views.ChairView.as_view(), name='chairPage'),
    path('contacts/<str:pk>/', views.ContactsView.as_view(), name='contactsPage'),
    path('desk/<str:pk>/', views.DeskView.as_view(), name='deskPage'),
    # path('face/<str:pk>/', views.FaceView.as_view(), name='facePage'),
    path('sofa/<str:pk>/', views.SofaView.as_view(), name='sofaPage'),
    path('wordrope/<str:pk>/', views.WordropeView.as_view(), name='wordropePage'),
    path('face_recognition/', views.face, name='face'),


    path('login/', views.login_view, name='login'),
    # path('logout', views.logout_view, name='logout'),
    path('classify/', views.find_user_view, name='classify'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
