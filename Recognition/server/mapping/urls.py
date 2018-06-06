import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, '..')  # use your own username here
if path not in sys.path:
    sys.path.append(path)

from django.urls import path
from server.mapping import views

urlpatterns = [
    path('photo', views.photo, name='photo'),
]
