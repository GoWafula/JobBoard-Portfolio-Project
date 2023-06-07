from django.urls import path
from . import views

# urls to display and search for jobs
urlpatterns =[
    path('',views.home, name = 'home'),
    path('job_search/', views.search, name = 'job_search'),
    path('job_detail/<int:pk>/', views.job_detail, name = 'job_detail')

]


# urls for empployer and admin to create,delete ad update jobs
urlpatterns += [
    path('employer_dashboard/', views.employer_dashboard, name = 'employer_dashboard'),
    path('create_job/', views.create_job, name='create_job'),
    path('update_job/<int:pk>/', views.update_job, name='update_job'),
    path('job_delete/<int:pk>/', views.job_delete, name='job_delete'),
    #path('job_detail/<int:pk>/',views.job_detail, name = 'job_detail')
]
'''
# API URLS
urlpatterns += [
    path('employers/', views.EmployerList.as_view()),
    path('employers/<int:pk>/', views.EmployerDetail.as_view()),
    path('jobs/', views.JobList.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('jobs/', views.JobRead.as_view()),
    path('jobs/<int:pk>/', views.JobDelete.as_view()),
]
'''