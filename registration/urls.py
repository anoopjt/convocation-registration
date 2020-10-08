from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
]

urlpatterns += [
    url(r'^captcha/', include('captcha.urls'))
]
