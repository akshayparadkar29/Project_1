from django.contrib import admin
from django.urls import path
from blogapp import views

# url patterns are defined here

urlpatterns = [
    path('udash',views.user_dashboard,name="user_dash"),
    path('cpost',views.create_post,name="create_post"),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('deactivate/<rid>',views.deactivate),
    path('activate/<rid>',views.activate),
    path('',views.index,name="index_page"),
    path('catfilter/<opt>',views.categoryFilter),
    path('actfilter/<opt>',views.activeFilter),
    path('djangoform',views.djangoform),
    path('register',views.user_register),
    path('setcookie',views.setcookies),
    path('getcookie',views.getcookies),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('about',views.about,name="about_page"),
   
]

'''
path('url_name', views.function, name='alias_name')
url alias-name is used for security 
hacker can attack using forms &/ url
so we are giving a secondary name to the url which will be visible to hacker
he couldn't access the original url name
And if suppose original url name is reffered to 10-20 pages or more
and if original url is changes then developer also have to change
the reffered url on 10-20 pages or more which will be very time consuming 
'''