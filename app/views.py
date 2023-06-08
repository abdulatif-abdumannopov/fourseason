from datetime import date

from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from .permissions import *
import requests
from .froms import *
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


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
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservationForm()

    return render(request, 'residents.html', {'reservation_form': form})


def dining(request):
    return render(request, 'dinning.html')


def gift_cards(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservationForm()

    return render(request, 'gift_cards.html', {'form': form})


def jet(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.reservation = 'jet'
            form.save()
            form = ReservationForm()
    return render(request, 'jet.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def history(request):
    return render(request, 'history.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
        else:
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def rates(request):
    errors = ''
    form = RatesForm()
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            form.save()
            form = RatesForm()
        else:
            form = RatesForm()
            errors = 'Incorrectly completed form'

    return render(request, 'rates.html', {'form': form, 'errors': errors})


@login_required(login_url='login')
def admin_panel(request):
    reservation = ReservationModel.objects.all().order_by('-created')
    rate = RatesModel.objects.all()
    contacts = ContactModel.objects.all()
    today = date.today().strftime('%Y-%m-%d')
    return render(request, 'admin_panel.html', {'reservation': reservation,
                                                'today': today,
                                                'rates': rate,
                                                'contact': contacts})

@login_required(login_url='login')
def admin_panel_full(request):
    reservation = ReservationModel.objects.all().order_by('-created')
    rate = RatesModel.objects.all()
    contacts = ContactModel.objects.all()
    today = date.today().strftime('%Y-%m-%d')
    return render(request, 'admin_full.html', {'reservation': reservation,
                                                'today': today,
                                                'rates': rate,
                                                'contact': contacts})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_panel')
        else:
            context = {'form': LoginUserForm}
            return render(request, 'login.html', context)
    else:
        context = {'form': LoginUserForm}
        return render(request, 'login.html', context)


@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('admin_panel')
        else:
            context = {'form': RegisterUserForm, 'error': 'Login or password error'}
            return render(request, 'register.html', context)
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def logo_out(request):
    logout(request)
    return redirect('login')
