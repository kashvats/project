from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('tlist/',views.teacherlist,name='teacherlist'),
    path('tadd/',views.teacheradd,name='teacheradd'),
    path('tupdate/<str:name>/',views.teacherupdate,name='tupdate'),
    path('tdel/<str:name>/',views.teacherdelete,name='tdelete'),
    path('stuadd/',views.studentadd,name='stuadd'),
    path('',views.studentlist,name='stulist'),
    path('stuupdate/<str:name>/',views.studentupdate,name='stuupdate'),
    path('studelete/<str:name>/',views.studentdelete,name='studelete'),
    path('login/',views.bogin,name='login'),
    # path('', auth_views.LoginView.as_view(template_name='login.html'),
    #      name='login'),
    # path('logout/', auth_views.LogoutView.as_view(),
    #      name='logout'),

    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
]
