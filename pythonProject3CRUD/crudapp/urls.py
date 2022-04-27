from django.urls import path

from crudapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginviews',views.loginview,name='loginview'),
    path('adminhome',views.adminview,name='adminhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentregister',views.studentregister,name='studentregister'),
    path('studentview',views.studentview,name='studentview'),
    path('studentupdate/<int:id>',views.studentupdate,name='studentupdate'),
    path('studentdelete/<int:id>',views.studentdelete,name='studentdelete'),
    path('logout',views.logoutview,name='logoutview'),
    path('BookAdd',views.BookAdd,name='BookAdd'),
    path('BookView',views.BookView,name='BookView'),
    path('BookUpdate/<int:idb>',views.BookUpdate,name='BookUpdate'),
    path('Bookdelete/<int:idb>',views.Bookdelete,name='Bookdelete'),
]