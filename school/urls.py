from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('tlist/',views.teacherlist,name='teacherlist'),
    path('tadd/',views.teacheradd,name='teacheradd'),
    path('tupdate/<int:id>/',views.teacherupdate,name='tupdate'),
    path('tdel/<str:name>/',views.teacherdelete,name='tdelete'),
    path('stuadd/',views.studentadd,name='stuadd'),
    path('',views.studentlist,name='stulist'),
    path('stuupdate/<int:id>/',views.studentupdate,name='stuupdate'),
    path('studelete/<str:name>/',views.studentdelete,name='studelete'),
    path('login/',views.bogin,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
]
