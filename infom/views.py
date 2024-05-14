# views.py
from .models import Employee
from .models import TaxesReport
from django.shortcuts import render
from django.http import HttpResponse

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
