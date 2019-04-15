from home import views
from django.urls import path,include

urlpatterns = [
path('',views.Home_page,name='home'),
]
