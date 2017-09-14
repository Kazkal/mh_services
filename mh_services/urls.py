"""mh_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from home import views as home_views
from portfolios import views as portfolio_views
from contacts import views as contacts_views
from django.views.static import serve
from .settings import MEDIA_ROOT
from blog import views as blog_views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from payments import views as payments_views


# url(r'^$', home_views.get_home, name='home'),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_home, name='home'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^person/$', accounts_views.person, name='person'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^portfolio/', portfolio_views.get_portfolios, name='portfolio'),
    url(r'^testimonial/', portfolio_views.get_testimonials, name='testimonial'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^contactus/$', contacts_views.new_contact, name='contactus'),
    url(r'^plumbing/$', contacts_views.get_plumbing, name='plumbing'),
    url(r'', include('blog.urls')),
    url(r'^blog/$', blog_views.list_posts, name='blog'),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.payment_return),
    url(r'^paypal-cancel', paypal_views.payment_cancel),
    url(r'^payinvoice/', payments_views.get_invoices, name='payinvoice'),
]
