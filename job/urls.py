from django.urls import path
from . import views


urlpatterns =[
    path('', views.job_list, name = 'job_list'),
    path('post_job/', views.post_job, name = 'post_job'),
    path('job_search/', views.search, name = 'job_search')

]