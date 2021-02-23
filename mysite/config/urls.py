from django.contrib import admin
from django.urls import path, include
# -----------[edit]-----------
from pybo import views
# -----------[edit]-----------


urlpatterns = [
    path('admin/', admin.site.urls),
# -----------[edit]-----------
    path('pybo/', include('pybo.urls')),
# -----------[edit]-----------

]
