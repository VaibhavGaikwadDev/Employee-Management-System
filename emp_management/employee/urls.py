from django.urls import path
from .views import EmployeeView, DepartmentView

urlpatterns = [
    path('departments/', DepartmentView.as_view(), name='departments'),
    path('employees/', EmployeeView.as_view(), name='employees'),
    path('employees/<int:pk>/', EmployeeView.as_view(), name='employee-detail'),
]
