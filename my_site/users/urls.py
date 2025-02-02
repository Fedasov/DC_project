from django.urls import path
from . import views
from users import views as user_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
 	path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),   #CreateProfilePageView.as_view()
    path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(), name='edit_user_profile'),
]