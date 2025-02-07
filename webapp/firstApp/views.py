from django.shortcuts import render
import joblib,json,os,yaml,psycopg2
from .models import mlops

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
