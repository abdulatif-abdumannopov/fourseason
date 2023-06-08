from django.urls import path, include, re_path
from .views import *
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', home, name='home'),
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('logout', logo_out, name='logout'),
    path('admin_panel', admin_panel, name='admin_panel'),
    path('admin_full', admin_panel_full, name='admin_full'),
    path('maldives', maldives, name='maldives'),
    path('residents', residents, name='residents'),
    path('dining', dining, name='dining'),
    path('gift-cards', gift_cards, name='gift_cards'),
    path('privatejet', jet, name='jet'),
    path('about', about, name='about'),
    path('history', history, name='history'),
    path('contact', contact, name='contact'),
    path('rates', rates, name='rates'),
    path('api/v1/reservation', ReservationList.as_view()),
    path('api/v1/rates', RatesList.as_view()),
    path('api/v1/contact', ContactList.as_view()),
    # path(r'api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
