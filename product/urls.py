from django.urls import path,include
from . import views

app_name='product'
urlpatterns = [
    path('',views.product_list,name="list"),
    #path('<int:id>',views.product_detail,name="detail")
    path('<slug:slug>',views.product_detail,name="detail")
]
