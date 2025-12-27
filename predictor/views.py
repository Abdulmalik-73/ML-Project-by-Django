from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import os
import numpy as np
import pandas as pd
from .forms import HousePredictionForm
from .models import PredictionHistory

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

def load_model():
    """Load the trained model and encoders"""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model_data = pickle.load(f)
        return model_data
    except FileNotFoundError:
        return None

class PredictionView(FormView):
    template_name = 'predict.html'
    form_class = HousePredictionForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_data = load_model()
        context['model_loaded'] = model_data is not None
        if model_data:
            context['r2_score'] = f"{model_data['r2_score']:.4f}"
        return context
    
    def form_valid(self, form):
        model_data = load_model()
        
        if not model_data:
            return render(self.request, 'error.html', {
                'error': 'Model not found. Please train the model first.'
            })
        
        # Extract form data
        bedrooms = form.cleaned_data['bedrooms']
        bathrooms = form.cleaned_data['bathrooms']
        house_size = form.cleaned_data['house_size']
        land_size = form.cleaned_data['land_size']
        location = form.cleaned_data['location']
        condition = form.cleaned_data['condition']
        year_built = form.cleaned_data['year_built']
        
        # Encode categorical variables
        le_location = model_data['le_location']
        le_condition = model_data['le_condition']
        
        location_encoded = le_location.transform([location])[0]
        condition_encoded = le_condition.transform([condition])[0]
        
        # Prepare features with proper feature names
        feature_names = model_data.get('feature_names', ['bedrooms', 'bathrooms', 'house_size', 'land_size', 'location', 'condition', 'year_built'])
        features = pd.DataFrame([[
            bedrooms,
            bathrooms,
            house_size,
            land_size,
            location_encoded,
            condition_encoded,
            year_built
        ]], columns=feature_names)
        
        # Make prediction
        model = model_data['model']
        predicted_price = model.predict(features)[0]
        
        # Calculate confidence range (±10%)
        lower_range = predicted_price * 0.9
        upper_range = predicted_price * 1.1
        
        # Save to history
        PredictionHistory.objects.create(
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            house_size=house_size,
            land_size=land_size,
            location=location,
            condition=condition,
            year_built=year_built,
            predicted_price=predicted_price
        )
        
        context = {
            'predicted_price': f"{predicted_price:,.0f}",
            'lower_range': f"{lower_range:,.0f}",
            'upper_range': f"{upper_range:,.0f}",
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'house_size': house_size,
            'land_size': land_size,
            'location': location,
            'condition': condition,
            'year_built': year_built,
            'r2_score': f"{model_data['r2_score']:.4f}",
            'mae': f"{model_data['mae']:,.0f}",
        }
        
        return render(self.request, 'result.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def api_predict(request):
    """API endpoint for predictions"""
    try:
        data = json.loads(request.body)
        
        model_data = load_model()
        if not model_data:
            return JsonResponse({
                'error': 'Model not found'
            }, status=500)
        
        # Extract data
        bedrooms = int(data.get('bedrooms'))
        bathrooms = int(data.get('bathrooms'))
        house_size = float(data.get('house_size'))
        land_size = float(data.get('land_size'))
        location = data.get('location')
        condition = data.get('condition')
        year_built = int(data.get('year_built'))
        
        # Encode
        le_location = model_data['le_location']
        le_condition = model_data['le_condition']
        
        location_encoded = le_location.transform([location])[0]
        condition_encoded = le_condition.transform([condition])[0]
        
        # Prepare features with proper feature names
        feature_names = model_data.get('feature_names', ['bedrooms', 'bathrooms', 'house_size', 'land_size', 'location', 'condition', 'year_built'])
        features = pd.DataFrame([[
            bedrooms,
            bathrooms,
            house_size,
            land_size,
            location_encoded,
            condition_encoded,
            year_built
        ]], columns=feature_names)
        
        # Predict
        model = model_data['model']
        predicted_price = model.predict(features)[0]
        
        lower_range = predicted_price * 0.9
        upper_range = predicted_price * 1.1
        
        return JsonResponse({
            'success': True,
            'predicted_price': predicted_price,
            'lower_range': lower_range,
            'upper_range': upper_range,
            'currency': 'ETB'
        })
    
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)

class ModelStatsView(TemplateView):
    template_name = 'model_stats.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_data = load_model()
        
        if model_data:
            context['r2_score'] = f"{model_data['r2_score']:.4f}"
            context['mae'] = f"{model_data['mae']:,.0f}"
            context['rmse'] = f"{model_data['rmse']:,.0f}"
            context['model_loaded'] = True
        else:
            context['model_loaded'] = False
        
        context['total_predictions'] = PredictionHistory.objects.count()
        
        return context
