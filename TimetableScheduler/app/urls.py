from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('faculties/', views.faculties, name='faculties'),
    path('subjects/', views.subjects, name='subjects'),
    path('classrooms/', views.classrooms, name='classrooms'),
    path('batches/', views.batches, name='batches'),
    path('constraints/', views.constraints, name='constraints'),
    path('timetable/', views.timetable, name='timetable'),
]
