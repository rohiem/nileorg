from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/',views.SignUp,name="signup"),
    #path('<int:id>',views.product_detail,name="detail")
    path('profiles/<slug:slug>',views.profile,name="profile")
]
