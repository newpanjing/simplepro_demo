from django.urls import path

from dialog import views

app_name = 'dialog'

urlpatterns = [
    path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('ajax', views.ajax, name='ajax'),
]
