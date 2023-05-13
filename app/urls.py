from django.urls import path, include, re_path
from .views import *
from django.conf.urls.static import static, settings

urlpatterns = [
    path('', home, name='home'),
    path('maldives', maldives, name='maldives'),
    path('residents', residents, name='residents'),
    path('dining', dining, name='dining'),
    path('gift-cards', gift_cards, name='gift_cards'),
    path('api/v1/post', PostList.as_view()),
    path('api/v1/post_delete/<int:pk>', PostDelete.as_view()),
    path('api/v1/post_update/<int:pk>', PostUpdate.as_view()),
    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

