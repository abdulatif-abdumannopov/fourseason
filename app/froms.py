from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['status', 'firstname', 'lastname', 'email', 'reservation']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'resident_status_select',
                'name': 'status',
                'placeholder': 'Status'
            }
            ),
            'firstname': forms.TextInput(attrs={
                'class': 'resident_name',
                'placeholder': 'Name',
                'name': 'firstname'
            }
            ),
            'lastname': forms.TextInput(attrs={
                'class': 'resident_item',
                'placeholder': 'Last Name',
                'name': 'lastname'
            }
            ),
            'email': forms.EmailInput(attrs={
                'class': 'resident_item',
                'placeholder': 'Email',
                'name': 'email'
            }
            ),
            'reservation': forms.Select(attrs={
                'class': 'resident_services',
                'name': 'reservation'
            }
            ),
        }

class RatesForm(forms.ModelForm):
    class Meta:
        model = RatesModel
        fields = ['firstname', 'lastname', 'phone', 'adult', 'children', 'start', 'end']

        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'rates_first_name_input',
                'name': 'first_name',
            }
            ),
            'lastname': forms.TextInput(attrs={
                'class': 'rates_second_name_input',
                'name': 'last_name',
            }
            ),
            'phone': forms.TextInput(attrs={
                'class': 'rates_phone_number',
                'name': 'phone',
            }
            ),
            'adult': forms.HiddenInput(attrs={
                'class': 'rates_count_input',
                'name': 'adult_count',
            }
            ),
            'children': forms.HiddenInput(attrs={
                'class': 'rates_count_input_children',
                'name': 'children_count',
            }
            ),
            'end': forms.TextInput(attrs={
                'class': 'rates_end_date',
                'name': 'end',
            }
            ),
            'start': forms.TextInput(attrs={
                'class': 'rates_start_date',
                'name': 'start',
            }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['status', 'firstname', 'lastname', 'phone', 'email', 'reservation', 'text']

        widgets = {
            'status': forms.Select(attrs={
                'class': 'resident_status_select',
                'name': 'status',
            }
            ),
            'firstname': forms.TextInput(attrs={
                'class': 'resident_name',
                'name': 'name',
                'placeholder': 'First Name'
            }
            ),
            'lastname': forms.TextInput(attrs={
                'class': 'resident_item',
                'name': 'name',
                'placeholder': 'Last Name'
            }
            ),
            'email': forms.TextInput(attrs={
                'class': 'resident_item',
                'name': 'email',
                'placeholder': 'Email'
            }
            ),
            'phone': forms.TextInput(attrs={
                'class': 'resident_item',
                'name': 'phone',
                'placeholder': 'Phone'
            }
            ),
            'reservation': forms.Select(attrs={
                'class': 'contact_services',
                'name': 'services',
            }
            ),
            'text': forms.Textarea(attrs={
                'class': 'contact_text_area',
                'name': 'text',
                'placeholder': 'How we can help you?'
            }
            ),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Register', widget=forms.TextInput(attrs={'class': 'login_username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login_password'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login_password'}))
    is_staff = forms.BooleanField(label='Is Staff', required=True, widget=forms.CheckboxInput(attrs={'class': 'confirm_staff'}))
    is_superuser = forms.BooleanField(label='Is Admin', required=False, widget=forms.CheckboxInput(attrs={'class': 'confirm_user'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff', 'is_superuser']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'login_username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'login_password'}))

    class Meta:
        model = User
