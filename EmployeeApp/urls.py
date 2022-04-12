from django import urls
from django.urls import re_path
from EmployeeApp import views

urlpatterns=[
    re_path(r'^mastercategory$',views.masterCategoryApi),
    re_path(r'^mastercategory/([0-9]+)$',views.masterCategoryApi)
]
