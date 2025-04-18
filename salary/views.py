from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.db.models import Sum
import datetime
from django.contrib.auth import get_user_model
from .models import Payroll, SalaryStructure, Deduction, AuditLog, Department
from .forms import SalaryStructureForm, DeductionForm
from .utils import PayrollProcessor

User = get_user_model()


class PayrollListView(LoginRequiredMixin, ListView):
    model = Payroll
    template_name = 'salary/payroll/list.html'
    context_object_name = 'payrolls'
    
    def get_queryset(self):
        # Changed is_hr to group check
        if self.request.user.groups.filter(name='hr').exists():
            return Payroll.objects.all()
        return Payroll.objects.filter(employee=self.request.user)


class GeneratePayrollView(UserPassesTestMixin, CreateView):
    model = Payroll
    fields = []
    template_name = 'salary/payroll/generate.html'
    
    def test_func(self):
        return (
            self.request.user.groups.filter(name='hr').exists() and 
            self.request.user.has_perm('salary.can_generate_payroll')
        )
    
    def form_valid(self, form):
        employee = get_object_or_404(User, pk=self.kwargs['employee_id'])
        month = datetime.date.today().replace(day=1)
        
        processor = PayrollProcessor(employee, month)
        try:
            payroll = processor.generate_payroll()
        except ValueError as e:
            messages.error(self.request, str(e))
            return redirect('salary:payroll-list')
        
        messages.success(self.request, f'Payroll generated for {employee.get_full_name()}')
        return redirect('salary:payroll-detail', pk=payroll.pk)


class ApprovePayrollView(UserPassesTestMixin, DetailView):
    model = Payroll
    template_name = 'salary/payroll/approve.html'
    
    # def test_func(self):
    #     return self.request.user.is_finance
    def test_func(self):
        return self.request.user.groups.filter(name='finance').exists()
    
    def post(self, request, *args, **kwargs):
        payroll = self.get_object()
        payroll.status = 'approved'
        payroll.save()
        
        AuditLog.objects.create(
            user=request.user,
            action='approve',
            model='Payroll',
            object_id=payroll.id
        )
        
        messages.success(request, 'Payroll approved successfully')
        return redirect('salary:payroll-detail', pk=payroll.pk)


class DeductionCreateView(LoginRequiredMixin, CreateView):
    model = Deduction
    form_class = DeductionForm
    template_name = 'salary/deductions/create.html'
    
    def get_success_url(self):
        return reverse('salary:deduction-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        # if not self.request.user.is_hr:
        #     form.instance.employee = self.request.user
        # return super().form_valid(form)
        if not self.request.user.groups.filter(name='hr').exists():
            form.instance.employee = self.request.user
        return super().form_valid(form)


class EmployeeDeductionListView(LoginRequiredMixin, ListView):
    model = Deduction
    template_name = 'salary/deductions/list.html'
    
    def get_queryset(self):
        return Deduction.objects.filter(employee=self.request.user)


class SalaryStructureUpdateView(UserPassesTestMixin, UpdateView):
    model = SalaryStructure
    form_class = SalaryStructureForm
    template_name = 'salary/structure/update.html'
    
    # For finance permissions
    def test_func_finance(self):
        return self.request.user.groups.filter(name='finance').exists()

    # For HR permissions
    def test_func_hr(self):
        return self.request.user.groups.filter(name='hr').exists()
    
    def get_success_url(self):
        return reverse('salary:employee-detail', kwargs={'pk': self.object.employee.pk})


class EmployeeSalaryDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'salary/structure/detail.html'
    context_object_name = 'employee'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salary_structure'] = get_object_or_404(SalaryStructure, employee=self.object)
        return context


class SalaryReportView(UserPassesTestMixin, TemplateView):
    template_name = 'salary/reports/monthly.html'
    
    # # For finance permissions
    # def test_func_finance(self):
    #     return self.request.user.groups.filter(name='finance').exists()

    # # For HR permissions
    # def test_func_hr(self):
    #     return self.request.user.groups.filter(name='hr').exists()
    def test_func(self):
        # Allow either finance or HR to access reports
        return self.request.user.groups.filter(name__in=['finance', 'hr']).exists()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            month = datetime.datetime.strptime(self.request.GET.get('month'), '%Y-%m').date()
        except (TypeError, ValueError):
            month = datetime.date.today().replace(day=1)
        
        context['report_data'] = {
            'total_payroll': Payroll.objects.filter(
                month=month,
                status='paid'
            ).aggregate(Sum('net_salary'))['net_salary__sum'] or 0,
            'department_breakdown': Department.objects.annotate(
                total=Sum('employee__payroll__net_salary')
            ).filter(
                employee__payroll__month=month
            ),
            'tax_summary': Deduction.objects.filter(
                deduction_type='tax',
                payroll__month=month
            ).aggregate(Sum('amount'))['amount__sum'] or 0
        }
        return context
