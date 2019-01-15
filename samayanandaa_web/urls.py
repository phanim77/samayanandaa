from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns = [
#url('^$', TemplateView.as_view(template_name='index.html')),
#url(r'^search-form/$', views.search_form),
url(r'^natal_horoscope$', views.natal_horoscope, name='natal_horoscope'),
url(r'([^/]*)', views.natal_horoscope, name='index'),
]