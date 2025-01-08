from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import complaints, criminal_list, detect, upload_criminal , search
from .views import UserDetailAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('upload_criminal/', upload_criminal, name='upload_criminal'),
    path('complaints/',complaints , name='complaints'),
    path('detect/', detect, name='detect'),
    path('search/', views.search, name='search'),
    path('criminal_list/',criminal_list,name='criminal_list'),
    path("get-details",UserDetailAPI.as_view()),
    
]