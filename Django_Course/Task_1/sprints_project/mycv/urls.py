from django.urls import path
from . import views

urlpatterns=[
        path('Hello/',views.Hello,name='Hello'),
]
