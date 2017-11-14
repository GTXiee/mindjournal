from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.journal_home, name='journal_home'),
    # url(r'^journal/$', views.journal_home, name='journal_home'),
    url(r'^journal/new/$', views.journal_new, name='journal_new'),
    url(r'^journal/entry/(?P<pk>\d+)/', views.journal_detail, name='journal_detail'),
    url(r'^journal/(?P<pk>\d+)/edit/$', views.journal_edit, name='journal_edit'),
    url(r'^journal/quotes/$', views.journal_quotes, name='journal_quotes')
]
