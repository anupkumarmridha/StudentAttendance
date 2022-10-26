from django.urls import path
from home import views

urlpatterns = [
      path('', views.homeView, name='homeView'),
      path('viewSubject', views.viewSubject, name='viewSubject'),
      path('addSubject', views.addSubject, name='addSubject'),
]