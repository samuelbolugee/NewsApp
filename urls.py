from django.urls import path
from .views import index,bbc,bbcsport,bleacher,bloomberg,businessinsider,cnn,espn,timesindia,nbcnews,abc

urlpatterns = [
    path('', index, name= 'index'),
    path('bbc/', bbc, name= 'bbc'),
    path('bbcsport/', bbcsport, name= 'bbcsport'),
    path('bleacher/', bleacher, name= 'bleacher'),
    path('bloomberg/', bloomberg, name= 'bloomberg'),
    path('binsider/', businessinsider, name= 'businessinsider'),
    path('cnn/', cnn, name= 'cnn'),
    path('espn/', espn, name= 'espn'),
    path('toi/', timesindia, name= 'timesofindia'),
    path('nbc/', nbcnews, name= 'nbcnews'),
    path('abc/', abc, name= 'abc'),
]
