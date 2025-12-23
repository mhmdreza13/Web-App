from django.urls import path
from . import views

app_name = 'home' 

urlpatterns = [
    path ('' , views.home ,name= 'home'),
    path ('product/',views.product , name = 'product'),
    path ('productdetail/<int:id>/',views.productdetail, name = 'productdetail'),
    path ('category/<slug>/<int:id>',views.product, name = 'category'),
]
handler404 = 'myapp.views.custom_404_view'