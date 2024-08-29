from django import forms
from apps.intern.models import Employee


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    position = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'})
    )
    department = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'})
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date', 'type': 'date'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Of Birth', 'type': 'date'})
    )

    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email','date_of_birth', 'phone_number',
            'position', 'department', 'start_date',
        ]