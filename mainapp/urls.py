from django.conf.urls import url
from . import views


app_name = 'mainapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<id>[\w{}.-]{1,40})/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^question/$', views.QuestionCreate.as_view(), name='question-add'),
    # contac section
    url(r'^contactus/$', views.ContactUs.as_view(), name='contactus'),
    url(r'^workinghours/$', views.WorkingHours.as_view(), name='WorkingHours'),
    url(r'^prices/$', views.Prices.as_view(), name='prices'),
    url(r'^personal/$', views.PersonalView.as_view(), name='personal'),
    url(r'^personal/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='personaldetail'),
    # articles section
    url(r'^articles/$', views.Articles.as_view(), name='articles'),
    url(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(), name='articledetail'),
    # gallery
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    # services
    url(r'^services/(?P<pk>[0-9]+)$', views.ServicesView.as_view(), name='services'),
    # send email
]
