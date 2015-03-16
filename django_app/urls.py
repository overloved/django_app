from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
# from django_app.views import hello, current_datetime, hours_ahead
# from books import views as books_views
from django_app.views import index
from contact import views as contact_views

#generic views of objects
from django.views.generic.list import ListView
# from books.models import Publisher

# publisher_info = {
#     'queryset': Publisher.objects.all(),
#     'template_name': 'publisher_list_page.html',
#     'template_object_name': 'publisher',
#     #add extra context
#     'extra_context': { 'book_list': Book.objects.all }
# }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^$', index),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact-us/$', contact_views.contact),
    # url(r'^hello/$', hello),
    # url(r'^time/$', current_datetime),
    # url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # url(r'^search-form/$', books_views.search_form),
    # url(r'^search/$', books_views.search),
    
    # url(r'^about/$', TemplateView, { 'template': 'about.html' }),
    # url(r'^about/(\w+)/$', books_views.about_pages),
    # url(r'^publishers/$', ListView.as_view(), publisher_info),   
)

# Customer
urlpatterns += patterns('customer.views', 

    url(r'^customer/login/$', 'login'),
    url(r'^customer/loginPost/$', 'loginPost'),
    url(r'^customer/logout/$', 'logout'),
    url(r'^customer/create/$', 'create'),
)
