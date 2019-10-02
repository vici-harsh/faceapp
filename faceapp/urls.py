from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faceapp/', include("Demo.urls")),
]
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


# https://upload.wikimedia.org/wikipedia/commons/d/d7/Green_Sea_Turtle_grazing_seagrass.jpg
# https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg
