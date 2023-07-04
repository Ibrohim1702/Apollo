from django.urls import path

from sayt.views import index

urlpatterns = [
    path("", index, name="home")
]