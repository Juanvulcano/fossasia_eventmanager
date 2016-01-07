from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.events, name='events'),
    url(r'^add/',TemplateView.as_view(template_name='addevents.html'), name='addevents'),
    url(r'^test/', views.addevents),    
    url(r'^about/$', views.about, name='about'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^event/(?P<event_title_slug>[\w\-]+)/$', views.details, name='details'),
    url(r'^participate/$', views.participate_event, name='participate_event'),
]


