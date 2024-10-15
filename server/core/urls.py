from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt import views as rviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('login/', rviews.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', rviews.TokenRefreshView.as_view(), name='token_refresh'),
]\
+\
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
