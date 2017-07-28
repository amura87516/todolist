from django.conf.urls import url
import django.contrib.auth.views as auth_view
from . import views

app_name = 'todolist'

urlpatterns = [

	url(r'^$', views.home, name='home'),
	url(r'^index$', views.index, name='index'),
	
	
	url(r'^login/', auth_view.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$',views.logout ,name='logout'),
	url(r'^register/', views.register, name='register'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^profile_submit/', views.profile_submit, name='profile_submit'),

	url(r'^complete/$', views.complete,name='complete'),
	url(r'^expired/$', views.expired, name='expired'),
	url(r'^tobedoned/$', views.tobedoned, name='tobedoned'),
	
	url(r'^(?P<tobedone_id>[0-9]+)/$', views.detail, name='detail'),
	
	url(r'^add/$', views.add,name='add'),
	url(r'^add_submit/$', views.add_submit,name='add_submit'),
	url(r'^update_submit/$', views.update_submit,name='update_submit'),
	url(r'^delete_submit/$', views.delete_submit,name='delete_submit'),
]
