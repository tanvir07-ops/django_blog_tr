from django.urls import path
app_name = "App_Login"
from .import views

urlpatterns = [
    path('signup/',views.sign_up,name = "signup"),
    path('login/',views.login_page,name = "login"),
    path('logout/',views.logout_user,name = "logout"),
    path('profile/',views.profile,name = "profile"),
    path('profile_change/',views.user_change,name = "user_change"),
   
    path('password/',views.pass_change,name = "pass_change"),
    path('add_picture/',views.add_pro_pic,name = "add_pro_pic"),
    path('change_picture/',views.change_pro_pic,name = "change_pro_pic"),
   
   
    
]

