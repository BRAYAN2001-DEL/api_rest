# project/urls.py
from django.urls import path
from app import views  # Importa las vistas desde la carpeta app

urlpatterns = [
    path('students/', views.get_students, name='get_students'),
    path('students/<int:id>/', views.get_studentId, name='get_student'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/patch/<int:id>/', views.update_student, name='update_student'),  # Para actualizar un estudiante por id



]
