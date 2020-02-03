from django.contrib import admin
from django.urls import path, include
from .views import Companyprofile,Jobsprofile,detail
urlpatterns = [
path('create/',Companyprofile.as_view(),name="create C"),
path('create-job/',Jobsprofile.as_view(),name="create job"),
path('detail/<int:id>/',detail,name="deteail job")
]

