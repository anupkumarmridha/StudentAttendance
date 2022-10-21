from django.urls import path
from accounts import views
from accounts import studentView
urlpatterns = [
  path('/signup/', views.handelSingup, name='handelSingup'),
  path('/login', views.handleLogin, name='handleLogin'),
  path('logout', views.handleLogout, name='handleLogout'),
  path('viewStudentProfile', studentView.viewStudentProfile, name='viewStudentProfile'),
  path('addStudent', studentView.addStudent, name='addStudent'),
  path('updateStudent/<int:pk>', studentView.updateStudent.as_view(), name='updateStudent'),
]