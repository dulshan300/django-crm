from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from leads.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', LandingPageView.as_view(), name="home"),    
    path('leads/',include('leads.urls')),
    
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
