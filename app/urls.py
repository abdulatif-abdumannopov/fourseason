from django.urls import path
from .views import *
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', home, name='home'),
    path('login', login_user, name='login'),
    path('edit/<int:pk>', user_edit, name='edit'),
    path('admin_register', admin_register, name='admin_register'),
    path('password/<int:pk>', change_password, name='password'),
    path('register', register, name='register'),
    path('logout', logo_out, name='logout'),
    path('noright', no_rights, name='no_rights'),
    path('admin_panel', admin_panel, name='admin_panel'),
    path('admin_full', admin_panel_full, name='admin_full'),
    path('admin_full/reservation/delete/<int:pk>', delete_reservation, name='delete_reservation'),
    path('admin_full/contact/delete/<int:pk>', delete_contact, name='delete_contact'),
    path('admin_full/rates/delete/<int:pk>', delete_rates, name='delete_rates'),
    path('users/delete/<int:pk>', delete_user, name='delete_user'),
    path('users/edit/<int:pk>', admin_change, name='admin_edit'),
    path('maldives', maldives, name='maldives'),
    path('residents', residents, name='residents'),
    path('dining', dining, name='dining'),
    path('users', admin_user, name='users'),
    path('gift-cards', gift_cards, name='gift_cards'),
    path('privatejet', jet, name='jet'),
    path('about', about, name='about'),
    path('history', history, name='history'),
    path('contact', contact, name='contact'),
    path('rates', rates, name='rates'),
    path('rates/edit/<int:pk>', rates_edit, name='rates_update'),
    path('api/v1/reservation', ReservationList.as_view()),
    path('api/v1/rates', RatesList.as_view()),
    path('api/v1/contact', ContactList.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
