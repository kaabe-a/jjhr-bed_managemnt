from django.urls import path
from . views import create_bed_management_view,bed_management_view,bed_management_detail_view

app_name = 'jjrh_bed'
urlpatterns = [
	path('',bed_management_view,name='bed_management'),
	path('create/',create_bed_management_view,name='create'),
	path('detail/<int:id>/',bed_management_detail_view,name='detail')
]