from datetime import date
from datetime import date, timedelta, datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *


@login_required(login_url='login')
def admin(request, template, template_admin):
    superuser = False
    if request.user.is_superuser or request.user.is_staff:
        reservation = ReservationModel.objects.all().order_by('-created')
        rate = RatesModel.objects.all().order_by('-created')
        contacts = ContactModel.objects.all().order_by('-created')
        today = date.today().strftime('%Y-%m-%d')

        def get_paginator(queryset, parameter_name):
            paginator = Paginator(queryset.order_by('-created'), 20)
            page_number = request.GET.get(parameter_name)
            page_obj = paginator.get_page(page_number)
            return page_obj

        res_page_obj = get_paginator(ReservationModel.objects.exclude(reservation='Jet'), 'reservation')
        jet_page_obj = get_paginator(ReservationModel.objects.filter(reservation='Jet'), 'jet')
        con_page_obj = get_paginator(contacts, 'contact')
        rates_page_obj = get_paginator(rate, 'rates')

        res_page_today = get_paginator(ReservationModel.objects.exclude(reservation='Jet').filter(created__date=today), 'reservation_today')
        jet_page_today = get_paginator(ReservationModel.objects.filter(reservation='Jet', created__date=today), 'jet_today')
        con_page_today = get_paginator(ContactModel.objects.filter(created__date=today), 'contact_today')
        rates_page_today = get_paginator(RatesModel.objects.filter(created__date=today), 'rates_today')

        context = {'reservation': reservation, 'today': today, 'rates': rate, 'contact': contacts,
                   'superuser': superuser, 'res_page': res_page_obj, 'jet_page': jet_page_obj,
                   'con_page': con_page_obj, 'rates_page': rates_page_obj, 'res_today': res_page_today,
                   'jet_object': jet_page_today, 'con': con_page_today, 'rate': rates_page_today}

        if request.user.is_superuser:
            context['superuser'] = True
            return render(request, template_admin, context)
        return render(request, template, context)
    else:
        return redirect('no_rights')


def admin_user_form(request, form, template):
    super_user = form.filter(is_superuser=True)
    staff = form.filter(is_staff=True)
    other = form.filter(is_superuser=False, is_staff=False)

    def get_page(queryset, parameter_name):
        paginator = Paginator(queryset, 100)
        page_number = request.GET.get(parameter_name)
        page_obj = paginator.get_page(page_number)
        return page_obj

    all_users = get_page(form, 'all')
    super_user_page = get_page(super_user, 'superuser')
    staff_page = get_page(staff, 'staff')
    other_page = get_page(other, 'simple')

    if request.user.is_superuser:
        return render(request, template, {'form': form,
                                          'super_user': super_user,
                                          'staff': staff,
                                          'other': other,
                                          'superuser_page': super_user_page,
                                          'staff_page': staff_page,
                                          'other_page': other_page,
                                          'all_users': all_users})
    return redirect('no_rights')


def callback(request, model, template):
    if request.user.is_authenticated:
        user = request.user
        initial_data = {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
        }
        form = model(initial=initial_data)
    else:
        form = model()

    if request.method == 'POST':
        form = model(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            form = model()
        else:
            return form()

    return render(request, template, {'form': form})

def rates_short(request, form_class, template):
    error = ''

    if request.user.is_authenticated:
        user = request.user
        initial_data = {
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
        }
        form = form_class(initial=initial_data)
    else:
        form = form_class()

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            start_str = form.cleaned_data['start']
            end_str = form.cleaned_data['end']
            today = date.today()
            tomorrow = today + timedelta(days=1)
            start_date = datetime.strptime(start_str, '%d/%m/%Y').date()
            end_date = datetime.strptime(end_str, '%d/%m/%Y').date()

            if start_date == end_date:
                error = "Start date can't be equal to departure date"
            elif start_date < today:
                error = "Start date can't be later than today"
            elif end_date < tomorrow:
                error = "End date can't be later than tomorrow"
            else:
                form.instance.user = request.user
                form.save()
                form = form_class()
        else:
            return render(request, template, {'form': form, 'error': error})

    return render(request, template, {'form': form, 'error': error})
