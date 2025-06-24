from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('login/index/', views.index_page, name = 'index'),
    path('home/', views.home_page, name = 'home'),
    path('login/dashboard/', views.dashboard, name = 'dashboard'),
    path('blog_list/', views.blog_list, name = 'blog_list'),
    path('blog_detail/<int:id>/', views.blog_detail, name = 'blog_detail'),
 
]