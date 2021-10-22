from django.urls import path

# from animals import views
from animals.views import AnimalListView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	# path('', views.index, name='animals-index'),
        path('', AnimalListView.as_view(), name='animal-list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)