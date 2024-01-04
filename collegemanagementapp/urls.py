from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('add_course',views.add_course,name="add_course"),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_student',views.add_student,name="add_student"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('show_details',views.show_details,name="show_details"),
    path('edit/<int:pk>',views.edit,name="edit"),
    path('editdb/<int:pk>',views.editdb,name="editdb"),
    path('delete/<int:pk>',views.delete,name="delete"),
    path('user_home',views.user_home,name="user_home"),
    path('teacher_signup',views.teacher_signup,name="teacher_signup"),
    path('add_teacherdb',views.add_teacherdb,name="add_teacherdb"),
    path('user_edit',views.user_edit,name="user_edit"),


    path('u_edit',views.u_edit,name="u_edit"),


    path('profile',views.profile,name="profile"),
    path('show_teacher',views.show_teacher,name="show_teacher"),
    path('deleteTeacher/<int:pk>',views.deleteTeacher,name="deleteTeacher"),

]