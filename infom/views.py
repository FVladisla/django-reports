# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeForm, WorkTimeRecordForm, PayrollReportForm, ShipmentRevenueForm, TariffForm, TaxesReportForm
from .models import Employee, WorkTimeRecord, PayrollReport, ShipmentRevenue, Tariff, TaxesReport


def employee_list(request):
    # Получаем параметры поиска из GET-запроса
    search_query = request.GET.get('search_query')
    search_criteria = request.GET.get('search_criteria')
    

    # Инициализируем переменную, в которой будут храниться сотрудники для отображения
    employees = Employee.objects.all()

    # Если есть параметры поиска, фильтруем сотрудников по ним
    if search_query and search_criteria:
        filter_args = {search_criteria + '__icontains': search_query}
        employees = Employee.objects.filter(**filter_args)
        if not employees:
            warning_message = "Нет сотрудников для отображения"
            context = {"warning_message": warning_message}
            return render(request, "employees/employee_list.html", context)
              

    # Передаем сотрудников в контекст для отображения
    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)


def enter_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infom:enter_data')
    else:
        form = EmployeeForm()
    return render(request, 'employees/enters/enter_employee.html', {'form': form})


def enter_work_time_record(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/enters/enter_work_time_record.html', context)

def submit_work_time_record(request):
    if request.method == 'POST':
        form = WorkTimeRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infom:enter_data')
    else:
        form = WorkTimeRecordForm
    return render(request, 'employees/enters/enter_work_time_record.html', {'form': form})

def enter_payroll_report(request):
    if request.method == 'POST':
        form = PayrollReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infom:enter_data')
    else:
        form = PayrollReportForm()
    return render(request, 'employees/enters/enter_payroll_report.html', {'form': form})    



def enter_shipment_revenue(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/enters/enter_shipment_revenue.html', context)

def submit_shipment(request):
    if request.method == 'POST':
        form = ShipmentRevenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infom:enter_data')
    else:
        form = ShipmentRevenueForm
    return render(request, 'employees/enters/enter_shipment_revenue.html', {'form': form})
    


def enter_tariff(request):
    if request.method == 'POST':
        form = TariffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_uel')
    else:
        form = TariffForm()
    return render(request, 'employees/enter_tariff.html', {'form': form})

def enter_taxes_report(request):
    if request.method == 'POST':
        form = TaxesReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infom:enter_data')
    else:
        form = TaxesReportForm()
    return render(request, 'employees/enters/enter_taxes_report.html', {'form': form}) 

def home(request):
    return render(request, 'employees/home.html')

from django.shortcuts import render, redirect



def enter_data(request):
    model_name = request.GET.get('model_name')
    
    if model_name == 'Employee':
        return redirect('infom:enter_employee')
    elif model_name == 'WorkTimeRecord':
        return redirect('infom:enter_work_time_record')
    elif model_name == 'PayrollReport':
        return redirect('infom:enter_payroll_report')
    elif model_name == 'ShipmentRevenue':
        return redirect('infom:enter_shipment_revenue')
    elif model_name == 'TaxesReport':
        return redirect('infom:enter_taxes_report')
    elif model_name == 'Tariff':
        return redirect('infom:enter_tariff')
    else:
        # Отображаем форму выбора модели, если модель не указана или указана неправильно
        return render(request, 'employees/enter_data.html')





def view_reports(request):
    search_query = request.GET.get('search_query')
    search_criteria = request.GET.get('search_criteria')

    if search_query and search_criteria:
        filter_args = {f'{search_criteria}__icontains': search_query}
        reports = TaxesReport.objects.filter(**filter_args)
    else:
        reports = TaxesReport.objects.all()

    if not reports:
        warning_message = "Нет данных для отображения."
        context = {'warning_message': warning_message}
        return render(request, 'employees/reports.html', context)

    context = {'reports': reports}
    return render(request, 'employees/reports.html', context)




# Create your views here.
