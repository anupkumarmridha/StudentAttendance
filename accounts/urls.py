from django.urls import path
from accounts import views
from accounts import studentView, facultyView
urlpatterns = [
  path('/signup/', views.handelSingup, name='handelSingup'),
  path('/login', views.handleLogin, name='handleLogin'),
  path('logout', views.handleLogout, name='handleLogout'),
  
  # url for studnt view
  path('viewStudentProfile', studentView.viewStudentProfile, name='viewStudentProfile'),
  path('addStudent', studentView.addStudent, name='addStudent'),
  path('updateStudent/<int:pk>', studentView.updateStudent.as_view(), name='updateStudent'),
  
  # url for facultyView
  path('viewFacultyProfile', facultyView.viewFacultyProfile, name='viewFacultyProfile'),
  path('addFaculty', facultyView.addFaculty, name='addFaculty'),
  path('updateFaculty/<int:pk>', facultyView.updateFaculty.as_view(), name='updateFaculty'),
]