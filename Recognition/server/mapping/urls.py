import sys
path = 'C:\\Users\\kom\\Desktop\\NormalSmartDevice\\Recognition'  # use your own username here
if path not in sys.path:
    sys.path.append(path)


from server.mapping import views
from django.urls import path

urlpatterns = [
    path('photo', views.photo, name='photo'),
]
