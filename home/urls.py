from django.urls import path
from home import views

urlpatterns = [
      path('', views.homeView, name='homeView'),
      path('viewSubject/<int:pk>', views.viewSubject, name='viewSubject'),
      # path('getLocation', views.getLocation, name='getLocation'),
      path('viewAttendance', views.viewAttendance, name='viewAttendance'),
      path('addAttendance', views.addAttendance, name='addAttendance'),
      path('subjects', views.subjects, name='subjects'),
      path('addSubject', views.addSubject, name='addSubject'),
]