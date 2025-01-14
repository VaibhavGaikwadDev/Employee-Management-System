from rest_framework import serializers
from .models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()  # Nested serializer to include department details

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_email(self, value):
        """Validate email format and uniqueness."""
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_phone(self, value):
        """Ensure phone number contains only digits and optional +."""
        if not value.isdigit() and not (value.startswith('+') and value[1:].isdigit()):
            raise serializers.ValidationError("Phone number must contain only digits, with an optional '+'.")
        return value