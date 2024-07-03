from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Student
import json


@csrf_exempt
def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        data = list(students.values())  # Convierte los objetos queryset en una lista de diccionarios
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_studentId(request, id):
    if request.method == 'GET':
        student = get_object_or_404(Student, id=id)  # Obtiene el estudiante por su id o devuelve un 404 si no existe
        data = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            #'date_of_birth': student.date_of_birth.strftime('%Y-%m-%d'),
            'date_of_birth': student.date_of_birth,
            'grade': student.grade,
            'phone': student.phone,
            'email': student.email,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)





@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        date_of_birth = data.get('date_of_birth', None)
        grade = data.get('grade', None)
        phone = data.get('phone', None)
        email = data.get('email', None)

        if not all([first_name, last_name, date_of_birth, grade, phone, email]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            grade=grade,
            phone=phone,
            email=email
        )

        return JsonResponse({'id': student.id, 'message': 'Student created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    



    
@csrf_exempt
def update_student(request, id):
    if request.method == 'PATCH':
        student = get_object_or_404(Student, id=id)
        data = json.loads(request.body)

        if 'first_name' in data:
            student.first_name = data['first_name']
        if 'last_name' in data:
            student.last_name = data['last_name']
        if 'date_of_birth' in data:
            student.date_of_birth = data['date_of_birth']
        if 'grade' in data:
            student.grade = data['grade']
        if 'phone' in data:
            student.phone = data['phone']
        if 'email' in data:
            student.email = data['email']

        student.save()
        return JsonResponse({'id': student.id,'first_name': student.first_name})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)