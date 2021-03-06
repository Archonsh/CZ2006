from django.urls import path
from .views import SchoolListView, SchoolDetailView, saveToList, guided_search, advanced_search, deleteFromList

urlpatterns = [
	path('guide_search/', guided_search, name='school'),

	# ex: /polls/5/
	path('advance/', advanced_search, name='detail'),
	path('', SchoolListView.as_view(), name='kindergarten-list'),
	path('<int:pk>/', SchoolDetailView.as_view(), name='kindergarten-detail'),
	path(r'^(?P<pk>)/save$', saveToList, name='saveToList'),
	path(r'^(?P<pk>)/delete$', deleteFromList, name='deleteFromList')
]
