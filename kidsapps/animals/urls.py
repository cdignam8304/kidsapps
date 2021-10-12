from django.urls import path

# from animals import views
from animals.views import AnimalListView


urlpatterns = [
	# path('', views.index, name='animals-index'),
        path('', AnimalListView.as_view(), name='animal-list'),
]
