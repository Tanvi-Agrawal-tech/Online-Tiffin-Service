from django.contrib import admin
from django.urls import path
from register import views


#from django.conf.urls.defaults import patters,include,url
# from register import views
urlpatterns = [
    # path('admin/',admin.site.urls),
    # path('',include('register.urls'))
    path('',views.index,name="index"),
    path('registration',views.registration,name="registration")

]