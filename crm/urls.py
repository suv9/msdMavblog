from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import logout, password_change as pwd_change, password_change_done as pwd_change_done, password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm, password_reset_complete as reset_complete

app_name = 'crm'
urlpatterns = [

    url(r'^logout/$', logout, name='logout'),
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^password-change/done/$', pwd_change_done, name='password_change_done'),
    url(r'^password-change/$', pwd_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),
    url(r'^password-reset/complete/$', reset_complete, name='password_reset_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', reset_confirm, {'post_reset_redirect': '/password-reset/complete/'}, name='password_reset_confirm'),
    url(r'^password-reset/done/$', reset_done, name='password_reset_done'),
    url(r'^password-reset/$', reset, {'post_reset_redirect': '/password-reset/done/', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^register/$', views.register, name='register'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
]
