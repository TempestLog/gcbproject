from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('home', views.home, name="home"),
    path('logout', views.logout, name="logout"),
    path('post/<str:pk>', views.post, name="post")
]