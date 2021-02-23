from django.urls import path
from . views import bed_list_view,unitname_create_view,bed_management_detail_view, \
	bed_update_view,bed_create_view,dashboard,bed_delete_view,view_all,unitname_list_view,\
	unitname_detail_view,unitname_update_view,unitname_delete_view

app_name = 'jjrh_bed'
urlpatterns = [
	#dashboard
	path('dashboard/',dashboard,name='dashboard'),
	path('view_all/',view_all,name='view_all'),
	#unit create view
	path('create/unit/',unitname_create_view,name='unit_create'),
	path('units/', unitname_list_view, name='units'),
	path('units/<int:id>/', unitname_detail_view, name='units_detail'),
	path('units/<int:id>/update/', unitname_update_view, name='units_update'),
	path('units/<int:id>/delete/', unitname_delete_view, name='units_delete'),

	#bed create view
	path('',bed_list_view,name='beds'),
	path('create/bed/',bed_create_view,name='bed_create'),
	path('update/<int:id>/',bed_update_view,name='update'),
	path('delete/<int:id>/',bed_delete_view,name='delete'),
	path('detail/<int:id>/',bed_management_detail_view,name='detail')
]