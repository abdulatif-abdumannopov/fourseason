from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ReservationModel(models.Model):
    res_choose = [
        ('Reservation', 'Reservation'),
        ('Hotel', 'Hotel'),
        ('Food', 'Food'),
        ('Gift-Card', 'Gift-Card'),
        ('Loss', 'Loss'),
        ('Jet', 'Jet'),
        ('Other', 'Other'),
    ]
    status_choose = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    ]
    status = models.CharField('Status', max_length=3, choices=status_choose, default=0)
    firstname = models.CharField('Name', max_length=100)
    lastname = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email', max_length=150)
    reservation = models.CharField('Reservation', max_length=120, choices=res_choose, default=0)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self) -> str:
        return f'{self.status}.{self.lastname}{self.created}'

class RatesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    firstname = models.CharField('First Name', max_length=100)
    lastname = models.CharField('Last Name', max_length=100)
    phone = models.CharField('Phone', max_length=150)
    adult = models.IntegerField('Adult', default=1)
    children = models.IntegerField('Children', default=0)
    start = models.CharField('Start', max_length=10)
    end = models.CharField('End', max_length=10)
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self) -> str:
        return f'{self.lastname}'

class ContactModel(models.Model):
    res_choose = [
        ('Make or Change Reservation', 'Make or Change Reservation'),
        ('General Question', 'General Question'),
        ('Travel Agent Inquiry', 'Travel Agent Inquiry'),
        ('Technical Support', 'Technical Support'),
        ('Office Of The President', 'Office Of The President'),
        ('Comments & Concerns', 'Comments & Concerns'),
        ('Other', 'Other'),
    ]
    status_choose = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
    ]
    status = models.CharField('Status', max_length=3, choices=status_choose, default=0)
    firstname = models.CharField('Name', max_length=100)
    lastname = models.CharField('Surname', max_length=100)
    email = models.EmailField('Email', max_length=150)
    phone = models.CharField('Phone', max_length=150)
    reservation = models.CharField('Reservation', max_length=120, choices=res_choose, default=0)
    text = models.TextField('Text', max_length=500)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return f'{self.status}.{self.lastname}'

class UserCustom(User):
    pass
