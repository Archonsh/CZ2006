from django.urls import path
from .views import SchoolListView,SchoolDetailView,saveToList

urlpatterns = [
	path('', SchoolListView.as_view(), name='kindergarten-list'),
    path('<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path(r'^(?P<pk>)/$',saveToList,name ='saveToList')
]