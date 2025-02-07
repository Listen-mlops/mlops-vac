from django.shortcuts import render
import joblib,json,os,yaml,psycopg2
from .models import mlops
from django.shortcuts import render
import joblib, json, os, yaml, psycopg2
from .models import mlops
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def index(request):
    return render(request, 'index.html')

@require_http_methods(["GET"])
def result(request):
    try:
        cls = joblib.load('../models/model.joblib')
        user_input = [
            int(request.GET.get('age', 0)), 
            int(request.GET.get('sex', 0)), 
            float(request.GET.get('bmi', 0.0)), 
            int(request.GET.get('children', 0)), 
            int(request.GET.get('smoker', 0)), 
            int(request.GET.get('region', 0))
        ]

        answer = cls.predict([user_input])

        mlops.objects.create(
            age=user_input[0],
            sex=user_input[1],
            bmi=user_input[2],
            children=user_input[3],
            smoker=user_input[4],
            region=user_input[5],
            charges=float(answer[0])
        )

        return JsonResponse({'answer': answer[0]})

    except ValueError as e:
        return JsonResponse({'error': f'Invalid input: {str(e)}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
def index(request):
    return render(request, 'index.html')

def result(request):
    cls = joblib.load('../models/model.joblib')
    
    try:
        # Convert input values to appropriate numeric types
        user_input = [
            int(request.GET['age']),      # Convert to integer
            int(request.GET['sex']),      # Convert to integer
            float(request.GET['bmi']),    # Convert to float
            int(request.GET['children']), # Convert to integer
            int(request.GET['smoker']),   # Convert to integer
            int(request.GET['region'])    # Convert to integer
        ]

        # Make a prediction
        answer = cls.predict([user_input])

        b = mlops(age= int(request.GET['age']),
                  sex=int(request.GET['sex']),
                  bmi=float(request.GET['bmi']),
                  children=int(request.GET['children']),
                  smoker=int(request.GET['smoker']),
                  region=int(request.GET['region']),
                  charges=float(answer[0]))
        b.save()

        return render(request, 'index.html', {'answer': answer[0]})

    except ValueError as e:
        return render(request, 'index.html', {'error': f'Invalid input: {str(e)}'})
