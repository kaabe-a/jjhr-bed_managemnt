from django.urls import path
from . views import create_bed_management_view,bed_management_view

urlpatterns = [

	path('',create_bed_management_view,name='bed_management'),
	path('beds/',bed_management_view,name='beds'),
]