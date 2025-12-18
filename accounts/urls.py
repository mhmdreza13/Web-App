from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path ('register/',views.user_register , name= 'user_register'),
    path ('login/',views.user_login , name= 'user_login'),
    path ("logout/",views.user_logout, name='user_logout'),
    path ("profile/",views.user_profile, name='user_profile'),
    path ("update/",views.user_update, name='user_update'),
    path ("addresses/",views.user_addresses, name='user_addresses'),
    path ("changepassowrd/",views.user_changepassword, name='user_changepassowrd'),
    path ("editaddress/<int:id>/",views.user_editaddress, name="user_editaddress"),# type: ignore
    path ("addaddress/",views.user_addaddress,name='user_addaddress'),# type: ignore
    path ('deleteaddress/<int:id>/',views.user_delete_address,name='user_delete_address'),
]
 