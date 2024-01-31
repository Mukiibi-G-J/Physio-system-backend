
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include("products.urls")),
    path("api/auth/", include("authentication.urls", namespace="authentication")),
    # path("authentication/", include("authentication.urls", namespace="authentication")),
    # path("", include("main.urls", namespace="main")),
    # path("physio_session/", include("physiosession.urls", namespace="physiosession")),
    path("patients/", include('patients.urls', namespace="patients"))
    
]
# ]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)