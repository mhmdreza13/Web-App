from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path ('register/',views.user_register , name= 'user_register'),
    path ('login/',views.user_login , name= 'user_login'),
    path ("logout/",views.user_logout, name='user_logout'),
    path ("profile/",views.user_profile, name='user_profile'),
    path ("update/",views.user_update, name='user_update'),
    path ("addesses/",views.user_addresses, name='user_addresses'),
    path ("changepassowrd/",views.user_changepassowrd, name='user_changepassowrd'),
]
 