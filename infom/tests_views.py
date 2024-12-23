from django.test import TestCase
from django.urls import reverse
from .models import Employee
from .views import employee_list


class EmployeeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестовые данные для базы данных
        number_of_employees = 5
        for employee_id in range(number_of_employees):
            Employee.objects.create(
                full_name=f'Test Employee {employee_id}',
                position='Test Position',
                email=f'test{employee_id}@example.com',
                phone='123456789'
            )

    def test_view_url_exists_at_desired_location(self):
        # Проверяем, доступен ли URL для просмотра сотрудников
        response = self.client.get('/infom/list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Проверяем, доступен ли URL для просмотра сотрудников по имени
        response = self.client.get(reverse('infom:employee_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Проверяем, что используется правильный шаблон
        response = self.client.get(reverse('infom:employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employee_list.html')

    def test_lists_all_employees(self):
        # Проверяем, что на странице отображаются все сотрудники
        response = self.client.get(reverse('infom:employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('employees' in response.context)
        self.assertEqual(len(response.context['employees']), 5)

    def test_search_employee_by_name(self):
        # Проверяем поиск сотрудника по имени
        response = self.client.get(reverse('infom:employee_list'), {'search_criteria': 'full_name', 'search_query': 'Test Employee 1'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('employees' in response.context)
        self.assertEqual(len(response.context['employees']), 1)


# Для запуска тестов выполните python manage.py test
