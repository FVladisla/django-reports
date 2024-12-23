from django.urls import path
from . import views


app_name = 'infom'

urlpatterns = [
    path('enter-data/', views.enter_data, name='enter_data'),
    path('enter-employee/', views.enter_employee, name='enter_employee'),
    path('enter-worktimerecord/', views.enter_work_time_record, name='enter_work_time_record'),
    path('submit-work-time-record/', views.submit_work_time_record, name='submit_work_time_record'),
    path('enter-payrollreport/', views.enter_payroll_report, name='enter_payroll_report'),
    path('enter-shipment/', views.enter_shipment_revenue, name='enter_shipment_revenue'),
    path('submit-shipment/', views.submit_shipment, name='submit_shipment'),
    path('enter-taxes-report/', views.enter_taxes_report, name='enter_taxes_report'),
    path('', views.home, name='home'),
    path('list/', views.employee_list, name='employee_list'),
    path('reports/', views.view_reports, name='reports'),
]

