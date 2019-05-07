from django.urls import path, include
from feeder import views

urlpatterns = [
    path('feeder/',views.FeederView.index, name = 'feeder')
]
