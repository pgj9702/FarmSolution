# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from crops import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crops/', include('crops.urls'))
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('crops/', include('crops.urls'))
# ]