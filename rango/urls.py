from django.conf.urls import include, url
from rango import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^mir/', views.mir, name='mir'),
    url(r'^hello/', views.hello, name='hello'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^page/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'search/$', views.search, name='search')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

