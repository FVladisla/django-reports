from django.db import models

# Create your models here
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self) -> str:
        return self.full_name
    

class WorkTimeRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateField()
    time_at_work = models.DurationField()
    def __str__(self) -> str:
        return f"{self.employee} {self.date}"

    class Meta:
        unique_together = ('employee', 'start_time', 'end_time')

class PayrollReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    period = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    report_content = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    revenue_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipment_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tariff_id = models.IntegerField(blank=True, null=True)
    time_at_work = models.DurationField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.title} {self.period}"

class ShipmentRevenue(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    action_id = models.IntegerField()
    revenue_volume = models.DecimalField(max_digits=10, decimal_places=2)
    shipment_volume = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    def __str__(self) -> str:
        return f"{self.employee} {self.date}"

    class Meta:
        unique_together = ('employee', 'action_id', 'date')

class Tariff(models.Model):
    tariff_id = models.AutoField(primary_key=True)
    tariff_name = models.CharField(max_length=150)
    tariff_value = models.DecimalField(max_digits=10, decimal_places=2)
    action_id = models.IntegerField(blank=True, null=True)

class TaxesReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    period = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    report_content = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    revenue_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipment_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tariff_id = models.IntegerField(blank=True, null=True)
    time_at_work = models.DurationField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    income_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    contribution_tax_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.title} {self.period}"
    