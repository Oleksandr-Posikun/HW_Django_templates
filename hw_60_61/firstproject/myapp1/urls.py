from django.urls import path

from myapp1.views import index, about

urlpatterns = [
    path('', index),
    path('about/', about)
]
