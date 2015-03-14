from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_app.views import hello, current_datetime, hours_ahead
from books import views as books_views
from contact import views as contact_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# url(r'^$', my_homepage_view),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search-form/$', books_views.search_form),
    url(r'^search/$', books_views.search),
    url(r'^contact-us/$', contact_views.contact),
)
