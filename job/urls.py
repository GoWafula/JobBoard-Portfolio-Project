from django.urls import path
from . import views

# urls to display and search for jobs
urlpatterns =[
    path('', views.job_list, name = 'job_list'),
    path('job_search/', views.search, name = 'job_search'),
    path('single_job/', views.single_job, name = 'single_job')

]


# urls for empployer and admin to create,delete ad update jobs
urlpatterns += [
    path('employer_dashboard/', views.employer_dashboard, name = 'employer_dashboard'),
    path('create_job/', views.create_job, name='create_job'),
    path('update_job/<int:pk>/', views.update_job, name='update_job'),
    path('job_delete/<int:pk>/', views.job_delete, name='job_delete'),
    path('job_detail<int:pk>/',views.job_detail, name = 'job_detail')
]