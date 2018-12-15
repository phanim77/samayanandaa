from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url('^$', TemplateView.as_view(template_name='index.html')),
	url('^about_us', TemplateView.as_view(template_name='about_us.html')),
	url('^natal_horoscope', TemplateView.as_view(template_name='natal_horoscope.html')),
	url('^horary', TemplateView.as_view(template_name='horary.html')),
	url('^annual_horoscopy', TemplateView.as_view(template_name='annual_horoscopy.html')),
	url('^muhurat', TemplateView.as_view(template_name='muhurat.html')),
	url('^remedies', TemplateView.as_view(template_name='remedies.html')),
	url('^matrimonial_horoscope_matching', TemplateView.as_view(template_name='matrimonial_horoscope_matching.html')),
	url('^feedback', TemplateView.as_view(template_name='feedback.html')),
]