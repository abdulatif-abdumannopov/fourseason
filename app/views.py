from datetime import date, timedelta, datetime
import re
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from .froms import *
from django.contrib.auth.decorators import login_required
from .utils import *


class ReservationList(ListCreateAPIView):
    queryset = ReservationModel.objects.all()
    serializer_class = PostSerializer


class RatesList(ListCreateAPIView):
    queryset = RatesModel.objects.all()
    serializer_class = RatesSerializer


class ContactList(ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer


def home(request):
    return render(request, 'home.html')


def maldives(request):
    return render(request, 'maldives.html')


def residents(request):
    form = ReservationForm
    return callback(request, form, 'residents.html')


def gift_cards(request):
    form = ReservationForm
    return callback(request, form, 'gift_cards.html')


def jet(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.reservation = 'Jet'
            form.save()
            form = ReservationForm()
    else:
        form = ReservationForm()

    return callback(request, ReservationForm, 'jet.html')


def dining(request):
    return render(request, 'dinning.html')


def about(request):
    return render(request, 'about.html')


def history(request):
    return render(request, 'history.html')


def no_rights(request):
    return render(request, 'no_rights.html')


def contact(request):
    form = ContactForm
    return callback(request, form, 'contact.html')


@login_required(login_url='login')
def rates(request):
    form = RatesForm
    return rates_short(request, form, 'rates.html')


def delete_object(request, model, pk):
    if request.user.is_superuser or request.user.is_staff:
        obj = model.objects.get(pk=pk)
        obj.delete()
    else:
        return redirect('no_rights')


def delete_reservation(request, pk):
    delete_object(request, ReservationModel, pk)
    return redirect('admin_full')


def delete_contact(request, pk):
    delete_object(request, ContactModel, pk)
    return redirect('admin_full')


def delete_rates(request, pk):
    delete_object(request, RatesModel, pk)
    return redirect('admin_full')


@login_required(login_url='login')
def rates_edit(request, pk):
    rate = RatesModel.objects.get(pk=pk)
    if not request.user.is_superuser or not request.user.is_staff:
        return redirect('no_rights')
    if request.method == 'POST':
        form = RatesForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return redirect('admin_full')
    else:
        form = RatesForm(instance=rate)

    return render(request, 'rates_detail.html', {'form': form, 'pk': pk})


def delete_user(request, pk):
    del_user = User.objects.get(pk=pk)
    if del_user.username != request.user.username and del_user.is_superuser:
        return redirect('users')
    delete_object(request, User, pk)
    return redirect('users')


@login_required(login_url='login')
def admin_user(request):
    model = User.objects.all()
    return admin_user_form(request, model, 'user.html')


@login_required(login_url='login')
def admin_panel(request):
    return admin(request, 'admin_panel.html', 'admin_panel_superuser.html')


@login_required(login_url='login')
def admin_panel_full(request):
    return admin(request, 'admin_full.html', 'admin_full_superuser.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            context = {'form': LoginUserForm}
            return render(request, 'login.html', context)
    else:
        context = {'form': LoginUserForm}
        return render(request, 'login.html', context)


def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.user.username != user.username:
        return redirect('edit', request.user.pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit', request.user.pk)
    else:
        form = UserEditForm(instance=user)
    return render(request, 'edit.html', {'form': form})


@login_required(login_url='login')
def admin_register(request):
    if not request.user.is_superuser:
        return redirect('no_rights')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('admin_panel')
        else:
            context = {'form': RegisterUserForm, 'error': 'Login or password error'}
            return render(request, 'admin_register.html', context)
    else:
        form = RegisterUserForm()
    return render(request, 'admin_register.html', {'form': form})


@login_required(login_url='login')
def admin_change(request, pk):
    user = User.objects.get(pk=pk)
    reg_date = user.date_joined
    last_date = user.last_login
    if not request.user.is_superuser:
        return redirect('no_rights')
    if user.username != request.user.username and user.is_superuser:
        return redirect('users')
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'admin_change_user.html',
                  {'form': form, 'user': user, 'registered': reg_date, 'last_date': last_date})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            login(request, user)
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def change_password(request, pk):
    user = User.objects.get(pk=pk)
    if (not request.user.is_superuser and request.user.username != user.username) or (
            user.is_superuser and request.user.username != user.username):
        return redirect('password', request.user.pk)
    if request.method == 'POST':
        if request.user.is_superuser or user.check_password(request.POST['old_password']):
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if len(password1) >= 8 and re.search(r'\d', password1) or request.user.is_superuser:
                    user.set_password(password1)
                    user.save()
                    update_session_auth_hash(request, user)
                    return redirect('login')
                else:
                    error_message = 'Password is simple'
            else:
                error_message = 'Пароли не совпадают'
        else:
            error_message = 'Неверный старый пароль'
    else:
        error_message = ''
    if request.user.is_superuser:
        return render(request, 'admin_change_password.html', {'error_message': error_message, 'form': user})
    else:
        return render(request, 'change_password.html', {'error_message': error_message, 'form': user})


@login_required(login_url='login')
def logo_out(request):
    logout(request)
    return redirect('login')
