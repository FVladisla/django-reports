from django import forms
from .models import Employee, WorkTimeRecord, PayrollReport, ShipmentRevenue, Tariff, TaxesReport

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkTimeRecordForm(forms.ModelForm):
    class Meta:
        model = WorkTimeRecord
        fields = '__all__'

class PayrollReportForm(forms.ModelForm):
    class Meta:
        model = PayrollReport
        fields = '__all__'

class ShipmentRevenueForm(forms.ModelForm):
    class Meta:
        model = ShipmentRevenue
        fields = '__all__'

class TariffForm(forms.ModelForm):
    class Meta:
        model = Tariff
        fields = '__all__'

class TaxesReportForm(forms.ModelForm):
    class Meta:
        model = TaxesReport
        fields = '__all__'
