from django.urls import path
from . import views 
from .views import *
urlpatterns=[
    path('',index,name="index"),
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('join/',join,name="join"),
    path('features/',features,name='features'),
    path('about/',about,name='about'),
    path('support/',support,name='support'),
    path('question/',questions,name="question"),
    
    
    path('randomquiz/',randomquiz,name="randomquiz"),
    
    path('play/<str:cat_name>/', play,name="play"),
    
    
    path('dashboardview/',dashboardview,name="dashboardview"),
    
    path('addquestions/',addquestions,name="addquestions"),
    path('createquiz/',createquiz,name="create quiz"),
    path('myquizes/',myquizes,name="myquizes"),
    path('details/',details,name="details"),
    path('register',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('result',views.result,name="result"),
    path('enter/', enter,name="enter"),
    path('addCategory/', addCategory,name="addCategory"),
]