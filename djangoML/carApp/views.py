# views.py

from django.shortcuts import render
from joblib import load

# Load the trained model
rf_random = load('./savedModels/rf_random.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    Present_Price = float(request.GET['Present_Price'])
    Kms_Driven = float(request.GET['Kms_Driven'])
    Years_Old = float(request.GET['Years_Old'])
        
        # Predict using the machine learning model with actual numeric values
    y_pred = rf_random.predict([[Present_Price, Kms_Driven, Years_Old,]])
        
    print(y_pred)
    return render(request, 'result.html',{'result' : y_pred})
