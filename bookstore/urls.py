from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='books.index', permanent=False)),
    path('api/books/', include('books.api.urls')),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('contactus/', include('contactus.urls')),
    path('aboutus/', include('aboutus.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'bookstore.views.custom_404'
