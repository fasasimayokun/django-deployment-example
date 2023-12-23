from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    #path('my-login/', views.my_login, name='my-login'),
    path('login/', auth_views.LoginView.as_view(template_name='fruitsapp/my-login.html'), name='login'),
    path('user-logout/', views.user_logout, name='user-logout'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('category/', views.category, name='category'),
    path('allfruits/', views.allfruits, name='allfruits'),
    path('simplefruits/', views.simplefruits, name='simplefruit'),
    path('fleshyfruits/', views.fleshyfruits, name='fleshyfruit'),
    path('multiple/', views.multiple, name='multiple'),
    path('dryfruits/', views.dryfruits, name='dryfruit'),
    path('aggregate/', views.aggregate, name='aggregate'),
    path('view_fruits/', views.show_fruits, name='view_fruits'),
    path('add_fruit/', views.add_fruit, name='add_fruit'),
    path('single_fruit/<int:pk>/', views.single_fruit, name='single_fruit'),
    path('update_fruit/<int:pk>/', views.update_fruit, name='update_fruit'),
    path('go_back/', views.go_back, name='go_back'),
]


# Add the following line at the end of your urls.py file to serve static files during development.
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)