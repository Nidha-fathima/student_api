from django.urls import path
from . import views


urlpatterns=[
    path('student/create',views.student_create,name='student_create'),
    path('students/',views.student_list,name='student_list'),
    path('student/<int:pk>',views.student_detail,name='student_detail'),
    path('student/<int:pk>/update',views.student_update,name='student_update'),
    path('student/<int:pk>/delete',views.student_delete,name='student_delete')


]

