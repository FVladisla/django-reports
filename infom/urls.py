from django.urls import path
from . import views


app_name = 'infom'

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('reports/', views.view_reports, name='reports'),
]
