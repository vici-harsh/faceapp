from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView

urlpatterns = [

    path('',views.Home,name='Home'),
    # path('Final/', views.CreatePostView.as_view(), name='add_post'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
