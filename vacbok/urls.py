from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),


    path('myprofile/<str:pk>/',views.myPro,name="myprofile"),
    path('',views.home,name="home"),
     path('update-user/',views.updateUser,name="update-user"),
    path('booking/',views.booking,name="book"),
    path('about/',views.aboutMe,name="about"),


    path('admin-home',views.ahome,name="admin-home"),
    path('centersE/',views.adminShow,name="centersE"),
    path('center/<str:pk>/',views.center,name="center"),
    path('add-location/',views.addloc,name="add-location"),
    path('update-location/<str:pk>/',views.updateloc,name="update-location"),
    path('delete/<str:pk>/',views.delelteCenter,name="delete"),
    path('updates/<str:pk>/',views.verifica,name="updates"),
    path('abookings',views.abookings,name="abookings"),
]
