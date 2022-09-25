from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('docsign/', views.docsign),
    path('quickbooks/', views.quickbooks),
    path('products', views.products),
    
    
     path('signup/', views.signup),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin/', views.signin),
    path('signout/', views.signout),
]


# urlpatterns = [
#     path('', views.home, name="home"),
#     path('signup', views.signup, name='signup'),
#     # path('activate/<uidb64>/<token>', views.activate, name='activate'),
#     path('signin', views.signin, name='signin'),
#     path('signout', views.signout, name='signout'),
# ]